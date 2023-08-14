.. meta::

   :description: Do your first steps with Kdenlive video editor, using chroma noise reduction effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, grain and noise, chroma noise reduction

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-chroma_noise_reduction:

Chroma Noise Reduction
======================

This effect/filter reduces :term:`chrominance` noise.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-chroma_noise_reduction.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-chroma_noise_reduction

   Chroma Noise Reduction effect

* **Y+U+V Threshold** - Set threshold for averaging chrominance values. Sum of absolute difference of Y, U and V pixel components of current pixel and neighbour pixels lower than this threshold will be used in averaging. :term:`Luma<luma>` component is left unchanged and is copied to output. Default value is 30. Allowed range is from 1 to 200.

* **Horizontal / Vertical size** - Set horizontal / vertical radius of rectangle used for averaging. Allowed range is from 1 to 100. Default value is 5.

* **Horizontal step** - Set horizontal step when averaging. Default value is 1. Allowed range is from 1 to 50. Mostly useful to speed-up filtering.

* **Y / U / V threshold** - Set Y / U / V threshold for averaging chrominance values. Set finer control for max allowed difference between Y / U / V components of current pixel and neighbour pixels. Default value is 200. Allowed range is from 1 to 200.

* **Distance** - Set distance type used in calculations. Options are **Manhatten** (absolute difference) and **Euclidean** (difference squared). Default is **Manhatten**.
