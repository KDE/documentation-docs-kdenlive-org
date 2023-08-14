.. meta::

   :description: Do your first steps with Kdenlive video editor, using ndvi filter effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, ndvi filter

.. metadata-placeholder

   :authors: - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |ndvi| raw:: html

   <a href="https://en.wikipedia.org/wiki/Normalized_Difference_Vegetation_Index" target="_blank">NDVI</a>


.. _effects-ndvi_filter:

NDVI Filter
===========

This effect/filter creates a Normalized Difference Vegetation Index\ [1]_ false image from a visible and infrared source.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-ndvi_filter.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-ndvi_filter

   NDVI Filter effect

* **Levels** - The number of color levels to use in the false image (divided by 1000)

* **VIS Scale** - A scaling factor to be applied to the visible component (divided by 10)

* **VIS Offset** - An offset to be applied to the visible component (mapped to [-100%, 100%])

* **NIR Scale** - A scaling factor to be applied to the near-infrared component (divided by 10)

* **NIR Offset** - An offset to be applied to the near-infrared component (mapped to [-100%, 100%])

.. rst-class:: clear-both


**Notes**

.. [1] For more information about NDVI refer to the |ndvi| article in Wikipedia
