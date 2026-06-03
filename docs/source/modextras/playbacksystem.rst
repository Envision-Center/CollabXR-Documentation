Playback System
=============================

The Mod Extras package provides in-editor support for live playback of animations and other frame-based content during a CollabXR session. This feature comes in the form of MonoBehaviours that can be appended to your Mod.

Playback Director
---------------------------------
A MonoBehaviour that can be added to your GameObject to control different Playback Components, including the `Animator Cycle Part`_ and `Object Cycle Part`_ components, among the others provided. It provides a simple interface for starting, stopping, and pausing playback, as well as setting the current time and playback speed.

To add a `Playback Director`_ to your Prefab, place it on the root GameObject of your mod, and add a "Playback Director" component from ``CollabXR.ModExtras``.

The `Playback Director`_ has a number of public fields that can be configured in the inspector. You may hover over the fields in the Unity Editor to read more through a tooltip, but the fields include:

- `Duration`: The total duration of the playback in seconds. Because the Playback Director can sync many different types of content, this value determines the overall length of the playback sequence. If you just have an animation clip, it is recommended to set the duration to the length of the clip, but you can set it to be longer or shorter if you so desire.
- `Loop`: A boolean that determines whether the playback should loop when it reaches the end of the duration.
- `View Model`: A reference to a `Playback View Model`_ component that will be used to visualize the state of the playback in the UI. **This field is required for proper visualisation in the UI, and must reference a Playback View Model component on the same GameObject.**
- `Effect Components`: A list of Playback Components that will be controlled by this Playback Director. You can add any number of components to this list, and they will all be synced together during playback. **Ensure that any Playback Components you want to control are added to this list.**
- `Sync Mode`: An enumerated value that determines how the Playback Director should handle syncing of the different Playback Components. The default value is `Scale Percent`, which means that all effects will be synced based on the percentage of the total duration that has elapsed. The other option is `Sync By Frame`, which means that the Playback Director will attempt to sync all effects based on their individual frame counts. The best option depends on the types of content you are trying to sync.

Playback View Model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A MonoBehaviour that provides a data model for the UI to visualize the state of the `Playback Director`_.
Once the `Playback Director`_ is added to your object, you should also add a `Playback View Model`_ component to the same GameObject from ``CollabXR.ModExtras``. **This component is required for proper visualisation in the UI, and must be on the same GameObject as the Playback Director.**


.. note::

    It is recommended to place the `Playback Director`_ and `Playback View Model`_ on the root GameObject of your mod, as it will be easier to reference from other components and scripts. However, it can technically be placed on any GameObject in the prefab's hierarchy.

Playback Components
---------------------------------
The Mod Extras package provides a variety of Playback Components that can be used to control different types of frame-based content, such as animations, GameObject cycling, and more. These components can be added to any GameObject in your prefab, and can be controlled by the `Playback Director`_. **Ensure that these components are assigned in the corresponding field in the Playback Director.**

Object Cycle Part
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A Playback Component that cycles through a list of GameObjects, activating one at a time based on the current time of the playback. This can be used to create simple frame-by-frame animations by swapping out GameObjects, or to cycle through different states of an object.

To add an `Object Cycle Part`_ to your prefab, add a child Transform, and then add an "Object Cycle Part" component from ``CollabXR.ModExtras``. You can then populate the `Objects` list with the GameObjects you want to cycle through. The order of the GameObjects in the list determines the order in which they will be activated during playback.

You can also choose to automatically populate the `Objects` list at runtime through the boolean options on the component, which will then attempt to populate the list using the child GameObjects (optionally sorting lexicographically). This list can also be populated in the editor through the provided inspector buttons.

Animator Cycle Part
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A Playback Component that controls an Animator component to play an animation clip based on the current time of the playback. This can be used to sync an animation with other effects during playback, or independently as a simple way to scrub through animations.

To add an `Animator Cycle Part`_ to your prefab, add a child Transform, and then add an "Animator Cycle Part" component from ``CollabXR.ModExtras``. You can then assign an Animator component to the `Target` field.

.. note::

    The Animator component that you assign to the `Target` field must have an Animator Controller with states that correspond to the animation clips you want to play. It is also recommended to have a default state that can be used when no specific state is assigned for an animation clip.

One feature of the `Animator Cycle Part`_ is the ability to switch between different combinations of Animation Clips in a CollabXR session to display different variations on the same Animator. These combinations, called **Animation Sets**, can be assigned in the inspector as well under the `Sets` field. Each set includes:

- `Name`: The name of the set, which is used for reference in the UI.
- `Animations`: A list of Animation Clip Info structures, which include:

    - `Clip`: The Animation Clip to be played for this set.
    - `State Name`: The name of the animation state to play for this set. **This field must correspond to an actual state in the Animation Controller corresponding to the specified clip.**
    - `Layer`: The index of the Animator layer to play the animation on. This defaults to 0, which is the base layer of the Animator.

When using the `Animator Cycle Part`_ during a CollabXR session, the user can switch between the different Animation Sets that you have configured in the inspector, where all specified animations in the set will be played together. This is especially useful if you have multiple animations to play on different layers, but take care that all your animations are of proper length relative to each other for proper visualisation.

Animation Audio Listener
""""""""""""""""""""""""""""""""""""""""
A MonoBehaviour that listens for Animation Events on an Animator component and triggers audio clips based on those events.

To add an `Animation Audio Listener`_ to your prefab, add an "Animation Audio Listener" component from ``CollabXR.ModExtras`` to the same GameObject as your Animator component. You can then populate the `Events` list with the audio events you want to trigger. Each event includes:

- `Call Index`: An index corresponding to this clip. When adding an animation event to a clip, populate the integer field with the corresponding call index of the audio you want to play.
- `Clip`: The Audio Clip to be played for this event.
- `Volume`: The volume at which to play the clip for this event, which is a value between 0 and 1. This allows you to have different events play at different volumes if desired.

.. note::
    This component is not necessarily reliant on the Playback System, but is best used in context with the `Animator Cycle Part`_ to play one-shot sounds during an animation.

Material Cycle Part
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A Playback Component that cycles through a list of Texture3Ds, applying one at a time to a specified Material based on the current time of the playback. This can be used to create simple frame-by-frame animations by swapping out textures on a material.

To add a `Material Cycle Part`_ to your prefab, add a child Transform, and then add a "Material Cycle Part" component from ``CollabXR.ModExtras``. You can then assign a Mesh Renderer and populate the `Textures` list with the Texture3Ds you want to cycle through. The order of the Texture3Ds in the list determines the order in which they will be applied during playback. More info can be found in tooltips.

Audio Cycle Part
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A Playback Component that lets you scrub through an Audio Clip based on the current time of the playback. This can be used to sync audio tracks across playback of an animation, or independently as a simple way to scrub through audio.

.. note::

    The Audio Cycle Part is used for continuous audio, and as such only works under the `Scale Percent` sync mode of the `Playback Director`_. It is not recommended for use with the `Sync By Frame` mode, as it does not have discrete frames to sync to. For event-based audio, use the `Audio Event Cycle Part`_ or the `Animation Audio Listener`_ instead.

To add an `Audio Cycle Part`_ to your prefab, add a child Transform, and then add an "Audio Cycle Part" component from ``CollabXR.ModExtras``. You can then assign an Audio Source and an Audio Clip to the corresponding fields in the inspector. The Audio Source will be used to play the audio clip during playback, and the clip will be scrubbed through based on the current time of the playback.

Audio Event Cycle Part
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A Playback Component that lets you trigger one-shot audio clips based on the current frame of the playback. This can be used to play timed sound effects during an animation, or to create a simple step sequencer by triggering different clips on different frames.

To add an `Audio Event Cycle Part`_ to your prefab, add a child Transform, and then add an "Audio Event Cycle Part" component from ``CollabXR.ModExtras``. You can then assign an Audio Source and populate the `Events` list with the audio events you want to trigger. Each event includes:

- `Frame`: The frame of the playback at which to trigger this event. This is determined by the total number of frames in the playback, which is calculated based on the `Duration` field of the `Playback Director`_ and the frame rate of the playback (which is determined by the number of frames in the longest Animation Clip or Object Cycle Part, or can be set manually in the inspector). When the playback reaches this frame, the specified audio clip will be played once on the assigned Audio Source.
- `Clip`: The Audio Clip to be played for this event.
- `Volume`: The volume at which to play the clip for this event, which is a value between 0 and 1. This allows you to have different events play at different volumes if desired.

Alternatively, you can use the `Animation Audio Listener`_ component to leverage Unity's Animation Event system to add events on animation clips as well.

Playback Preview
-------------------------------
To test the playback of your animations and other content in the Unity Editor, you can use the `Playback Director`_'s Editor Window to simulate the playback of your content without having to enter Play mode or start a CollabXR session.

To access the window, navigate to `CollabXR > Mod Extras > Playback Director` in the Unity Editor menu bar. This will open a window that allows you to control the playback of the content on a specified `Playback Director`_ component in the editor.

In this editor, you can use the play, pause, and stop buttons to control the playback. You can also scrub through the playback using the timeline slider, and adjust the playback speed using the speed slider. You can also swap between animation sets here as well.
