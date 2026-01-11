.. meta::

   :description: Kdenlive Video Effects - VR360 Stabilize
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, VR360 and 3D, VR360 stabilize

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


VR360 Stabilize
===============

.. figure:: /images/effects_and_compositions/effects-vr360_stabilize-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| VR360 Stabilize

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      frei0r
   :**Source filter**:
      bigh0t_stabilize_360\ [1]_
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter stabilizes 360 footage.

The filter works in two phases: analysis and stabilization. When analyzing footage, it detects frame-to-frame rotation, and when stabilizing it tries to correct high-frequency motion (shake).


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 10 65
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Analyze
     - Switch
     - Switch on for analysis phase, switch off for stabilization
   * - Motion analysis file
     - 
     - Path to file that will be used to store the analysis data
   * - Start offset
     - Float
     - The offset into the stabilization file that corresponds to the start of this clip. For example, if you have a 30 second clip, analyze it all, and then split it into three clips of 10 seconds each, then the start offsets should be 0s, 10s, and 20s
   * - Analysis sample radius
     - Integer
     - The radius of the square that the stabilizer will sample.
   * - Analysis search radius
     - Integer
     - The maximum amount of motion the stabilizer will detect.
   * - Analysis offset
     - Integer
     - The distance between the track points.
   * - Use backwards-facing track point
     - Switch
     - If set, six backwards-facing track points will also be used to detect pitch and yaw motion. Disable if, for example, you show up holding the camera there.
   * - Yaw / Pitch / Roll amount
     - Percentage
     - The amount of stabilization to apply. 100% means that the stabilizer will make the camera as steady as it can. Smaller values reduce the amount of stabilization.
   * - Yaw / Pitch / Roll smoothing
     - Integer
     - The number of frames to use to smooth out the shakes. The higher the value, the slower the camera will follow any intended motion.
   * - Yaw / Pitch / Roll time bias
     - Percentage
     - Shift the frames used to smooth out the shakes relative to the stabilized frame. A value less than zero will give more weight to past frames, and the camera will seem to lag behind intended movement. A value greater than zero will give more weight to future frames, and the camera will appear to move ahead of the intended camera movement. A value of zero should make the camera follow the intended path.
   * - Interpolation
     - Selection
     - Defines output quality


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


.. rubric:: How to Stabilize 360-degree Video

#. Add the 360-degree footage to the timeline

#. Apply the :doc:`/effects_and_filters/video_effects/vr360_and_3d/vr360_hemi2equi` effect to it so it is in equirectangular format

#. Apply the :doc:`/effects_and_filters/video_effects/vr360_and_3d/vr360_transform` effect

#. Apply this effect (VR360 Stabilize)

#. Select a file to store stabilization data in (:guilabel:`Motion Analysis File`)

#. Enable :guilabel:`Analyze` mode

#. Use the :doc:`/effects_and_filters/video_effects/vr360_and_3d/vr360_transform` effect to rotate the footage so that the point straight ahead is over the center cluster of track points

#. Play the footage from start to finish.

#. When the footage has completed playing, switch off the :guilabel:`Analyze` mode.

#. You should now have stable 360 video


----

.. |bigsh0t| raw:: html

   <a href="https://bitbucket.org/leo_sutic/bigsh0t/src/main/" target="_blank">bigsh0t</a>


.. [1] Parts of this documentation have been taken from the website of the filter's developer |bigsh0t|.
