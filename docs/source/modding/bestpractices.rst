Best Practices
============================

Tips and tricks for the best mod creation and end-user experience.

User Experience
--------------------------------

Users may expect certain functionality from a mod depending on the context.
To minimize friction and maximize immersion while interacting with your mod, make these considerations.

- **Set up** :doc:`depth occlusion <materials>` **on your materials**, so mods will appear more integrated with the real world.
- **Fine-tune your collision box**. Meeting the user's expectations of where you can and cannot grab or interact with a prefab will minimize confusion.
- **Use a** :ref:`custom thumbnail <custom-thumbnails>` to make your prefab easier to find in the spawn menu.
- **Consider the maximum and minimum scale** when annotating your menu item for uploading. Do you need to see your prefab really small? Do you need to scale it to real-scale for extra detail?

Download Size
------------------
Large mods can take a long time to download, which may be problematic in a classroom setting.
Additionally, large mods take much longer to package.
Here are some tips on minimizing mod size for the best CollabXR experience.

- **Only include your "menu item" prefabs in the Asset Bundle**. Unity will automatically gather their dependencies when building the mod, ignoring unnecessary content.
- **Keep related prefabs in the same Asset Bundle**. If multiple mods are depending on many of the same resources (like meshes and textures), sometimes it is best to combine all them in the same Asset Bundle so users only need to download one mod in order to see all menu items.
- Likewise, **keep unrelated prefabs in separate Asset Bundles**. If two menu items are only sharing a few resources, like a shader, but are using their own resources otherwise, keeping them separate Asset Bundles splits up the time spent downloading between activities.

Packaging Speed
--------------------------
Due to the nature of Unity's asset management, with the needs of the Mod Packager, the mod packager can be very slow to work with.
Here are some tips on how to minimize iteration time with your mods.

- Enabling `parallel asset imports`_ can reduce the amount of time spent re-importing assets.
- Only have the Mod Packager window open when you are ready to build a mod. While open, the Mod Packager will listen for changes in the file system in order to re-import files and update its internal database, which can slow down your workflow.
- Select the Target AssetBundle you want in the Mod Builder tab before signing in to your Mod Repository. The Mod Packager may otherwise sign you out while updating the asset database.

.. _parallel asset imports: https://docs.unity3d.com/6000.0/Documentation/Manual/ParallelImport.html
