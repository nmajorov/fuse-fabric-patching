# Patching POC for  Fuse fabric 6.2.1

download and copy in current directory fllowing files:

        jboss-fuse-full-6.2.1.redhat-084.zip
        jboss-fuse-full-6.2.1.redhat-186.zip    
        patch-management-for-fuse-620-6.2.1.redhat-186.zip


## Intallation instuctions

* intall vagrant and run command:

            vagrant up

it will create 3 vms fuse-server and node1 node2

**Optional** run playbook to prepare hosts (only for old centos box):


        ansible-playbook prepare_hosts.yml



run main playbook

                
        ansible-playbook playbook.yml


it will install fuse fabric cluster.

verify if fuse-fabric started and works correctly.
you should see one root container and two ssh containers.

apply patch to fabric:


       ansible-playbook patch-apply-playbook.yml



description of patch process links:

[ Patching a Fabric Container with a Rollup Patch](https://access.redhat.com/documentation/en-US/Red_Hat_JBoss_Fuse/6.2.1/html/Configuring_and_Running_JBoss_Fuse/ESBRuntimePatchFabricRollup.html)


[https://access.redhat.com/solutions/2940541](https://access.redhat.com/solutions/2940541)

