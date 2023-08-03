.. meta::

   :description: Do your first steps with Kdenlive video editor, using VR360 hemispherical to equirectangular effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, VR360 and 3D, VR360 hemispherical to equirectangular

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |ffmpeg| raw:: html

   <a href="https://stackoverflow.com/questions/11552565/vertically-or-horizontally-stack-mosaic-several-videos-using-ffmpeg" target="_blank">ffmpeg</a>

.. |bigsh0t| raw:: html

   <a href="https://bitbucket.org/leo_sutic/bigsh0t/src/main/" target="_blank">bigsh0t</a>


.. _effects-vr360_hemi2equi:

VR360 Hemispherical to Equirectangular
======================================

This effect/filter converts a video frame with two hemispherical images to a single equirectangular frame.

The plugin assumes that both hemispheres are in the frame. If you have a camera like the Garmin Virb360 that produces two videos, one from each camera, you should start by converting them to a single movie by placing them side by side using, for example, |ffmpeg| (you can also add parameters to produce lossless, intra-only output here for easier editing):

.. code:: bash

   ffmpeg \
    -i left.mp4 \
    -i right.mp4 \
    -filter_complex hstack \
    output.mp4

The effect has keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-vr360_hemi2equi.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-vr360_hemi2equi

   VR360 Hemispherical to Equirectangular effect

* **Projection** - The fisheye projection type. Only option is **Equidistant Fisheye**.

* **Interpolation** - Determines the sampling method. Options are **Nearest-Neighbor** (default) and **Bilinear**.

* **Alignment Yaw / Pitch / Roll** - Adjust the rotation along the Z- (yaw), X- (pitch) and Y-axis (roll) to compensate for any alignment differences

* **Lens FOV** - Field of View of a single hemisphere in degrees

* **Lens Radius** - Radius of the image circle as a fraction of the frame width (for example 0.25 = 25% of 1920)

* **Front X / Y** - Defines the center of the image of the front-facing camera. X is expressed as a fraction of the image width, Y as a fraction of the image height.

* **Front UP** - Defines the "up" direction in the image in degrees counting clockwise from a directions towards the top edge

* **Back X / Y** - Defines the center of the image of the back-facing camera. X is expressed as a fraction of the image width, Y as a fraction of the image height.

* **Back UP** - Defines the "up" direction in the image in degrees counting clockwise from a directions towards the top edge

* **Nadir Radius / Start** - Adjust the nadir of the camera if you have parts of the camera or equipment in the image

.. rst-class:: clear-both


**Notes**

Parts of this documentation have been taken from the website of the filter's developer |bigsh0t|.
