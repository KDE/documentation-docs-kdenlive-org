.. meta::

   :description: Kdenlive Video Effects - NDVI Filter
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, ndvi filter

.. metadata-placeholder

   :authors: - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


NDVI Filter
===========

.. figure:: /images/effects_and_compositions/effects-ndvi_filter-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-ndvi_filter-2504.webp

.. sidebar:: |kdenlive-show-video| NDVI Filter

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      frei0r
   :**Source filter**:
      ndvi
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No
   :**Color depth**:
      8bit
   :**Tutorial**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter creates a Normalized Difference Vegetation Index\ [1]_ false image from a visible and infrared source.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Levels
     - Float
     - The number of color levels to use in the false image (divided by 1000)
   * - VIS Scale
     - Float
     - A scaling factor to be applied to the visible component (divided by 10)
   * - VIS Offset
     - Float
     - An offset to be applied to the visible component (mapped to [-100%, 100%])
   * - NIR Scale
     - Float
     - A scaling factor to be applied to the near-infrared component (divided by 10)
   * - NIR Offset
     - Float
     - An offset to be applied to the near-infrared component (mapped to [-100%, 100%])


----

.. |ndvi| raw:: html

   <a href="https://en.wikipedia.org/wiki/Normalized_Difference_Vegetation_Index" target="_blank">NDVI</a>

.. [1] For more information about NDVI refer to the |ndvi| article in Wikipedia
