.. meta::

   :description: Kdenlive Video Effects - VR360 Equirectangular to Rectilinear 
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, VR360 and 3D, VR360 equirectangular to rectilinear

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


VR360 Equirectangular to Rectilinear
====================================

.. figure:: /images/effects_and_compositions/effects-vr360_equi2rect-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-vr360_equi2rect-2504.webp

.. sidebar:: |kdenlive-show-video| VR360 Equirectangular to Rectilinear

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      bigsh0t_eq_to_rect\ [1]_
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter converts an equirectangular frame (panoramic) to a rectilinear frame (what you are used to seeing). Can be used to preview what will be shown in a 360 video viewer.


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
   * - Yaw
     - Degree
     - Defines the direction of view left or right
   * - Pitch
     - Degree
     - Defines the direction of view up or down
   * - Roll
     - Degree
     - Defines the direction of view like tilting your head left or right
   * - FOV
     - Degree
     - The horizontal field of view, in degrees, of the resulting frame. Any value over 179 results in a fisheye projection.
   * - Fisheye
     - Percent
     - The amount of fisheye to mix in. 100% means that you get a 100% fisheye lens.


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


----

.. |bigsh0t| raw:: html

   <a href="https://bitbucket.org/leo_sutic/bigsh0t/src/main/" target="_blank">bigsh0t</a>


.. [1] Parts of this documentation have been taken from the website of the filter's developer |bigsh0t|.
