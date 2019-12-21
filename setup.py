#!/usr/bin/env python
#coding=utf8

try:
    from  setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
        name = 'pybase',
        version = '1.0',
        install_requires = [], 
        description = 'base objects',
        url = 'https://github.com/zhouxianggen/pybase.git', 
        author = 'zhouxianggen',
        author_email = 'zhouxianggen@gmail.com',
        classifiers = [ 'Programming Language :: Python :: 3.8',],
        packages = ['pybase'],
        data_files = [ ],  
        entry_points = { }   
        )
