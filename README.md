# network_inventory

[![.github/workflows/publish.yml](https://github.com/Nebucatnetzer/network_inventory/actions/workflows/publish.yml/badge.svg?branch=master)](https://github.com/Nebucatnetzer/network_inventory/actions/workflows/publish.yml)

I started this project in order to have solution for keeping an
inventory over my various servers and other network equipment.

## Production Setup

1. Clone the repository
2. Copy the `.env-example` file to `.env` and change the `POSTGRES_PASSWORD`
   and `DJANGO_SECRET_KEY` variables to something secure.
3. Run `docker-compose up` and connect to http://localhost

## Development Setup

There is currently only one supported way to work with this repository. You
will need a Linux system (WSL might work) onto wich you install the Nix package
manager with Flakes enabled[^1] and direnv[^3]. Afterwards you can enter the development
environment with `direnv allow`.

[^1]: https://nixos.org/download.html
[^3]: https://direnv.net/

After you've entered the development environment with either method you can
start the development server with `dev run`. This will start a PostgreSQL
database running and start the Django development server.

_It will prompt you for your sudo password because it opens port 8000 in your
firewall. This is because I sometimes develope from my iPad on my notebook and
with this tweak I can access the dev server running on my notebook._

You can then access the project in the browser under the FQDN of your
computer. E.g. `http://mypc.domain.local:8000`.

In case you want a fresh start or remove the project you can just remove the
`.direnv` directory at the root of the project. All the data of the PostgreSQL
database is stored there together with the symlinks to the Nix store.

In case you want to tweak something these are the applications use do build the
development environment:

- Nix package manager
- direnv
- overmind[^4]

The `dev` command is a simple BASH script called `dev.sh` at the root of the
project.

[^4]: https://github.com/DarthSim/overmind

Run the `dev` command without an argument to see all options.

> Why aren't you using Docker/containers for development.

_I think containers have their uses but developing with them is in my opinion a
pain in the ass. You just can't easily interact with the tools inside the
container and you have to hack around to get your editor working with it.
In addition they aren't fully reproducable. Nix solves all of these
problems. Overmind then comes into play to orchestrate the few tasks that are
required to get a development environment up an running._

**Manual way**

The manual way you have to install poetry[^2] and then run `poetry shell` to
enter the virtual environment. You will then need a local PostgreSQL server or
modify the settings so that you can use your prefered database.

Please note that I will only use and test the first method.

[^2]: https://python-poetry.org

## Environment Variables

To customise the application in the Docker container you can use environment
variables in the docker-compose.yml file. Currently the following variables are
supported.

- **DJANGO_SECRET_KEY** the secret key is mandatory, otherwise the application
  doesn't run. Make sure that it is some long random string.
- **DJANGO_DEBUG** settings this variable to any value enables the Django debug
  mode. Make sure that you don't set it on a production server.
- **DJANGO_SETTINGS_MODULE** the path to the settings file to use in the
  container. This requires a dotet syntax. The default is
  `network_inventory.settings.docker`.

## Documentation

Currently there isn't a lot of documentation present. I try to document my
thoughts and other related information in the [Notes
file](./docs/notes.org).
