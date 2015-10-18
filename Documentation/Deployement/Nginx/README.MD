# Deploy DeportedCommentary in Nginx
Inspired from https://michael.lustfield.net/nginx/bottle-uwsgi-nginx-quickstart

```apt-get install uwsgi uwsgi-plugin-python python-bottle nginx```

Edit /etc/uwsgi/apps-available/bottle.ini:

```
[uwsgi]
socket = /run/uwsgi/app/bottle/socket
chdir = /var/www/bottle
master = true
plugins = python
file = app.wsgi
uid = www-data
gid = www-data
```

```
ln -s /etc/uwsgi/apps-available/bottle.ini /etc/uwsgi/apps-enabled/bottle.ini
service uwsgi restart
```

Edit /etc/nginx/conf.d/bottle.conf:

```
upstream _bottle {
    server unix:/run/uwsgi/app/bottle/socket;
}

server {
    listen [::]:80;
    listen 80;
    server_name deb.ngx.cc;
    root /var/www/bottle;

    location / {
        try_files $uri @uwsgi;
    }

    location @uwsgi {
        include uwsgi_params;
        uwsgi_pass _bottle;
    }
}
```

```
service nginx restart
```
