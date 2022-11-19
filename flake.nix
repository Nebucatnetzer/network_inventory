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
      overlay = nixpkgs.lib.composeManyExtensions [
        poetry2nix.overlay
        (final: prev: {
          inventory = prev.poetry2nix.mkPoetryEnv {
            projectDir = ./.;
            overrides = prev.poetry2nix.defaultPoetryOverrides.extend
              (self: super: {
                findpython = super.findpython.overridePythonAttrs (
                  old: {
                    buildInputs = (old.buildInputs or [ ]) ++ [ super.pdm ];
                  }
                );
                django-floppyforms =
                  super.django-floppyforms.overridePythonAttrs
                    (
                      old: {
                        buildInputs = (old.buildInputs or [ ]) ++ [ super.setuptools ];
                      }
                    );
                django-crispy-forms = super.django-crispy-forms.overridePythonAttrs
                  (
                    old: {
                      buildInputs = (old.buildInputs or [ ]) ++ [ super.setuptools ];
                    }
                  );
                django-nested-admin = super.django-crispy-forms.overridePythonAttrs
                  (
                    old: {
                      buildInputs = (old.buildInputs or [ ]) ++ [ super.setuptools ];
                    }
                  );
                exceptiongroup = super.exceptiongroup.overridePythonAttrs
                  (
                    old: {
                      buildInputs = (old.buildInputs or [ ]) ++ [ super.flit-scm ];
                    }
                  );
                mixer = super.mixer.overridePythonAttrs
                  (
                    old: {
                      buildInputs = (old.buildInputs or [ ]) ++ [ super.setuptools ];
                    }
                  );
                python-monkey-business = super.python-monkey-business.overridePythonAttrs
                  (
                    old: {
                      buildInputs = (old.buildInputs or [ ]) ++ [ super.flit-scm ];
                    }
                  );
                pytoolconfig = super.pytoolconfig.overridePythonAttrs
                  (
                    old: {
                      buildInputs = (old.buildInputs or [ ]) ++ [ super.pdm-pep517 ];
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
        devShell = pkgs.mkShell {
          buildInputs = [
            pkgs.gnumake
            pkgs.poetry
          ];
        };
        shellHook = ''
          export DJANGO_SETTINGS_MODULE=network_inventory.settings.local
        '';
      }));
}
