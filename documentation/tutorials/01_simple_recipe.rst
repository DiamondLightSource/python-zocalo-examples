Simple Recipe
-------------

This tutorial will explain the structure and content of a simple recipe.

The aim is to demonstrate how to write a recipe to provide instructions to a service.
The service we will be using is the **Simple Service**, included as part of python-zocalo-examples.
Find the source code for that service
`here <https://github.com/DiamondLightSource/python-zocalo-examples/blob/master/zocalo_examples/services/simple_service.py/>`_.

If you want to skip ahead, you can find the entire recipe `here <https://github.com/DiamondLightSource/python-zocalo-examples/blob/master/zocalo_examples/recipes/simple_service_recipe.json/>`_
or at the bottom of the page.

JSON
^^^^

To start with, all Zocalo recipes are currently `json <https://www.w3schools.com/whatis/whatis_json.asp/>`_
files.
This can make them a little difficult to write but it makes them very simple for a machine to read.
As we are trying to automate data analysis, this is quite useful!

The entire recipe is wrapped in a big json dictionary.

So, start your recipe by opening an editor, creating *simple_service_recipe.json*, and starting a blank dictionary:

.. code-block:: json

    {

    }

This will give us plenty of space to write the rest of the recipe.

**Note:** JSON files can be written in one line but it is good practice to use indentation and line breaks to make them more readable

Steps
^^^^^

Each recipe is made up of a number of processing steps, one or more.
The simple recipe is only composed of one step, we will add more later.

Steps are recorded as entries in the dictionary and are dictionaries themselves.
The keys are always numbers with speech marks around them.

So let's add our first step with an empty dictionary:

.. code-block:: json

    {
        "1": {
        }
    }

Queues and parameters
^^^^^^^^^^^^^^^^^^^^^

Now, we can start detailing this processing step.

First, we must specify what queue we wish to send the recipe to.

Queue names should be uniquely attached to a particular service.
Otherwise there is a strong chance that the wrong service will read the message!

In this case, we are using the *simpleservice.submission* queue.
To check which queue you wish to send to, it is often necessary to check the source code
of the service itself.

Add this to the step dictionary (we will recap how the the whole file should be looking shortly):

.. code-block:: json

    "queue": "simpleservice.submission",

This brings us on to defining parameters for the service.
The **Simple Service** takes the following parameters:

- *commands* - list of commands to execute
- *workingdir* - working directory
- *output_file* - file in *workingdir* to record the command outputs in

To start with, we will just provide a basic echo command.
Note, *commands* is a list so even if there is only one value it must be surrounded in square brackets:

.. code-block:: json

    "commands": [
        "echo This is a command"
    ]

Specify your own working directory and filename, with the output expected in *workingdir*/*output_file*.
The recipe should look like this:

.. code-block:: json

    {
    "1": {
        "queue": "simpleservice.submission",
        "parameters": {
            "commands": [
                "echo This is a command"
            ],
            "workingdir": "/output/folder",
            "output_file": "out.txt"
        }
    }
}

Where to start?
^^^^^^^^^^^^^^^

Having specified the processing steps, we need to tell Zocalo what the first step is.
This may seem obvious for our recipe but a more complex recipe can have many steps.

The *start* value of the recipe can trigger multiple steps to begin processing.
This means you can choose whether to start many processing steps at once, if they are
all using the same raw data, or to adopt a linear approach, important when processing
steps depend on each other.

It is also possible to provide some initial information during this step, which will be
covered later.
For the time being, send an empty list.

At the same level as the processing step, add:

.. code-block:: json

    "start": [
        [
            1,
            []
        ]
    ]

The total recipe should now look like:

.. code-block:: json

    {
    "1": {
        "queue": "simpleservice.submission",
        "parameters": {
            "commands": [
                "echo This is a command"
            ],
            "workingdir": "/output/folder",
            "output_file": "out.txt"
        }
    },
    "start": [
        [
            1,
            []
        ]
    ]
}

It is very easy to make a mistake when writing JSON by hand.
To check for errors, use the *workflows.validate_recipe* tool to check the recipe will
work for Zocalo.

.. code-block:: bash

    workflows.recipe_validate /path/to/my/recipe.json

If there is an error, amend it.
Pay close attention to commas!

Actually running the recipe!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To run the recipe, we need to start some services!

Open three terminals and make sure that they are all in an environment which has the zocalo
commands available.

In the first terminal, start a **Dispatcher** service in the test space.
This reads recipes, adds information if necessary and then puts the message on the correct queue.

.. code-block:: bash

    $ zocStarted service: Dispatcher
    Service successfully connected to transport layer
    Dispatcher starting
    Logbook disabled: Not running in live mode
    Starting queue listener thread
    Queue listener thread started
    alo.service --test -s Dispatcher -v

In the second terminal, start a **SimpleService** in the test space.
This is the service which will actually execute our commands.

.. code-block:: bash

    $ zocalo.service --test -s SimpleService -v
    Started service: Simple Service
    Service successfully connected to transport layer
    Simple Service starting
    Starting queue listener thread
    Queue listener thread started

And finally, in the third termianl, send the recipe in the test space.
The "-f" option lets you point to the location where you saved the recipe.

.. code-block:: bash

    $ zocalo.go --test -f zocalo_examples/recipes/simple_service_recipe.json 1234
    Running recipe from file zocalo_examples/recipes/simple_service_recipe.json
    for data collection 1234

    Submitted.

Now if you read your output file, you should see:

::

    This is a command

**Congratulations!!** You have just written and executed your first recipe!
