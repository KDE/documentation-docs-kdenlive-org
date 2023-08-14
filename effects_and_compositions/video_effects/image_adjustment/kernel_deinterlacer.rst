.. meta::

   :description: Do your first steps with Kdenlive video editor, using kernel deinterlacer effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, image adjustment, kernel deinterlacer

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-kernel_deinterlacer:

Kernel Deinterlacer
===================

This effect/filter deinterlaces input video by applying Donald Graft’s adaptive kernel deinterling. Work on interlaced parts of a video to produce progressive frames.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-kernel_deinterlacer.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-kernel_deinterlacer

   Kernel Deinterlacer effect

* **Threshold** - Sets the threshold which affects the filter’s tolerance when determining if a pixel line must be processed. It must be an integer in the range [0,255] and defaults to 10. A value of 0 will result in applying the process on every pixels.

* **Paint in white pixels exceeding the threshold** - Paint pixels exceeding the threshold value to white if set to **On**. Default is **Off**.

* **Swap fields** - Sets the fields order. Swap fields if set to **On**, leave fields alone if **Off**. Default is **Off**.

* **Enable additional sharpening** - Default is **Off**

* **Enable twoway sharpening** - Default is **Off**
