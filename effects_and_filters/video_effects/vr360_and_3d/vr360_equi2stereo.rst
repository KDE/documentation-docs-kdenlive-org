.. meta::

   :description: Kdenlive Video Effects - VR360 Equirectangular to Stereo
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, VR360 and 3D, VR360 equirectangular to stereo

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


VR360 Equirectangular to Stereo
===============================

.. figure:: /images/effects_and_compositions/effects-vr360_equi2stereo-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-vr360_equi2stereo-2504.webp

.. sidebar:: |kdenlive-show-video| VR360 Equirectangular to Stereo

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      bigsh0t_eq_stereo\ [1]_
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter projects a stereographic image from an equirectangular source. Use this to create the "Little Planet" effect from VR360 footage.



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
     - Integer
     - Field of View (the wider the angle the wider/zoomed out the view)
   * - Amount
     - Percent
     - Determines the amount of stereographic projection to mix in. Range is from 0% (standard rectilinear projection ) to 100% (full stereographic projection)


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
