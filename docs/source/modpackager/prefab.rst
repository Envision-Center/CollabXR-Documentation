Making a Mod
============

CollabXR relies on `Prefabs` for spawning and interacting with.

A mod may contain multiple prefabs, or just a single one.
When a prefab is spawned, all clients must download the corresponding mod (if it is not already cached),
so take bundle size into consideration when choosing how to organize your mod(s).

.. _Prefabs: https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingPrefabs.html

Prefab Setup
------------

The top-level Transform for a prefab should always have a Box Collider that encapsulates the object.
This allows users to grab and resize the object at will.

Adding Functionality
------------------------

Additional functionality, like Toggle Controllers, Object Cyclers, and Passthrough Shaders can be added via the `Mod Extras`_ package. See the `Mod Extras`_ documentation for details.

.. _Mod Extras: modextras

Custom Thumbnails
------------------------

Sometimes it is necessary to create a custom thumbnail for your Prefab (for example, if many Transforms are toggled off by default).
