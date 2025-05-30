.. meta::

   :description: Kdenlive Video Effects - Draw Box
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, generate, draw box

.. metadata-placeholders

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Draw Box
========

.. figure:: /images/effects_and_compositions/effects-draw_box-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-draw_box-2504.webp

.. sidebar:: |kdenlive-show-video| Draw Box

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      avfilter
   :**Source filter**:
      drawbox
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter draws a colored box on the input video.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Color
     - Picker
     - Defines the color for the box
   * - Replace color and alpha
     - Switch
     - If the input has alpha, checking this	will overwrite the video's color and alpha pixels with the pixels of the painted box. By default (off), the box will be composited onto the input, leaving the video's alpha intact.
   * - Top-left X / Y
     - Integer
     - Defines the coordinates for the top left-hand corner of the box (coordinates are based on the project dimension settings)
   * - Width (px)
     - Integer
     - Defines the width in pixels
   * - Height (px)
     - Integer
     - Defines the height in pixels
   * - Thickness (px)
     - Integer
     - Defines the thickness of the line in pixels. If set high enough, the box is essentially filled.
