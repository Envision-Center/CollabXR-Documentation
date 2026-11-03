============================
Application Setup
============================

.. |menu| image:: /images/icons/menu.svg
.. |colocate| image:: /images/icons/colocate.svg

This covers everything you need from installing CollabXR, to creating and joining your own classroom.
If you are trying to playtest a developer build, see :ref:`Playtesting <section playtesting>`.

Installing CollabXR
--------------------------------

Currently, CollabXR must be `installed manually <https://github.com/Envision-Center/CollabXR#installation>`_ for both Meta Quest and Desktop VR.
We currently only support Meta Quest and Windows Desktop platforms.

The latest stable builds are located on the `GitHub releases <github.com/Envision-Center/CollabXR/releases>`_ page.

- Meta Quest: You can install the ``.apk`` file onto your headset via the `Meta Quest Developer Hub`_.
- Desktop VR: Unzip the ``.zip`` file and run the executable. It will launch in your currently active OpenXR runtime (i.e. `Meta Horizon Link`_).

.. _Meta Quest Developer Hub: https://developers.meta.com/vr/downloads/package/oculus-developer-hub-win/
.. _Meta Horizon Link: https://www.meta.com/en-gb/help/quest/1517439565442928/

.. _section connecting to the internet:

Connecting to the Internet
--------------------------------

CollabXR requires a stable internet connection.
Before starting CollabXR, ensure your device has a working Wi-Fi connection and access to the internet.

- `Connect your Meta Quest headset to Wi-Fi <https://www.meta.com/en-gb/help/quest/1816744325172615/>`_
- `Troubleshoot joining a Wi-Fi network on Meta Quest <https://www.meta.com/en-gb/help/quest/517103729284781/>`_

Creating Your Own Room
--------------------------------

.. note::

	This step is only necessary for those intending to use passthrough (Augmented Reality).
	A room code can be any string of text.

To create your own room, use a free QR Code generator.
The QR code can simply contain a word or phrase--it does not need to be a URL.
Because users joining a classroom remotely may need to manually type the phrase on your QR code, a memorable word such as "classroom" is typically good enough.

Once generated, print out the QR Code on a sheet of paper.
Make sure it's large enough to be read by the headset, about 6 inches across minimum.
Place the QR code directly on the floor in a well-lit area.
We recommend reading the :ref:`colocation section <section colocation>` to minimize issues with scanning QR codes.

And that's it! CollabXR will create the room automatically upon scanning the QR code.

.. _section joining room:

Joining a Room
----------------------------

Once the application is open, you should see a menu that says "Join a Classroom."

.. image:: /images/collab/setup/join_a_classroom.jpg

.. note::

	Joining a room without changing your Photon App IDs will place you in a room using the Envision Center's development API keys.
	**This is intended only for testing and evaluating CollabXR.**
	If you are using CollabXR for research, education, or any other production environment we ask that you :ref:`use a custom App ID<section custom app id>`.

Joining with a QR Code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have a QR Code for your room, ensure the QR Code is on a flat surface and in bright lighting so it is easily visible in the headset.

Press "Scan room code" to enter scanning mode, stand next to the QR Code, and look directly at it.
Once scanned, axis arrows should show up on top of the QR Code--this means you are connected!

- If the QR Code does not scan initially, try getting closer to it and looking at the code from different angles.
- If the UI abruptly disappears, before showing "Join a Classroom" again, check your :ref:`internet connection <section connecting to the internet>`.

Connecting Directly
^^^^^^^^^^^^^^^^^^^^^^^^^

You can optionally enter a room name into the text box "Enter room name..." and press connect to directly join a room.
You will not be :ref:`colocated <section colocation>` upon joining when using this method,
but you can still co-locate while in the room if you have a QR Code available.

.. _section custom app id:

Using a Custom App ID
----------------------

By default, CollabXR includes an App ID (API token) for Photon Fusion and Photon Voice, the networking backend that makes CollabXR possible.
This is intended to allow for easier testing and evaluation of CollabXR.
This is a development license with a maximum of 20 concurrent users, and is shared by all users testing the application.

For this reason, **we ask that you use your own App IDs as soon as you are done evaluating CollabXR**.
If you just want to join a classroom to test the application, skip to :ref:`the next section <section joining room>`.

To do this, follow the below instructions:

1. `Create a Photon account <https://www.photonengine.com/>`_
2. Create both a Photon Fusion and a Photon Voice app. Apps in the development cloud are free for development and testing and work with up to 20 concurrent users.
3. Obtain the App ID for each as shown in the image below.

.. image:: /images/collab/setup/photon_fusion_appid.png

4. If you plan to use CollabXR on a Meta Quest, create a separate QR code for each using any online QR code generator.
5. Open CollabXR, navigate to the Settings tab on the bottom bar, and then Networking.
6. Enable the "Use Custom Photon App ID" switch.
7. Press the QR icon next to each field to scan a QR code, or enter the IDs manually.
8. Your App IDs will be saved automatically to the headset, and you may continue on to :ref:`joining a room <section joining room>`.

.. image:: /images/collab/setup/network_settings.jpg

From now on, when you launch CollabXR you will be using these custom App IDs.
Note that this must be done once per headset.
**Any user you intend to connect to will also need to be using these App IDs.**
