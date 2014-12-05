from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-oaipmh',
    version=version,
    description="OAI-PMH Harvester for CKAN",
    long_description="",
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Liip AG',
    author_email='ogd@liip.ch',
    url='http://www.liip.ch',
    license='AGPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.oaipmh'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points=\
    """
    [ckan.plugins]
    oaipmh_harvester=ckanext.oaipmh.harvester:OaipmhHarvester
    [paste.paster_command]
    harvester=ckanext.oaipmh.command:OaipmhHarvesterCommand
    """,
)
