.. meta::

   :description: Do your first steps with Kdenlive video editor, using histogram equalizer effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, histogram equalizer

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-histogram_equalizer:

Histogram Equalizer
===================

This effect/filter applies a global color histogram equalization on a per-frame basis.

It can be used to correct video that has a compressed range of pixel intensities. The filter redistributes the pixel intensities to equalize their distribution across the intensity range. It may be viewed as an "automatically adjusting contrast filter". This filter is useful only for correcting degraded or poorly captured source video.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-histogram_equalizer.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-histogram_equalizer

   Histogram Equalizer effect

* **Strength** - Determine the amount of equalization to be applied. As the strength is reduced, the distribution of pixel intensities more and more approaches that of the input frame. The value must be a float number in the range from 0 to 1 and defaults to 0.200.

* **Intensity** - Set the maximum intensity that can generate and scale the output values appropriately. The strength should be set as desired and then the intensity can be limited if needed to avoid wash-out. The value must be a float number in the range from 0 to 1 and defaults to 0.210.

* **Antibanding level** - Set the antibanding level. If enabled the filter will randomly vary the :term:`luminance` of output pixels by a small amount to avoid banding of the histogram. Possible values are **None**, **Weak** or **Strong**. It defaults to **None**.
