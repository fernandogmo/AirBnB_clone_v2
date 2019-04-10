#!/usr/bin/python3
'''
Fabric script that generates a `.tgz` archive from
the contents of the `web_static` folder of your
AirBnB Clone repo, using the function `do_pack`.
'''
from os import makedirs
from os.path import exists, basename
from fabric.api import *
from datetime import datetime


@runs_once
def do_pack():
    '''
    On the local machine:
        Creates `versions` dir and archives timestamped `web_static` inside.

    Returns filepath on success, else `None`.
    '''
    if not exists('versions'):
        makedirs('versions')
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filepath = 'versions/web_static_' + timestamp + '.tgz'
    # local('echo ' + filepath)
    pack = local('tar -cvzf ' + filepath + ' web_static')
    return None if pack.failed else filepath


env.hosts = ['35.237.166.85', '35.227.65.117']


def do_deploy(archive_path):
    '''
    On the local machine:
       TODO description.

    Returns `True` on success, else `False`.
    '''
    try:
        tarfile = basename(archive_path)
        if exists('/tmp/' + tarfile):
            run('rm -rf /tmp/' + tarfile)
        put(archive_path, '/tmp/')
        dest = '/data/web_static/releases/' + tarfile.split('.')[0] + '/'
        run('rm -rf ' + dest)
        run('mkdir -p ' + dest)
        run('tar -xzf /tmp/' + tarfile + ' -C ' + dest)
        run('rm -r /tmp/' + tarfile)
        run('mv ' + dest + 'web_static/* ' + dest)
        run('rm -rf ' + dest + 'web_static')
        run('unlink /data/web_static/current')
        run('ln -sf ' + dest + ' /data/web_static/current')
        print('New version deployed!')
        return True
    except Except:
        return False


def deploy():
    '''Runs do_pack and do_deploy'''
    filepath = do_pack()
    if filepath:
        exit_status = do_deploy(filepath)
        return exit_status
    else:
        return False
