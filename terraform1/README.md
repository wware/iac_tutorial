# Terraform

First you need to install it in your Virtualbox instance.

* https://releases.hashicorp.com/terraform/0.11.7/terraform_0.11.7_linux_amd64.zip
* https://www.terraform.io/intro/getting-started/install.html

```
$ unzip terraform_0.11.7_linux_amd64.zip
Archive:  terraform_0.11.7_linux_amd64.zip
  inflating: terraform
$ sudo mv terraform /usr/local/bin
$ rm terraform_0.11.7_linux_amd64.zip
```

## OK, it's installed, now what?

[Terraform can do Docker.](https://www.terraform.io/docs/providers/docker/index.html)
And it turns out
[Docker containers can run on AWS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html)
(see [slideshow](https://www.slideshare.net/brikis98/an-intro-to-docker-terraform-and-amazon-ecs)).

Interesting Github gist:
[The Simplest Terraform with Docker on macOS](https://gist.github.com/brianshumate/09adf967c563731ca1b0c4d39f7bcdc2)
