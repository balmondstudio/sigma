#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
        name = "sigma",
        version = "1.0",
        description = "Sigma Library",
        author = "Emmanouil Matsis",
        author_email = "em@balmondstudio.com",
        url = "https://www.balmondstudio.com",
        packages = [
            "sigma"
            ],
        scripts = [
            "script/sigma",
            ],
        classifiers = [
            "Environment :: Console",
            "Programming Language :: Python :: 2.7",
            "Operating System :: OS Independent",
            "Intended Audience :: Artist & Designers",
            "Topic :: Art & Design",
            ],
        )
