#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "dnspython",
    "PyYAML"
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='onionrouter',
    version='0.1.0',
    description="Python Routed Onion Deliveries",
    long_description=readme + '\n\n' + history,
    author="Ehlo Onion",
    author_email='onionmx@lists.immerda.ch',
    url='https://github.com/ioparaskev/onionrouter',
    packages=[
        'onionrouter',
    ],
    package_dir={'onionrouter':
                 'onionrouter'},
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='onionrouter',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)