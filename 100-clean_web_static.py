#!/usr/bin/python3
import os
from fabric.api import *

env.hosts = ['100.25.19.204', '54.157.159.85']


def do_clean(number=0):
    """Delete out-of-date_archives.

    Args:
        number (int): The_number_of_archives to_keep.

    If number is 0 or 1, keeps_only the_most recent_archive. If
    number is 2, keeps_the most_and second-most_recent_archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
