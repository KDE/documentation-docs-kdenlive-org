.. meta::

   :description: Do your first steps with Kdenlive video editor, using normalize rgb video effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, normalize rgb video

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |wikipedia_normalization| raw:: html

   <a href="https://en.wikipedia.org/wiki/Normalization_(image_processing)" target="_blank">normalization</a>


.. _effects-normalize_rgb_video:

Normalize RGB Video
===================

This effect/filter normalizes RGB video (aka histogram stretching, contrast stretching).

The effect has keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-normalize_rgb_video.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-normalize_rgb_video

   Normalize RGB Video effect

* **Temporal smoothing** - The number of previous frames to use for temporal smoothing. The input range of each channel is smoothed using a rolling average over the current frame and the smoothing previous frames. The default is 0 (no temporal smoothing).

* **Proportion of independent** - Controls the ratio of independent (color shifting) channel normalization to linked (color preserving) normalization. 0.0 is fully linked, 1.0 is fully independent. Defaults to 1.0 (fully independent).

* **Strength** - Overall strength of the filter. 1.0 is full strength. 0.0 is a rather expensive no-op. Defaults to 1.0 (full strength).

* **Output darkest / brightest input color** - Colors which define the output range. The minimum input value is mapped to the *output darkest input color*. The maximum input value is mapped to the *output brightest input color*. The defaults are black and white respectively. Specifying white for *output darkest input color* and black for *output brightest input color* will give color-inverted, normalized video. Shades of grey can be used to reduce the dynamic range (contrast). Specifying saturated colors here can create some interesting effects.

.. rst-class:: clear-both

.. note:: The Normalize RGB Video and :ref:`effects-normaliz0r` effects essentially do the same but produce slightly different results.

**Notes**

For more information refer to the Wikipedia article about |wikipedia_normalization|.
