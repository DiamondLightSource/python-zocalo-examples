from setuptools import setup

# these lines allow the version to be specified in Makefile.private
import os

version = os.environ.get("MODULEVER", "0.0")

setup(
    #    install_requires = ['cothread'], # require statements go here
    name="zocalo_examples",
    version=version,
    description="Module",
    author="Tim Guite",
    author_email="tim.guite@diamond.ac.uk",
    packages=["zocalo_examples"],
    install_requires=["zocalo", "nested_lookup"],
    entry_points={
        "console_scripts": [
            "zocalo.examples.set_working_directory = zocalo_examples.recipes.set_working_directory:main"
        ],
        "workflows.services": [
            "Echo = zocalo_examples.services.echo_service:EchoService",
            "SimpleService = zocalo_examples.services.simple_service:SimpleService",
        ],
    },  # this makes a script
    #    include_package_data = True, # use this to include non python files
    zip_safe=False,
)
