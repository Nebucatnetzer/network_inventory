{
  description = "A Python API for various tools I use at work.";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = { self, nixpkgs, flake-utils }:
    (flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
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
            pkgs.poetry
            pkgs.overmind
            pkgs.postgresql_15
            (pkgs.writeScriptBin "dev" "${builtins.readFile ./dev.sh}")
          ];
          PYTHON_KEYRING_BACKEND = "keyring.backends.fail.Keyring";
          LD_LIBRARY_PATH = "${pkgs.stdenv.cc.cc.lib}/lib";
          shellHook = ''
            export DJANGO_SETTINGS_MODULE=network_inventory.settings.local
          '';
        };
        packages = {
          container = pkgs.dockerTools.buildImage {
            name = "network-inventory";
            tag = "latest";
            created = "now";
            copyToRoot = pkgs.buildEnv {
              name = "image-root";
              paths = [
                inventory
                pkgs.bashInteractive
                pkgs.coreutils
                pkgs.poetry
                (pkgs.writeShellScriptBin "start-inventory" ''
                  if [ -f .first_run ]; then
                      sleep 2
                      django-admin collectstatic --noinput
                      django-admin makemigrations
                      django-admin migrate
                  else
                      django-admin collectstatic --noinput
                      django-admin makemigrations backups
                      django-admin makemigrations computers
                      django-admin makemigrations core
                      django-admin makemigrations customers
                      django-admin makemigrations devices
                      django-admin makemigrations licenses
                      django-admin makemigrations nets
                      django-admin makemigrations softwares
                      django-admin makemigrations users
                      django-admin makemigrations
                      django-admin migrate
                      django-admin loaddata backups
                      django-admin loaddata computers
                      django-admin loaddata core
                      django-admin loaddata devices
                      django-admin loaddata nets
                      django-admin loaddata softwares
                      django-admin shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password')"
                      touch .first_run
                  fi
                  gunicorn network_inventory.wsgi:application --reload --bind 0.0.0.0:8000 --workers 3
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

