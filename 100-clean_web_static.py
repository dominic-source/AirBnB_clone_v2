#!/usr/bin/python3
"""Clean up all the mess"""
from fabric.api import env
from fabric.operations import sudo, run, local
from fabric.context_managers import lcd, cd


env.hosts = ['3.94.185.85', '100.24.255.207']


def do_clean(number=0):
    """Clean up the archive"""

    if number == 0 or number == 1:
        val = 1
    else:
        val = int(number) - 1
    with cd("/data/web_static/releases"):
        sudo("ls -t | tail -n +{} | xargs -I {{}} rm -rf {{}}".format(val + 1))

    with lcd("versions"):
        local("ls -t | tail -n +{} | xargs -I {{}} rm -rf {{}}".format(val + 1))
