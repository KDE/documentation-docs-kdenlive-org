.. meta::

   :description: Kdenlive Video Effects - Emboss
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, emboss

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Emboss
======

.. figure:: /images/effects_and_compositions/effects-emboss-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-emboss-2504.webp

.. sidebar:: |kdenlive-show-video| Emboss

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      emboss
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

This effect/filter creates a greyish embossed relief appearance of the source image.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Light direction
     - Integer
     - The direction of the embossing (practically simulating a light source). Value is an angle between 0 and 360 degrees.
   * - Background lightness
     - Integer
     - Defines the brightness/lightness of the areas not embossed
   * - Bump height
     - Integer
     - Defines the thickness of the edges increasing/decreasing the perceived depth of the embossed areas
