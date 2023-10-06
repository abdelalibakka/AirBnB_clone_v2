#!/usr/bin/python3
"""Compress_web static_package
"""
from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['18.207.141.252', '54.236.16.254']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/private_key'


def do_deploy(archive_path):
        """Deploy web_files_to_server
        """
        try:
                if not (path.exists(archive_path)):
                        return False

                # upload_archive
                put(archive_path, '/tmp/')

                # create_target_dir
                timestamp = archive_path[-18:-4]
                run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(timestamp))

                # uncompress_archive_and_delete .tgz
                run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'
                    .format(timestamp, timestamp))

                # remove_archive
                run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

                # move_contents_into_host web_static
                run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

                # remove_extraneous_web_static dir
                run('sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static'
                    .format(timestamp))

                # delete_pre-existing sym_link
                run('sudo rm -rf /data/web_static/current')

                # re-establish_symbolic_link
                run('sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(timestamp))
        except:
                return False

        # return_True_on_success
        return True
