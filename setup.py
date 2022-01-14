from setuptools import setup, find_packages

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
    packages=find_packages(),
    install_requires=["workflows>=1.7", "zocalo", "nested_lookup"],
    entry_points={
        "console_scripts": [
            "zocalo.examples.set_working_directory = zocalo_examples.recipes.set_working_directory:main"
        ],
        "workflows.services": [
            "Echo = zocalo_examples.services.echo_service:EchoService",
            "Dispatcher = zocalo_examples.services.generic_dispatcher:Dispatcher",
            "SimpleService = zocalo_examples.services.simple_service:SimpleService",
            "WrapperService = zocalo_examples.services.wrapper_service:WrapperService",
        ],
        "zocalo.wrappers": [
            "SimpleWrapper = zocalo_examples.wrappers.simple_wrapper:SimpleWrapper"
        ],
    },  # this makes a script
    #    include_package_data = True, # use this to include non python files
    zip_safe=False,
)
