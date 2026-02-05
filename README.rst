CollabXR Documentation Repository
=======================================

`CollabXR`_ is a mixed-reality classroom. See the `docs`_!

.. _CollabXR: https://envision.center/collabxr
.. _docs: https://envision-center.github.io/CollabXR-Documentation/

======
Development
======

1. Python setup:
	* Create a virtual environment: ``python3 -m venv .venv/``
	* Enter virtual environment: ``source .venv/bin/activate`` (or ``.\.venv\Scripts\activate.bat`` if on Windows)
	* Install dependencies: ``pip install -r docs/requirements.txt``
2. Install Prettier for auto-formatting configs: ``npm i -g prettier``
3. Setup pre-commit hooks for code cleanliness: ``pre-commit install``

To build the site locally after setting up your environment:
* On Unix: ``cd docs && make html``

======
Resources
======

* `reStructuredText Docs`_

.. _reStructuredText Docs: https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html
