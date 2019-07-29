from __future__ import absolute_import, division, print_function

import json
import logging
import os

import zocalo.wrapper

logger = logging.getLogger("zocalo.example.simple_wrapper")


class SimpleWrapper(zocalo.wrapper.BaseWrapper):
    """
    Simple wrapper to demonstrate concept and development
    Writes parameters, job parameters, payloads to file in working_directory
    Sends true on to "any"
    """

    def run(self):

        # Check that a recipe wrapper has been passed
        assert hasattr(self, "recwrap"), "No recipewrapper object found"

        # Collect the job parameters - working directory and results directory usually expected
        params = self.recwrap.recipe_step["parameters"]
        job_params = self.recwrap.recipe_step["job_parameters"]
        payload = self.recwrap.payload

        # Move to the working directory
        working_directory = job_params["working_directory"]
        if not os.path.exists(working_directory):
            os.makedirs(working_directory)
        os.chdir(working_directory)

        # Logs to {name}.e{job_id} in the working directory of the recipe
        logging.info("Running wrapper commands")

        # Write params, job params, payload to files
        with open("params.json", "w") as params_fh:
            json.dump(params, params_fh, indent=2)
        with open("job_params.json", "w") as job_params_fh:
            json.dump(job_params, job_params_fh, indent=2)
        with open("payload.json", "w") as payload_fh:
            json.dump(payload, payload_fh, indent=2)

        logging.info("Wrapper complete")

        self.recwrap.send_to("all", {"Example Wrapper Results": True})

        return True
