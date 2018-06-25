# The first simple example

I did this work in a Virtualbox VM starting with an Ubuntu 16.04 desktop installation.

I installed Ansible and Docker for this work, using Ansible both to construct the Docker
image and to kick off three Docker instances.

## Try this

* Pull down the repository and run some webserver Docker containers, test them, get rid of them
    * cd iac_tutorial/simple
    * sudo ansible-playbook docker_go.yml
    * curl http://localhost:5000/     # value1
    * curl http://localhost:5001/     # value2
    * curl http://localhost:5002/     # value3
    * sudo ansible-playbook docker_stop.yml
