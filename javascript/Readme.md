# Install

## At IUT-ORSAY

Run the command:

```docker
docker build -t apacheserver .
```
Wait until the image be ready

```docker
docker run --name "myContainerApache" -p 80:80 -p 443:443 -v $PWD/code:/app/ -it apacheserver
```

## At home

```docker
docker-compose up
```

## Access the server

Go to: http://localhost:80

## Modify the files

The javascript files as well html code must to be created in the folder: /code
The changes will be direct reflected in your disk no need to restart the container
