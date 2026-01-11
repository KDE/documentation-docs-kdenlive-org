.. meta::

   :description: Kdenlive Video Effects - Scharr
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, scharr, edge, detection, 10bit

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Scharr
======

.. figure:: /images/effects_and_compositions/effects-scharr-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Scharr

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      avfilter
   :**Source filter**:
      scharr
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

This effect/filter applies the Scharr\ [1]_ operator to the input video stream for edge detection.

Compare :doc:`/effects_and_filters/video_effects/stylize/sobel_planes`, :doc:`/effects_and_filters/video_effects/stylize/kirsch`, :doc:`/effects_and_filters/video_effects/stylize/prewitt` and :doc:`/effects_and_filters/video_effects/stylize/roberts` effects.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Planes to filter
     - Selection (see below)
     - Set which :term:`planes<plane>` will be processed, unprocessed planes will be copied. Set to **All** by default.
   * - Scale
     - Float
     - Sets the value which the filtered result will be multiplied with
   * - Delta
     - Float
     - Sets the value which will be added to filtered result

The following selection items are available:

:guilabel:`Planes to filter`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Alpha
     - 
   * - Luminance (Y)
     - 
   * - Chroma (U plane)
     - 
   * - Chroma (V plane)
     - 
   * - Red
     - 
   * - Green
     - 
   * - Blue
     - 
   * - All
     - Default


----

.. |scharr| raw:: html

   <a href="https://en.wikipedia.org/wiki/Sobel_operator#Alternative_operators" target="_blank">Alternative Operators</a>


.. [1] For more (mathematical) details refer to the Wikipedia article about Sobel, and there specifically about |scharr|.
