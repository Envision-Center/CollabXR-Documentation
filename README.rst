CollabXR Documentation Repository
=======================================

`CollabXR`_ is a mixed-reality classroom. See the `docs`_!

.. _CollabXR: https://envision.center/collabxr
.. _docs: https://envision-center.github.io/CollabXR-Documentation/

=========
Development
=========

1.  Create a virtual Python environment: ``python3 -m venv .venv/``
2. Enter virtual environment: ``source .venv/bin/activate`` (or ``.\.venv\Scripts\activate.bat`` if on Windows)
3. Install dependencies: ``pip install -r docs/requirements.txt``
4. Optionally install esbonio language server for Sphnix (preferablly global): ``pip install esobnio``
5. Install Prettier for auto-formatting configs: ``npm i -g prettier``
6. Setup pre-commit hooks for code cleanliness: ``pre-commit install``

To build the site locally after setting up your environment:

* On Unix: ``cd docs && make html``
* Your built static-site should appear under `docs/builds/html/`

======
Resources
======

* `reStructuredText Docs`_

.. _reStructuredText Docs: https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html
