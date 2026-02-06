Shaders
======

Shader Parameter Driver
-----------------------------

MonoBehavior that automatically drives shader parameter inputs based on a referenced Transform. Can be used to more consistently animate shaders via animation or interaction.

**Targets** - Specifies a list of shaders to drive, when given a Renderer target and corresponding material index.

**Drivers** - Specifies a list of shader parameters and how to drive them.

* The `Parameter` field specifies the name of the shader parameter. The name is automatically prefixed with an underscore during processing.

* The `Driver` field specifies the Transform to drive this parameter with.

* `Value` specifies what spatial data value should be taken from the object.

	* `Position` specifies the driver's position. W is always passed as zero.
 	* `Rotation Euler` specifies the driver's rotation in Euler Angles, in degrees. W is always passed as zero.
 	* `Rotation Quaternion` specifies the driver's rotation as a Quaternion.
 	* `Scale` specifies the driver's *lossy* scale. W is always passed as zero.

  * The `Type` field specifies what data type is used to drive the shader.

	* `Float` passes the length of the vector.
	* `Integer` passes the length of the vector, rounded to the nearest integer.
	* `Vector` passes the vector with up to 4 coordinates (XYZW). It can be used for any vector type parameter (Vector2, Vector3, Vector4).

* If `Local Space` is checked, the value is automatically converted into the target renderer's local coordinate space. Otherwise, the value is always in world space.
