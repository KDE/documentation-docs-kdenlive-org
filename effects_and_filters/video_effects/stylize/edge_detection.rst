.. meta::

   :description: Kdenlive Video Effects - Edge Detection
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, edge detection

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |canny_edge_detector| raw:: html

   <a href="https://en.wikipedia.org/wiki/Canny_edge_detector" target="_blank">Canny edge detector</a>


Edge Detection
==============

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-edge_detection.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-edge_detection

.. sidebar:: |kdenlive-show-video| Edge Detection

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      edgedetect
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter detects and draws edges using the Canny edge detection algorithm\ [1]_.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Low / High threshold
     - Float
     - Set low and high threshold values used by the algorithm. The :guilabel:`High threshold` selects the "strong" edge pixels, which are then connected through 8-connectivity with the "weak" edge pixels selected by the :guilabel:`Low threshold`. Range is from 0.000 to 1.000 with :guilabel:`Low threshold` being lower or equal to :guilabel:`High threshold`.
   * - Modes
     - Selection
     - Define the drawing mode
   * - Planes
     - Selection
     - Select the :term:`planes<plane>` for filtering

The following selection items are available:

:guilabel:`Modes`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Wires
     - Draw white/gray wires on black background (default)
   * - Colormix
     - Mix the colors to create a paint/cartoon effect
   * - Canny
     - Applies Canny edge detector on all selected :term:`planes<plane>`

:guilabel:`Planes`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - None
     - 
   * - Y/U/V
     - Also combinations of the planes are possible. Default is **YUV**.
   * - Alpha
     - 


----

.. [1] For more details refer to the |canny_edge_detector| article in Wikipedia.
