#!/usr/bin/env python


import os, sys
from setuptools import setup
from py_simple_lorem.version import version

root = os.path.abspath(os.path.dirname(__file__))

name = "py_simple_lorem"
license = "GPLv3+"
author = maintainer = "Andrew Spangler"
email = "AndrewSpangler@users.noreply.github.com"
description = (
    "Simple, compressed Lorem Ipsum generator. Get a different output each time."
)
requirements = []
url = f"https://github.com/AndrewSpangler/{name}/"
SETUPDATA = {
    "build-system": {
        "requires": ["setuptools>=61.0"],
        "build-backend": "setuptools.build_meta",
    },
    "project": {
        "name": name,
        # "author": author,
        # "url": url,
        "version": version,
        "description": description,
        # "maintainter": maintainer,
        # "copyright": "Copyright 2022, Andrew Spangler",
        "readme": "README.md",
        "requires-python": ">=3.8",
        "classifiers": [
            "Development Status :: 1 - Planning",
            "Environment :: Console",
            "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
        ],
        "dependencies": requirements,
        "keywords": [],
    },
    "project.urls": {
        '"Homepage"': url,
        '"Bug Tracker"': url + "issues",
    },
}


def read(file):
    return open(os.path.join(root, file)).read()


def make_toml(tables: dict):
    toml = ""
    for t in tables:
        toml += f"[{t}]\n"
        # Get table dict and write it
        tab = tables[t]
        for l in tab:
            if isinstance(tab[l], str):
                toml += f'{l} = "{tab[l]}"\n'
            else:
                toml += f"{l} = {tab[l]}\n"
        toml += "\n"
    return toml.strip()


if __name__ == "__main__":
    from setuptools import setup

    # Regenerate pyproject.toml
    with open(os.path.join(root, "pyproject.toml"), "w+") as f:
        f.write(make_toml(SETUPDATA))

    setup(
        name=name,
        # author=author,
        # version=version,
        # author_email=email,
        # url=url,
        # description=description,
        long_description=read("README.md"),
        # packages=packages,
        # package_dir={name: name},
    )
