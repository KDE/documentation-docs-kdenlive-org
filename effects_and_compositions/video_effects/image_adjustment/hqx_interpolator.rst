.. meta::

   :description: Do your first steps with Kdenlive video editor, using hqx interpolator effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, image adjustment, hqx interpolator

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |hqnx| raw:: html

   <a href="https://en.wikipedia.org/wiki/Pixel-art_scaling_algorithms#hqnx_family" target="_blank">Maxim Stepin's hqnx</a>


.. _effects-hqx_interpolator:

HQ*X Interpolator
=================

This effect/filter scales the input stream by 2, 3 or 4 using the Hq*X [1]_ magnification algorithm designed for pixel art.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-hqx_interpolator.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-hqx_interpolator

   HQ*X Interpolator effect

* **Interpolation factor** - Options are **2xHq*X**, **3xHq*X**, and **4xHq*X**

* **Maximum number of threads** - Sets the number of CPU threads to use for calculation

* **Position to set the filter** - Options are **frame**, **filter**, **source**, and **producer**.

.. rst-class:: clear-both


.. note:: When set to :guilabel:`frame` this can result in significantly longer rendering times.


**Notes**

.. [1] See the article in Wikipedia about |hqnx| family of algorithms.
