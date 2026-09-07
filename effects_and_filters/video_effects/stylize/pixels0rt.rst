.. meta::

   :description: Kdenlive Video Effects - pixels0rt
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, pixels0rt, pixel, sort

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0

.. .. versionadded:: 26.08


Pixels0rt
=========

.. figure:: /images/effects_and_compositions/effects-pixels0rt-2608.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| pixels0rt

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      pixels0rt
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter produces a pixel sorting effect.


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
     - Float
     - Relative size of the line that will be sorted
   * - Direction
     - Selection
     - Sorting direction. See available options below
   * - Reversed
     - Switch
     - Reverses the pixel sort order.
   * - Transparency threshold
     - Float
     - Determines what transparancy level should be bypassed by the filter. 0 processes all pixels, 1 ignores all transparent pixels.

The following selection items are available:

:guilabel:`Direction`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Vertical top to bottom
     - Default
   * - Vertical bottom to top
     - 
   * - Horizontal left to right
     - 
   * - Horizontal right to left
     -           