.. meta::

   :description: Kdenlive Video Effects - HSL Range
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, hue shift

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             - Eugen Mohr

   :license: Creative Commons License SA 4.0


HSL Range
=========

.. figure:: /images/effects_and_compositions/effects-hsl_range-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| HSL Range

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      hslrange
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

Adjust :term:`hue`, :term:`saturation` and lightness for a range of hue values. You can specify the range of the hue values to be adjusted. HSL color space is useful when performing subtle color changes.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 20 55
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Hue Center
     - 0° to 360°
     - The center value for the hue range
   * - Hue Range
     - 0% to 100%
     - The width of the hue range
   * - Blend
     - 0% to 100%
     - The amount to blend the edges of the hue range
   * - Hue Shift
     - 0% to 100%
     - The amount to shift the hue in the hue range
   * - Saturation Scale
     - 0% to 100%
     - The amount to scale the saturation in the hue range
   * - Lightness Scale
     - 0% to 100%
     - The amount to scale the lightness in the hue range
