### Commands

#### Run an ephemeral container

oc run test-pod --image=ubuntu  --rm -it -- /bin/sh
oc run test-pod --image=docker.io/username/cat-game:latest --image-pull-policy="Always" --rm -it 

#### Create a new app

oc new-app docker.io/username/cat-game:latest --name=exploding-kittens-app