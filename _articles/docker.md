---
title: Docker Commands
date: 2017-09-23
layout: article
---

# Docker Commands

An overview of various Docker commands are discussed below. The commands were
tested on a Mac running running but they should be similar on other systems.

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

List all images on your local system:

```bash
docker images
```

Remove an image:

```bash
docker rmi imageName
```

## Containers

Show all running Docker containers:

```bash
docker ps
```

To see all containers, even ones that are not running:

```bash
docker ps -a
```

Stop and remove a running container named "mycontainer":

```bash
docker rm -f mycontainer
```

## Volumes

List all the volumes that Docker knows about:

```bash
docker volume ls
```

Removing containers that were not created with the `-v` option can cause
dangling volumes which are no longer referenced by a container. To find
dangling volumes use the command:

```bash
docker volume ls -f dangling=true
```

Use the following command to remove a volume called "myvolume" that is no
longer needed:

```bash
docker volume rm myvolume
```

## Files

Copy files from a Docker container named "mycontainer" to the host machine:

```bash
docker cp mycontainer:/file/path/within/container /host/path/
```

