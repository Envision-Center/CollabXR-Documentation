Developer Setup
=================

Consistent, clean, and readable code is important when making contributions in order to reduce friction between developers.
While not required, installing these tools and adhering to code style guidelines is **strongly recommended** for a streamlined PR review process.

Recommended setup order:

1. :ref:`Install Git LFS<section gitlfs>`
4. :ref:`Playtesting<section playtesting>`

.. _CollabXR repository: https://github.com/Envision-Center
.. _section gitlfs:

Git LFS
----------

Ensure `Git LFS`_ is installed in order to pull binary assets.

After installing, run these commands in the root of your repository:

1. ``$ git lfs install``
2. ``$ git lfs pull``

.. _Git LFS: https://git-lfs.com/

.. _section dotnet:

DotNet
----------

We recommended .NET SDK version 10, but anything support by .NET Standard 2.1 should be okay,
although some tools like CSharpier may not work with older SDK versions.

1. Ensure the proper `dotnet`_ version is installed: ``$ dotnet --version``
2. In the root directory of the `CollabXR repository`_, install the dotnet tool manifest: ``$ dotnet tool restore``
Most IDEs support "format on save" operations, see :doc:`IDE specific setup<ide>`.
If not automatically handled by your IDE, you can format using CSharpier at any time: ``$ dotnet csharpier .``

.. _dotnet: https://dotnet.microsoft.com/en-us/download/dotnet
.. _CSharpier: https://csharpier.com/docs/About
.. _CSharpier plugin list: https://csharpier.com/docs/Editors

.. _section pre-commit:

Pre-Commit Hooks
------------------------

`pre-commit`_ is used for formatting fixes and validation before making commits and pushing them.
Their documentation provides a recommended installation method.

.. note::

	If you're working on Debian, pre-commit can be installed globally via apt: ``$ sudo apt install pre-commit``

Once pre-commit is installed on your system, you can set it up within the root directory of the `CollabXR repository`_: ``$ pre-commit install``

Now, any time you make a commit, pre-commit should fix any formatting or whitespace issues before the commit is made.
If any issues arise, pre-commit will abort the commit, allowing you to add changes before committing again.

.. note::

	If you're using GitHub Desktop, you may need to `use the beta version`_ for proper commit hooks support (if it works). Or, we recommend using an `alternative GUI client`_ like GitKraken (free version).

.. _pre-commit: https://pre-commit.com/
.. _use the beta version: https://desktop.github.com/beta/
.. _section playtesting:

Playtesting
------------------

Testing in Editor
^^^^^^^^^^^^^^^^^^^^^

To simulate a Quest environment, we use the `Meta XR Simulator`_, which must be downloaded from their site.
We typically use the **QuestDebug** Build Profile for testing both in-editor and outside of the editor, since it is the primary platform we develop for.

Once everything is installed, launch the Meta XR Simulator and re-open the Unity project.
You should see a MetaXR simulator icon near the Play button. Click it so it turns blue.

.. image:: /images/metaxr_simulator_arm.png

Open the ``Assets/Scenes/Menu.unity`` scene, and then press Play.
This should drop you in the main menu for CollabXR.
After connecting to a lobby, you can press B to open the spawn menu and tool selector.
You may need to disable one of the simulated controllers using the **Open Inputs > Global Input Settings** in order to open or interact with menus.

.. _Meta XR Simulator: https://developers.meta.com/horizon/downloads/package/meta-xr-simulator/

Testing in Headset
^^^^^^^^^^^^^^^^^^^^^^^^

Build an APK using the **QuestDebug** Build Profile.
You may need to install the `Meta Quest Developer Hub`_ to load the build onto a Quest headset.

.. _Meta Quest Developer Hub: https://developers.meta.com/horizon/documentation/android-apps/meta-quest-developer-hub



Additional Tools
--------------------

.. toctree::

	ide
