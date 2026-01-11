.. meta::

   :description: Kdenlive Video Effects - Chroma Noise Reduction
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, grain and noise, chroma noise reduction

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Chroma Noise Reduction
======================

.. figure:: /images/effects_and_compositions/effects-chroma_noise_reduction-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Chroma Noise Reduction

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      chromanr
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter reduces :term:`chrominance` noise.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Y+U+V Threshold
     - Integer
     - Set threshold for averaging chrominance values. Sum of absolute difference of Y, U and V pixel components of current pixel and neighbor pixels lower than this threshold will be used in averaging. :term:`Luma<luma>` component is left unchanged and is copied to output. Default value is 30. Allowed range is from 1 to 200.
   * - Horizontal / Vertical size
     - Integer
     - Set horizontal / vertical radius of rectangle used for averaging. Allowed range is from 1 to 100. Default value is 5.
   * - Horizontal step
     - Integer
     - Set horizontal step when averaging. Default value is 1. Allowed range is from 1 to 50. Mostly useful to speed-up filtering.
   * - Y / U / V threshold
     - Integer
     - Set Y / U / V threshold for averaging chrominance values. Set finer control for max allowed difference between Y / U / V components of current pixel and neighbor pixels. Default value is 200. Allowed range is from 1 to 200.
   * - Distance
     - Selection
     - Set distance type used in calculations


The following selection items are available:

:guilabel:`Distance`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Manhatten
     - absolute difference (default)
   * - Euclidean
     - difference squared
