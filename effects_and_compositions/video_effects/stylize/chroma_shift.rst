.. meta::

   :description: Kdenlive Video Effects - Chroma Shift
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, chroma shift

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Chroma Shift
============

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-chroma_shift.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-chroma_shift

.. sidebar:: |kdenlive-show-video| Chroma Shift

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      chromashift
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter shifts chroma pixels horizontally and/or vertically similar to the Tik Tok logo effect. Compare :doc:`/effects_and_compositions/video_effects/stylize/rgba_shift` and :doc:`/effects_and_compositions/video_effects/stylize/rgbsplit0r` effects.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Chroma-blue H shift
     - Integer
     - Set amount to shift chroma-blue horizontally
   * - Chroma-blue V shift
     - Integer
     - Set amount to shift chroma-blue vertically
   * - Chroma-red H shift
     - Integer
     - Set amount to shift chroma-red horizontally
   * - Chroma-red V shift
     - Integer
     - Set amount to shift chroma-red vertically
   * - Edge mode
     - Selection
     - Set edge mode determining what happens to pixels when shifted outside the frame

The following selection items are available:

:guilabel:`Edge mode`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Smear
     - Shifted pixel leave a trail (default)
   * - Wrap
     - Shifted pixels wrap around the image and appear on the opposite side
