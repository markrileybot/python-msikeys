#!/usr/bin/env python

from setuptools import setup

setup(
    name='msikeys',
    version='0.0.1',
    author='Mark Riley',
    author_email='mark@markriley.net',
    url='https://github.com/markrileybot/python-msikeys',
    license='MIT',
    description=open('README.md').readline(),
    long_description=open('README.md').read(),
    scripts=[
        'bin/msikeys-config.py',
        'bin/msikeys-init.py'
    ],
    packages=[
        # library
        'msikeys',
        # gui
        'msikeys.ui',
    ],
    install_requires=[
        'hidapi >= 0.7.99',
        'iniparse >= 0.4',
    ],
    extras_require={
        'wxWidgetsApp': ['wxpython >= 3.0.2'],
    },
    zip_safe=True
)
