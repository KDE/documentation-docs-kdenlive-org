.. meta::

   :description: Do your first steps with Kdenlive video editor, using xbr interpolator effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, image adjustment, xbr interpolator

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |xbr_wiki| raw:: html

   <a href="https://en.wikipedia.org/wiki/Pixel-art_scaling_algorithms#xBR_family" target="_blank">xBR family</a>

.. |xbr_tutorial| raw:: html

   <a href="https://forums.libretro.com/t/xbr-algorithm-tutorial/123" target="_blank">xBR tutorial</a>


.. _effects-xbr_interpolator:

XBR Interpolator
================

This effect/filter applies the xBR [1]_ high-quality magnification filter which is designed for pixel art. It follows a set of edge-detection rules. [2]_

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-xbr_interpolator.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-xbr_interpolator

   XBR Interpolator effect

* **Interpolation factor** - Sets the scaling factor: 2xBR, 3xBR or 4xBR

* **Maximum number of threads** - Sets the number of CPU threads to use

* **Position to set the filter** - Options are: **frame**, **filter**, **source**, and **producer**. When set to **frame** render times may be very high.

.. rst-class:: clear-both


**Notes**

.. [1] For more details see this section about the |xbr_wiki| of algorithms in Wikipedia (scroll down two pages)

.. [2] See this |xbr_tutorial|
