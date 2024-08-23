.. meta::

   :description: Kdenlive Video Effects - VR360 Equirectangular Mask
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, VR360 and 3D, VR360 equirectangular mask

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


VR360 Equirectangular Mask
==========================

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-vr360_equi_mask.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-vr360_equi_mask

.. sidebar:: |kdenlive-show-video| VR360 Equirectangular Mask

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      bigsh0t_eq_mask\ [1]_
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter adds a black matte to the frame. Use this if you filmed using a 360 camera but only want to use part of the 360 image, for example if you and the film crew occupy the 90 degrees behind the camera.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 30 10 60
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Interpolation
     - Selection
     - Choose the interpolation algorithm
   * - Vertical Start / End
     - Integer
     - Define the vertical FOV (field of vision). **Start** defines the width in degrees of the un-matted area; **End** is the width in degrees where the matte is 100%.
   * - Horizontal Start / End
     - Integer
     - Define the horizontal FOV. **Start** is half the height in degrees of the un-matted area; **End** is half the height in degrees where the matte is 100%.


The following selection items are available:

:guilabel:`Interpolation`

.. list-table::
   :width: 100%
   :widths: 30 70
   :class: table-simple

   * - Nearest-Neighbor
     - default
   * - Bilinear
     - 


----

.. |bigsh0t| raw:: html

   <a href="https://bitbucket.org/leo_sutic/bigsh0t/src/main/" target="_blank">bigsh0t</a>


.. [1] Parts of this documentation have been taken from the website of the filter's developer |bigsh0t|.
