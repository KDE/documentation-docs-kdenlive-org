.. meta::

   :description: Kdenlive Video Effects - VR360 Hemispherical to Equirectangular
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, VR360 and 3D, VR360 hemispherical to equirectangular

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |ffmpeg| raw:: html

   <a href="https://stackoverflow.com/questions/11552565/vertically-or-horizontally-stack-mosaic-several-videos-using-ffmpeg" target="_blank">ffmpeg</a>


VR360 Hemispherical to Equirectangular
======================================

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-vr360_hemi2equi.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-vr360_hemi2equi

.. sidebar:: |kdenlive-show-video| VR360 Hemispherical to Equirectangular

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      bigsh0t_hemi_to_eq\ [1]_
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter converts a video frame with two hemispherical images to a single equirectangular frame.

The plugin assumes that both hemispheres are in the frame. If you have a camera like the Garmin Virb360 that produces two videos, one from each camera, you should start by converting them to a single movie by placing them side by side using, for example, |ffmpeg| (you can also add parameters to produce lossless, intra-only output here for easier editing):

.. code:: bash

   ffmpeg \
    -i left.mp4 \
    -i right.mp4 \
    -filter_complex hstack \
    output.mp4


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 10 65
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Projection
     - Selection
     - The fisheye projection type
   * - Interpolation
     - Selection
     - Determines the sampling method
   * - Alignment Yaw / Pitch / Roll
     - Integer
     - Adjust the rotation along the Z- (yaw), X- (pitch) and Y-axis (roll) to compensate for any alignment differences
   * - Lens FOV
     - Integer
     - Field of View of a single hemisphere in degrees
   * - Lens Radius
     - Float
     - Radius of the image circle as a fraction of the frame width (for example 0.25 = 25% of 1920)
   * - Front X / Y
     - Float
     - Defines the center of the image of the front-facing camera. X is expressed as a fraction of the image width, Y as a fraction of the image height.
   * - Front UP
     - Integer
     - Defines the "up" direction in the image in degrees counting clockwise from a directions towards the top edge
   * - Back X / Y
     - Float
     - Defines the center of the image of the back-facing camera. X is expressed as a fraction of the image width, Y as a fraction of the image height.
   * - Back UP
     - Integer
     - Defines the "up" direction in the image in degrees counting clockwise from a directions towards the top edge
   * - Nadir Radius / Start
     - Float
     - Adjust the :abbr:`nadir (direction pointing directly below a particular location)` of the camera if you have parts of the camera or equipment in the image


The following selection items are available:

:guilabel:`Projection`

.. list-table::
   :width: 100%
   :widths: 25 75
   :class: table-simple

   * - Equidistant Fisheye
     - default


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
