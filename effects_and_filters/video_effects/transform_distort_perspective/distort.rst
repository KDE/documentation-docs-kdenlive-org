.. meta::

   :description: Kdenlive Video Effects - Distort
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, distort

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Distort
=======

.. figure:: /images/effects_and_compositions/effects-distort-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Distort

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      distort0r
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No
   :**Color depth**:
      8bit
   :**Tutorial**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter creates an overlapping wave distortion with adjustable amplitude, frequency, and speed giving the video a plasma appearance.

Compare with the :doc:`/effects_and_filters/video_effects/transform_distort_perspective/wave` effect.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Use Velocity
     - Switch
     - Determine whether the :guilabel:`Velocity` parameter is used (**On** default) or the velocity is time based (**Off**)
   * - Amplitude
     - Percent
     - Set the amplitude of the plasma signal. Smaller values work best.
   * - Frequency
     - Percent
     - Set the frequency of the plasma signal. Smaller values work best.
   * - Velocity
     - Percent
     - Set the speed of the plasma signal. Smaller values work best.
