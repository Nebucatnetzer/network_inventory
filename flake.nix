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
        src = with pkgs.lib;
          cleanSource (cleanSourceWith {
            filter = name: type:
              let
                baseName = baseNameOf (toString name);
              in
                !(builtins.elem baseName [
                  ".coverage"
                  ".coveragerc"
                  ".dir-locals.el"
                  ".direnv"
                  ".git"
                  ".github"
                  ".env"
                  ".envrc"
                  ".flake8"
                  ".gitignore"
                  ".gitlab-ci.yml"
                  "docker-compose.yaml"
                  "flake.lock"
                  "flake.nix"
                  "Makefile"
                  "poetry.lock"
                  "poetry.toml"
                  "pyproject.toml"
                  "pytest.ini"
                ]);
            src = ./.;
          });
        inventory = pkgs.stdenv.mkDerivation {
          inherit src;
          version = "latest";
          pname = "network-inventory";
          installPhase = ''
            mkdir -p $out
            cp -r ./src $out/code
          '';
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
                pkgs.inventoryEnv
                inventory
                (pkgs.writeShellScriptBin "start-inventory" ''
                  cd /code
                  if [ -f .second_run ]; then
                      sleep 2
                      ${pkgs.python3}/bin/python manage.py collectstatic --noinput
                      ${pkgs.python3}/bin/python manage.py makemigrations
                      ${pkgs.python3}/bin/python manage.py migrate
                  else
                      ${pkgs.python3}/bin/python manage.py collectstatic --noinput
                      ${pkgs.python3}/bin/python manage.py makemigrations backups
                      ${pkgs.python3}/bin/python manage.py makemigrations computers
                      ${pkgs.python3}/bin/python manage.py makemigrations core
                      ${pkgs.python3}/bin/python manage.py makemigrations customers
                      ${pkgs.python3}/bin/python manage.py makemigrations devices
                      ${pkgs.python3}/bin/python manage.py makemigrations licenses
                      ${pkgs.python3}/bin/python manage.py makemigrations nets
                      ${pkgs.python3}/bin/python manage.py makemigrations softwares
                      ${pkgs.python3}/bin/python manage.py makemigrations users
                      ${pkgs.python3}/bin/python manage.py makemigrations
                      ${pkgs.python3}/bin/python manage.py migrate
                      ${pkgs.python3}/bin/python manage.py loaddata backups
                      ${pkgs.python3}/bin/python manage.py loaddata computers
                      ${pkgs.python3}/bin/python manage.py loaddata core
                      ${pkgs.python3}/bin/python manage.py loaddata devices
                      ${pkgs.python3}/bin/python manage.py loaddata nets
                      ${pkgs.python3}/bin/python manage.py loaddata softwares
                      ${pkgs.python3}/bin/python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password')"
                      touch .second_run
                  fi
                  ${pkgs.python310Packages.gunicorn}/bin/gunicorn network_inventory.wsgi:application --reload --bind 0.0.0.0:8000 --workers 3
                '')
              ];
            };
            config = {
              Cmd = [ "start-inventory" ];
              Env = [
                "POSTGRES_DB=network_inventory"
                "DJANGO_SETTINGS_MODULE=network_inventory.settings.production"
                "PYTHONPATH=/lib/python3.10:/lib/python3.10/site-packages"
              ];
            };
          };
          default = self.packages.container;
        };
      }));
}

