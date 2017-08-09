#!/bin/bash
set -x
set -e

REGISTRY_BASE=908991866159.dkr.ecr.eu-west-1.amazonaws.com
APP=fx-engine-py
VERSION=$(git describe --always)

if [[ ! -z $(git status --porcelain 2> /dev/null | tail -n1) ]]; then
			# If the "git status" is dirty, add the time of the build:
      VERSION=$VERSION-dirty-$(date +%Y-%m-%dT%H-%M-%S)
fi
IMAGE=$REGISTRY_BASE/$APP:$VERSION

echo Starting deploy

docker build . -t $IMAGE 1>/dev/null

echo Logging-in into docker ECR
eval $(aws ecr get-login | sed 's/-e none//')

echo Pushing docker image
docker push $IMAGE


kubectl set image deployment/fx-engine fx-engine=$IMAGE && echo Success!
