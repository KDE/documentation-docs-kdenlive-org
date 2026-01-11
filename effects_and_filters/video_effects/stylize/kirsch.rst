.. meta::

   :description: Kdenlive Video Effects - Kirsch
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, kirsch, 10bit

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Kirsch
======

.. figure:: /images/effects_and_compositions/effects-kirsch-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Kirsch

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      avfilter
   :**Source filter**:
      kirsch
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

This effect/filter applies the Kirsch\ [1]_ operator to the input video stream. It detects edges (non-linear edge detector) and, in the default settings, colors them in yellowish green, and colors are somewhat posterized. Compare :doc:`/effects_and_filters/video_effects/stylize/prewitt`, :doc:`/effects_and_filters/video_effects/stylize/roberts` and :doc:`/effects_and_filters/video_effects/stylize/sobel` effects.


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
     - Set which :term:`planes<plane>` will be processed, unprocessed planes will be copied. Default is **Y**.
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

   * - Alpha
     - Alpha channel (if present)
   * - Y (Luminance)
     - Luminance
   * - U (Chroma)
     - The blue-difference chroma component
   * - V (Chroma)
     - The red-difference chroma component
   * - Red
     - 
   * - Green
     - 
   * - Blue
     - 
   * - All
     - Default


----

.. |kirsch| raw:: html

   <a href="https://en.wikipedia.org/wiki/Kirsch_operator" target="_blank">Kirsch operator</a>


.. [1] For more (mathematical) details about this refer to the |kirsch| article in Wikipedia.
