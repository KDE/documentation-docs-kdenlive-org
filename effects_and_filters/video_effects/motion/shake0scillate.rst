.. meta::

   :description: Kdenlive Video Effects - shakeoscillate
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, motion, shakeoscillate, shake, oscillate

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0

.. .. versionadded:: 26.08


Shake0scillate
==============

.. figure:: /images/effects_and_compositions/effects-shake0scillate-2608.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| shake0scillate

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      shake0scillate
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter animates the input image for a smooth and controlled oscillation. It is similar to :doc:`/effects_and_filters/video_effects/motion/camerashake` but by far not as shaky and erratic.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 30 10 60
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - X Movement
     - Float
     - Maximum horizontal displacement. Goes into both directions with 0.5 being centered (no movement).
   * - X Speed
     - Float
     - Speed of the horizontal movement.
   * - Y Movement
     - Float
     - Maximum vertical displacement. Goes into both directions with 0.5 being centered (no movement).
   * - Y Speed
     - Float
     - Speed of the horizontal movement.
   * - Rotation
     - Float
     - Maximum rotation. Goes into both directions with 0.5 being centered (no rotation)
   * - Rotation Speed
     - Float
     - Speed of the rotation
   * - Scale
     - Float
     - Zoom factor to hide black borders. Only useful if mirrored is off and you want to prevent black borders or other clips to show when moving or rotating out of bounds.
   * - Phase
     - Float
     - Entry points into the sine and cosine functions.
   * - Mirrored
     - Switch
     - If selected, mirrors the image if movement or rotation moves it out of bounds. Only useful if scaling is not used and you want to prevent black borders or other clips to show.


.. note:: 
   Using motion blur slows down the shake effect significantly.
