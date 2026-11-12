.. _install:

============
Installation
============

Getting started is pretty simple. The first step is to install the library.

Pip Install
===========

The easiest way to get terminaltables3 is to use `pip <https://pip.pypa.io>`_. Simply run this command.

.. code-block:: bash

    pip install terminaltables3

Latest from GitHub
==================

You can also elect to install the latest bleeding-edge version by using pip to install directly from the GitHub
repository.

.. code-block:: bash

    pip install git+https://github.com/matthewdeanmartin/terminaltables3.git

Clone and Install
=================

Lastly you can also just clone the repo and install from it. Usually you only need to do this if you plan on
`contributing <https://github.com/matthewdeanmartin/terminaltables3/blob/master/CONTRIBUTING.md>`_ to the project.

.. code-block:: bash

    git clone https://github.com/matthewdeanmartin/terminaltables3.git
    cd terminaltables3
    pip install .

For development, use `uv <https://docs.astral.sh/uv/>`_ instead:

.. code-block:: bash

    uv sync --frozen
