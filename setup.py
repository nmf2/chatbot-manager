# coding: utf-8

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
    description="API to manage chatbots",
    zip_safe=False,
    author_email="nmf2@cin.ufpe.br",
    url="",
    keywords=["Swagger", "Chatbot Manager"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml', 'docker-compose.template.yml']},
    entry_points={
        'console_scripts': ['chatbot_manager=chatbot_manager.__main__:main']},
    long_description="""\
    This is a API to create and manage chatbots in docker containers
    """
)
