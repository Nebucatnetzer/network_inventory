#!/usr/bin/env bash

# Helper functions not exposed to the user {
# Load example data
_init() {
    python ./src/manage.py loaddata src/network_inventory.yaml
}

# Setup the database
_setup() {
    overmind start -l db -D
    if [ -f .direnv/first_run ]; then
        sleep 2
        python ./src/manage.py collectstatic --noinput
        python ./src/manage.py makemigrations
        python ./src/manage.py migrate
    else
        python ./src/manage.py collectstatic --noinput
        python ./src/manage.py makemigrations backups
        python ./src/manage.py makemigrations computers
        python ./src/manage.py makemigrations core
        python ./src/manage.py makemigrations customers
        python ./src/manage.py makemigrations devices
        python ./src/manage.py makemigrations licenses
        python ./src/manage.py makemigrations nets
        python ./src/manage.py makemigrations softwares
        python ./src/manage.py makemigrations users
        python ./src/manage.py makemigrations
        python ./src/manage.py migrate
        python ./src/manage.py loaddata backups
        python ./src/manage.py loaddata computers
        python ./src/manage.py loaddata core
        python ./src/manage.py loaddata devices
        python ./src/manage.py loaddata nets
        python ./src/manage.py loaddata softwares
        python ./src/manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password')"
        _init
        touch .direnv/first_run
    fi
    overmind quit
    sleep 2
}

_open_url() {
    if [[ ! -z "${DEFAULT_BROWSER}" ]]; then
        $DEFAULT_BROWSER $url
    elif type explorer.exe &>/dev/null; then
        explorer.exe $url
    fi
}

_create_url() {
    if [ -f /etc/wsl.conf ]; then
        echo "http://localhost:$WEBPORT"
    else
        echo "http://$(hostname -f):$WEBPORT"
    fi
}
#}

# Main tasks start
declare -A tasks
declare -A descriptions

run() {
    _setup
    find . -name __pycache__ -o -name "*.pyc" -delete
    url=$(_create_url)
    sudo iptables -I INPUT -p tcp --dport $WEBPORT -j ACCEPT
    overmind start -D
    printf "\n---\n webserver: $url\n---\n"
    _open_url $url
}
descriptions["run"]="Start the webserver."
tasks["run"]=run
descriptions["start"]="Alias for run."
tasks["start"]=run

stop() {
    overmind quit
}
descriptions["stop"]="Stop the webserver and DB."
tasks["stop"]=stop

venv() {
    nix build .#venv -o .venv
}
descriptions["venv"]="Build a pseudo venv that editors like VS Code can use."
tasks["venv"]=venv

build-container() {
    nix build && docker load <result && docker run --rm -ti network-inventory:latest
}
descriptions["build-container"]="Build and load OCI container."
tasks["build-container"]=build-container

clean() {
    find . \( -name __pycache__ -o -name "*.pyc" \) -delete
    rm -rf htmlcov/
    rm -f .direnv/first_run
    rm -f src/*/migrations/0*.py
    rm -rf .direnv/postgres/
}
descriptions["clean"]="Reset the project to a fresh state including the database."
tasks["clean"]=clean

cleanall() {
    git clean -xdf
}
descriptions["cleanall"]="Completly remove any files which are not checked into git."
tasks["cleanall"]=cleanall

debug() {
    pytest --pdb --nomigrations --cov=. --cov-report=html ./src/
}
descriptions["debug"]="Run the tests and drop into the debugger on failure."
tasks["debug"]=debug

lint() {
    echo "Running pylint"
    poetry run \
        pylint \
        --rc-file="$PROJECT_DIR/pyproject.toml" \
        -j 0 \
        -E "$PROJECT_DIR/src"
    echo "Running mypy"
    poetry run \
        mypy --config-file="$PROJECT_DIR/pyproject.toml" "$PROJECT_DIR/src"
}
descriptions["lint"]="Run the linters against the src directory."
tasks["lint"]=lint

test() {
    DJANGO_SETTINGS_MODULE=network_inventory.settings.ram_test poetry run \
        pytest \
        -nauto \
        --nomigrations \
        --cov-config="$PROJECT_DIR/.coveragerc" \
        --cov-report=html \
        "$PROJECT_DIR/src"
}
descriptions["test"]="Run the tests in the RAM DB and write a coverage report."
tasks["test"]=test

check() {
    lint
    test
}
descriptions["check"]="Run lint and test in one session"
tasks["check"]=check

update() {
    poetry update
}
descriptions["update"]="Update the dependencies."
tasks["update"]=update

# only one task at a time
if [ $# != 1 ]; then
    printf "usage: dev <task_name>\n\n"
    for task in "${!tasks[@]}"; do
        echo "$task - ${descriptions[$task]}"
    done

else
    # Check if task is available
    if [[ -v "tasks[$1]" ]]; then
        ${tasks["$1"]}
    else
        echo "Task not found."
    fi
fi
