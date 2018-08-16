# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "chatbot_manager"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Simple Inventory API",
    author_email="nmf2@cin.ufpe.br",
    url="",
    keywords=["Swagger", "Simple Inventory API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['chatbot_manager=chatbot_manager.__main__:main']},
    long_description="""\
    This is a simple API
    """
)

