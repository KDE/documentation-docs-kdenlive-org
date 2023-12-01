.. meta::

   :description: Kdenlive Video Effects - Pixs0r effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, misc, miscellaneous, pixs0r

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Pixs0r
======

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-pixs0r.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-pixs0r

.. sidebar:: |kdenlive-show-video| Pixs0r

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      frei0r
   :**Source filter**:
      pixs0r
   :**Available**:
      |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter creates a glitch effect by shifting rows left and right.

.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - shift_intensity
     - Float
     - Agressiveness of row/column-shifting
   * - block_height
     - Float
     - Height of each block whose shift is invariant. If set to **0**, block height will be randomized.
   * - block_height_min
     - Float
     - If in random mode, sets the minimum height of block
   * - block_height_max
     - Float
     - If in random mode, sets the maximum height of block
