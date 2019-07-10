import workflows.recipe
from workflows.services.common_service import CommonService
from datetime import datetime
from pathlib import Path


class EchoService(CommonService):
    """Service which writes the string in the text field to out.txt in the working directory"""

    # Human readable service name
    _service_name = "Echo Service"

    # Logger name
    _logger_name = "example.services.echo"

    def initializing(self):
        """Subscribe to the archiver queue. Received messages must be
       acknowledged."""
        self.log.info("Archiver starting")

        workflows.recipe.wrap_subscribe(
            self._transport,
            "examples.queue",
            self.echo_information,
            acknowledgement=True,
            log_extender=self.extend_log,
        )

    def echo_information(self, rw, header, message):
        self.log.info(
            f"Running service at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )

        # Extract working directory
        workingdir = rw.recipe_step["parameters"]["workingdir"]

        try:
            # Create output file path
            output_file_path = Path(workingdir) / "out.txt"

            # Write output to file
            with open(output_file_path, "a") as f:
                f.write(
                    f"From echo service at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                )

        except Exception:
            self.log.exception(f"Could not write output to file in {workingdir}")

        # Conditionally acknowledge receipt of the message
        # This allows the message server to know that the message has been dealt with properly
        txn = self._transport.transaction_begin()
        self._transport.ack(header, transaction=txn)
        self._transport.transaction_commit(txn)
