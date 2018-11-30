# Docker Swarm Deploy

### add production module
```
vim trading_sample/settings/production.py
```

### build image
```
docker image build --rm -t python:django ./src
docker image build --rm -t nginx:django ./nginx
```

### add secrets
```
echo "<--username-->" | sudo docker secret create pg_username -
echo "<--password-->" | sudo docker secret create pg_password -
```

### add configs
```
docker config create nginx nginx/nginx.conf
docker config create my_nginx nginx/my_nginx.conf
```

### generate certificates
```
docker run --rm \
  -p 443:443 -p 80:80 --name letsencrypt \
  -v "/etc/letsencrypt:/etc/letsencrypt" \
  -v "/var/lib/letsencrypt:/var/lib/letsencrypt" \
  certbot/certbot certonly -n \
  -m "YOUR_EMAIL" \
  -d example.com \
  --standalone --agree-tos
```

### deploy
```
docker stack deploy -c docker-compose.yml django
```

### django setup
```
docker container exec -it <--django container--> bash
```
```
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```

### renew certificates
```
docker run --rm --name letsencrypt \
    -v "/etc/letsencrypt:/etc/letsencrypt" \
    -v "/var/lib/letsencrypt:/var/lib/letsencrypt" \
    -v "/usr/share/nginx/html:/usr/share/nginx/html" \
    certbot/certbot:latest \
    renew --quiet
```

### references
* [SSL with Docker Swarm, Let's Encrypt and Nginx](https://finnian.io/blog/ssl-with-docker-swarm-lets-encrypt-and-nginx/)
* [docker-django-nginx-uwsgi-postgres-tutorial](https://github.com/twtrubiks/docker-django-nginx-uwsgi-postgres-tutorial)

### helpful command

check address already in use or not
```
netstat -pna | grep $THE_PORT
```

check service errors
```
docker service ps --no-trunc <--service name-->
```

### next step
1. split compose files
2. Django settings via Docker secrets
