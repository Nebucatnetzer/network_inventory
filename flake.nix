{
  description = "A Python API for various tools I use at work.";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = { self, nixpkgs, flake-utils, poetry2nix }:
    (flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };
        ld_path = pkgs.lib.makeLibraryPath [ pkgs.openssl ];
        inventory = pkgs.stdenv.mkDerivation {
          src = ./.;
          version = "latest";
          pname = "network-inventory";
          buildInputs = [
            pkgs.pdm
            pkgs.python310
          ];
          installPhase = ''
            runHook preInstall
            mkdir -p $out/code
            pdm sync --production --no-editable --fail-fast
            cp pdm.toml pdm.lock pyproject.toml $out/code/
            cp -r .venv $out/code/.venv
            cp -r ./src $out/code/src
            runHook postInstall
          '';
        };
      in
      rec {
        devShells.default = pkgs.mkShell {
          buildInputs = [
            pkgs.pdm
            pkgs.overmind
            pkgs.postgresql_15
            pkgs.python310
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
            checkInputs = [ pkgs.pdm ];
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
            checkInputs = [ pkgs.pdm pkgs.postgresql_15 pkgs.overmind ];
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
                pkgs.pdm
                pkgs.python310
                (pkgs.writeShellScriptBin "start-inventory" ''
                  if [ -f .first_run ]; then
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
                      touch .first_run
                  fi
                  ${pkgs.inventoryEnv}/bin/gunicorn network_inventory.wsgi:application --reload --bind 0.0.0.0:8000 --workers 3
                '')
              ];
            };
            config = {
              Cmd = [ "pdm run start-inventory" ];
              WorkingDir = "/code";
              Env = [
                "POSTGRES_DB=network_inventory"
                "DJANGO_SETTINGS_MODULE=network_inventory.settings.production"
                "PYTHONPATH=$PYTHONPATH:/lib/python3.10:/lib/python3.10/site-packages:/code/src:/code/.venv/lib/python3.10/site-packages"
                "PATH=$PATH:/bin:/code/.venv/bin"
                "LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${ld_path}"
              ];
            };
          };
          default = packages.container;
        };
      }));
}

