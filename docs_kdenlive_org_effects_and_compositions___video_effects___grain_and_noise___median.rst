.. meta::

   :description: Do your first steps with Kdenlive video editor, using median effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, grain and noise, median

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-median:

Median
======

This effect/filter picks the median pixel from a given rectangle defined by :guilabel:`Spatial sigma`.

The effect has keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-median.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-median

   Median effect

* **Planes** - Sets which :term:`planes<plane>` to process. Defaults to **Y**.

* **Spatial sigma** - Sets the horizontal radius size. Allowed values are from 1.000 to 127.000, default is 1.

* **Median vertical radius** - Sets the vertical radius size. Allowed values are from 1.000 to 127.000, default is 0. If it is 0, value will be picked from :guilabel:`Spatial sigma` parameter.

* **Median percentile** - Set median percentile. Default is 0.5. Default value will pick always median values, 0 will pick minimum values, and 1 maximum values.
