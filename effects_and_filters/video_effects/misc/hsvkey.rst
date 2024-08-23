.. meta::

   :description: Kdenlive Video Effects - Hsvkey effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, misc, miscellaneous, hsvkey

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Hsvkey
======

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-hsvkey.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-hsvkey

.. sidebar:: |kdenlive-show-video| Hsvkey

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      hsvkey
   :**Available**:
      |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter turns a certain :abbr:`HSV (Hue, Saturation, Value)` range into transparency.

This filter measures color difference between set HSV color in options and ones measured in video stream. Depending on options, output colors can be changed to transparent by adding alpha channel.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - av.hue
     - Float
     - Set the :term:`hue` value which will be used in color difference calculation. Allowed range is from -360.000 to 360.000. Default value is 0.000.
   * - av.sat
     - Float
     - Set the :term:`saturation` value which will be used in color difference calculation. Allowed range is from -1.000 to 1.000. Default value is 0.000.
   * - av.val
     - Float
     - Set the value which will be used in color difference calculation. Allowed range is from -1.000 to 1.000. Default value is 0.000.
   * - av.similarity
     - Float
     - Set similarity percentage with the key color. Allowed range is from 0.000 to 1.000. Default value is 0.010.  0.001 matches only the exact key color, while 1.000 matches everything.
   * - av.blend
     - Float
     - Blend percentage. Allowed range is from 0.000 to 1.000. Default value is 0.000. 0.000 makes pixels either fully gray, or not gray at all. Lower values result in more gray pixels, with a higher value the more similar the pixels color is to the key color.


.. rubric:: Notes

.. attention::
   This effect does not do anything as of this writing (version 23.04.3). A bug report has been filed.
