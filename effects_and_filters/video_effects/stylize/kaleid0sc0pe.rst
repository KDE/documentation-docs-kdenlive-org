.. meta::

   :description: Kdenlive Video Effects - Kaleidoscope
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, kaleidoscope, kaleid0sc0pe

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0

.. .. versionchanged:: 24.12
  
Kaleidoscope
============

.. figure:: /images/effects_and_compositions/effects-kaleid0sc0pe-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Kaleidoscope

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
   :**Color depth**:
      8bit
   :**Tutorial**:
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
   * - Specify Source Segment 
     - Switch
     - If **on**, the source angle is read from :guilabel:`Source segment`, otherwise auto-calculated
   * - Segmentation Direction
     - Selection
     - Options are **None**, **Counter clockwise**, and **Clockwise** (default)
   * - Reflect Edges
     - Switch
     - If **on**, then reflections that end up outside the source reflect back into it, otherwise the specified background color is used
   * - Preferred Corner
     - Selection
     - Options are **Top right** (default), **Top left**, **Bottom left**, and **bottom right**
   * - Corner Search
     - Switch
     - If **on**, search clockwise for furthest corner, otherwise counter clockwise
   * - No Alpha Background
     - Switch
     - If reflection lies outside of source image and not reflecting back in, the selected color is used. Default is **On**.
   * - Origin X 
     - Float
     - X-coordinate of the origin of the kaleidoscope. Default **50** (center).
   * - Origin Y
     - Float
     - Y-coordinate of the origin of the kaleidoscope. Default **50** (center).
   * - Segmentation 
     - Float
     - Kaleidoscope segmentation / 128. Segmentations of 1, 2 or multiples of 4 work best. Default **16** (16/128 = 0.125)
   * - Source Segment
     - Float
     - Centre of source segment if :guilabel:`Specify source segment` is **on**. 0 is in +x and rotates counter clockwise
   * - Edge Threshold
     - Float
     - Edge threshold / 4, reflections outside the image but within this distance clamp to the edge. Default is **0**
   * - Background Color
     - Picker
     - Color to use if reflection lies outside of source image and not reflecting back in (:guilabel:`Reflect edges` is **off**). Default is pink.
