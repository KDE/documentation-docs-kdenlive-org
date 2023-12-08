.. meta::

   :description: Kdenlive Video Effects - Draw Grid
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, generate, draw grid

.. metadata-placeholders

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Draw Grid
=========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-draw_grid.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-draw_grid

.. sidebar:: |kdenlive-show-video| Draw Grid

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      avfilter
   :**Source filter**:
      drawgrid
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter draws a colored grid on the input video.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - X / Y
     - Integer
     - Defines the starting point of the grid in pixels from the top left-hand corner of the monitor (coordinates are based on the project dimension settings)
   * - Width
     - Integer
     - Defines the distance between vertical grid lines in pixels
   * - Height
     - Integer
     - Defines the distance between horizontal grid lines in pixels
   * - Thickness
     - Integer
     - Defines the thickness of the line in pixels. If set high enough the grid is filled.
   * - Color
     - Picker
     - Defines the color for the grid


.. hint:: 
   This effect can be used in combination with the :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/chroma_key` or :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/chroma_key_advanced` effects to create interesting transitions by animating the number of grid lines and their thickness.
