.. meta::

   :description: Kdenlive Video Effects - Prewitt
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, prewitt, 10bit

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Prewitt
=======

.. figure:: /images/effects_and_compositions/effects-prewitt-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Prewitt

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      prewitt
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

This effect/filter applies the Prewitt\ [1]_ operator to the input video stream. It detects edges (discrete differentiation operator) and, in the default settings, colors them white and pinkish. Compare :doc:`/effects_and_filters/video_effects/stylize/kirsch`, :doc:`/effects_and_filters/video_effects/stylize/roberts` and :doc:`/effects_and_filters/video_effects/stylize/sobel` effects.


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


----

.. |prewitt| raw:: html

   <a href="https://en.wikipedia.org/wiki/Prewitt_operator" target="_blank">Prewitt Operator</a>


.. [1] For more details refer to the |prewitt| article in Wikipedia


.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Icons used here (remove comment indent to enable them for this document)
   
   .. |linux| image:: /images/icons/linux.png
   :width: 14px
      :class: no-scaled-link

   .. |appimage| image:: /images/icons/kdenlive-appimage_3.svg
   :width: 14px
      :class: no-scaled-link

   .. |windows| image:: /images/icons/windows.png
   :width: 14px
      :class: no-scaled-link

   .. |apple| image:: /images/icons/apple.png
   :width: 14px
      :class: no-scaled-link
