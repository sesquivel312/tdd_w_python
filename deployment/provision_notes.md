For a new site
--------------

## Required OS packages
* nginx
* Python 3 (check b4 install)
* git
* screen (check if installed)
* pip
    * virtualenv  << may not be necessary b/c venv is included in python 3 (at least 3.6)
    * gunicorn (WSGI app server)

## Nginx virtual host config

* see nginx_tmpl.conf
* replace <xx> with appropriate values

## Gunicorn
### Systemd config for gunicorn
* see gunicorn_systemd_unit.service
* replace <..> with appropriate values

### Unix sockets
* Using unix sockets for comms between WSIG app sever and NGINX may be better than starting Gunicorn on different ports - one for live and another for stage
* For this tutorial, created a socket @ /tmp/stage.socket
* Use this command to start it:
    ../virtualenv/bin/gunicorn --bind unix:/tmp/stage.socket superlists.wsgi:application

## Folder structure
/<some>/<path>/
|-- sites
      |-<SITENAME>
         |-database
         |-source
         |-static
         |-virutalenv
