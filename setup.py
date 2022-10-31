import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="master_thesis",
    version="0.1.0",
    author="Filip Twardy",
    author_email="filip.twardy.v01@gmail.com",
    description=(
        "Master thesis code"
    ),
    packages=["gnn_lib", "tests"],
    long_description=read("README.md"),
)
