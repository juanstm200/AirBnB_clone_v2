#!/usr/bin/python3
""" This module generates a .tgz """

from fabric.api import env, put, run
from os.path import exists


def do_deploy(archive_path):
    """Is a Fabric script function do_deploy"""

    env.hosts = ["35.185.4.79", "35.196.72.165"]

    if not exists(archive_path):
        return False

    try:
        name_extention = archive_path.split("/")[-1]
        name = name_extention.split(".")[0]
        path = "/data/web_static/releases/"

        put(archive_path, "/tmp/")
        run("mkdir -p {}{}/".format(path, name))
        run("tar -xzf /tmp/{} -C {}{}/".format(name_extention, path, name))
        run("rm /tmp/{}".format(name_extention))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, name))
        run('rm -rf {}{}/web_static'.format(path, name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, name))

        return True

    except Exception:
        return False
