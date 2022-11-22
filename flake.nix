{
  description = "A Python API for various tools I use at work.";
  inputs = {
    nixpkgs.url = github:NixOS/nixpkgs/nixos-unstable;
    flake-utils.url = github:numtide/flake-utils;
    poetry2nix = {
      url = "github:Nebucatnetzer/poetry2nix?rev=283a1398ee9c080c8c3310c8fd1aa937f6e84b62";
      inputs.nixpkgs.follows = "nixpkgs";
    };

  };
  outputs = { self, nixpkgs, flake-utils, poetry2nix }:
    {
      overlay = nixpkgs.lib.composeManyExtensions [
        poetry2nix.overlay
        (final: prev: {
          inventoryEnv = prev.poetry2nix.mkPoetryEnv
            {
              projectDir = ./.;
              overrides = prev.poetry2nix.defaultPoetryOverrides.extend
                (self: super: {
                  python-monkey-business = super.python-monkey-business.overridePythonAttrs
                    (
                      old: {
                        buildInputs = (old.buildInputs or [ ]) ++ [ super.setuptools ];
                      }
                    );
                });
            };
        })
        poetry2nix.overlay
        (final: prev: {
          inventory = prev.poetry2nix.mkPoetryApplication
            {
              projectDir = ./.;
              checkPhase = "pytest --ds=network_inventory.settings.ram_test -nauto --nomigrations";
              overrides = prev.poetry2nix.defaultPoetryOverrides.extend
                (self: super: {
                  python-monkey-business = super.python-monkey-business.overridePythonAttrs
                    (
                      old: {
                        buildInputs = (old.buildInputs or [ ]) ++ [ super.setuptools ];
                      }
                    );
                });
            };
        })
      ];
    } // (flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
          overlays = [ self.overlay ];
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
        packages.venv = pkgs.inventoryEnv;
        packages.inventory = pkgs.inventory;
        packages.default = pkgs.inventory;
      }));
}
