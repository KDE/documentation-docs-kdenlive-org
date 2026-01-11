.. meta::
   :description: Kdenlive Documentation - Configuration JogShuttle
   :keywords: KDE, Kdenlive, documentation, user manual, configuration, preferences, jogshuttle, jog shuttle, contour shuttlepro, contour shuttlexpress, contour, video editor, open source, free, learn, easy


.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Jog Shuttle
-----------

Configure a connected jog shuttle device. Contour *ShuttlePro* and Contour *ShuttleXpress* are known to work.

.. figure:: /images/getting_started/configure_jogshuttle_2412.webp
   :width: 700px
   :figwidth: 700px
   
   Configure section Jogshuttle

:1: :guilabel:`Enable Jog Shuttle device`. Select this if you want to use a connected jog shuttle device (provided it is supported by your OS and Kdenlive).

:2: :guilabel:`Device name`. Select the device from this list. Click on |view-refresh| to refresh the list.

:3: Enter here device-specific parameters or identifiers (see below).

.. _configure_jog_shuttle_linux:

Linux
~~~~~

Ensure that your Jog-Shuttle device is connected via USB and working. An ``udev`` rule is necessary to correct the access rights to the device file. Use the text editor of your choice and create a file :file:`/etc/udev/rules.d/90-contour-shuttleXpress.rules` with the line:

.. code-block:: bash

   SUBSYSTEMS=="usb", ATTRS{idVendor}=="0b33", ATTRS{idProduct}=="0020", MODE="0444"

for Contour ShuttleXpress, or

.. code-block:: bash

   SUBSYSTEMS=="usb", ATTRS{idVendor}=="0b33", ATTRS{idProduct}=="0030", MODE="0444"

for Contour ShuttlePRO V2.

Obtain the device file by the command in the terminal

.. code-block:: bash

   $ fgrep Contour -A4 /proc/bus/input/devices

The last line of the output says

.. code-block:: bash

   H: Handlers=mouse0 event3

which should tell the device file to be entered into Kdenlive's setting dialog. In the text field (**3**) enter ``/dev/input/**event3**`` (use the last word on the line above to specify the device file in /dev/input), set the buttons and apply the changes.


.. figure:: /images/getting_started/KDENLIVE_Configure_jog_shuttle.png
   :width: 500px
   :figwidth: 500px
   
Enable Jog-Shuttle. For the Contour ShuttleXpress the buttons 5 - 9 are relevant, whereas Contour ShuttlePro uses all buttons. The actions for the jog and the shuttle wheel are working as expected.


.. _configure_jog_shuttle_windows:

Windows
~~~~~~~

On the desktop open the system tray. Right-click on the Contour icon and choose **Open Control Panel**. 


.. image:: /images/getting_started/Contour_open-cotrol-panel.png
   
In the configuration window, under **Application setting** choose the program *Adobe Premiere Pro CS&CC (Edit)*. Then click on :menuselection:`Options --> Create new settings --> Copy contents from Current Settings`. 


.. image:: /images/getting_started/Contour_new_settings.png
   
Then choose :file:`kdenlive.exe` in :file:`C:\\Program Files\\kdenlive\\bin`. 


.. image:: /images/getting_started/Contour_Design_Choose_Aplication.png
   
Now the basic functionality should work. Adjust the buttons of the shuttle with shortcuts as you like.

.. This is not available anymore, is it?
   .. hint::

   You can make Kdenlive settings from scratch using :menuselection:`Options --> Create new settings --> Create Empty Settings` when creating new settings.
