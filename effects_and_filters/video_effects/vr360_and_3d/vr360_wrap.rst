.. meta::

   :description: Kdenlive Video Effects - VR360 Wrap 
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, VR360 and 3D, VR360 wrap

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


VR360 Wrap
==========

.. figure:: /images/effects_and_compositions/effects-vr360_wrap-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| VR360 Wrap

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      bigsh0t_eq_wrap\ [1]_
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter stretches a section of the equirectangular panorama to cover the entire VR sphere.


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
     - Determines the sampling method.
   * - Top
     - Degrees
     - Degrees from the center of the image to keep unchanged
   * - Bottom
     - Degrees
     - Degrees from the center of the image to keep unchanged
   * - Left
     - Degrees
     - Degrees from the center of the image to keep unchanged
   * - Right
     - Degrees
     - Degrees from the center of the image to keep unchanged
   * - Blur start
     - Degrees
     - Horizontal fraction of the unchanged area to blur over in the equator band
   * - Blur end
     - Degrees
     - Horizontal fraction of the unchanged area to blur over at the poles


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