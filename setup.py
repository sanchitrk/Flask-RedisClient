
"""
Flask-RedisClient
-------------

A simple Flask Redis Client
"""
import os
import codecs
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()

setup(
    name='Flask-RedisClient',
    version='0.1',
    url='https://github.com/sanchitrk/Flask-RedisClient',
    license='MIT',
    author='Sanchit Rk',
    author_email='sanchit.aark@gmail.com',
    description='A simple flask redis client',
    long_description=long_description,
    packages=['flask_redisclient'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'redis'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
