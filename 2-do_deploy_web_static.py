#!/usr/bin/python3
'''
Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the
function `do_deploy`.
Usage:
fab -f 2-do_deploy_web_static.py do_deploy:archive_path=versions/web_static_20170315003959.tgz -i my_ssh_private_key -u ubuntu
'''
from os import makedirs
from os.path import exists, basename
from fabric.api import *
from datetime import datetime


env.hosts = ['35.237.166.85', '35.227.65.117']

def do_deploy(archive_path):
    '''
    On the local machine:
       TODO description.

    Returns `True` on success, else `False`.
    '''
    try:
        run('ls -l /tmp/')
        tarfile = basename(archive_path)
        if exists('/tmp/' + tarfile):
            print('FILE FOUND')
            run('rm -r /tmp/' + tarfile)
        run('ls -l /tmp/')
        put(archive_path, '/tmp/')
        dest = '/data/web_static/releases/' + tarfile.split('.')[0] + '/'
        if exists(dest):
            run('rm -r' + dest)
        run('mkdir -p ' + dest)
        run('tar -xzf /tmp/' + tarfile + ' -C ' + dest)
        run('rm -r /tmp/' + tarfile)
        run('unlink /data/web_static/current')
        run('ln -sf ' + dest + ' /data/web_static/current')
        print('New version deployed!')
        return True
    except:
        return False
