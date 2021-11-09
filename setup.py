# setup.py for readthedocs. We need this to install into a venv so we
# can pull in dependencies.
from setuptools import setup

import os.path

if os.path.exists('test_requirements.txt'):
    reqs = open('test_requirements.txt', 'r').read().splitlines()
else:
    reqs = []


if __name__ == '__main__':
    setup(name='interface-pgbouncer-extra-config',
          version='1.0.0',
          author='Aymen Frikha',
          author_email='aymen.frikha@canonical.com',
          license='GPL3',
          py_modules=['requires'],
          install_requires=reqs)
