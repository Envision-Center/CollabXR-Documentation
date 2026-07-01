Developer Setup
=================

Consistent, clean, and readable code is important when making contributions in order to reduce friction between developers.
While not required, installing these tools and adhering to code style guidelines is **strongly recommended** for a streamlined PR review process.

Recommended setup order:

1. :ref:`Install Git LFS<section gitlfs>`
2. :ref:`Set up DotNet runtime<section dotnet>`
3. :ref:`Install pre-commit hooks<section pre-commit>`
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
3. Install corresponding plugins for your IDE as necessary (`CSharpier plugin list`_)

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
.. _alternative GUI client: https://git-scm.com/tools/guis
.. _section playtesting:

Project Setup
---------------------------------

Getting the Unity Project
^^^^^^^^^^^^^^^^^^^^^^^^^^
1. Clone the repository: https://github.com/Envision-Center/CollabXR
2. Setup git submodules. If cloned with Github Desktop, this has been done automatically. Otherwise, run ``$ git submodule update --init --recursive``.
3. Add the project to Unity Hub and install the associated editor version. Include **Android Build Support**. 

Getting Photon Fusion
^^^^^^^^^^^^^^^^^^^^^^^^^^
1. Create a Photon account (required to download): https://www.photonengine.com/
2. Download Photon Fusion 2.0.12: https://doc.photonengine.com/fusion/current/getting-started/sdk-download
3. Download Fusion Physics 2.0.5: https://www.photonengine.com/sdks#fusion
4. Download Unity Voice SDK 2.6.3: https://www.photonengine.com/sdks#voice

You should now have 3 Unity package files.

Resolving Errors
^^^^^^^^^^^^^^^^^^^^^^^^^^
1. Open the Unity Project in **unsafe mode**.
2. Go to ``Assets > Import Package > Custom Package``. Then add the 3 Photon Unity Package Files one at a time. Approve any "Script Updating Consent" windows that appear in this step.
3. You may get 1 or more MetaXR errors. Ignore the error about passthrough enabled. Anything else you may fix.

Photon Fusion and API Keys
^^^^^^^^^^
1. Open the PUN Wizard via ``Window > Photon > Unity Networking > PUN Wizard``. Then, click PUN setup, and paste your **Photon App ID**.  
2. You may also need to setup credentials for Cesium Ion, the Oculus Platform, and the OpenSky API
3. Finally, open the Photon Fusion Hub via ``Tools > Fusion > Fusion Hub``. This should resolve any last errors you may have.

Playtesting
------------------

.. _section configure default room:

Setting Developer Preferences
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to minimize interference with other developers while testing, **we heavily advise setting your default room via Developer Preferences**.
The "default room" is the lobby you enter when you press "Connect" on the main menu without adding a lobby ID or scanning a QR Code.

To do this, first hit Play using the arrow at the top of the screen.
This should automatically create an asset at ``Assets/Resources/Preferences/DeveloperPreferences.asset``.
Stop the play mode, then change the "Default Room" field on that asset to something unique.

You can optionally create a QR Code using the provided button, in order to create a print out you can scan at any time.
The developer preferences only apply while testing in editor.

Testing in Editor with the Simulator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To simulate a Quest environment, we use the `Meta XR Simulator`_, which must be downloaded from their site.
We typically use the **QuestDebug** Build Profile for testing both in-editor and outside of the editor, since it is the primary platform we develop for.

Once everything is installed, launch the Meta XR Simulator and re-open the Unity project.
You should see a MetaXR simulator icon near the Play button. Click it so it turns blue.

.. image:: /images/metaxr_simulator_arm.png

Open the ``Assets/Scenes/Menu.unity`` scene, and then press Play.
This should drop you in the main menu for CollabXR. Press "Connect" to enter into your `configured default room <section configure default room>`_.
After connecting to a lobby, you can press B to open the spawn menu and tool selector.
You may need to disable one of the simulated controllers using the **Open Inputs > Global Input Settings** in order to open or interact with menus.

.. _Meta XR Simulator: https://developers.meta.com/horizon/downloads/package/meta-xr-simulator/

Testing in Editor with Meta Horizon Link
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the feature being tested does not require a true Quest environment (for example, it does not depend on mixed reality features such as depth or passthrough) the `Meta Horizon Link`_ app may be used in place of the simulator. Download and install this from their site.

In the Meta Horizon Link desktop app, go to **Settings > General** and scroll to the bottom. Next to **OpenXR runtime** click **Set Meta Horizon Link as active**. Allow any following prompts.

Ensure your Quest headset is connected with a USB 3.0 compatible port and cable. In the headset, enter Link mode from the Quick settings panel. Then, launch your app in Unity and your app should display in headset.

.. _Meta Horizon Link : https://www.meta.com/help/quest/1517439565442928/

Testing in Headset
^^^^^^^^^^^^^^^^^^^^^^^^

Build an APK using the **QuestDebug** Build Profile.
You may need to install the `Meta Quest Developer Hub`_ to load the build onto a Quest headset.

.. _Meta Quest Developer Hub: https://developers.meta.com/horizon/documentation/android-apps/meta-quest-developer-hub
