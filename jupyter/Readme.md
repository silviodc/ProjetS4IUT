# Install

## At IUT-ORSAY

Run the command:

```docker
docker build --build-arg http_proxy=http://proxy.iut-orsay.fr:3128 --build-arg https_proxy=http://proxy.iut-orsay.fr:3128 -t jupyternotebook .
```
Wait until the image be ready

```docker
docker run --name "myContainerJupyter" -p 8888:8888 -e GRANT_SUDO="yes" -v $PWD/notebook:/home/jovyan/work/ -it jupyternotebook
```

## At home

```docker
docker-compose up
```

## Access the server

Go to: http://localhost:8888

## Modify the files

The jupyter notebooks you created will go to folder: /notebook
The changes will be direct reflected in your disk
