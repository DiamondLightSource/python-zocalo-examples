# Zocalo Examples

This repo stores a variety of Zocalo examples which can be used as the basis
 for learning about [Zocalo](https://github.com/DiamondLightSource/python-zocalo)
  and developing:
- recipes
- services
- wrappers

Zocalo Examples is a python 3 package developed by Diamond Light Source.

## Installation

To work with the examples and perform development it is best to create a virtual environment.
This helps to isolate your development work from the wider system installation of python.

Using python 3, go to the directory you are going to be developing in and type:

```bash
python -m venv zocalo_venv
source zocalo_venv/bin/activate
```

**Note:** zocalo_venv is an example name for the venv, it is best to give usefule names.

Now install the package directly from Github:

```bash
pip install -e git+git://github.com/DiamondLightSource/python-zocalo-examples.git#egg=python_zocalo_examples
```

Running the `pip list` command should now show your installed packages, including zocalo_examples.

Running `zocalo.service --help` will provide you with a list of available services, including examples such as Echo and SimpleService:
```bash
-s SVC, --service=SVC
                    Name of the service to start. Known services:
                    Schlockmeister, SampleConsumer, SampleProducer,
                    SampleTxn, SampleTxnProducer, Echo, SimpleService
```

### Coming soon

- An actual read me tutorial
- Links to further tutorials
- What everything means
- How to write a recipe
- How to write a service
- How to write a wrapper
- How to test that everything works in an isolated test environment
- How to deploy this more widely

### Contributors

- Tim Guite