.. meta::

   :description: Kdenlive Video Effects - VR360 Transform
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, VR360 and 3D, VR360 transform

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


VR360 Transform
===============

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-vr360_transform.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-vr360_transform

.. sidebar:: |kdenlive-show-video| VR360 Transform

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      bigsh0t_transform_360
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter rotates a panoramic image.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 10 65
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Interpolation
     - Selection
     - Choose the interpolation algorithm
   * - yaw
     - Integer
     - Defines the direction of view left or right
   * - pitch
     - Integer
     - Defines the direction of view up or down
   * - roll
     - Integer
     - Defines the direction of view like tilting your head left or right


The following selection items are available:

:guilabel:`Interpolation`

.. list-table::
   :width: 100%
   :widths: 25 75
   :class: table-simple

   * - Nearest-Neighbor
     - default
   * - Bilinear
     - 
