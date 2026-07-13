Building CollabXR
==========================

If you would like to use CollabXR for large-scale or secure applications, you may need to recompile it with your own API keys.

These steps will walk you through cloning the `CollabXR repository`_ and getting it set up on your system.

.. _CollabXR repository: https://github.com/Envision-Center/CollabXR

Prerequisites
----------------------

Install Unity
^^^^^^^^^^^^^^^^^^^^

You will need to install `Unity Hub`_ in order to set up the CollabXR project.
From their site, install Unity hub and select a license.
Installing the Unity Editor is covered later in this guide.

.. _Unity Hub: https://unity.com/

Git LFS
^^^^^^^^^^^^^^^^^^^^^^^^^^

Ensure `Git LFS`_ is installed before cloning the repository in order to pull necessary binary files.

.. _Git LFS: https://git-lfs.com/

Project Setup
--------------------------------

Getting the Unity Project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Clone the `CollabXR repository`_. Take note of where you installed it!
2. Setup git submodules. If cloned with Github Desktop, this has been done automatically. Otherwise, run ``$ git submodule update --init --recursive`` in the project directory.
3. Ensure Git LFS files are pulled by running these commands in the project directory: ``$ git lfs install``, then ``$ git lfs pull``
4. Add the project to Unity Hub and install the associated editor version. You may need the **Android Build Support** and **Windows Build Support (IL2CPP)** editor modules in order to compile the project.

Getting Photon Fusion
^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Create a `Photon account`_ (required to download their SDKs).
2. Download `Photon Fusion 2.0.12`_.
3. Download `Fusion Physics 2.0.5`_.
4. Download `Unity Voice SDK 2.6.3`_.

You should now have 3 Unity package files.

.. _Photon account: https://www.photonengine.com/
.. _Photon Fusion 2.0.12: https://doc.photonengine.com/fusion/current/getting-started/sdk-download
.. _Fusion Physics 2.0.5: https://www.photonengine.com/sdks#fusion
.. _Unity Voice SDK 2.6.3 : https://www.photonengine.com/sdks#voice

Resolving Errors
^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Open the Unity Project in **unsafe mode**.
2. Go to ``Assets > Import Package > Custom Package``. Then add the 3 Photon Unity Package Files one at a time. Approve any "Script Updating Consent" windows that appear in this step.
3. You may get 1 or more MetaXR errors. Ignore the error about passthrough enabled. Anything else you may fix.

Photon Fusion and API Keys
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Photon Fusion`_ and `Photon Voice`_ App IDs are required for base CollabXR functionality.
Free plans are available for up to 20 concurrent users for testing and development.

1. In Photon App Settings, enter your **Fusion App ID** and **Voice App ID** into their respective fields.
2. Open the PUN Wizard via ``Window > Photon > Unity Networking > PUN Wizard``. Then, click PUN setup, and paste your **Photon App ID** and **Photon Voice ID**.
3. **Optionally** add credentials for Cesium Ion (for geospatial integration) at ``Assets/Keys/Resources/ion.cesium.com`` and OpenSky (for live ADSB data on top of geospatial integration) at ``Assets/Keys/Resources/OpenSky API``.
4. Finally, open the Photon Fusion Hub via ``Tools > Fusion > Fusion Hub``. This should resolve any last errors you may have.

.. _Photon Fusion: https://www.photonengine.com/fusion/pricing
.. _Photon Voice: https://www.photonengine.com/voice/pricing

Making a Build
--------------------

See Unity's documentation on `creating a build <https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettings.html>`_.
We have some pre-made Build Profiles that should already be configured.
However, for Android platforms, users may need to change their Bundle ID and Bundle Version Code inside the Player Settings.
See Unity's documentation on `building for Android <https://docs.unity3d.com/6000.0/Documentation/Manual/android-BuildProcess.html>`_ for more information.
