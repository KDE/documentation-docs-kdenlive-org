.. meta::

   :description: Do your first steps with Kdenlive video editor, using limiter effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, limiter

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-limiter:

Limiter
=======

This effect/filter limits the pixel components values to the specified range.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-limiter.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-limiter

   Limiter effect

* **Min** - Lower bound. Defaults to the lowest allowed value for the input.

* **Max** - Upper bound. Defaults to the highest allowed value for the input.

* **Planes** - Specify which :term:`planes<plane>` will be processed. Options are **None**, **Y**, **YU**, **V**, **YV**, **UV**, **YUV** and **Alpha**. Defaults to **YUV**.
