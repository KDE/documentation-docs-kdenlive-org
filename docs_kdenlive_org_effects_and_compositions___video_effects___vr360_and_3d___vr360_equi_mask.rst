.. meta::

   :description: Do your first steps with Kdenlive video editor, using VR360 equirectangular mask effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, VR360 and 3D, VR360 equirectangular mask

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |bigsh0t| raw:: html

   <a href="https://bitbucket.org/leo_sutic/bigsh0t/src/main/" target="_blank">bigsh0t</a>


.. _effects-vr360_equirectangular_mask:

VR360 Equirectangular Mask
==========================

This effect/filter adds a black matte to the frame. Use this if you filmed using a 360 camera but only want to use part of the 360 image, for example if you and the film crew occupy the 90 degrees behind the camera.

The effect has keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-vr360_equi_mask.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-vr360_equi_mask

   VR360 Equirectangular Mask effect

* **Interpolation** - Select from **Nearest-Neighbor** (default) and **Bilinear**

* **Vertical Start / End** - Define the vertical FOV (field of vision). **Start** defines the width in degrees of the un-matted area; **End** is the width in degrees where the matte is 100%.

* **Horizontal Start / End** - Define the horizontal FOV. **Start** is half the height in degrees of the un-matted area; **End** is half the height in degrees where the matte is 100%.

.. rst-class:: clear-both


**Notes**

Parts of this documentation have been taken from the website of the filter's developer |bigsh0t|.
