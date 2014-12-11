#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
        name = "sigma",
        version = "1.0.0",
        description = "Sigma Library",
        author = "Emmanouil Matsis",
        author_email = "em@balmondstudio.com",
        url = "https://www.balmondstudio.com",
        classifiers = [
            "Environment :: Console",
            "Programming Language :: Python :: 2.7",
            "Operating System :: OS Independent",
            "Intended Audience :: Artist & Designers",
            "Topic :: Art & Design",
            ],
        packages = [
            "sigma"
            ],
        test_suite = "test",
        scripts = [
            "script/sigma_script",
            ],
        entry_points = {
            "console_scripts": [
                "sigma = sigma.__main__:main"
                ],
            },
        package_data = {
            "sigma": ["data/*.dat"],
            },
        )
