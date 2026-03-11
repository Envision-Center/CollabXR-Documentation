My First CollabXR Mod
===========================

CollabXR relies on `Prefabs`_ for spawning and interacting with.

A mod may contain multiple prefabs, or just a single one.
When a prefab is spawned, all clients must download the corresponding mod (if it is not already cached),
so take bundle size into consideration when choosing how to organize your mod(s).

.. _Prefabs: https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingPrefabs.html

Prefab Setup
--------------------

In any scene, create an empty Transform for the root of your prefab, and ensure that its scale is ``(1, 1, 1)``.
Add a Box Collider to it--this will ensure users inside Collab can grab and manipulate your prefab.

Adding Functionality
^^^^^^^^^^^^^^^^^^^^^^^^

Additional functionality, like Toggle Controllers, Object Cyclers, and Passthrough Shaders can be added via the :doc:`Mod Extras packages<../modextras>`.

Custom Thumbnails
^^^^^^^^^^^^^^^^^^^^^^^^^

The mod packager will automatically generate Prefab thumbnails during the build process.

However, sometimes it is necessary to create a custom thumbnail for your Prefab (for example, if many Transforms are toggled off by default).
Thumbnails should be imported to Unity as a 64x64 PNG image with the following import settings.

.. image:: /images/mod_thumbnail_import.png

You can assign this texture to your prefab in the Mod Uploading window.

Uploading
--------------

To upload your mod, you will need to add the CollabXR Mod Packager package to your project, and access to a :doc:`mod repository<../modpackager/modrepository>`.

Once the mod packager is installed, go to **CollabXR Modding Tools > Open Mod Packager** on the window toolbar.

1. Authenticate with your repository (if necessary), then go to the **Mod Builder** tab.
2. Select your target AssetBundle. The mod packager will reimport all the assets.
3. Find your desired Prefab(s) and check the Menu Object box, before filling out the mod information.
4. Once all prefabs are marked, select your target platforms on the bottom left.
5. Finally, press **Build and Publish**. This will build the AssetBundles to ``Assets/Build/``, and upload them to the mod repository (if authenticated).
6. You can refresh your mod list in CollabXR by going to **Settings > Mods**, or by just rejoining a room.
