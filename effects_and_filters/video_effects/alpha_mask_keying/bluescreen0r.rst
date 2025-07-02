.. meta::

   :description: Kdenlive Video Effects - Alpha Strobing
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, alpha strobing

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Bluescreen0r
============

.. figure:: /images/effects_and_compositions/effects-bluescreen0r-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-bluescreen0r-2504.webp

.. sidebar:: |kdenlive-show-video| Alpha Strobing

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      bluescreen0r
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No
   :**Color depth**:
      8bit
   :**Tutorial**:
      No

.. rst-class:: clear-both


.. rubric:: Description

Turns the selected color into the alpha channel (blue or green screen effect).


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Invert
     - Switch
     - Whether to produce the inverse of the effect on the alpha channel
   * - Color
     - Picker
     - Defines the color that will be turned into the alpha channel
   * - Distance to Color
     - Float
     - Defines the distance between the values of the selected color and the pixel in the image. The lower the number, the closer the colors need to match. Range is from 0.000 (exact match) to 1.000 (very loose match). Default is 0.288.
