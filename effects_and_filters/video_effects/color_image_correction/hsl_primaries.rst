.. meta::

   :description: Kdenlive Video Effects - HSL Primaries
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, hue shift

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             - Eugen Mohr

   :license: Creative Commons License SA 4.0


HSL Primaries
=============

.. figure:: /images/effects_and_compositions/kdenlive2412_effects-hsl_primaries.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2412_effects-hsl_primaries

.. sidebar:: |kdenlive-show-video| HSL Primaries

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      MLT
   :**Source filter**:
      hslprimaries
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

Adjust :term:`hue`, :term:`saturation` and lightness for each of the 3 primary colors (Red, Green, Blue) and 3 secondary colors (Cyan, Magenta, Yellow). HSL color space is useful when performing subtle color changes.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 20 55
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Hue Shift color
     - 0° to 360°
     - 0° (or 360°) is red, 120° is green, 240° is blue
   * - Saturation Scale color
     - 0% to 100%
     - Intensity of a color: 0% completely gray, 50% gray, 100% color
   * - Lightness Scale color
     - 0% to 100%
     - How much light you want to give the color: 0% no light (dark)
   * - Overlap
     - 0% to 100%
     - The amount of overlap or blending between primaries
