.. meta::

   :description: Kdenlive Video Effects - Kernel Deinterlacer
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, image adjustment, kernel deinterlacer

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Kernel Deinterlacer
===================

.. figure:: /images/effects_and_compositions/effects-kernel_deinterlacer-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Kernel Deinterlacer

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      kerndeint
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter deinterlaces input video by applying Donald Graft’s adaptive kernel deinterlacing. It works on interlaced parts of a video to produce progressive frames.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Threshold
     - Integer
     - Sets the threshold which affects the filter's tolerance when determining if a pixel line must be processed. It must be an integer in the range [0,255] and defaults to 10. A value of 0 will result in applying the process on every pixel.
   * - Paint in white pixels exceeding the threshold
     - Switch
     - Paint pixels exceeding the threshold value to white if set to **On**. Default is **Off**.
   * - Swap fields
     - Switch
     - Sets the fields order. Swap fields if set to **On**, leave fields alone if **Off**. Default is **Off**.
   * - Enable additional sharpening
     - Switch
     - Default is **Off**
   * - Enable two-way sharpening
     - Switch
     - Default is **Off**
