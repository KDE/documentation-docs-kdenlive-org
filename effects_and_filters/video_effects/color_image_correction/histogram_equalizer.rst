.. meta::

   :description: Kdenlive Video Effects - Histogram Equalizer
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, histogram equalizer

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Histogram Equalizer
===================

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-histogram_equalizer.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-histogram_equalizer

.. sidebar:: |kdenlive-show-video| Histogram Equalizer

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      histeq
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter applies a global color histogram equalization on a per-frame basis.

It can be used to correct video that has a compressed range of pixel intensities. The filter redistributes the pixel intensities to equalize their distribution across the intensity range. It may be viewed as an "automatically adjusting contrast filter". This filter is useful only for correcting degraded or poorly captured source video.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Strength
     - Float
     - Determine the amount of equalization to be applied. As the strength is reduced, the distribution of pixel intensities more and more approaches that of the input frame. The value must be a float number in the range from 0 to 1 and defaults to 0.200.
   * - Intensity
     - Float
     - Set the maximum intensity that can generate and scale the output values appropriately. The strength should be set as desired and then the intensity can be limited if needed to avoid wash-out. The value must be a float number in the range from 0 to 1 and defaults to 0.210.
   * - Antibanding level
     - Selection
     - Set the antibanding level. If enabled the filter will randomly vary the :term:`luminance` of output pixels by a small amount to avoid banding of the histogram.


The following selection items are available:

:guilabel:`Antibanding level`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - None
     - Default
   * - Weak
     - 
   * - Strong
     - 
