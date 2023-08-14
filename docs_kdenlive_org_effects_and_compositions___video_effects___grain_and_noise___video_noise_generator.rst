.. meta::

   :description: Do your first steps with Kdenlive video editor, using video noise generator effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, grain and noise, video noise generator

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-video_noise_generator:

Video Noise Generator
=====================

This effect/filter adds noise to the video input frame.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-video_noise_generator.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-video_noise_generator

   Video Noise Generator effect

* **All components noise seed** - Set noise seed for all pixel components

* **Component #0 / #1 / #2 / #3 noise seed** - Set noise seed for specific pixel component

* **All component strength** - Set noise strength for all pixel components

* **Component #0 / #1 / #2 / #3 noise seed** - Set noise strength for specific pixel component

* **Flag all** - Set pixel component flag for all components

* **Flag component 0 / 1 / 2 / 3** - Set pixel component flags

.. rst-class:: clear-both

The :guilabel:`Flag` parameter has the following options:

* **Average temporal noise** - Averaged temporal noise (smoother)

* **Mixed random noise** - Mix random noise with a (semi-)regular pattern

* **Temporal noise** - Temporal noise (noise pattern changes between frames)

* **Uniform noise** - Uniform noise (Gaussian otherwise)
