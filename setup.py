#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import textwrap

if __name__ == "__main__":
    setuptools.setup(
        name="Flask-NPM",
        version="1.0.0",
        description="Flask extension for Node modules",
        author="lightsing",
        author_email="light.tsing@gmail.com",
        url="https://github.com/lightsing/Flask-NPM",
        long_description=textwrap.dedent("""\
            """),
        packages=[
            "flask_npm",
        ],
        install_requires = [
            "Flask",
        ],
        include_package_data=True,
        classifiers=[
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],
        zip_safe=False,
    )