.. meta::

   :description: Do your first steps with Kdenlive video editor, using hsvkey effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, misc, miscellaneous, hsvkey

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-hsvkey:

Hsvkey
======

This effect/filter turns a certain HSV\ [1]_ range into transparency.

This filter measures color difference between set HSV color in options and ones measured in video stream. Depending on options, output colors can be changed to transparent by adding alpha channel.

.. note:: This effect does not do anything as of this writing and in version 23.04.3. A bug report has been filed.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-hsvkey.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-hsvkey

   Hsvkey effect

* **hue** - Set the :term:`hue` value which will be used in color difference calculation. Allowed range is from -360.000 to 360.000. Default value is 0.000.

* **sat** - Set the :term:`saturation` value which will be used in color difference calculation. Allowed range is from -1.000 to 1.000. Default value is 0.000.

* **val** - Set the value which will be used in color difference calculation. Allowed range is from -1.000 to 1.000. Default value is 0.000.

* **similarity** - Set similarity percentage with the key color. Allowed range is from 0.000 to 1.000. Default value is 0.010.  0.001 matches only the exact key color, while 1.000 matches everything.

* **blend** - Blend percentage. Allowed range is from 0.000 to 1.000. Default value is 0.000. 0.000 makes pixels either fully transparent, or not transparent at all. Lower values result in semi-transparent pixels, with a higher value the more similar the pixels color is to the key color.

.. rst-class:: clear-both


**Notes**

.. [1] HSV := Hue, Saturation, Value
