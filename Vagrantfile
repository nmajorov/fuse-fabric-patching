# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  
    
    config.vm.define "fuse-server" do |nconfig|
    
    
    nconfig.vm.box = "centos/7"
    nconfig.ssh.forward_agent = "true"
    nconfig.vm.hostname = "fuse-server.elginscotland.org"
    nconfig.vm.network :private_network, ip: "10.42.0.2"

        nconfig.vm.provider "virtualbox" do |vb|
                vb.customize ["modifyvm", :id, "--memory", "2048"]
                vb.customize ["modifyvm", :id, "--cpus", "1"]
        end
    end
    
    # child node server
    config.vm.define "node1" do |nconfig|
       
    nconfig.vm.box = "centos/7"
    nconfig.ssh.forward_agent = "true"
    nconfig.vm.hostname = "node1.elginscotland.org"
    nconfig.vm.network :private_network, ip: "10.42.0.3"
        

        nconfig.vm.provider "virtualbox" do |vb|
                vb.customize ["modifyvm", :id, "--memory", "2048"]
                vb.customize ["modifyvm", :id, "--cpus", "1"]
        end
    end
   
    
    # node 2 server
    config.vm.define "node2" do |nconfig|
        nconfig.vm.box = "centos/7"
        nconfig.vm.provider :virtualbox do |vb, override|
            vb.customize ["modifyvm", :id, "--memory", "2048"]
            vb.customize ["modifyvm", :id, "--cpus", "1"]
        end
        nconfig.vm.hostname = "node2.elginscotland.org"
        nconfig.vm.network :private_network, ip: "10.42.0.4"
        
    end

end

