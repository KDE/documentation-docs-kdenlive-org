.. meta::

   :description: Kdenlive Video Effects - Color Levels
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, color_levels

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Color Levels
============

.. figure:: /images/effects_and_compositions/effects-color_levels-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-color_levels-2504.webp

.. sidebar:: |kdenlive-show-video| Color Levels

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      colorlevels
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter adjusts video input frames using levels.

*Input levels* are used to lighten highlights (bright tones), darken shadows (dark tones), change the balance of bright and dark tones. *Output levels* allows manual selection of a constrained output level range.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - | Red
       | Green
       | Blue black input
     - Float
     - Adjust red, green and blue input black point. Allowed values are 0 to 1.0, default is 0.
   * - | Red
       | Green
       | Blue white input
     - Float
     - Adjust red, green and blue input white point. Allowed values are 0 to 1.0, default is 1.
   * - | Red
       | Green
       | Blue black output
     - Float
     - Adjust red, green and blue output black point. Allowed values are 0 to 1.0, default is 0.
   * - | Red
       | Green
       | Blue white output
     - Float
     - Adjust red, green and blue output white point. Allowed values are 0 to 1.0, default is 1.
