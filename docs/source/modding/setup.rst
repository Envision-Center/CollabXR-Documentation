Preparing for Mod Creation
===============================

These are some initial steps you will need to take in order to start creating mods for CollabXR.

.. _Asset Bundles: https://docs.unity3d.com/6000.0/Documentation/Manual/AssetBundlesIntro.html

Creating a Unity Project
------------------------------

You will want to create a new `Universal Render Pipeline`_ project in `Unity 6000.0`_, to best ensure mod compatibility with CollabXR.
Mods built in other versions of Unity may be forward-compatible, but are unlikely to be backwards-compatible.
The patch number should not matter.

.. _Unity 6000.0: https://unity.com/releases/editor/archive
.. _Universal Render Pipeline: https://docs.unity.cn/6000.0/Documentation/Manual/universal-render-pipeline.html

Installing Mod Packager
-----------------------------

The :doc:`CollabXR Mod Packager <../modpackager>` is necessary to bundle your content into `Asset Bundles`_ with additional metadata for distribution.
We recommend reading up on `Asset Bundles`_ to understand to their limitations before creating your mod.

Once installed, while in Unity Editor, click **CollabXR Modding Tools > Open Mod Packager**.
Upon first opening, the Mod Packager will build a database of all assets in your project.
This may take a few minutes.

Afterwards, a small window titled "CollabXR Mod Packager" should pop up.
This means the packager is fully set up!
Close it for now until you are ready to upload.

Mod Extras
------------------------
Because `Asset Bundles`_ cannot contain code, we created the :doc:`CollabXR Mod Extras <../modextras>` package.
This package provides various components you can add to your mods, which will retain or add functionality when spawned into CollabXR.
