#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='sadb',
    version='0.0.2',
    author='linroid',
    author_email='linroid@gmail.com',
    url='https://linroid.com',
    description=u'在多设备时更方便地操作adb',
    packages=['sadb'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'sadb=sadb:sadb'
        ]
    }
)
