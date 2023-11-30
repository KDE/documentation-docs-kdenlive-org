.. meta::

   :description: Kdenlive Video Effects - XBR Interpolator
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, image adjustment, xbr interpolator

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


XBR Interpolator
================

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-xbr_interpolator.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-xbr_interpolator

.. sidebar:: |kdenlive-show-video| XBR Interpolator

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      xbr
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter applies the xBR\ [1]_ high-quality magnification filter which is designed for pixel art. It follows a set of edge-detection rules.\ [2]_


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 30 10 60
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Interpolation factor
     - Selection
     - Sets the scaling factor
   * - Maximum number of threads
     - Integer
     - Sets the number of CPU threads to use
   * - Position to set the filter
     - Selection
     - Defines where in the render pipeline the filter will be applied. When set to **frame** this can result in significantly longer rendering times.

The following selection items are available:

:guilabel:`Interpolation factor`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - 2xBR
     - 
   * - 3xBR
     - 
   * - 4xBR
     - 


:guilabel:`Position to set the filter`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - frame
     - Default
   * - filter
     - 
   * - source
     - 
   * - producer
     - 


----

.. |xbr_wiki| raw:: html

   <a href="https://en.wikipedia.org/wiki/Pixel-art_scaling_algorithms#xBR_family" target="_blank">xBR family</a>

.. |xbr_tutorial| raw:: html

   <a href="https://forums.libretro.com/t/xbr-algorithm-tutorial/123" target="_blank">xBR tutorial</a>


.. [1] For more details see this section about the |xbr_wiki| of algorithms in Wikipedia (scroll down two pages)

.. [2] See this |xbr_tutorial|
