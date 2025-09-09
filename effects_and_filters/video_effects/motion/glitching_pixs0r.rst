.. meta::

   :description: Kdenlive Video Effects - Glitching (rows only)
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, misc, miscellaneous, glitch, shifting, pixs0r

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Glitching (rows only)
=====================

.. figure:: /images/effects_and_compositions/effects-pixs0r-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-pixs0r-2504.webp

.. sidebar:: |kdenlive-show-video| Glitching (rows only)

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
   :**Color depth**:
      8bit
   :**Tutorial**:
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
   * - Shift Intensity
     - Float
     - Aggressiveness of row/column-shifting
   * - Block Height
     - Float
     - Height of each block whose shift is invariant. If set to **0**, block height will be randomized.
   * - Minimum Block Height
     - Float
     - If in random mode, sets the minimum height of block
   * - Maximum Block Height
     - Float
     - If in random mode, sets the maximum height of block
