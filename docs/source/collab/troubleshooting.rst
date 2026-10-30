===============================
Troubleshooting
===============================

.. _section qrcode troubleshooting:

QR Codes Best Practices
----------------------------

We heavily recommend printing a sheet of paper for each QR Code for portability and consistency.

- Ensure your QR Code is large enough to be clearly visible on the headset cameras
- Ensure your QR Code is in bright lighting or on a bright screen
- Ensure there is a small, white border surrounding your QR code so it can be detected by the headset
- Ensure only one QR Code is visible within your peripheral vision at a time (to prevent the headset from focusing on the wrong QR Code)
- Pair a label with the QR code so you can remember what it is

.. _section colocation:

|colocate| Colocation
-----------------------

**"Colocation" is a state where multiple devices are tied to the same shared, collaborative space.**
This is key to the instructional aspect of CollabXR, where interactions in both a physical space *and* digital space can work together.

Colocation and QR Codes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

QR Codes are useful for colocating, as they define a position and orientation in 3D space in a way that most devices can understand.
For the best experience, it is recommended to follow these practices when using QR Codes.

- Always place your room's QR Code flat on the floor
- Do not move the QR Code after connecting to a room
- Place your QR Code in a spot where it is unlikely to be stepped on
- If printed, include the room code as text on the same sheet of paper so a user can manually type in the room coode if needed

Colocation Drift
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Devices can sometimes "drift" and lose their colocation due to poor tracking, latency, or the device falling asleep.
You can tell if a user is not co-located because the "User" tag above their head will be offset or not be visible, and they will not see objects in the same position as you do.
This can be fixed by re-scanning the QR Code while inside the room.

1. Open the menu using the red |menu| Menu button on your Quest controller
2. On the bottom bar, select the |colocate| Colocate button
3. Stand next to your QR Code and look directly at it

If the colocation was successful, you should see the axis arrows re-appear on top of the QR Code.


Enabling Permissions
--------------------------------

CollabXR requires camera access and spatial data in order to perform certain actions such as scanning QR Codes and enabling depth.

If you did not enable permissions, or were not prompted to, you can change them by opening the main settings, scrolling to the **Privacy and Safety** category on the left-hand side of the menu, and finding the CollabXR application.

.. image:: /images/collab/troubleshooting/open-settings.jpg

.. image:: /images/collab/troubleshooting/privacy-and-safety.jpg

.. image:: /images/collab/troubleshooting/collabxr-app-settings.jpg
