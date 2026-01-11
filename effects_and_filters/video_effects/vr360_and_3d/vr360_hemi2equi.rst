.. meta::

   :description: Kdenlive Video Effects - VR360 Hemispherical to Equirectangular
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, VR360 and 3D, VR360 hemispherical to equirectangular

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |ffmpeg| raw:: html

   <a href="https://stackoverflow.com/questions/11552565/vertically-or-horizontally-stack-mosaic-several-videos-using-ffmpeg" target="_blank">ffmpeg</a>

.. |hugin| raw:: html

   <a href="https://hugin.sourceforge.io/" target="_blank">Hugin</a>


VR360 Hemispherical to Equirectangular
======================================

.. figure:: /images/effects_and_compositions/effects-vr360_hemi2equi-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
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
     - The fisheye projection type. Currently only equidistant fisheyes, like the Ricoh Theta and Garmin Virb360 are supported.
   * - Use sensor response parameters
     - Switch
     - Switch on to use sensor response parameters (see EMoR h(x) parameters below)
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
   * - Lens distortion A / B / C
     - Float
     - Lens distortion correction parameters. The first three parameters are the same as in |hugin|.
   * - Lens distortion radius
     - Float
     - Lens distortion correction parameters. If you use |hugin| parameters, the Radius should be set to the value of (0.5 * min(image width, image height) / image width). For a 2:1 aspect dual hemispherical image, that would be 0.25.
   * - Lens vignetting A / B / C / D
     - Float
     - Lens vignetting correction parameters. The first four parameters are the same as in |hugin|, corresponding to the V\ :sub:`a` , V\ :sub:`b` , V\ :sub:`c` , and V\ :sub:`d` image parameters.
   * - Lens vignetting radius
     - Float
     - If you use Hugin parameters, the radius should be set to the value of (0.5 * image diagonal / image width). For a 2:1 aspect dual hemispherical image, that would be 0.5590. Use the :kbd:`A` parameter to scale the effect and avoid overexposing highlights.
   * - EMoR h(1 / 2 / 3 / 4 / 5)
     - Float
     - Sensor response parameters. The EMoR h(x) parameters are the same as |hugin|'s R\ :sub:`a` - R\ :sub:`e` in the lens parameters. If you use |hugin|-derived values for vignetting correction, you should also use these parameters, as |hugin|'s vignetting correction assumes that the sensor response has been corrected.


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
