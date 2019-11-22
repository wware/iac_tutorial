# The first Ansible example

I did this work in a Virtualbox VM starting with an Ubuntu 16.04 desktop installation.

I installed Ansible and Docker for this work, using Ansible both to construct the Docker
image and to kick off three Docker instances.

[Super useful Ansible info](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-ansible-on-ubuntu-18-04)

## Try this

Pull down the repository and run some webserver Docker containers, test them, get rid of them.

```
cd iac_tutorial/ansible1
sudo ansible-playbook docker_build.yml
sudo ansible-playbook docker_go.yml
curl http://localhost:5000/     # value1
curl http://localhost:5001/     # value2
curl http://localhost:5002/     # value3
sudo ansible-playbook docker_stop.yml
```

## Make life a little easier

All these `sudo`s can go away if you do this. You'll probably need to log out and log back in,
or possibly even reboot your laptop.
```
sudo usermod -aG docker $(whoami)
```

## Avoid frustration

Building the `simple_flask:0.1` image can be quite time-consuming, and Ansible won't give you any
visible feedback during that time, so you won't know if anything is going wrong. Personally I hate
that kind of situation, so I prefer to skip the `docker_build.yml` step and build manually:

```
docker build -t simple_flask:0.1 --rm .
```
