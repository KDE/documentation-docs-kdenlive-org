.. meta::

   :description: Kdenlive Video Effects - RGBA Shift
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, rgba shift, 10bit

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


RGBA Shift
==========

.. figure:: /images/effects_and_compositions/effects-rgba_shift-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-rgba_shift-2504.webp

.. sidebar:: |kdenlive-show-video| RGBA Shift

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      rgbashift
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No
   :**Color depth**:
      10bit |color-management|
   :**Tutorial**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter shifts R/G/B/A pixels horizontally and/or vertically creating an appearance similar to the Tik Tok logo. Compare the :doc:`/effects_and_filters/video_effects/stylize/rgbsplit0r` and :doc:`/effects_and_filters/video_effects/stylize/chroma_shift` effects which essentially do the same but in the case of :doc:`/effects_and_filters/video_effects/stylize/rgbsplit0r` lack the ability to determine the edge operation.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Red Horizontal Shift
     - Integer
     - Set amount to shift red horizontally. Positive values shift right, negative values shift left.
   * - Red Vertical Shift
     - Integer
     - Set amount to shift red vertically. Positive values shift up, negative values shift down.
   * - Green Horizontal Shift
     - Integer
     - Set amount to shift green horizontally. Positive values shift right, negative values shift left.
   * - Green Vertical Shift
     - Integer
     - Set amount to shift green vertically. Positive values shift up, negative values shift down.
   * - Blue Horizontal Shift
     - Integer
     - Set amount to shift blue horizontally. Positive values shift right, negative values shift left.
   * - Blue Vertical Shift
     - Integer
     - Set amount to shift blue vertically. Positive values shift up, negative values shift down.
   * - Alpha Horizontal Shift
     - Integer
     - Set amount to shift red horizontally. Positive values shift right, negative values shift left.
   * - Alpha Vertical Shift
     - Integer
     - Set amount to shift alpha vertically. Positive values shift up, negative values shift down.
   * - Edge Operation
     - Selection
     - Set edge mode


The following selection items are available:

:guilabel:`Edge operation`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Smear
     - Shifted pixel leave a trail (default)
   * - Wrap
     - Shifted pixels wrap around the image and appear on the opposite side
