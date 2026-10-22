============================
Socket Annotations
============================

.. |linker| image:: /images/icons/linker.svg

The |linker| Linker allows data to be passed between objects, such as a 3D visualization providing legend information to a display panel.

Modders can add Socket Annotations to their own mods to provide data for data consumer sockets.
Currently, only built-in mods in CollabXR have the ability to consume data.

.. warning::

	Sockets are currently experimental and may be subject to change.
	Please report any issues you find `on our GitHub <https://github.com/Envision-Center/CollabXR/issues>`_!

Adding a Socket Annotation
----------------------------------

To add a socket annotation to your mod, create an empty transform inside your mod prefab, and attach a **Socket Annotation** component to it.
Configure this component with your desired socket data.

At runtime, a data provider socket will be spawned on the prefab at the location of the Transform.
If you need multiple socket annotations, it is recommended to place them all on separate transforms as siblings that are spaced apart, so users can easily choose which one to link.

Texture Data Type
--------------------

You can reference both 2D and 3D textures in a socket annotation.
This texture reference can be animated using an Animator component and the :doc:`Playback System <playbacksystem>`.

Optionally specify a "Point of Reference" Transform to give a reference of where 3D texture data is located within your prefab.

ScriptableObject Data Types
---------------------------------

ScriptableObjects can contain complex data structures for providing in your socket that can't otherwise be provided.
A few types are provided.

Legend Metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^

Legends can hook into :doc:`Toggle Controllers <togglecontroller>` to only show certain variables when they are toggled on.
To do this, set the "Point of Reference" on the socket annotation to the Transform that has your Toggle Controller component.
