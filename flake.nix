{
  description = "A Python API for various tools I use at work.";
  inputs = {
    nixpkgs.url = github:NixOS/nixpkgs/nixos-unstable;
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
              overrides = pkgs.poetry2nix.defaultPoetryOverrides.extend
                (self: super: {
                  findpython = super.findpython.overridePythonAttrs (
                    old: {
                      buildInputs = (old.buildInputs or [ ]) ++ [ pkgs.pdm ];
                    }
                  );
                  django-floppyforms =
                    super.django-floppyforms.overridePythonAttrs
                      (
                        old: {
                          buildInputs = (old.buildInputs or [ ]) ++ [ pkgs.python310Packages.setuptools ];
                        }
                      );
                  django-crispy-forms = super.django-crispy-forms.overridePythonAttrs
                    (
                      old: {
                        buildInputs = (old.buildInputs or [ ]) ++ [ pkgs.python310Packages.setuptools ];
                      }
                    );
                  exceptiongroup = super.exceptiongroup.overridePythonAttrs
                    (
                      old: {
                        buildInputs = (old.buildInputs or [ ]) ++ [ pkgs.python310Packages.flit-scm ];
                      }
                    );
                });
            })
            pkgs.python310Packages.poetry
          ];
        };
        shellHook = ''
          export DJANGO_SETTINGS_MODULE=network_inventory.settings.local
        '';
      });
}
