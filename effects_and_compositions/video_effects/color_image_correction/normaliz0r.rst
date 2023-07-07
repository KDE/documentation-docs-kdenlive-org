.. meta::

   :description: Do your first steps with Kdenlive video editor, using normaliz0r effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, normaliz0r

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |wikipedia_normalization| raw:: html

   <a href="https://en.wikipedia.org/wiki/Normalization_(image_processing)" target="_blank">normalization</a>


.. _effects-normaliz0r:

Normaliz0r
===========

This effect/filter normalizes RGB video (aka histogram stretching, contrast stretching).

The effect has keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-normaliz0r.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-normaliz0r

   Normaliz0r effect

* **Smoothing** - The number of previous frames to use for temporal smoothing. The input range of each channel is smoothed using a rolling average over the current frame and the smoothing previous frames. The default is 0 (no temporal smoothing).

* **Independence** - Controls the ratio of independent (color shifting) channel normalization to linked (color preserving) normalization. 0.0 is fully linked, 1.0 is fully independent. Defaults to 1.0 (fully independent).

* **Strength** - Overall strength of the filter. 1.0 is full strength. 0.0 is a rather expensive no-op. Defaults to 1.0 (full strength).

* **BlackPt / WhitePt** - Colors which define the output range. The minimum input value is mapped to the *blackpt*. The maximum input value is mapped to the *whitept*. The defaults are black and white respectively. Specifying white for *blackpt* and black for *whitept* will give color-inverted, normalized video. Shades of grey can be used to reduce the dynamic range (contrast). Specifying saturated colors here can create some interesting effects.

.. rst-class:: clear-both

.. note:: The Normaliz0r and :ref:`effects-normalize_rgb_video` effects essentially do the same but produce slightly different results.

**Notes**

For more information refer to the Wikipedia article about |wikipedia_normalization|.
