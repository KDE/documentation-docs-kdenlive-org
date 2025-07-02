.. meta::

   :description: Kdenlive Video Effects - 3-way Rotate
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, rotate, 3-way

.. metadata-placeholder

   :authors: - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Jack (https://userbase.kde.org/User:Jack)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


3-way Rotate
============

.. figure:: /images/effects_and_compositions/effects-rotate_3_way-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-rotate_3_way-2504.webp

.. sidebar:: |kdenlive-show-video| 3-way Rotate

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      affine
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

This effect/filter rotates the clip in any of the three directions: X, Y, and Z. It allows to specify an offset for the image to be moved before rotation, effectively moving the center of rotation.
The :guilabel:`Scale` parameter is applied irrespective of the rotation - it scales along the X and Y axis of the monitor.

.. warning:: 
   This effect may move pixels outside of the project frame. This will crop the clip, meaning that a :doc:`/effects_and_filters/video_effects/transform_distort_perspective/transform` effect after the 3-way Rotate effect will be applied to the cropped clip, and moving the clip will not show the pixels "rotated out" of the project frame.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Disable Repeat
     - Switch
     - When animating properties with keyframes, whether to repeat the animation after it reaches the last key frame. Default is **on**.
   * - Disable Mirror
     - Switch
     - When animating properties with keyframes and :guilabel:`Disable repeat` is **off**, whether the animation alternates between reverses and forwards for each repetition. Default is **on**.
   * - Invert Scale
     - Switch
     - Whether to invert the :guilabel:`Scale X` and :guilabel:`Scale Y` values. This is helpful to make animation interpolation sane because otherwise the scale values do not animate linearly. Default is **on**.
   * - Rotate X / Y / Z
     - Integer
     - Set the amount of rotation along the respective axes in degrees of rotation.
   * - Offset X / Y
     - Integer
     - Horizontal (X) and vertical (Y) offset
   * - Scale X / Y
     - Integer
     - Scale factor applied to the X and Y axis
   * - Background Color
     - Picker
     - Define the background color to be used when rotating reveals the background. Default is **Alpha**.


.. attention:: 
   The axes for rotation are different than for moving a clip. The latter uses the monitor plane: X = width or horizontal axis, Y = height or vertical axis. For rotation the plane is tilted by 90 degrees "into the monitor" and rotated 90 degrees clockwise around the vertical axis. This results in the X axis coming out of/going into the monitor, the Y axis being along the width of the monitor and the Z axis being along the height of the monitor. See image below.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-rotate_and_shear_axes.webp
   :width: 400px
   :figwidth: 400px
   :align: center
   :alt: kdenlive2304_effects-rotate_and_shear_axes

   Rotation axes visualization


.. https://youtu.be/Wfx1Cp5g6Mo
