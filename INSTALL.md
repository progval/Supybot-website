In order to deploy this website on a Debian host, you have to run this 
commands as root:

```bash
aptitude install python-django python-django-piston python-markdown \
    python-django-voting python-django-south python-setuptools \
    mysql-server python-mysqldb python-django-mptt python-pygments \
    python-requests python-sphinx
easy_install django-templateaddons django-haystack whoosh
```

Then, configure yourself the WSGI server. You can use this sample Apache
configuration (install package `libapache2-mod-wsgi` first):

```apache
<VirtualHost *:80>
    ServerAdmin progval@gmail.com
    ServerName supybot.aperio.fr

    DocumentRoot /home/progval/Supybot-website/website
    <Directory /home/progval/Supybot-website/website/>
        Order allow,deny
        allow from all
    </Directory>
    WSGIScriptAlias / /home/progval/Supybot-website/website/django.wsgi
    Alias /media/ /home/progval/Supybot-website/website/media/
    Alias /static/ /home/progval/Supybot-website/website/static/
    Alias /doc/ /home/progval/Supybot-website/website/doc/_build/html/

</VirtualHost>
```
