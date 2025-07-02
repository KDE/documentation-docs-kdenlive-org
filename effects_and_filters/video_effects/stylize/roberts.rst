.. meta::

   :description: Kdenlive Video Effects - Roberts
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, roberts, 10bit

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Roberts
=======

.. figure:: /images/effects_and_compositions/effects-roberts-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-roberts-2504.webp

.. sidebar:: |kdenlive-show-video| Roberts

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      roberts
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No
   :**Color depth**:
      10bit |color-management|
   :**Tutorial**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter applies the Roberts cross operator\ [1]_ to the input video stream. It detects edges (differential operator) and, in the default settings, colors them white and grainy. Compare :doc:`/effects_and_filters/video_effects/stylize/kirsch`, :doc:`/effects_and_filters/video_effects/stylize/prewitt` and :doc:`/effects_and_filters/video_effects/stylize/sobel` effects.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Planes
     - Selection
     - Set which :term:`planes<plane>` will be processed, unprocessed planes will be copied. Default is **All**.
   * - Scale
     - Integer
     - Set value which will be multiplied with filtered result
   * - Delta
     - Integer
     - Set value which will be added to filtered result

The following selection items are available:

:guilabel:`Planes`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - None
     - 
   * - Y (Luminance)
     - 
   * - U (Chroma red-diff)
     - 
   * - YU
     - 
   * - V (Chroma blue-diff)
     - 
   * - YV
     - 
   * - UV
     - 
   * - All
     - Default
   * - Alpha
     - 


----

.. |roberts| raw:: html

   <a href="https://en.wikipedia.org/wiki/Roberts_cross" target="_blank">Roberts Cross</a>


.. [1] For more details refer to the |roberts| article in Wikipedia
