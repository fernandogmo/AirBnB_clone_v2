#!/usr/bin/python3
'''
Fabric script that generates a `.tgz` archive from
the contents of the `web_static` folder of your
AirBnB Clone repo, using the function `do_pack`.
'''
from os import makedirs
from os.path import exists
from fabric.api import *
from datetime import datetime


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
    pack = local('tar -cvfz ' + filepath + ' web_static')
    if exists(filepath):
        return filepath
    else:
        return None
