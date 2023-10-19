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

  outputs = { self, nixpkgs, devenv, systems }@inputs:
    let
      forEachSystem = nixpkgs.lib.genAttrs (import systems);
    in
    {
      packages = forEachSystem (system: {
        devenv-up = self.devShells.${system}.default.config.procfileScript;
      });
      devShells = forEachSystem
        (system:
          let
            pkgs = nixpkgs.legacyPackages.${system};
          in
          {
            default = devenv.lib.mkShell {
              inherit inputs pkgs;
              modules = [
                {
                  packages = [
                    pkgs.overmind
                    (pkgs.writeScriptBin "dev" "${builtins.readFile ./dev.sh}")
                  ];
                  env = {
                    DJANGO_SETTINGS_MODULE = "network_inventory.settings.local";
                    PYTHON_KEYRING_BACKEND = "keyring.backends.fail.Keyring";
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
                  processes.webserver.exec = "poetry run python ./src/manage.py runserver 0.0.0.0:$WEBPORT";
                  services.postgres = {
                    enable = true;
                    initialDatabases = [{ name = "django"; }];
                    package = pkgs.postgresql_15;
                  };
                }
              ];
            };
          });
    };
}
