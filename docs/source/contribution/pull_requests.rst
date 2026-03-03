Pull Request Guidelines
=================

Keep Changes Small
-----------------------

Ideally, split up Pull Requests based on what they implement.
A good rule-of-thumb is one Pull Request per bugfix or feature.

Larger pull requests are more difficult to review, test, and iterate on.
Keeping your pull request small will reduce review and iteration time.

Do not touch unrelated areas of the codebase when possible.

Be mindful of adding dependencies such as Unity packages.
Packages may slow down the build process and reduce portability.

Avoid changing core Prefabs and Scenes in order to minimize merge conflicts.
If you change an existing Prefab or Scene, explain your changes in the PR so maintainers know what changed.

Always check your change list before you commit!

Document Your Code
----------------------

Documentation is key to collaboration (you're reading docs right now!).
There are a handful of ways to keep good documentation.

- **Use XML docs for reusable methods/classes/variables.** C# supports built-in `XML documentation`_ which provides in-IDE documentation for users.
- **Comment your code.** It is helpful for other contributors to see your thought process as you work, to avoid potentially breaking it later.
- **Add tooltips to fields.** When creating any editor-facing fields, use Unity's `Tooltip Attributes`_ to minimize confusion where able.
- **Extend the docs.** If you are adding features or modifying known behavior, it may be advisable to contribute directly to this documentation.

.. _XML documentation: https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/xmldoc/
.. _Tooltip Attributes: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TooltipAttribute.html


Respect Licensing and Copyright
------------------------------------

If you are using code from somewhere else, or including an external library,
ensure that the code is distributable under our license.


Project Management
------------------------

Be sure to mention the issue you are trying to resolve in the description of your Pull Request, so other contributors can keep track of what work is being completed.
A typical way to do this is to include the issue number in your description, such as ``Resolves #73``, so GitHub will automatically reference it.
This will also automatically close the issue when merged.

Keep your Pull Request marked as a draft until ready for review.
