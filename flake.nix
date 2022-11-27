{
  description = "A Python API for various tools I use at work.";
  inputs = {
    nixpkgs.url = github:NixOS/nixpkgs/nixos-unstable;
    flake-utils.url = github:numtide/flake-utils;
    poetry2nix = {
      url = "github:nix-community/poetry2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };

  };
  outputs = { self, nixpkgs, flake-utils, poetry2nix }:
    {
      overlays.default = nixpkgs.lib.composeManyExtensions [
        poetry2nix.overlay
        (final: prev: {
          inventoryEnv = prev.poetry2nix.mkPoetryEnv {
            projectDir = ./.;
          };
          inventoryPackage = prev.poetry2nix.mkPoetryApplication {
            projectDir = ./.;
          };
        })
      ];
    } // (flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
          overlays = [ self.overlays.default ];
        };
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = [
            pkgs.gnumake
            pkgs.inventoryEnv
            pkgs.poetry
            pkgs.python310Packages.pip
          ];
          shellHook = ''
            export DJANGO_SETTINGS_MODULE=network_inventory.settings.local
          '';
        };
        checks = {
          lint = pkgs.stdenv.mkDerivation {
            dontPatch = true;
            dontConfigure = true;
            dontBuild = true;
            dontInstall = true;
            doCheck = true;
            name = "lint";
            src = ./.;
            checkInputs = [ pkgs.inventoryEnv ];
            checkPhase = ''
              mkdir -p $out
              flake8 . --count --show-source --statistics
            '';
          };
          tests = pkgs.stdenv.mkDerivation {
            dontPatch = true;
            dontConfigure = true;
            dontBuild = true;
            dontInstall = true;
            doCheck = true;
            name = "test";
            src = ./.;
            checkInputs = [ pkgs.inventoryEnv ];
            checkPhase = ''
              mkdir -p $out
              pytest --ds=network_inventory.settings.ram_test \
                     -nauto \
                     --nomigrations \
                     --cov=./src \
                     ./src
            '';
          };
        };
        packages.venv = pkgs.inventoryEnv;
        packages.inventory = pkgs.inventoryPackage;
        packages.default = pkgs.inventoryPackage;
      }));
}

