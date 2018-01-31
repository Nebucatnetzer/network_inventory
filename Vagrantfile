# coding: utf-8
# -*- mode: ruby -*-
# vi: set ft=ruby :
BOX_IMAGE = "debian/stretch64"
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

    config.vm.box = BOX_IMAGE
    config.vm.hostname = "network-inventory"
    config.vm.provider "virtualbox" do |v|
        v.memory = 1024
        v.cpus = 2
    end

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

    # Der Webserver ist unter http://localhost:8000 erreichbar
    config.vm.network "forwarded_port", guest: 8000, host: 8000
    config.vm.network "forwarded_port", guest: 80, host: 8080

    #Diese Option würde erlauben den Server an ein virtuelles
    #Netzwerk anzuschliessen.
    #config.vm.network "private_network", type: "dhcp"

    config.vm.synced_folder ".", "/vagrant", type: "virtualbox"

    #Begin des Installationsscripts
    config.vm.provision "shell", inline: <<-SHELL
    DEBIAN_FRONTEND=noninteractive
    apt-get update

    #zu installierende Pakete
    apt-get install -y apache2 mariadb-server avahi-daemon \
        libnss-mdns libapache2-mod-wsgi-py3 python3-mysqldb python3-venv


    /vagrant/setup.sh
    SHELL

end
