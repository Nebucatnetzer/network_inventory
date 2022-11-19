{
  description = "A Python API for various tools I use at work.";
  inputs = {
    nixpkgs.url = github:NixOS/nixpkgs/nixos-22.05;
    flake-utils.url = github:numtide/flake-utils;
  };
  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };
      in
      {
        devShell = pkgs.mkShell {
          buildInputs = [
            pkgs.gnumake
            (pkgs.poetry2nix.mkPoetryEnv {
              projectDir = ./.;
              overrides = pkgs.poetry2nix.defaultPoetryOverrides.extend (self: super: {
                findpython = super.findpython.overridePythonAttrs (
                  old: {
                    buildInputs = (old.buildInputs or [ ]) ++ [ pkgs.pdm ];
                  }
                );
                idna = super.idna.overridePythonAttrs (
                  old: {
                    buildInputs = (old.buildInputs or [ ]) ++ [ pkgs.python39Packages.flit-core ];
                  }
                );
              });
            })
            pkgs.python39Packages.poetry
          ];
        };
        shellHook = ''
          export DJANGO_SETTINGS_MODULE=network_inventory.settings.local
        '';
      });
}
