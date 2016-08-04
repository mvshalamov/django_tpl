# -*- mode: ruby -*-
# vi: set ft=ruby :

PROJECT_NAME = "django"
PROJECT_FOLDER = PROJECT_NAME + "_prj"

Vagrant.configure(2) do |config|
  config.vm.box = "debian/contrib-jessie64"
  config.vm.hostname = PROJECT_NAME

  config.vm.provider "virtualbox" do |vb|
    # Customize the amount of memory on the VM:
    vb.memory = "1024"
    vb.customize ["setextradata", :id, "VBoxInternal2/SharedFoldersEnableSymlinksCreate/v-root", "1"]
  end

  config.vm.synced_folder ".", "/home/vagrant/" + PROJECT_FOLDER
  config.vm.provision :shell, path: "provision.sh", args: PROJECT_FOLDER

  ENV["LC_ALL"] = "en_US.UTF-8"

  #config.ssh.forward_agent = true
  config.ssh.insert_key = true

  config.vm.network "forwarded_port", guest: 8000, host: 9000  # django
  config.vm.network "forwarded_port", guest: 5432, host: 9452  # postgresql
  config.vm.network "forwarded_port", guest: 27017, host: 9017  # mongo
end
