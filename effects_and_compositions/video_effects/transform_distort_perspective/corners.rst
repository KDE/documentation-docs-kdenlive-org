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

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-corners.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-corners

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

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter allows accurate perspective distortion of the input source's geometry. Instead of using the sliders or entering the values you can use the corner handles to change the geometry. Edit Mode must be switched on for this.


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
   * - Corner 1-4 X / Y
     - Integer
     - Set the coordinates for the corners. Corner 1 is the top left corner, corner 4 the bottom left. Ranges are 0 to 6000.
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


.. rubric:: Notes
   
Corners can be moved towards the inside and the outside of the frame. Hence the default values of 1999 and 4000. Imagine the frame of the clip being a frame sitting on a bigger canvas (see yellow hatch pattern below). The top left corner of the canvas has the coordinates X=0 and Y=0, the bottom right X=6000 and Y=6000. When moving the corners you are stretching the image of the clip across the canvas distorting the clip accordingly.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-corners_schematic.webp
   :width: 500px
   :figwidth: 500px
   :alt: kdenlive2304_effects-corners_schematic

   Corners effect schematic
   
:**1 - 4**:
 The corners numbering scheme.

:Grey background:
 Project Monitor background

:Yellow hatch pattern:
 The virtual canvas

:Red rectangle:
 The maximum extend of the virtual canvas, and currently the extend to which the clip has been stretched (compare the small rectangle in the middle which is the clip in the Project Monitor @ 1920x1080 resolution)


.. note:: 
   The Project Monitor has been zoomed out very much to show this schematic.
