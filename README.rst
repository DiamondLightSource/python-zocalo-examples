===============
Zocalo Examples
===============

This repo stores a variety of Zocalo examples which can be used as the basis
for learning about `Zocalo <https://github.com/DiamondLightSource/python-zocalo/>`_
and developing:

* recipes
* services
* wrappers

Zocalo Examples is a python 3 package developed by `Diamond Light Source <https://www.diamond.ac.uk/>`_.

Installation
------------

To work with the examples and perform development it is best to create a virtual environment.
This helps to isolate your development work from the wider system installation of python.

Using python 3, go to the directory you are going to be developing in and type:

.. code-block:: bash

    python -m venv zocalo_venv
    source zocalo_venv/bin/activate

**Note:** zocalo_venv is an example name for the venv, it is best to give useful names.

Now install the package directly from Github:

.. code-block:: bash

    pip install -e git+git://github.com/DiamondLightSource/python-zocalo-examples.git#egg=python_zocalo_examples

Running the *pip list* command should now show your installed packages, including zocalo_examples.

Running *zocalo.service -h* will provide you with a list of available services, including examples such as Echo and SimpleService:

.. code-block:: bash

    -s SVC, --service=SVC
                        Name of the service to start. Known services:
                        Schlockmeister, SampleConsumer, SampleProducer,
                        SampleTxn, SampleTxnProducer, Echo, SimpleService

Start with Zocalo
-----------------

Zocalo is made up of many small services, so even this simple example will require more than
one terminal.
Although this may seem complicated now, this framework provides simplicity later on.

Dispatcher Service
^^^^^^^^^^^^^^^^^^

The **Dispatcher** service takes Zocalo recipes in and checks validity before sending on to the correct service
for processing.

Open a terminal and activate the virtual environment:

.. code-block:: bash

    source zocalo_venv/bin/activate

Start a Dispatcher service in the test space:

.. code-block:: bash

    zocalo.service --test -s Dispatcher -v

**Note:** Services running in the test space only view messages from your account, allowing Zocalo developers to work
independently from each other and ensure that live services will not be interrupted.

You should see the Dispatcher service starting up and now listening for information.

.. code-block:: bash

    Started service: Dispatcher
    Service successfully connected to transport layer
    Dispatcher starting
    Logbook disabled: Not running in live mode
    Starting queue listener thread
    Queue listener thread started

Simple Service
^^^^^^^^^^^^^^

The **SimpleService** is an example service which will be used to demonstrate how to use Zocalo.
It is very simple, runs specific commands on the command line and records the output into a file.

Open a new terminal, activate the virtual environment and start the SimpleService in the test space:

.. code-block:: bash

    source zocalo_venv/bin/activate
    zocalo.service --test -s SimpleService -v

You should see the SimpleService start up:

.. code-block:: bash

    Started service: Simple Service
    Service successfully connected to transport layer
    Simple Service starting
    Starting queue listener thread
    Queue listener thread started

The SimpleService is now waiting for an input which we will provide next.

Sending a Recipe
^^^^^^^^^^^^^^^^

Recipes define the data processing pipeline for a particular job or set of data.

They can be very complex but let's use one that was prepared earlier!

Recipes are sent with the *zocalo.go* command.
As well as taking prepared recipes, it can be pointed to any valid recipe file.
Here, use zocalo_examples/recipes/readme_recipe.json from the package itself.

Open a new terminal, activate the virtual environment and send the recipe with a valid *workingdir*:

.. code-block:: bash

    source zocalo_venv/bin/activate
    zocalo.go --test -f zocalo_examples/recipes/readme_recipe.json -s workingdir="/my/working/dir"

Assuming you have provided a valid *workingdir*, SimpleService should let you know it ran,
Dispatcher should be showing its message processing,
and there should be a **zocalo_out.txt** in your *workingdir*:

.. code-block:: bash

    Congratulations! This is your first zocalo output!

Find out more in the **Tutorials**

Coming soon
-----------

- Links to further tutorials
- What everything means
- How to write a recipe
- How to write a service
- How to write a wrapper
- How to test that everything works in an isolated test environment
- How to deploy this more widely

Contributors
------------

- Tim Guite