#!/usr/bin/env python

# Remove .egg-info directory if it exists, to avoid dependency problems with
# partially-installed packages (20160119/dphiffer)

import os, sys
from shutil import rmtree

cwd = os.path.dirname(os.path.realpath(sys.argv[0]))
egg_info = cwd + "/mapzen.whosonfirst.placetypes-utils.egg-info"
if os.path.exists(egg_info):
    rmtree(egg_info)

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read()
version = open("VERSION").read()

setup(
    name='mapzen.whosonfirst.placetypes.utils',
    namespace_packages=['mapzen', 'mapzen.whosonfirst', 'mapzen.whosonfirst.placetypes', 'mapzen.whosonfirst.placetypes.utils'],
    version=version,
    description='Helper methods for working with Who\'s On First placetypes',
    author='Mapzen',
    url='https://github.com/whosonfirst/py-mapzen-whosonfirst-placetypes-utils',
    install_requires=[
        'mapzen.whosonfirst.placetypes>=0.11',
    ],
    dependency_links=[
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-placetypes/tarball/master#egg=mapzen.whosonfirst.placetypes-0.11',
    ],
    packages=packages,
    scripts=[

        ],
    download_url='https://github.com/whosonfirst/py-mapzen-whosonfirst-placetypes-utils/releases/tag/' + version,
    license='BSD')
