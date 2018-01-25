# Install

## At IUT-ORSAY

Run the command:

```docker
docker build -t jupyternotebook .
```
Wait until the image be ready

```docker
docker run --name "myContainerJupyter" -p 8888:8888 -v $PWD/notebook:/home/jovyan/work/ -it jupyternotebook
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
