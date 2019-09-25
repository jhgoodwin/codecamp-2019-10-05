# Not your Daddy's Docker 101

by John Goodwin

## Agenda

- Attendee Intentions
- Docker in 60 seconds
- Demo
- Decomposition of Demo
  - Process
  - Environment
  - Storage / Mounts
  - Network
  - cgroup
  - pipelining
  - signals
- Q&A
- Resources

## Attendee Intentions

At this time, want to ask each person what they hoped this talk would cover.

## Docker in 60 seconds

- <https://docs.docker.com/engine/docker-overview/>

## Demo

```shell
docker run python:3.7-alpine python3 --version
docker run python:3.7-alpine python3 -c 'print("Hello codecamp!")'
```

## Process

```shell
docker ps -a
docker inspect
```

- Path
- Args
- State

## Environment

- Config

## Storage / Mounts

- Union Filesystems
- Mounts

## Network

- resolv.conf
- hostname
- hosts
- NetworkSettings

## cgroup

- what are cgroups
- HostConfig

> cgroups (abbreviated from control groups) is a Linux kernel feature that limits, accounts for, and isolates the resource usage (CPU, memory, disk I/O, network, etc.) of a collection of processes.
> Engineers at Google (primarily Paul Menage and Rohit Seth) started the work on this feature in 2006 under the name "process containers".
>> source <https://en.wikipedia.org/wiki/Cgroups>

## pipelining

```shell
docker run --rm python:3.7-alpine python3 --version > version.txt && cat version.txt
```

<div style="background-color:silver; text-align:center; vertical-align: middle; padding:10px 10px;">
  <img src="images/Stdstreams-notitle.svg" width="100%" />
</div>

## signals

- <https://www.gnu.org/software/libc/manual/html_node/Termination-Signals.html>
- entrypoint vs command

```shell
docker run --rm -it --mount type=bind,source=$(pwd)/sigterm.py,dst=/tmp/sigterm.py python:3.7-alpine python3 /tmp/sigterm.py
```

(note this is the same)

```shell
docker run --rm -it --mount type=bind,source=$(pwd)/sigterm.py,dst=/tmp/sigterm.py --entrypoint=/bin/sh python:3.7-alpine -c "python3 /tmp/sigterm.py"
```

(but this hangs)

```shell
docker run --rm -it --mount type=bind,source=$(pwd),dst=/app python:3.7-alpine /app/callsigterm.sh
```

## Q&A

## Resources

- <https://docs.docker.com/>
- <https://katacoda.com/>
