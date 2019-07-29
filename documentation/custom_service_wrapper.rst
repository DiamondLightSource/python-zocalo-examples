==========================
Custom Services & Wrappers
==========================

Entry Points
------------

Services and wrappers have particular entry points which make them available to Zocalo.

To make a custom service or wrapper available, you will need to set up your code like a python package
so that it can be easily installed.

Here are some resources on how to do that:

- https://medium.com/small-things-about-python/lets-talk-about-python-packaging-6d84b81f1bb5
- https://python-packaging.readthedocs.io/en/latest/
- https://dzone.com/articles/executable-package-pip-install

Within *setup.py*, entry points are defined.

Here are the entry points to use to provide a service and a wrapper respectively:

.. code-block:: python

    entry_points = {
        "workflows.services": ["MyService = mypackage.mymodule.myservice:MyServiceClass"],
        "zocalo.wrappers": ["MyWrapper = mypackage.mymodule.mywrapper:MyWrapper"]
    }

For clarity, see the *setup.py* of the `examples repository <https://github.com/DiamondLightSource/python-zocalo-examples/blob/master/setup.py/>`_.

Having done this, `install your package locally in an editable state <https://packaging.python.org/tutorials/installing-packages/#installing-from-a-local-src-tree/>`_:

.. code-block:: bash

    pip install -e mypackage

Now check that your service/wrapper appears as an option when running:

.. code-block:: bash

    # For service:
    zocalo.service -h
    # For wrapper:
    zocalo.wrapper -h