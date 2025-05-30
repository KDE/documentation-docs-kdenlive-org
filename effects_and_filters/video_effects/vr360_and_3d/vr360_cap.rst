.. meta::

   :description: Kdenlive Video Effects - VR360 Cap Top and Bottom 
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, VR360 and 3D, VR360 cap top and bottom

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


VR360 Cap Top and Bottom
========================

.. figure:: /images/effects_and_compositions/effects-vr360_cap-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-vr360_cap-2504.webp

.. sidebar:: |kdenlive-show-video| VR360 Cap Top and Bottom

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      bigsh0t_eq_cap\ [1]_
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter attempts to fill in zenith and nadir by stretching and blurring the image data. It samples a band of latitude near the start of the effect and stretches and blurs it over the pole.


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
   * - Top Enabled
     - Switch
     - Enables parameters for top portion
   * - Bottom Enabled
     - Switch
     - Enables parameters for bottom portion
   * - **--Top--** Start\ [2]_
     - Degrees
     - Degrees from the horizon where we start to fill in
   * - End
     - Degrees
     - Degrees from the horizon where we reach maximum blur
   * - Blend In
     - Degrees
     - Degrees towards the horizon to sample from
   * - Blend Out
     - Degrees
     - Degrees away from the horizon to sample to
   * - Fade In
     - Degrees
     - Degrees to fade the effect in over
   * - Blur width at start
     - Degrees
     - Horizontal angle to blur over at the start of the fill-in
   * - Blur width at end
     - Degrees
     - Horizontal angle to blur over	at the end of the fill-in
   * - Blur height at start
     - Degrees
     - Vertical angle to blur over at the start of the fill-in
   * - Blur height at end
     - Degrees
     - Vertical angle to blur over at the end of the fill-in
   * - **--Bottom--** Start\ [3]_
     - Degrees
     - Degrees from the horizon where we start to fill in
   * - End
     - Degrees
     - Degrees from the horizon where we reach maximum blur
   * - Blend In
     - Degrees
     - Degrees towards the horizon to sample from
   * - Blend Out
     - Degrees
     - Degrees away from the horizon to sample to
   * - Fade In
     - Degrees
     - Degrees to fade the effect in over
   * - Blur width at start
     - Degrees
     - Horizontal angle to blur over at the start of the fill-in
   * - Blur width at end
     - Degrees
     - Horizontal angle to blur over	at the end of the fill-in
   * - Blur height at start
     - Degrees
     - Vertical angle to blur over at the start of the fill-in
   * - Blur height at end
     - Degrees
     - Vertical angle to blur over at the end of the fill-in


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

.. [2] The following eight parameters relate to the top half (zenith) of the VR360 source

.. [3] The following eight parameters relate to the bottom half (nadir) of the VR360 source