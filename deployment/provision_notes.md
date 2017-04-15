For a new site
--------------

## Required OS packages
* nginx
* Python 3 (check b4 install)
* git
* screen (check if installed)
* pip
    * virtualenv

## Nginx virtual host config

* see nginx_tmpl.conf
* replace <xx> with appropriate values

## Systemd config for gunicorn

* see gunicorn_systemd_unit.service
* replace <..> with appropriate values

## Folder structure
/<some>/<path>/
|-- sites
      |-<SITENAME>
         |-database
         |-source
         |-static
         |-virutalenv
