#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='sadb',
    version='0.0.6',
    author='linroid',
    author_email='linroid@gmail.com',
    url='https://linroid.com',
    description=u'在多设备时更方便地操作adb',
    packages=['sadb'],
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        ],
    entry_points={
        'console_scripts': [
            'sadb=sadb:sadb'
        ]
    }
)