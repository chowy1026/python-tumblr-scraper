import sys
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import tumblr_scraper

requires = [
    'requests',
]

setup(
    name='python-tumblr-scraper',
    version=tumblr_scraper.__version__,
    description='A command-line utility for scraper a Tumblr site.',
    long_description=open('README.rst').read(),
    keywords='tumblr',
    license=open('LICENSE').read(),
    author='Tristan Waddington',
    author_email='tristan.waddington@gmail.com',
    url='https://github.com/twaddington/python-tumblr-scraper',
    install_requires=requires,
    packages=['tumblr_scraper'],
    scripts=['bin/tumblr-scraper'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
