import json
import workflows.recipe
from workflows.services.common_service import CommonService
from datetime import datetime
from pathlib import Path
import subprocess


class WrapperService(CommonService):
    """Service to execute zocalo wrappers"""

    # Human readable service name
    _service_name = "Wrapper Service"

    # Logger name
    _logger_name = "examples.wrapperservice"

    def initializing(self):
        """Subscribe to the simpleservice.submission queue. Received messages must be
       acknowledged."""
        self.log.info("Wrapper Service starting")

        if self._environment.get("live"):
            self.log.error(
                "This service must be run in the zocalo test space, please use zocalo.service --test"
            )
            self._shutdown()

        workflows.recipe.wrap_subscribe(
            self._transport,
            "wrapperservice.submission",
            self.process,
            acknowledgement=True,
            log_extender=self.extend_log,
        )

    def process(self, rw, header, message):
        """Process the incoming recipes"""
        self.log.info(
            f"Running Wrapper Service at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )

        # Conditionally acknowledge receipt of the message
        # This allows the message server to know that the message has been dealt with properly
        txn = self._transport.transaction_begin()
        self._transport.ack(header, transaction=txn)

        # Extract parameters
        try:
            workingdir = rw.recipe_step["parameters"]["workingdir"]
            commands = rw.recipe_step["parameters"]["commands"]
        except KeyError as e:
            self.log.exception("Recipe did not contain both workingdir and commands")
            # Stop processing message
            self._transport.transaction_commit(txn)
            return

        # Create a recipewrap file to pass to the wrapper script
        if "recipewrapper" in rw.recipe_step["parameters"]:
            recipewrapper = rw.recipe_step["parameters"]["recipewrapper"]
            self.log.debug(f"Storing serialized recipe wrapper in {recipewrapper}")
            try:
                with open(recipewrapper, "w") as fh:
                    json.dump(
                        {
                            "recipe": rw.recipe.recipe,
                            "recipe-pointer": rw.recipe_pointer,
                            "environment": rw.environment,
                            "recipe-path": rw.recipe_path,
                            "payload": rw.payload,
                        },
                        fh,
                        indent=2,
                    )
            except OSError:
                self.log.error(f"Could not write recipewrap to file at {recipewrapper}")
            # Replace the $RECIPEWRAP keyword in the command with the new recipewrapper file
            commands = [com.replace("$RECIPEWRAP", recipewrapper) for com in commands]

        # Try to get an output file
        try:
            output_file = rw.recipe_step["parameters"]["output_file"]
        except KeyError:
            # Couldn't find it
            output_file = None

        try:
            # Split the list of commands into lists of instructions
            if len(commands) > 0:
                commands_list = [cmd.split(" ") for cmd in commands]

                # Execute the commands one by one
                for cmd in commands_list:
                    # Run command
                    if output_file:
                        # Send output to output file
                        with open(Path(workingdir) / output_file, "a") as out:
                            result = subprocess.run(cmd, timeout=10, stdout=out)
                    else:
                        # Output goes to terminal
                        result = subprocess.run(cmd, timeout=10)
                    # Check that there were no errors or timeouts
                    result.check_returncode()
            else:
                self.log.error("Did not receive any commands to execute")
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            self.log.exception(f"Had error running command: {cmd}")
        except PermissionError as e:
            self.log.exception(
                f"Do not have permission to write to {Path(workingdir) / output_file, 'w'}"
            )
        except subprocess.TimeoutExpired as e:
            self.log.exception(f"Time ran out running command: {cmd}")
        except Exception:
            self.log.exception(f"Could not execute commands")

        # Send results onwards
        rw.set_default_channel("job_processed")
        rw.send({"processed": True}, transaction=txn)

        # Stop processing message
        self._transport.transaction_commit(txn)

        return
