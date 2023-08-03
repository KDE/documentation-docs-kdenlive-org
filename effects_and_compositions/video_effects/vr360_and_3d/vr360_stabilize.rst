.. meta::

   :description: Do your first steps with Kdenlive video editor, using VR360 stabilize effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, VR360 and 3D, VR360 stabilize

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |bigsh0t| raw:: html

   <a href="https://bitbucket.org/leo_sutic/bigsh0t/src/main/" target="_blank">bigsh0t</a>


.. _effects-vr360_stabilize:

VR360 Stabilize
===============

This effect/filter stabilizes 360 footage.

The filter works in two phases: analysis and stabilization. When analyzing footage, it detects frame-to-frame rotation, and when stabilizing it tries to correct high-frequency motion (shake).

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-vr360_stabilize.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-vr360_stabilize

   VR360 Stabilize effect

* **Analyze** - Switch on for analysis phase, switch off for stabilization

* **Motion Analysis File** - Path to file that will be used to store the analysis data

* **Analysis Sample Radius** - The radius of the square that the stabilizer will sample.

* **Analysis Search Radius** - The maximum amount of motion the stabilizer will detect.

* **Analysis Offset** - The distance between the track points.

* **Track Points** - When checked, the filter will apply the frame-to-frame transform in order to show the quality of the analysis. When you are satisfied with the analysis quality you can turn this off, as it adds approximately 50% to the analysis time.

* **Yaw / Pitch / Roll Amount** - The amount of stabilization to apply. 100% means that the stabilizer will make the camera as steady as it can. Smaller values reduce the amount of stabilization.

* **Yaw / Pitch / Roll Smoothing** - The number of frames to use to smooth out the shakes. The higher the value, the slower the camera will follow any intended motion.

* **Yaw / Pitch / Roll Time Bias** - Shift the frames used to smooth out the shakes relative to the stabilized frame. A value less than zero will give more weight to past frames, and the camera will seem to lag behind intended movement. A value greater than zero will give more weight to future frames, and the camera will appear to move ahead of the intended camera movement. A value of zero should make the camera follow the intended path.

* **Interpolation** - Defines output quality. Options are **Nearest-Neighbor** (default) and **Bilinear**.

.. rst-class:: clear-both


.. rubric:: How to Stabilize 360-degree Video

#. Add the 360-degree footage to the timeline

#. Apply the :ref:`effects-vr360_hemi2equi` effect to it so it is in equirectangular format

#. Apply the :ref:`effects-vr360_transform` effect

#. Apply this effect (VR360 Stabilize)

#. Select a file to store stabilization data in (:guilabel:`Motion Analysis File`)

#. Enable :guilabel:`Analyze` mode

#. Use the :ref:`effects-vr360_transform` effect to rotate the footage so that the point straight ahead is over the center cluster of track points

#. Play the footage from start to finish.

#. When the footage has completed playing, switch off the :guilabel:`Analyze` mode.

#. You should now have stable 360 video


**Notes**

Parts of this documentation have been taken from the website of the filter's developer |bigsh0t|.
