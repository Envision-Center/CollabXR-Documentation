============================
Socket Annotations
============================

.. |linker| image:: /images/icons/linker.svg

The |linker| :ref:`Linker <section linker tool>` allows data to be passed between objects, such as a 3D visualization providing legend information to a display panel.

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

.. image:: /images/modextras/socketannotation.png

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

Legend Metadata can be used to output legend information about a visualization, which can connected to the built-in Legend prefab.
This allows the legend to be handled and moved independently from the dataset, allowing mod makers to focus on the visualization itself.

.. image:: /images/modextras/legendmetadata.png

Because creating and maintaining these annotations can be a very time-consuming process for large datasets, we heavily recommend generating these automatically in your visualization pipeline.
For this reason, the Legend Metadata class supports optionally loading from JSON files.

.. code-block:: json
	:caption: example-legend.json
	:name: legend-json-schema

	{
		"variables": [
			{
				"colorsHex": ["#808080", "#ADADAD", "#D9D9D9", "#FFFFFF"],
				"displayLabel": true,
				"displayValues": true,
				"enabled": false,
				"id": "qc",
				"name": "Cloud Water Mixing Ratio",
				"rangeMaximum": 2.0,
				"rangeMinimum": 0.5,
				"thresholds": [0.5, 0.7, 1.2, 2.0],
				"unit": "g/kg"
			},
			{
				"colorsHex": ["#3B392C", "#7A753D", "#BAAF2F", "#FAE500"],
				"displayLabel": true,
				"displayValues": true,
				"enabled": false,
				"id": "zvort_pos",
				"name": "Z Vorticity (+)",
				"rangeMaximum": 0.025,
				"rangeMinimum": 0.01,
				"thresholds": [0.01, 0.015, 0.02, 0.025],
				"unit": "s^-1"
			}
		]
	}

.. note::

	See the `Legend Metadata.Variable struct <https://github.com/Envision-Center/CollabXR-Mod-Extras/blob/stable/Runtime/Measurement/LegendMetadata.cs>`_ to see the full JSON schema.

...or you can set up your own Editor Script for a custom pipeline.

.. code-block:: csharp
	:caption: pipeline-example.cs
	:name: legend-pipeline

	using UnityEditor;
	using System.IO;
	using CollabXR.ModExtras.Measurement;

	// Import legend metadata
	LegendMetadata legend = ScriptableObject.CreateInstance<LegendMetadata>();
	legend.importFrom = meta.legendJsonPath;
	legend.title = meta.title;
	string legendJsonText = File.ReadAllText(legend.importFrom);
	legend.LoadFromString(legendJsonText); // Automatically fill out legend

	// ...make changes to legend as necessary

	// Delete old Legend to avoid conflicts
	AssetDatabase.DeleteAsset(Path.Join(meta.directory, "legend.asset"));

	// Save legend to filesystem
	AssetDatabase.CreateAsset(legend, Path.Join("Assets", meta.directory, "legend.asset"));


Toggle Controller Integration for Legends
"""""""""""""""""""""""""""""""""""""""""""""""""

Legends can hook into :doc:`Toggle Controllers <togglecontroller>` to only show certain variables when they are toggled on.
To do this, set the "Point of Reference" on the socket annotation to the Transform that has your Toggle Controller component.
Then set the "Toggle Index" field on each Legend variable to match the corresponding index of the Togglable Child in the Toggle Controller list.
