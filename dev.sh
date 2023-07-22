#!/usr/bin/env bash

declare -A tasks

run () {
    setup
    find . -name __pycache__ -o -name "*.pyc" -delete
    sudo iptables -I INPUT -p tcp --dport $WEBPORT -j ACCEPT
    overmind start -D
    echo "http://$(hostname -f):$WEBPORT"
}
tasks["run"]=run
tasks["start"]=run

setup () {
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
        init
        touch .direnv/first_run
    fi
    overmind quit
    sleep 2

}

venv () {
    nix build .#venv -o .venv
}
tasks["venv"]=venv

build-container (){
    nix build && docker load < result && docker run --rm -ti network-inventory:latest
}
tasks["build-container"]=build-container

clean () {
    find . \( -name __pycache__ -o -name "*.pyc" \) -delete
    rm -rf htmlcov/
    rm -f .direnv/first_run
    rm -f src/*/migrations/0*.py
    rm -rf .direnv/postgres/
}
tasks["clean"]=clean

cleanall () {
    git clean -xdf
}
tasks["cleanall"]=cleanall

init () {
    python ./src/manage.py loaddata src/network_inventory.yaml
}

debug () {
    pytest --pdb --nomigrations --cov=. --cov-report=html ./src/
}
tasks["debug"]=debug

check (){
    nix flake check
}
tasks["check"]=check


test (){
    export DJANGO_SETTINGS_MODULE=network_inventory.settings.ram_test
    pytest -nauto --nomigrations --cov-config="$PROJECT_DIR/.coveragerc" --cov-report=html "$PROJECT_DIR/src"
}
tasks["test"]=test

update (){
    poetry update --lock
}
tasks["update"]=update

# only one task at a time
if [ $# != 1 ]; then
    echo "usage: dev <task_name>"
    echo "All tasks: ${!tasks[@]}"
else
    # Check if task is available
    if [[ -v "tasks[$1]" ]] ; then
        ${tasks["$1"]}
    else
        echo "Task not found."
    fi
fi
