============
Explanations
============

The goal of Zocalo is to provide the capability and tools for creating and supporting automated data analysis work, particularly in combination with
`ISpyB <https://www.esrf.eu/ispyb/>`_, a database program developed specifically for crystallography.

In the past, attempts at this were difficult to debug as tasks could not be easily tracked down and analysis pipelines
were prone to being run repeatedly in their entirety because just one stage had failed.

Zocalo provides key tools to monitor requests and interrogate jobs which were not processed correctly or went wrong.

It fits into the Diamond computing infrastructure where jobs are run on clusters without having to worry about which particular machine is being used.

Although initially developed for the Macromolecular Crystallography (MX) team, it is hoped that it can be used
for other areas of research at Diamond and beyond.

Terminology
-----------

Find below explanations for some of the terminology commonly used when developing for Zocalo.

Recipe
^^^^^^

A recipe is a specification for a data analysis pipeline

- It specifies what action is to be taken on which data and in which order with nodes
- It can specify processing pathways and trigger a wide variety of processes
- Recipes are usually created with recipe templates which are then instantiated with relevant information at runtime
- One recipe to be used many times for different users/experiments
- Once instantiated, the complete recipe will be passed from node to node along with information about what node is currently being computed and other useful information
- This means that any machine can look at the recipe at any point and know what to do with it

Service
^^^^^^^

A process which runs continuously and waits for work

- Services are constantly waiting until a message arrives so that they can do some work
- There are often many instances of the same service running at any one time
- Sometimes they are all waiting for work, sometimes there is too much work for them so some has to wait, and sometimes the amount of work is just right
- Zocalo services are based on the `Python Workflows <https://github.com/DiamondLightSource/python-workflows/>`_ CommonService class, which provides the code to listen out for Zocalo recipes and send output to the next node

Job
^^^

Process which runs only when it is needed

- Generally more lightweight than a service, as it may have to be started many times
- Zocalo jobs are wrapped in a wrapper which allows them to interface with Zocalo recipes
- A Zocalo job is not necessarily a cluster job, but it can be

Wrapper
^^^^^^^

Zocalo interface for jobs

- Zocalo provides the wrapper as a way to interface the paramters and information in the recipe to a job
- This could be a command line program which needs to be handled carefully
- It also allows for processing of the incoming data and processing of the data output
- Perhaps most imporantly, it allows more complex debugging to take place as useful error messages can be generated quickly, saving time for engineers and developers
- Wrappers are run from the command line
- Within a recipe, a wrapper is run through a general service as a command line instruction

Queue
^^^^^

A safe way to transfer messages asynchronously

- Zocalo is built on top of the `ActiveMQ <https://activemq.apache.org/>`_ messaging protocol
- To run Zocalo, an ActiveMQ server must be run and maintained
- Recipes and messages sit in a queue until they are ready to be processed
- The ActiveMQ server makes a note of which messages have been read and whether or not they were correctly processed
- This is part of what gives Zocalo its power
- A job which causes an error or is running when a service crashes will go back onto the queue and another service will try to process it
- Jobs which are inherently bad and fail multiple times are removed from the queue

Parameters
^^^^^^^^^^

Parameters provide flexibility over how a job is processed

- Most often, this involves specifying the processing ID and where to put results
- Depending on the service or wrapper, parameters can completely define behaviour
- When executing a wrapper from inside a service, it is common to differentiate the parameters using the *parameters* and *job_parameters* keywords