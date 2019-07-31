3: Adding Steps
---------------

Now that we've got the hang of using Zocalo and running multiple commands,
you might be wondering what happens if you wanted to use more than one service?

Or how to send the results of one processing step to the next one?

We'll get there but let's focus on doing more than one processing step.

For the moment, we'll just use the **Simple Service** but it should be straightforward to change this in the
future to use more than one service.

See the final recipe `here <https://github.com/DiamondLightSource/python-zocalo-examples/blob/master/zocalo_examples/recipes/simple_service_steps.json>`_.

Add another step
^^^^^^^^^^^^^^^^

Take the recipe which we developed above, copy the step and paste it on the same level.
Change the number of the step from 1 to 2.

There should now be two similar steps:

.. code-block:: json

    {
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
        "2": {
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

Change the message in the second step to something different so that when it runs you can tell the difference
from the previous recipe.

Now, at the end of the first step, on the same level as the queue and parameters information, add another key called
*output*:

.. code-block:: json

     "output_file": "out.txt"
        }
    },
    "output":

and point it to the second step:

.. code-block:: json

    "output": 2

This is how to define the next step in Zocalo.

The *output* key can take a single value, like this, or a list or dictionary.

Note that the 2 points to the "2" which defines the second step.
If the second step in your recipe has a different number, or you want to skip some steps, just make sure the
number specified in the output matches the step you want to run.

When running this recipe, pay attention to the **Simple Service** which will execute twice - once for the
first step, once for the second step!