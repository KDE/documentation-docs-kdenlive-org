.. meta::

   :description: Kdenlive Video Effects - Rectangular Alpha Mask
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, alpha, mask, keying, rectangular

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Roger (https://userbase.kde.org/User:Roger)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |mask0mate| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-mask0mate/" target="_blank">mask0mate</a>


Rectangular Alpha Mask
======================

.. figure:: /images/effects_and_compositions/effects-rectangular_alpha_mask-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-rectangular_alpha_mask-2504.webp

.. sidebar:: |kdenlive-show-video| Rectangular Alpha Mask

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      |mask0mate|
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

Creates a rectangular alpha-channel mask. Its size and position is defined by the values for its edges (left, right, top, bottom).


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Invert
     - Switch
     - Invert the selection
   * - Left
     - Integer
     - Defines the left edge of the rectangular in number of pixels from the left of the frame
   * - Right
     - Integer
     - Defines the right edge of the rectangular in number of pixels from the right of the frame
   * - Top
     - Integer
     - Defines the top edge of the rectangular in number of pixels from the top of the frame
   * - Bottom
     - Integer
     - Defines the bottom edge of the rectangular in number of pixels from the bottom of the frame
   * - Blur
     - Integer
     - Defines the number of pixels around the edge of the rectangular where :abbr:`feathering (Smoothing or blurring the edges of a feature)` takes place. Default is 0 (hard edge).

.. rubric:: Screenshot

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-rect_alpha_mask_1.webp
   :width: 90%
   :alt: kdenlive2304_effects-rect_alpha_mask

   Rectangular Alpha Mask effect panel and example


.. rubric:: Notes

This effect was previously called *Mask0Mate* and is the frei0r |mask0mate| MLT filter.
