{
  description = "A Python API for various tools I use at work.";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    systems.url = "github:nix-systems/default";
    devenv.url = "github:cachix/devenv";
  };
  nixConfig = {
    extra-trusted-public-keys = "devenv.cachix.org-1:w1cLUi8dv3hnoSPGAuibQv+f9TZLr6cv/Hm9XgU50cw=";
    extra-substituters = "https://devenv.cachix.org";
  };

  outputs =
    {
      self,
      nixpkgs,
      devenv,
      systems,
    }@inputs:
    let
      forEachSystem = nixpkgs.lib.genAttrs (import systems);
    in
    {
      devShells = forEachSystem (
        system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
          config = self.devShells.${system}.default.config;
        in
        {
          default = devenv.lib.mkShell {
            inherit inputs pkgs;
            modules = [
              {
                enterShell = ''
                  export PATH=$PATH:$DEVENV_ROOT/tooling/bin/
                  export PGPORT=$(($WEBPORT + 100))
                  export PROJECT_DIR=$(pwd)
                  export WEBPORT=$(($RANDOM + 1100))
                  ln -sf ${config.process-managers.process-compose.configFile} ${config.env.DEVENV_ROOT}/process-compose.yml
                '';
                env = {
                  DJANGO_SETTINGS_MODULE = "network_inventory.settings.local";
                  PYTHON_KEYRING_BACKEND = "keyring.backends.fail.Keyring";
                  LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
                    pkgs.stdenv.cc.cc
                    # Add any missing library needed You can use the nix-index package
                    # to locate them, e.g.
                    # nix-locate -w --top-level --at-root /lib/libudev.so.1
                  ];
                };
                languages.python = {
                  enable = true;
                  package = pkgs.python310;
                  poetry = {
                    activate.enable = true;
                    enable = true;
                    install.enable = true;
                  };
                };
                process.implementation = "process-compose";
                process-managers.process-compose.enable = true;
                # https://github.com/cachix/devenv/blob/main/examples/process-compose/devenv.nix
                processes = {
                  webserver = {
                    exec = "poetry run python ./src/manage.py runserver 0.0.0.0:$WEBPORT";
                    process-compose.depends_on = {
                      setup = {
                        condition = "process_completed_successfully";
                      };
                    };
                  };
                  setup.exec = "dev setup";
                };
                services.postgres = {
                  enable = true;
                  initialDatabases = [ { name = "django"; } ];
                  package = pkgs.postgresql_15;
                };
              }
            ];
          };
        }
      );
    };
}
