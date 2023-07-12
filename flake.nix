{
  description = "A Python API for various tools I use at work.";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    poetry2nix = {
      url = "github:Nebucatnetzer/poetry2nix/execnet-overrides";
      inputs.nixpkgs.follows = "nixpkgs";
    };

  };
  outputs = { self, nixpkgs, flake-utils, poetry2nix }:
    {
      overlays.default = nixpkgs.lib.composeManyExtensions [
        poetry2nix.overlay
        (final: prev: rec {
          inventoryDevEnv = prev.poetry2nix.mkPoetryEnv
            {
              projectDir = ./.;
              groups = [ "main" "dev" ];
            };
          inventoryPackage = prev.poetry2nix.mkPoetryApplication {
            projectDir = ./.;
            groups = [ "main" ];
          };
          inventoryEnv = inventoryPackage.dependencyEnv;
        })
      ];
    } // (flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
          overlays = [ self.overlays.default ];
        };
        inventory = pkgs.stdenv.mkDerivation {
          src = ./.;
          version = "latest";
          pname = "network-inventory";
          installPhase = ''
            mkdir -p $out
            cp -r ./src $out/code
          '';
        };
      in
      rec {
        devShells.default = pkgs.mkShell {
          buildInputs = [
            pkgs.gnumake
            pkgs.inventoryDevEnv
            pkgs.poetry
            pkgs.python310Packages.pip
            (pkgs.writeScriptBin "dev" "${builtins.readFile ./dev.sh}")
          ];
          PYTHON_KEYRING_BACKEND = "keyring.backends.fail.Keyring";
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
            checkInputs = [ pkgs.inventoryDevEnv ];
            checkPhase = ''
              mkdir -p $out
              pylint --rc-file pyproject.toml -j 0 -E src/
              cd src/ && mypy --config-file=../pyproject.toml .
            '';
            DJANGO_SETTINGS_MODULE = "network_inventory.settings.ram_test";
          };
          tests = pkgs.stdenv.mkDerivation {
            dontPatch = true;
            dontConfigure = true;
            dontBuild = true;
            dontInstall = true;
            doCheck = true;
            name = "test";
            src = ./.;
            checkInputs = [ pkgs.inventoryDevEnv ];
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
        packages = {
          venv = pkgs.inventoryEnv;
          container = pkgs.dockerTools.buildImage {
            name = "network-inventory";
            tag = "latest";
            created = "now";
            copyToRoot = pkgs.buildEnv {
              name = "image-root";
              paths = [
                pkgs.bashInteractive
                pkgs.coreutils
                inventory
                (pkgs.writeShellScriptBin "start-inventory" ''
                  if [ -f .second_run ]; then
                      sleep 2
                      ${pkgs.inventoryEnv}/bin/django-admin collectstatic --noinput
                      ${pkgs.inventoryEnv}/bin/django-admin makemigrations
                      ${pkgs.inventoryEnv}/bin/django-admin migrate
                  else
                      ${pkgs.inventoryEnv}/bin/django-admin collectstatic --noinput
                      ${pkgs.inventoryEnv}/bin/django-admin makemigrations backups
                      ${pkgs.inventoryEnv}/bin/django-admin makemigrations computers
                      ${pkgs.inventoryEnv}/bin/django-admin makemigrations core
                      ${pkgs.inventoryEnv}/bin/django-admin makemigrations customers
                      ${pkgs.inventoryEnv}/bin/django-admin makemigrations devices
                      ${pkgs.inventoryEnv}/bin/django-admin makemigrations licenses
                      ${pkgs.inventoryEnv}/bin/django-admin makemigrations nets
                      ${pkgs.inventoryEnv}/bin/django-admin makemigrations softwares
                      ${pkgs.inventoryEnv}/bin/django-admin makemigrations users
                      ${pkgs.inventoryEnv}/bin/django-admin makemigrations
                      ${pkgs.inventoryEnv}/bin/django-admin migrate
                      ${pkgs.inventoryEnv}/bin/django-admin loaddata backups
                      ${pkgs.inventoryEnv}/bin/django-admin loaddata computers
                      ${pkgs.inventoryEnv}/bin/django-admin loaddata core
                      ${pkgs.inventoryEnv}/bin/django-admin loaddata devices
                      ${pkgs.inventoryEnv}/bin/django-admin loaddata nets
                      ${pkgs.inventoryEnv}/bin/django-admin loaddata softwares
                      ${pkgs.inventoryEnv}/bin/django-admin shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password')"
                      touch .second_run
                  fi
                  ${pkgs.inventoryEnv}/bin/gunicorn network_inventory.wsgi:application --reload --bind 0.0.0.0:8000 --workers 3
                '')
              ];
            };
            config = {
              Cmd = [ "start-inventory" ];
              WorkingDir = "/code";
              Env = [
                "POSTGRES_DB=network_inventory"
                "DJANGO_SETTINGS_MODULE=network_inventory.settings.production"
                "PYTHONPATH=/lib/python3.10:/lib/python3.10/site-packages:/code"
              ];
            };
          };
          default = packages.container;
        };
      }));
}

