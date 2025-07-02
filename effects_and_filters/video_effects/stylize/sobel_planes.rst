.. meta::

   :description: Kdenlive Video Effects - Sobel with Planes
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, sobel with planes, 10bit

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Sobel with Planes
=================

.. figure:: /images/effects_and_compositions/effects-sobel_planes-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-sobel_planes-2504.webp

.. sidebar:: |kdenlive-show-video| Sobel with Planes

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      avfilter
   :**Source filter**:
      sobel
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

This effect/filter is the same as the :doc:`/effects_and_filters/video_effects/stylize/sobel` effect but has parameters for more control. Compare :doc:`/effects_and_filters/video_effects/stylize/kirsch`, :doc:`/effects_and_filters/video_effects/stylize/prewitt` and :doc:`/effects_and_filters/video_effects/stylize/roberts` effects.


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
     - Set which :term:`planes<plane>` will be processed, unprocessed planes will be copied.
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
