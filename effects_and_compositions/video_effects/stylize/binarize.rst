.. meta::

   :description: Do your first steps with Kdenlive video editor, using binarize effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, binarize

.. metadata-placeholder

   :authors: - Roger (https://userbase.kde.org/User:Roger)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. used to be threshold


.. |threshold| raw:: html

   <a href="https://ffmpeg.org/ffmpeg-filters.html#threshold" target="_blank">ffmpeg.threshold</a>


.. _effects-binarize:

Binarize
========

This effect/filter creates a monochrome (black & white) image based on the threshold value.

The effect has keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-binarize.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-binarize

   Binarize effect

* **Use transparency** - If selected, compares the midpoint (set by :guilabel:`Threshold value`) with the alpha channel instead of :term:`luma`

* **Threshold value** - Set the threshold (midpoint)

.. rst-class:: clear-both


**Notes**

This is the |threshold| filter that used to be called *Threshold*
