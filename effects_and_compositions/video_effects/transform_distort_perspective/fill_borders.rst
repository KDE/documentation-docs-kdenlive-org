.. meta::

   :description: Do your first steps with Kdenlive video editor, using fill borders effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, fill borders

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-fill_borders:

Fill Borders
============

This effect/filter fills borders of the input video without changing video stream dimensions. Sometimes video can have garbage at the four edges and you may not want to crop the video input to keep the size a multiple of some number.

The effect has keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-fill_borders.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-fill_borders

   Fill Borders effect

* **Left / Right** - Number of pixels to fill from left / right border

* **Top / Bottom** - Number of pixels to fill from top / bottom border

* **Mode** - Set fill mode. Options are **Smear** (default; fill pixels using outermost pixels), **Mirror** (fill pixels using mirroring (half sample symmetric)), and **Fixed** (fill pixels with :guilabel:`Color`).

* **Color** - Set color for pixels in **Fixed** mode. Default is black.

.. rst-class:: clear-both


.. note:: As of this writing in version 23.04 the :guilabel:`Color` value is ignored.
