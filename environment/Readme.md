# Install

## At IUT-ORSAY salle RDC

Run the command:


```docker
docker run -p 3306:3306 --name myserver -e MYSQL_ROOT_PASSWORD=S4_2018 -e MYSQL_DATABASE=S4_2018 -d mysql:latest
```

```docker
docker run --name myadmin -e MYSQL_ROOT_PASSWORD=S4_2018 -e MYSQL_PASSWORD=S4_2018 -d --link myserver:db -p 8080:80 phpmyadmin/phpmyadmin
```

```docker
docker build -t twitterapp .
```
Wait until the image be ready

```docker
docker run -p 8899:8899 --name mytwitter --link myserver -d -e MYSQL_ROOT_PASSWORD=S4_2018 -e MYSQL_DATABASE=S4_2018 -e MYSQL_USER=root -e MYSQL_DB_HOST=$(docker inspect myserver --format '{{ .NetworkSettings.IPAddress }}') -v $PWD/python-code/:/twitter/  twitterapp
```



## At IUT-ORSAY Salle Réseaux

Run the command:


```docker
docker run -p 3306:3306 --name myserver -e MYSQL_ROOT_PASSWORD=S4_2018 -e MYSQL_DATABASE=S4_2018 -d mysql:latest
```

```docker
docker run --name myadmin -e MYSQL_ROOT_PASSWORD=S4_2018 -e MYSQL_PASSWORD=S4_2018 -d --link myserver:db -p 8080:80 phpmyadmin/phpmyadmin
```

```docker
docker build --build-arg http_proxy=http://proxy.iut-orsay.fr:3128 --build-arg https_proxy=https://proxy.iut-orsay.fr:3128 -t twitterapp .
```
Wait until the image be ready

```docker
docker run -p 8899:8899 --name mytwitter --link myserver -d -e MYSQL_ROOT_PASSWORD=S4_2018 -e MYSQL_DATABASE=S4_2018 -e MYSQL_USER=root -e MYSQL_DB_HOST=$(docker inspect myserver --format '{{ .NetworkSettings.IPAddress }}') -v $PWD/python-code/:/twitter/  twitterapp
```


## At home ou IUT-ORSAY Salle RDC

```docker
docker-compose up
```

## AT IUT-ORSAY Salle Réseaux

```docker
./runCompose.sh
```

## Access the server

To access the twitter app go to: http://localhost:8899

To access the phpmyadmin go to: http://localhost:8080


## Modify the files

Case you perform any change in /python-code the docker container must be stoped and relaunched

Example: docker stop 10b213i1
docker start 10b213i1
