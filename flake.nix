{
  description = "A Python API for various tools I use at work.";
  inputs = {
    nixpkgs.url = github:NixOS/nixpkgs/nixos-22.05;
    flake-utils = {
      url = github:numtide/flake-utils;
    };
    pypi = {
      url = "github:DavHau/pypi-deps-db";
      flake = false;
    };
    mach-nix = {
      inputs.pypi-deps-db.follows = "pypi";
      url = "mach-nix/3.5.0";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, flake-utils, mach-nix, ... }@inputs:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        machNix = mach-nix.lib."${system}";
        devEnvironment = machNix.mkPython {
          requirements = builtins.readFile ./requirements/local.txt;
          _.pytest-cov.propagatedBuildInputs.mod = pySelf: self: oldVal: oldVal ++ [ pySelf.tomli ];
        };
      in
      {
        devShell = pkgs.mkShell {
          buildInputs = [
            devEnvironment
            pkgs.gnumake
            pkgs.python39Packages.pip
          ];
          shellHook = ''
            export DJANGO_SETTINGS_MODULE=network_inventory.settings.local
          '';
        };
        packages.venv = devEnvironment;
      });
}
