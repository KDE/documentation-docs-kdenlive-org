.. meta::
   :description: The Kdenlive User Manual
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, help, learn, Linux workaround, problem solving

.. metadata-placeholder

   :authors: - Eugen Mohr

   :license: Creative Commons License SA 4.0


.. _linux_issues:

Linux issues
==============

.. contents::


.. _color_picker:

Color picker is missing
-----------------------

During the color selection this window appears only:

.. image:: /images/select_color.png
   :alt: select color

Clicking on the red circled :guilabel:`+` you only get:

.. image:: /images/select_color_choose.png
   :alt: select color choose

To get the correct color picker you have to change the variable `QT_QPA_PLATFORMTHEME` to `qt5ct`

- either for each user in the file `~.profile` to `export QT_QPA_PLATFORMTHEME="qt5ct"`

- or globally: add in the file `etc/enviroment` the variable `QT_QPA_PLATFORMTHEME=qt5ct` (if set globally: do not make the entry in file `~.profile`).

After you have changed the the variable `QT_QPA_PLATFORMTHEME` to `qt5ct` you get the correct color picker:

.. image:: /images/color_picker.png
   :alt: color picker