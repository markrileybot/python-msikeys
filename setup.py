#!/usr/bin/env python

from setuptools import setup

VERSION = '0.0.3'

setup(
    name='msikeys',
    version=VERSION,
    author='Mark Riley',
    author_email='mark@markriley.net',
    url='https://github.com/markrileybot/python-msikeys',
    license='MIT',
    description=open('README.md').readline(),
    long_description=open('README.md').read(),
    download_url='https://github.com/markrileybot/python-msikeys/tarball/%s' % VERSION,
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
    keywords=[
        'MSI', 'Keyboard', 'Backlight'
    ],
    zip_safe=True
)
