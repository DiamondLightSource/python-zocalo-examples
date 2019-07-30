==============================
Zocalo at Diamond Light Source
==============================

Diamond Light Source currently uses Zocalo for automated data analysis and have developed some utilities
and services which are designed to work specifically within our infrastructure.

Test space
----------

When developing a zocalo service or recipe, it is important to use a testing evironment, to prevent your changes
from causing issues with live data analysis.

This is now very simple to do.

Set up a local ActiveMQ server on your machine:

.. code-block:: bash

    $ module load activemq/zocdev

    Using local ActiveMQ installation in /dls/tmp/riw56156/zocdev-activemq/2019-07-30
    Starting ActiveMQ development instance...
    INFO: Loading '/dls_sw/apps/activemq/zocalo/apache-activemq-5.15.9//bin/env'
    INFO: Using java '/dls_sw/apps/java/x64/jdk1.8.0_181/bin/java'
    INFO: Starting - inspect logfiles specified in logging.properties and log4j.properties to get details
    INFO: pidfile created : '/dls/tmp/riw56156/zocdev-activemq/2019-07-30/activemq.pid' (pid '35131')


    ActiveMQ web interface:  http://127.0.0.1:8161

    user: admin
    password: 82x_mSrPgnPrOke3FmT4

This should set up a private test space where messages will stay on your computer.

To run up a service in this test space, simply use the "--test" option:

.. code-block:: bash

    zocalo.service --test -s Dispatcher -v

This will isolate your development work both from the live environment and also from other Zocalo developers who
may be working on the same services/queues as you and could be accidentally crashing your services or consuming
your messages!

Production Recipes
------------------

Our recipes for use in production are stored in a repo on our **internal Gitlab** server called *zocalo-configuration*.

The recipes are cloned from here to a production location which is read only to almost all users.

If you wish to use a recipe in production, for the repo or start a new branch and issue a pull request.
This will enable Zocalo developers to approve the recipe before it is deployed.