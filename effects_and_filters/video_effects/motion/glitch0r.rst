.. meta::

   :description: Kdenlive Video Effects - Glitch0r 
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, misc, miscellaneous, glitch0r

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Glitch0r
========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-glitch0r.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-glitch0r

.. sidebar:: |kdenlive-show-video| Glitch0r

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

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter adds glitches and block shifting.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 30 10 60
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Glitch frequency
     - Integer
     - How frequently the glitch should be applied
   * - Block height
     - Integer
     - Height range of the block that will be shifted/glitched
   * - Shift intensity
     - Integer
     - How much blocks should be moved when glitching
   * - Color glitching intensity
     - Integer
     - How intensive color distortion should be


.. hint:: 
   The smaller the :guilabel:`Block height`, the more visible the effect even with lower values for :guilabel:`Glitch frequency`.
