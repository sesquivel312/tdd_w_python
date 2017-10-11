#!/usr/bin/env python3

"""
Uses fabric3 to facilitate automating tasks against hosts on which you'd manually use SSH
to carry out admin tasks.  Fabric3 is a "drop in" fork of fabric supporting python3.  See
the regular fabric docs for info, usage, etc.

At a very high-level, you do this:

fabric <command>[:<args>]

fabric looks for a file called fabfile.py in the current directory and runs the function
called <command>.  fabric will include a "directory" like object full of config and other
environment/state variables, including the ones you pass using the <args> optional arguments.
You can include args like this if you like:

    :arg1=value1,...
"""


from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run
import random

REPO_URL = 'https://github.com/sesquivel312/tdd_w_python.git'


def _create_dirs(dir):

    for subdir in ('database', 'static', 'virtualenv', 'source'):
        run(f'mkdir -p {dir}/{subdir}')


def _get_source(dir):

    # if the .git diectory exits, the cd to it and fetch current code from remote repo
    # else clone the repo (assume it doesn't exist)
    if exists(f'{dir}/.git'):
        run(f'cd {dir} && git fetch')
    else:
        run(f'git clone {REPO_URL} {dir}')

    # git command prints one log entry (assume latest) and formats output based
    # on the format string given, which, in this case, is just the commit hash
    # so, this line stores the most recent commit hash in the variable current_commit
    curr_commit = local('git log -n 1 --format=%H', capture=True)

    # change to repo dir on the server and reset to the latest commit
    # need to have run a git push at least once for this to work
    run(f'cd {dir} && git reset --hard {curr_commit}')


def _update_settings(dir, site):
    settings = f'{dir}/superlists/settings.py'

    sed(settings, 'DEBUG = True', 'DEBUG = False')
    sed(settings, 'ALLOWED_HOSTS =.+$', f'ALLOWED_HOSTS = ["{site}"]')

    secret = f'{dir}/superlists/secret_key.py'

    if not exists(secret):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))  # generator expression inside join()
        append(secret, f'SECRET_KEY="{key}"')

    append(settings, '\nfrom .secret_key import SECRET_KEY')


def _update_venvs(dir):
    venv_dir = f'{dir}/../virtualenv'

    if not exists(f'{venv_dir}/bin/pip'):
        run(f'python3 -m venv {venv_dir')
    run(f'{venv_dir}/bin/pip install -r {dir}/requirements.txt')


def _update_static(dir):
    run(f'cd {dir} && ../virtualenv/bin/python manage.py collectstatic --noinput')


def _update_db(dir):
    run(f'cd {dir} && ../virtualenv/bin/python manage.py migrate --noinput')



def deploy():
    site_folder = f'/home/{env.user}/sites/{env.host}'
    source_folder = f'{site_folder}/source'
    _create_dirs(site_folder)
    _get_source(source_folder)
    _update_settings(source_folder, env.host)
    _update_venvs(source_folder)
    _update_static(source_folder)
    _update_db(source_folder)
