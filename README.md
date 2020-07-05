# network_inventory

[![Build Status](https://travis-ci.com/Nebucatnetzer/network_inventory.svg?branch=master)](https://travis-ci.com/Nebucatnetzer/network_inventory)

I started this project in order to have solution for keeping an
inventory over my various servers and other network equipment.

## Production Setup

1. Clone the repository
2. Copy the `.env-example` file to `.env` and change the `POSTGRES_PASSWORD`
   and `DJANGO_SECRET_KEY` variables to something secure.
3. Run `docker-compose up` and connect to http://localhost

### Local Development Setup

The local setup is mainly intended to run the tests quickly. I recommend that
you use the Docker setup if you want to interact with the website.

1. Run `make local` to create the virtual environment for development.
   You're now all set to start developing.

### Docker Development Setup

This is very similar to the production setup with the difference that the image
for the `web` application gets built locally instead of getting pulled from
Dockerhub.

1. Run `make` to start the server. You can access it
   at   http://localhost . You're now all set to start working.
2. If you want to have some example data to work with run the command `make
   init` after you successfully run `make`.

#### Environment Variables

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
