.. meta::

   :description: Kdenlive Video Effects - Glitching (rows and color) 
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, motion, glitch, block, color, shifting, glitch0r

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Glitching (rows and color)
==========================

.. figure:: /images/effects_and_compositions/effects-glitch0r-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Glitching (rows and color)

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      glitch0r
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

This effect/filter adds color glitches and block shifting.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 30 10 60
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Glitch Frequency
     - Integer
     - How frequently the glitch should be applied
   * - Block Height
     - Integer
     - Height range of the block that will be shifted/glitched
   * - Shift Intensity
     - Integer
     - How much blocks should be moved when glitching
   * - Color Glitching Intensity
     - Integer
     - How intensive color distortion should be


.. hint:: 
   The smaller the :guilabel:`Block height`, the more visible the effect even with lower values for :guilabel:`Glitch frequency`.
