# Dockerfile

**Membuat Aplikasi PHP Menjadi Image Docker**

```
$ docker build -t sacode-php:1.1 .
```

**Membuat & Menjalankan Aplikasi PHP menggunakan Image yang dibuat sebelumnya**

```
$ docker run -it --name my-sacode-app -p 8080:80 sacode-php:1.1
```

**Buka Aplikasi PHP di Browser:** 

- ```http://127.0.0.1:8080```


**Access Database Interactive Terminal**

```
$ docker exec -it my-sacode-app mysql -u root -p
```


**Upload Images ke Docker Registry**

```
$ docker tag sacode-php:1.1 YOUR_DOCKERHUB_USER/sacode-php
$ docker login
$ docker push YOUR_DOCKERHUB_USER/sacode-php
```
