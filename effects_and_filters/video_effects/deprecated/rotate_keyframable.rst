.. meta::

   :description: Kdenlive Video Effects - Rotate (keyframable)
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, rotate keyframable

.. metadata-placeholder

   :authors: - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Jack (https://userbase.kde.org/User:Jack)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Rotate (keyframable)
====================


.. attention::
   Replaced by :doc:`/effects_and_filters/video_effects/transform_distort_perspective/rotate_3_way`


.. figure:: /images/effects_and_compositions/kdenlive2304_effects-rotate_keyframable.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-rotate_keyframable

.. sidebar:: |kdenlive-show-video| Rotate (keyframable)

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

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter rotates the clip in any of the three directions: X, Y, and Z.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Disable repeat
     - Switch
     - When animating properties with keyframes, whether to repeat the animation after it reaches the last key frame. Default is **on**.
   * - Disable mirror
     - Switch
     - When animating properties with keyframes and :guilabel:`Disable repeat` is **off**, whether the animation alternates between reverses and forwards for each repetition. Default is **on**.
   * - Rotate X / Y / Z
     - Integer
     - Set the amount of rotation in ``degrees * 10``. For example: 900 = 90 degrees rotation.
   * - Offset X / Y
     - Integer
     - Horizontal (X) and vertical (Y) offset
   * - Background Color
     - Picker
     - Define the background color to be used when rotating reveals the background. Default is Alpha.


.. attention:: 
   The axes for rotation are different than for moving a clip. The latter uses the monitor plane: X = width or horizontal axis, Y = height or vertical axis. For rotation the plane is tilted by 90 degrees "into the monitor" and rotated 90 degrees clockwise around the vertical axis. This results in the X axis coming out of/going into the monitor, the Y axis being along the width of the monitor and the Z axis being along the height of the monitor. See image below.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-rotate_and_shear_axes.webp
   :width: 400px
   :figwidth: 400px
   :align: center
   :alt: kdenlive2304_effects-rotate_and_shear_axes

   Rotation axes visualization


.. https://youtu.be/Wfx1Cp5g6Mo
