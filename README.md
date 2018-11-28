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


### deploy
```
docker stack deploy -c docker-compose.yml django
```

### setup
```
docker container exec -it <--django container--> bash
```
```
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```

### add firewall rules
tcp/8080