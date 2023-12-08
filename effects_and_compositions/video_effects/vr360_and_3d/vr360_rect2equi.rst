.. meta::

   :description: Kdenlive Video Effects - VR360 Rectilinear to Equirectangular
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, VR360 and 3D, VR360 rectilinear to equirectangular

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


VR360 Rectilinear to Equirectangular
====================================

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-vr360_rect2equi.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-vr360_rect2equi

.. sidebar:: |kdenlive-show-video| VR360 Rectilinear to Equirectangular

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      bigsh0t_rect_to_eq\ [1]_
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter converts a rectilinear (a normal-looking) image to an equirectangular image. Use this together with Transform 360 to place "normal" footage in a 360 movie. It is the opposite of the :doc:`/effects_and_compositions/video_effects/vr360_and_3d/vr360_equi2rect` effect.


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
   * - Vertical Star
     - Integer
     - Determines the vertical FOV\ [2]_
   * - Horizontal Start
     - Integer
     - Determines the horizontal FOV\ [2]_


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

.. [2] FOV = Field of view (in degrees)
