.. meta::

   :description: Kdenlive Video Effects - Corners
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, corners

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Corners
=======

.. figure:: /images/effects_and_compositions/effects-corners-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-corners-2504.webp

.. sidebar:: |kdenlive-show-video| Corners

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      corners
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

This effect/filter allows accurate perspective distortion of the input source's geometry. Instead of using the sliders or entering the values you can use the corner handles to change the geometry. Edit Mode must be switched on for this. See the :ref:`Notes <corners_notes>` below for an explanation how this effect works and the parameters need to be interpreted.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 30 10 60
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Enable Stretch
     - Switch
     - Needs to be **on** for :guilabel:`Stretch X / Y` to have an effect,
   * - Interpolator
     - Selection
     - Select the method for interpolation
   * - Transparent Background
     - Switch
     - Select how to treat the background when exposed. :guilabel:`Feather Alpha` only works when this is **on** (default).
   * - Alpha Operation
     - Selection
     - 
   * - Top-left X / Y
     - Integer
     - Set the coordinates for the top-left corner. Range is 0 to 3000, default is 1000
   * - Top-right X / Y
     - Integer
     - Set the coordinates for the top-right corner. Range is 0 to 3000, default is 2000 and 1000, respectively
   * - Bottom-right X / Y
     - Integer
     - Set the coordinates for the bottom-right corner. Range is 0 to 3000, default is 2000
   * - Bottom-left X / Y
     - Integer
     - Set the coordinates for the bottom-left corner. Range is 0 to 3000, default is 1000 and 2000, respectively
   * - Stretch X / Y
     - Integer
     - Stretches the source clip along the X and/or Y axis by "moving" the virtual center of the frame left/right or up/down.
   * - Feather Alpha
     - Integer
     - Set the feather width of the border between the frame and the exposed background. Only works if :guilabel:`Transparent Background` is checked.

The following selection items are available:

:guilabel:`Interpolator`

.. list-table::
   :width: 100%
   :widths: 30 70
   :class: table-simple

   * - Nearest neighbor
     - 
   * - Bilinear
     - default
   * - Bicubic smooth/sharp
     - 
   * - Spline 4x4/6x6
     - 
   * - Lanczos
     - 

:guilabel:`Alpha Operation`

.. list-table::
   :width: 100%
   :widths: 30 70
   :class: table-simple

   * - Write on clear
     - default
   * - Maximum
     - 
   * - Minimum
     - 
   * - Add
     - 
   * - Subtract
     - 


.. _corners_notes:

.. rubric:: Notes
   
Corners can be moved towards the inside and the outside of the frame. Hence the default values of 999 and 2000. Imagine the frame of the clip being a frame sitting on a bigger canvas (see yellow hatch pattern below). The top left corner of the canvas has the coordinates X=0 and Y=0, the bottom right X=3000 and Y=3000. When moving the corners you are stretching the image of the clip across the canvas distorting the clip accordingly.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-corners_schematic.webp
   :width: 500px
   :figwidth: 500px
   :alt: kdenlive2304_effects-corners_schematic

   Corners effect schematic
   
:**1 - 4**:
 The corners numbering scheme: Top-left, top-right, bottom-right, bottom-left.

:Grey background:
 Project Monitor background

:Yellow hatch pattern:
 The virtual canvas

:Red rectangle:
 The maximum extend of the virtual canvas, and currently the extend to which the clip has been stretched (compare the small rectangle in the middle which is the clip in the Project Monitor @ 1920x1080 resolution)


.. note:: 
   The Project Monitor has been zoomed out very much to show this schematic.
