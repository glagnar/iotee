# Nodered Template for IDA

[![Twitter: @thomasbjgilbert](https://img.shields.io/badge/contact-@thomasbjgilbert-blue.svg?style=flat)](https://twitter.com/thomasbjgilbert)
[![Language: Javascript](https://img.shields.io/badge/lang-Javascript-yellow.svg?style=flat)](https://nodered.org)
[![License: AGPL-3.0](https://img.shields.io/badge/license-AGPL-lightgrey.svg?style=flat)](http://opensource.org/licenses/AGPL-3.0)

## What is the template for ?
It is a starting point for any NodeRed projects you may need. I will make up more documentation as we go along.

## Features
- You can do whatever you like with it
- For **beginners**
- **Not** for production just yet

## WARNING
IF YOU CHOOSE TO COMMIT YOUR SECURITY TOKENS TO GIT THEN YOU ARE ON YOUR OWN
IF YOU BUILD YOU DOCKER IMAGE WITH SECURITY TOKENS THEN YOU ARE ON YOUR OWN

## Getting started
After cloning the REPO you can either start designing your flows with this command, without any extensions or anything.
```
docker run --rm -it -p 1880:1880 -p 1883:1883 -v $PWD/node-red-data:/data nodered/node-red-docker
```

On windows you may have to type on of these two commands
```
docker run --rm -it -p 1880:1880 -p 1883:1883 -v %cd%/node-red-data:/data nodered/node-red-docker
docker run --rm -it -p 1880:1880 -p 1883:1883 -v ${PWD}/node-red-data:/data nodered/node-red-docker
```

Once you are happy, you can build a container with all your flows etc. with this command. This will copy node-red-data folder into the container and install extra npm dependencies as specified in Dockerfile
```
docker build -t yournamehere .
```

If you dont want the vanilla Nodered experience, but require additional npm packages, add them to the Dockerfile and build the image as described above. Once done, simply run the command below which will use your new image instead, while still mounting the host volume.
```
docker run --rm -it -p 1880:1880 -p 1883:1883 -v $PWD/node-red-data:/data yournamehere
```

## Have fun
