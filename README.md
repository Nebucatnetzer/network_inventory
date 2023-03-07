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

There are two ways to work on this project.
For the first one you will need to install the Nix package manager[^1].
Afterwards you can enter the development environment with `nix develop`.

For the other way you have to install poetry[^2] and then run `poetry shell` to
enter the virtual environment.

Please note that I will only use and test the first method.

[^1]: https://nixos.org/download.html
[^2]: https://python-poetry.org

After you've entered the development environment with either method you can
start the server. With the nix version you can start it with `dev run`. With
poetry `./dev.sh run`. This will start a PostgreSQL database running inside a
docker container and start the Django development server. You can then access
it in the browser under the FQDN of your computer. E.g.
`http://mypc.domain.local:8000`. Run the `dev` command without an argument to
see all options.

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
