# Docker Dasar

### Mengambil Image MySQL dari Container Registry (Docker Hub)

```
$ docker images
$ docker pull mysql:8.0.1
```

### Membuat & Menjalankan MySQL di Docker Container

```
$ docker container create --name sacode_mysql -e MYSQL_ROOT_PASSWORD=sacode mysql:8.0.1
$ docker container start sacode_mysql
```

**Access Database Interactive Terminal**

```
$ docker exec -it nama_container_mysql mysql -u root -p
```

---

### Menjalankan PHPMyAdmin di Docker Container

```
$ docker run --name phpmyadmin -d --link sacode_mysql:db -p 8081:80 phpmyadmin/phpmyadmin
```

**Buka PHPMyAdmin di Browser:** 

- ```localhost:8081```

---

### Menjalankan Aplikasi PHP di Docker Container

```
$ docker run -d -p 8080:80 -v "$PWD":/var/www/html php:7.4-apache
```

**Buka Aplikasi PHP di Browser:** 

- ```localhost:8080```