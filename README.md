# Tutorial on Infrastructure-as-Code

This repository is a collection of examples and explanations of the concept of
infrastructure-as-code and of the tools used to implement that concept. The
[Wikipedia article](https://en.wikipedia.org/wiki/Infrastructure_as_Code) is a
great place to start.

This repository is also intended to accompany the
[Wikibook on this topic](https://simple.wikibooks.org/wiki/Getting_Started_with_Infrastructure_as_Code)
that I am putting together. For a while, both the repository and the wikibook are
going to be a work in progress. This is as much an exercise in self-education as
anything else.

## Set up a Virtualbox sandbox for this stuff

* Create an empty Ubuntu 16.04 instance from the ISO.
    * Download a copy of the 16.04 desktop ISO. I'm using a 64-bit Intel processor.
    * Choose Ubuntu 64-bit for the type of virtual machine you're creating.
    * Get a decent amount of RAM, I'm choosing 6 gig.
    * Create a virtual hard disk, VDI format, dynamically allocated, 20 gigs.
    * System > Processor, enable PAE/NX
    * Display > Screen, enable 3d acceleration
    * Storage - select the 16.04 ISO as the optical drive for this VM
    * Click OK at the bottom.
* Hit "Start" to begin the installation. Click thru all the standard stuff.
* Apt-get fun
    * sudo apt-get update; sudo apt-get upgrade
    * sudo apt-get install -y build-essential vim git curl linux-headers-$(uname -r)
    * Install Guest Additions CD and click thru the "install this stuff" thing
        * Devices > Shared clipboard > Bidirectional
        * Devices > Drag and drop > Bidirectional
        * Eject disk
    * Restart the VM. Not sure if this is strictly necessary at this point.
    * Follow instructions at https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04
        * sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
        * sudo apt-get update; sudo apt-get install -y --allow-unauthorized docker-ce
        * sudo systemctl status docker     # should show some Docker log statements
        * sudo docker run hello-world     # should show "Hello from Docker!" among other things
    * Follow instructions at https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-ansible-on-ubuntu-16-04
        * sudo apt-get update; sudo apt-get install -y software-properties-common
        * sudo apt-add-repository ppa:ansible/ansible
        * sudo apt-get update; sudo apt-get install -y ansible
* Python stuff
    * sudo apt-get install python-setuptools
    * sudo easy_install pip virtualenv
    * sudo pip install docker-py
* Pull down this repository
    * git clone https://github.com/wware/iac_tutorial.git
