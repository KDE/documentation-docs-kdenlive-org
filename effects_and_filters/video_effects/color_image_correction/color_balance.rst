.. meta::

   :description: Kdenlive Video Effects - Color Balance
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, color balance

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Color Balance
=============

.. figure:: /images/effects_and_compositions/effects-color_balance-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-show-video| Color Balance

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      colorbalance
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect modifies the intensity of primary colors (red, green and blue). It allows adjustment in the shadow, mid-tones or highlights regions for the red-cyan, green-magenta or blue-yellow balance.

A positive value shifts the balance towards the primary color, a negative value towards the complementary color.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 10 65
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - | Red
       | Green
       | Blue Shadows
     - Float
     - Adjust the red, green and blue shadows (darkest pixels)
   * - | Red
       | Green
       | Blue Midtones
     - Float
     - Adjust the red, green and blue mid-tones (medium pixels)
   * - | Red
       | Green
       | Blue Highlights
     - Float
     - Adjust the red, green and blue highlights (brightest pixels)
   * - Preserve lightness
     - Switch
     - Preserve lightness when changing color balance. Default is **Off**.
