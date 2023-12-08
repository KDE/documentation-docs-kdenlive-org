.. meta::

   :description: Kdenlive Video Effects - Sobel with Planes
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, sobel with planes

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Sobel with Planes
=================

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-sobel_planes.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-sobel_planes

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

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter is the same as the :doc:`/effects_and_compositions/video_effects/stylize/sobel` effect but has parameters for more control. Compare :doc:`/effects_and_compositions/video_effects/stylize/kirsch`, :doc:`/effects_and_compositions/video_effects/stylize/prewitt` and :doc:`/effects_and_compositions/video_effects/stylize/roberts` effects.


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
   * - Y
     - 
   * - U
     - 
   * - YU
     - 
   * - V
     - 
   * - YV
     - 
   * - UV
     - 
   * - YUV
     - Default
   * - Alpha
     - 
