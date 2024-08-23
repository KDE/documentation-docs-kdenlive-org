.. meta::

   :description: Kdenlive Video Effects - Flippo
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, flippo

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Flippo
======

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-flippo.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-flippo

.. sidebar:: |kdenlive-show-video| Flippo

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      frei0r
   :**Source filter**:
      flippo
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter flips the input video along the X and/or Y axis. It basically combines the :doc:`/effects_and_filters/video_effects/transform_distort_perspective/flip_horizontally` and :doc:`/effects_and_filters/video_effects/transform_distort_perspective/flip_vertically` effects. Also compare with :doc:`/effects_and_filters/video_effects/transform_distort_perspective/mirror`.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - X axis
     - Switch
     - Flip along the X axis (flip vertically)
   * - Y axis
     - Switch
     - Flip along the Y axis (flip horizontally)
