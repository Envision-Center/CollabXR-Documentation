IDE Specifics
===============

Visual Studio 2022
------------------------

To enable formatting with CSharpier, go to `Tools` on the top bar > `Options` > search `CSharpier` > `General` and then set `Reformat with CSharpier on Save` to True, either globally or on the specific solution.

The CSharpier plugin only loads the config on startup, so **you will need to restart Visual Studio on install in order to reload the config,** or whenever you modify the ``.editorconfig``.

Zed
---------

To enable formatting with CSharpier, add this to your user or project settings file.

.. code-block:: json
	:caption: manifest.json
	:name: config-zed-csharpier

	{
		"languages": {
			"CSharp": {
				"format_on_save": "on",
				"formatter": {
					"external": {
						"command": "dotnet-csharpier",
						"arguments": ["--write-stdout"],
					}
				}
			}
		}
	}
