# Configure Docker provider and connect to the local Docker socket
provider "docker" {
  host = "unix:///var/run/docker.sock"
}

resource "docker_container" "foo1" {
  image = "simple_flask:0.1"
  name  = "foo1"
  ports {
    internal = 5000
    external = 5000
  }
  command = ["python", "hello.py"]
  env = [
    "KEY=value0"
  ]
}

resource "docker_container" "foo2" {
  image = "simple_flask:0.1"
  name  = "foo2"
  ports {
    internal = 5000
    external = 5001
  }
  command = ["python", "hello.py"]
  env = [
    "KEY=value1"
  ]
}

resource "docker_container" "foo3" {
  image = "simple_flask:0.1"
  name  = "foo3"
  ports {
    internal = 5000
    external = 5002
  }
  command = ["python", "hello.py"]
  env = [
    "KEY=value2"
  ]
}
