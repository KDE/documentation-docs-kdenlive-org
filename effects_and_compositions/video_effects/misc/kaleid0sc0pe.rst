.. meta::

   :description: Kdenlive Video Effects - Kaleid0sc0pe
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, misc, miscellaneous, high quality, denoiser

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Kaleid0sc0pe
============

.. figure:: /images/effects_and_compositions/kdenlive2308_effects-kaleid0sc0pe.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2308_effects-kaleid0sc0pe

.. sidebar:: |kdenlive-show-video| Kaleid0sc0pe

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      kaleid0sc0pe
   :**Available**:
      |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

Applies a kaleidoscope effect.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - origin_x 
     - Float
     - X-coordinate of the origin of the kaleidoscope. Default **0.5** (center).
   * - origin_y
     - Float
     - Y-coordinate of the origin of the kaleidoscope. Default **0.5** (center).
   * - segmentation 
     - Float
     - Kaleidoscope segmentation / 128. Segmentations of 1, 2 or multiples of 4 work best. Default **16/128** (0.125)
   * - specify_source 
     - Switch
     - If **on** then source angle is read from :guilabel:`source_segment`, otherwise auto-calculated
   * - source_segment
     - Float
     - Centre of source segment if :guilabel:`specify_source` is **on**. 0 is in +x and rotates counter clockwise
   * - segmentation_direction
     - Float
     - Segmentation direction, < 1/3 is none, < 2/3 is counter clockwise, otherwise clockwise
   * - reflect_edges
     - Switch
     - If **on** then reflections that end up outside the source reflect back into it, otherwise the specified background 
   * - edge_threshold
     - Float
     - Edge threshold / 4, reflections outside the image but within this distance clamp to the edge. Default is **0**
   * - preferred_corner
     - Float
     - Preferred corner, **0** is top right, **0.25** top left, **0.5** bottom left, **0.75** bottom right
   * - corner_search
     - Switch
     - If **on** search clockwise for furthest corner, otherwise counter clockwise
   * - bg_alpha
     - Float
     - Alpha to use if reflection lies outside of source image and not reflecting back in. Default is **1**.
   * - multithreaded 
     - Switch
     - Set to **on** to enable multithreaded calculation. Default is **on**.
   * - n_threads
     - Float
     - The number of threads to use, if 0 then auto-calculate otherwise value * 32. Default is **0**
   * - bg_color
     - Picker
     - Color to use if reflection lies outside of source image and not reflecting back in. Default 1,0,1 (pink)
