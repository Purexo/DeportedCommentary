# Deploy DeportedCommentary in Apache
Inspired from [Bottle Doc](http://bottlepy.org/docs/dev/deployment.html)    
and [Django Doc](https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/modwsgi/)

You need mod_wsgi for apache :
```
sudo apt-get install libapache2-mod-wsgi
sudo service apache2 restart
```

or search the equivalent package if your not on a debian OS
https://code.google.com/p/modwsgi/wiki/InstallationOnLinux for more details

# Old Apache :
```apache
<VirtualHost *>
    ServerName example.com

    WSGIDaemonProcess yourapp user=www-data group=www-data processes=1 threads=5
    WSGIScriptAlias / /var/www/yourapp/app.wsgi
    WSGIPythonPath /path/to/mysite.com:/path/to/your/venv/lib/python3.X/site-packages

    <Directory /var/www/yourapp>
        WSGIProcessGroup yourapp
        WSGIApplicationGroup %{GLOBAL}
        Order deny,allow
        Allow from all
    </Directory>
</VirtualHost>
```

Make sure you give the correct path to your virtualenv, and replace python3.X with the correct Python version (e.g. python3.4).

# New Apache (2.4 >=)
```apache
<VirtualHost *>
    ServerName example.com

    WSGIDaemonProcess yourapp user=www-data group=www-data processes=1 threads=5
    WSGIScriptAlias / /var/www/yourapp/app.wsgi
    WSGIPythonPath /path/to/mysite.com:/path/to/your/venv/lib/python3.X/site-packages

    <Directory /var/www/yourapp>
        WSGIProcessGroup yourapp
        WSGIApplicationGroup %{GLOBAL}
        Require all granted
    </Directory>
</VirtualHost>
```