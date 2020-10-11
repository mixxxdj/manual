#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="sphinx-mixxx",
    version="0.1",
    url="http://github.com/mixxxdj/manual",
    license="GPL",
    author="Jan Holthuis",
    author_email="jholthuis@mixxx.org",
    description="Mixxx extension for Sphinx",
    zip_safe=False,
    classifiers=[
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Documentation",
        "Topic :: Utilities",
    ],
    platforms="any",
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        "Sphinx>=0.6",
        "sphinxcontrib-domaintools>=0.1",
    ],
)
