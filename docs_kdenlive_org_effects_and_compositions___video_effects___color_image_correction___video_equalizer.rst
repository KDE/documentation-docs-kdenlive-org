.. meta::

   :description: Do your first steps with Kdenlive video editor, using video equalizer effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, video equalizer

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-video_equalizer:

Video Equalizer
===============

This effect/filter sets brightness, contrast, :term:`saturation` and approximate :term:`gamma` adjustment.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-video_equalizer.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-video_equalizer

   Video Equalizer effect

* **Contrast** - Set the contrast expression. Negative values give a negative image. The value must be a float value in range -3.00 to 3.00. The default value is 1.00.

* **Brightness** - Set the brightness expression. The value must be a float value in range -1.00 to 1.00. The default value is 0.00.

* **Saturation** - Set the saturation expression. The value must be a float in range 0.00 to 5.00. The default value is 1.00.

* **Gamma** - Set the gamma expression. The value must be a float in range 0.00 to 3.00. The default value is 1.00.

* **Red / Green / Blue Gamma** - Set the gamma expression for red, green or blue. The value must be a float in range 0.00 to 3.00. The default value is 1.00.

* **Gamma Weight** - Set the gamma weight expression. It can be used to reduce the effect of a high gamma value on bright image areas, e.g. keep them from getting over amplified and just plain white. The value must be a float in range 0.00 to 1.00. A value of 0.0 turns the gamma correction all the way down while 1.00 leaves it at its full strength. Default is 1.00.
