# CKAN Harvester for OAI-PMH

## Developing without running jobs manually

To make it easier to develop, tests are setup that allow to do that:

    . ~/default/bin/activate
    cd /vagrant/ckanext-oaipmh

    nosetests --logging-filter=ckanext.oaipmh.harvester --ckan --with-pylons=test.ini ckanext/oaipmh/tests

In this example the logging filter is used to only show messages of the harvester.
