# network_inventory

I started this project in order to have solution for keeping an
inventory over my various servers and other network equipment.

## Setup

1. Clone the repository
2. Now decide if you want to develop fully locally or inside the docker
   container. Locally you'll use SQlite for the database and inside the Docker
   container you'll use Postgres for the database. For the moment there aren't
   any features implemented which require Postgres. However this might change
   in the future and SQlite is not supported for production.

### Local Setup
3. Run `make local` to create the virtual environment for development.
   You're now all set to start developing.

### Docker Setup
3. Run `make` to start the development server. You can access it
   at   http://localhost:8000 . You're now all set to start developing. \
   If you need to run migrations you can simply restart the Docker container.

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

## Todos
- [ ] Create an Nginx configuration
- [ ] extend the CSS
    - A more centered layout would be nice
    - Maybe some colours
- [ ] include a RAID calculator
    - <https://thoughtworksnc.com/2017/08/30/writing-a-raid-calculator-in-python/>
      I would like to use this to show the usable space in a RAID system.
- [ ] calculate the used space on a host
    Means calculate the size all the VMs would use if they were thick.
