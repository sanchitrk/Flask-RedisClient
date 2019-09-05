
"""
Flask-RedisClient
-------------

A simple Flask Redis Client
"""
from setuptools import setup


setup(
    name='Flask-RedisClient',
    version='1.0',
    url='https://github.com/sanchitrk/Flask-RedisClient',
    license='BSD',
    author='Sanchit Rk',
    author_email='sanchit.aark@gmail.com',
    description='A simple flask redis client',
    long_description=__doc__,
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
