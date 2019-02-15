#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ 'ndex2==3.0.0a1',
                 'ndexutil==0.1.0a2',
                 'biothings_client',
                 'requests',
                 'pandas']

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Chris Churas",
    author_email='contact@ndexbio.org',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Loads NCI-PID data into NDEx",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='ndexncipidloader',
    name='ndexncipidloader',
    packages=find_packages(include=['ndexncipidloader']),
    scripts=[ 'ndexncipidloader/loadndexncipidloader.py'],
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/coleslaw481/ndexncipidloader',
    version='0.1.0',
    zip_safe=False,
)
