Developer Setup
==============

Consistent, clean, and readable code is important when making contributions in order to reduce friction between developers.
While not required, installing these tools and adhering to code style guidelines is **strongly recommended** for a streamlined PR review process.

DotNet
----------

We recommended .NET SDK version 10, but anything support by .NET Standard 2.1 should be okay,
although some tools like CSharpier may not work with older SDK versions.

1. Ensure the proper `dotnet`_ version is installed: ``$ dotnet --version``
2. In the root directory of the `CollabXR repository`_, install the dotnet tool manifest: ``$ dotnet tool restore``
3. Install corresponding plugins for your IDE as necessary (`CSharpier plugin list`_)

If not automatically handled by your IDE, you can format using CSharpier at any time: ``$ dotnet csharpier .``

.. _dotnet: https://dotnet.microsoft.com/en-us/download/dotnet
.. _CSharpier: https://csharpier.com/docs/About
.. _CSharpier plugin list: https://csharpier.com/docs/Editors

Pre-Commit Hooks
-----------------------

`pre-commit`_ is used for formatting fixes and validation before making commits and pushing them.
Their documentation provides a recommended installation method.

- If you're working on Debian, pre-commit can be installed globally via apt: ``$ sudo apt install pre-commit``

Once pre-commit is installed on your system, you can set it up within the root directory of the `CollabXR repository`_: ``$ pre-commit install``

Now, any time you make a commit, pre-commit should fix any formatting or whitespace issues before the commit is made.
If any issues arise, pre-commit will abort the commit, allowing you to add changes before committing again.

.. _pre-commit: https://pre-commit.com/
.. _CollabXR repository:
