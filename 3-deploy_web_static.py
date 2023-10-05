#!/usr/bin/python3
""" This module bundles the full deploy"""
do_deploy = __import__("2-do_deploy_web_static").do_deploy
do_pack = __import__("1-pack_web_static").do_pack


def deploy():
    """deploy code automatically"""

    archive_path = do_pack()
    if archive_path is None:
        return False
    value = do_deploy(archive_path)
    return value
