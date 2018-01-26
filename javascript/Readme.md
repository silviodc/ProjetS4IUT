# Install

## At IUT-ORSAY Salle RDC

Run the command:

```docker
docker build -t apacheserver .
```
Wait until the image be ready

```docker
docker run --name "myContainerApache" -p 8889:80 -p 8443:443 -v $PWD/code:/app/ -it apacheserver
```

## At IUT-ORSAY Salle Réseaux

Run the command:

```docker
docker build --build-arg http_proxy=http://proxy.iut-orsay.fr:3128 --build-arg https_proxy=https://proxy.iut-orsay.fr:3128 -t apacheserver .
```
Wait until the image be ready

```docker
docker run --name "myContainerApache" -p 8889:80 -p 8443:443 -v $PWD/code:/app/ -it apacheserver
```

## At home ou IUT-ORSAY Salle RDC

```docker
docker-compose up
```

## IUT-ORSAY Salle Réseaux

```docker
./runCompose.sh
```

## Access the server

Go to: http://localhost:8889

## Modify the files

The javascript files as well html code must to be created in the folder: /code
The changes will be direct reflected in your disk no need to restart the container
