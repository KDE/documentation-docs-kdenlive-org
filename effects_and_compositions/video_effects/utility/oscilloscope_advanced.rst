.. meta::

   :description: Do your first steps with Kdenlive video editor, using oscilloscope (advanced) effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, utility, oscilloscope (advanced)

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |rms| raw:: html

   <a href="https://undergroundmathematics.org/glossary/root-mean-square" target="_blank">this article</a>


.. _effects-oscilloscope_advanced:

Oscilloscope (advanced)
=======================

This effect/filter draws a 2D oscilloscope over the clip. It does the same as :ref:`effects-oscilloscope` but offers more parameters and features, such as drawing a line across the frame that is used for the computations.

The effect has keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-oscilloscope_advanced.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-oscilloscope_advanced

   Oscilloscope (advanced) effect

* **Channel** - Channel to numerically display at the bottom of the scope

* **R / G / B trace** - Show R / G / B trace on scope

* **Y / Pr / Pb trace** - Show Y' / Pr / Pb trace on scope

* **Alpha trace** - Show Alpha trace on scope

* **Display average** - If switched on, averages are displayed

* **Display RMS** - If switched on, the RMS\ [1]_ value is displayed

* **Display minimum / maximum** - If switched on, minimum and maximum values are displayed

* **256 scale** - If switched on, the oscilloscope uses the range 0..255 instead of 0.0..1.0 for value display

* **Color** - Set :term:`color space` to use. Options are **CCIR rec. 601** (default) and **CCIR rec. 709**.

* **X / Y / Tilt / Length** - X / Y position, Tilt and Length of the profile marker (the line in the middle of the screen indicating where the scope values are taken from)

.. rst-class:: clear-both

* **Marker 1 / 2** - Position of marker 1 / 2 (starting on the left side)

* **Crosshair color** - Color of the profile marker


**Notes**

.. [1] RMS = Root Mean Squared. Useful when trying to measure the average "size" of numbers, where their sign is not important, as the squaring makes all numbers positive. The most common case of using the root mean square is when calculating the standard deviation of a set of numbers. For the mathematical details, refer to |rms| in undergroundmathematics.org
