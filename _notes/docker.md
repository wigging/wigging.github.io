---
title: Docker
excerpt: Useful commands for working with containers.
date: 2016-11-05
---

# Docker commands

An overview of various Docker commands are discussed below. The commands were
tested on a Mac but they should be similar on other systems.

## Images

Run a Docker container from an image named "myimage":

```bash
docker run myimage
```

Run an interactive container from an image named "myimage" from a Bash shell
inside the container:

```bash
docker run -it myimage bash
```

List all images on your local system and remove an image:

```bash
docker images
docker rmi imageName
```

## Containers

Useful commands when dealing with Docker containers are shown below. The example refers to a container named "mycontainer".

```bash
# Show all running containers
docker ps

# Show all running and not running containers
docker ps -a

# Stop and remove a running container
docker rm -f mycontainer
```

## Volumes

Commands for working with volumes in Docker are shown below. The example refers to a volume named "myvolume".

```bash
# List all volumes seen by Docker
docker volume ls

# Remove a volume
docker volume rm myvolume
```

Removing containers that were not created with the -v option can cause
dangling volumes which are no longer referenced by a container. To find
dangling volumes use the command:

```bash
docker volume ls -f dangling=true
```

## Files

Copy files from a Docker container named "mycontainer" to the host machine:

```bash
docker cp mycontainer:/file/path/within/container /host/path/
```

