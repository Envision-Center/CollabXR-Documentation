================================
Surface Materials
================================

Material Compatibility
-------------------------------

These steps will take you through the process of adding Occlusion materials to your models to ensure they look right in mixed reality. These will change the opacity when a real-world object (such as your hands) pass in front of the model.

1. In your Unity project, go to Window -> Package Manager. Click on the "+" sign in the top left of this window.
2. Click "Add package by name..." and paste in ``com.unity.xr.management``
3. Click "Add package from git URL" and paste in ``https://github.com/oculus-samples/Unity-DepthAPI.git?path=/Packages/com.meta.xr.depthapi.urp``
4. Ensure you have the :doc:`Mod Extras<../modextras>` package installed
5. For each Material your model uses, change the shader to "Meta/Depth/URP/Occlusion Lit" (or any of the URP Occlusion shaders)
6. If your model uses shaders other than the basic URP shaders, ensure they are made compatible (see :ref:`Shader Compatibility`).

.. _Shader Compatibility:

Shader Compatibility
-----------------------------

If your model uses Shader Graph, make sure the Graph Settings are set to target ``Universal`` and that the Surface Type is ``Transparent``. You will need to add an `OcclusionSubGraph`_ node, and multiply your final Alpha by this output. This will cause your object to become transparent (hidden) when something (i.e. your arm, a wall, or another person) occludes it in mixed reality.

If your model uses custom shaders, or you are going for a look that is not achievable with the standard URP shaders, you may need to implement depth in your own shader. Check `Meta's guide`_ and `their GitHub`_ for more information.

.. _OcclusionSubGraph: https://developers.meta.com/horizon/documentation/unity/unity-depthapi-occlusions-advanced-usage/
.. _Meta's guide: https://developers.meta.com/horizon/documentation/unity/unity-depthapi-occlusions-advanced-usage/
.. _their GitHub: https://github.com/oculus-samples/Unity-DepthAPI
