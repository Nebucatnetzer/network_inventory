{
  description = "A Python API for various tools I use at work.";
  inputs = {
    nixpkgs.url = github:NixOS/nixpkgs/nixos-21.11;
    flake-utils = {
      url = github:numtide/flake-utils;
    };
    mach-nix = {
      url = "github:DavHau/mach-nix";
      inputs = {
        nixpkgs.follows = "nixpkgs";
        flake-utils.follows = "flake-utils";
        pypi-deps-db = {
          url = "github:DavHau/pypi-deps-db";
        };
      };
    };
  };

  outputs = { self, nixpkgs, flake-utils, mach-nix, ... }@inputs:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        machNix = mach-nix.lib."${system}";
      in
      {
        devShell = machNix.mkPythonShell {
          packagesExtra = with pkgs; [ pkgs.gnumake ];
          requirements = builtins.readFile ./requirements/local.txt;
          _.pytest-cov.propagatedBuildInputs.mod = pySelf: self: oldVal: oldVal ++ [ pySelf.tomli ];
        };
        defaultPackage = (machNix.mkDockerImage {
          packagesExtra = with pkgs; [ pkgs.bash ];
          requirements = builtins.readFile ./requirements/docker.txt;
          _.pytest-cov.propagatedBuildInputs.mod = pySelf: self: oldVal: oldVal ++ [ pySelf.tomli ];
        }).override (oldAttrs: {
          name = "network-inventory";
          config.Cmd = [ "run.sh" ];
        });
      });
}
