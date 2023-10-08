#!/usr/bin/python3
"""This module houses the function for distributing the versions"""

from fabric.api import env
from fabric.operations import sudo, put, local
import os

env.hosts = ['3.94.185.85', '100.24.255.207']


def do_deploy(archive_path):
    """The deployment of the web static files"""

    local("test -e {}".format(archive_path))
    result = local("echo $?")
    if result:
        return False
    res = put(archive_path, "/tmp/")
    filename = os.path.basename(archive_path)
    dfile = filename.split(".")[0]
    op5 = sudo("mkdir -p /data/web_static/releases/{}".format(dfile))
    op1 = sudo("tar -xzf /tmp/{} -C /data/web_static/releases/{}".
               format(filename, dfile))
    op2 = sudo("rm /tmp/{}".format(filename))
    op6 = sudo(
        "mv /data/web_static/releases/{}/web_static/* "
        "/data/web_static/releases/{}/"
        .format(dfile, dfile))
    op7 = sudo("rm -rf /data/web_static/releases/{}/web_static"
               .format(dfile))
    op3 = sudo("rm -rf /data/web_static/current")
    op4 = sudo("ln -s /data/web_static/releases/{} /data/web_static/current"
               .format(dfile))
    if op1.failed or op2.failed or op3.failed or op4.failed:
        return False
    if op5.failed or op6.failed or op7.failed or res.failed:
        return False
    return True
