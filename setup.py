#!/usr/bin/python3

from setuptools import setup
import os

dir = os.path.dirname(__file__)
path_to_main_file = os.path.join(
    dir, "ruddo_beancount_extensions/__init__.py"
)
path_to_readme = os.path.join(dir, "README.md")
for line in open(path_to_main_file):
    if line.startswith("__version__"):
        version = line.split()[-1].strip("'").strip('"')
        break
else:
    raise ValueError(
        '"__version__" not found in "ruddo_beancount_extensions/__init__.py"'
    )
readme = open(path_to_readme).read(-1)

classifiers = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Intended Audience :: End Users/Desktop",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python :: 3 :: Only",
]

setup(
    name="ruddo_beancount_extensions",
    version=version,
    description="A few plugins for Beancount",
    long_description=readme,
    long_description_content_type='text/markdown',
    author="Manuel Amador (Rudd-O)",
    author_email="rudd-o@rudd-o.com",
    license="GPL",
    url="http://github.com/Rudd-O/beancount-extensions",
    classifiers=classifiers,
    packages=["ruddo_beancount_extensions"],
    requires=["beancount"],
    zip_safe=False,
    options={"bdist_rpm": {"requires": "python3-beancount", "no_autoreq": True}},
)
