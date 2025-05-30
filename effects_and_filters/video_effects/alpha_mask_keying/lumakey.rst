.. meta::

   :description: Kdenlive Video Effects - Lumakey
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, alpha, chroma key, greenscreen, bluescreen, keying, lumakey

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Lumakey
=======

.. figure:: /images/effects_and_compositions/effects-lumakey-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-lumakey-2504.webp

.. sidebar:: |kdenlive-show-video| Lumakey

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      MLT
   :**Source filter**:
      lumakey
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This filter modifies the image's alpha channel as a function of its :term:`luma` value. This is used together with a compositor to combine two images so that bright or dark areas of source image are overwritten on top of the destination image.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 30 10 60
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Threshold
     - Integer
     - Luma value that defines the center point of transition from prelevel to postlevel opacity value.
   * - Slope
     - Integer
     - Defines the width of the transition from prelevel to postlevel luma value. Start point of transition in opacity value is `threshold - slope` and end point is `threshold + slope`, values are forced in range 0 - 255.
   * - Pre-Threshold Luma Level
     - Integer
     - Opacity value before the transition in opacity value begins
   * - Pre-Threshold Luma Level
     - Integer
     - Opacity value after the transition in opacity value ends
