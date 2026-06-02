============================
Application Setup
============================

This covers everything you should need to join a CollabXR lobby or create your own.
If you are trying to playtest a developer build, see :ref:`Playtesting <section playtesting>`.

.. _section connecting to the internet:

Connecting to the Internet
--------------------------------

CollabXR requires an internet connection to function.
Before starting CollabXR, ensure your device has a working Wi-Fi connection.

- `Connect your Meta Quest headset to Wi-Fi <https://www.meta.com/en-gb/help/quest/1816744325172615/>`_
- `Troubleshoot joining a Wi-Fi network on Meta Quest <https://www.meta.com/en-gb/help/quest/517103729284781/>`_

Joining a Room
----------------------------

Once the application is open, you should see a menu that says "Join a Classroom."

Joining with a QR Code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have a QR Code for your lobby, ensure the QR Code is on a flat surface and in bright lighting so it is easily visible in the headset.

Press "Scan room code" to enter scanning mode, stand next to the QR Code, and look directly at it.
Once scanned, axis arrows should show up on top of the QR Code--this means you are connected!

- If the QR Code does not scan initially, try getting closer to it and looking at the code from different angles.
- If the UI abruptly disappears, before showing "Join a Classroom" again, check your :ref:`internet connection <section connecting to the internet>`.

Connecting Directly
^^^^^^^^^^^^^^^^^^^^^^^^^

You can optionally enter the room name into the text box "Enter room name..." and press connect to directly join a room.
You will not be :ref:`colocated <section colocation>` upon joining when using this method,
but you can still co-locate while in the lobby if you have a QR Code available.

.. _section colocation:

Colocation
-----------------------

**"Colocation" is a state where multiple devices are tied to the same shared, collaborative space.**
This is key to the instructional aspect of CollabXR, where interactions in both a physical space *and* digital space can work together.

Colocation and QR Codes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

QR Codes are useful for colocating, as they define a position and orientation in 3D space in a way that most devices can understand.
For the best experience, it is recommended to follow these practices when using QR Codes.

- Always place your QR Code flat on the floor
- Do not move the QR Code after connecting to a lobby
- With the above two in mind, place your QR Code in a spot where it is unlikely to be stepped on
- Ensure your QR Code is large enough to be clearly visible on camera
- Ensure your QR Code is in bright lighting

Colocating while in a Lobby
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Devices can sometimes "drift" and lose their colocation due to poor tracking, latency, or the device falling asleep.
You can tell if a user is not co-located because the "User" tag above their head will be offset or not be visible, and they will not see objects in the same position as you do.
This can be fixed by re-scanning the QR Code while inside the lobby.

1. Open the menu using the bottom button on your Quest controller
2. On the bottom bar, select the "Colocate" tab with the QR Code icon
3. Stand next to your QR Code and look directly at it

If the colocation was successful, you should see the axis arrows re-appear on top of the QR Code.


Creating Your Own Lobby
--------------------------------

To create your own lobby, use a QR Code generator from online.
Lobby codes just need to be raw text, they do not need to be a web URL or anything.
Enter in the desired name of your lobby, and print out the QR Code on a sheet of paper--make sure it's large enough to be read by the headset, about 6 inches across minimum.

Place the QR Code on the ground, and you should be ready!
