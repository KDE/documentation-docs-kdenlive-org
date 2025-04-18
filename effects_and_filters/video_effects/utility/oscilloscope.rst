.. meta::

   :description: Kdenlive Video Effects - Oscilloscope
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, utility, oscilloscope

.. metadata-placeholder

   :authors: - Roger (https://userbase.kde.org/User:Roger)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Oscilloscope
============

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-oscilloscope.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-oscilloscope

.. sidebar:: |kdenlive-show-video| Oscilloscope

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      oscilloscope
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter creates a 2D video oscilloscope overlay. Useful to measure spatial impulse, step responses, chroma delays, etc. If you need more parameters to control, use the :doc:`/effects_and_filters/video_effects/utility/oscilloscope_advanced` effect.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - av.x / av.y
     - Float
     - Set scope center x / y position
   * - av.s
     - Float
     - Set scope size, relative to frame diagonal
   * - av.t
     - Float
     - Set scope tilt/rotation
   * - av.o
     - Float
     - Set scope opacity
   * - av.tx / av.ty
     - Float
     - Set trace center x /y position
   * - av.tw / av.th
     - Float
     - Set trace width / height, relative to width / height of frame
   * - av.c
     - Integer
     - Set which components to trace. By default it traces YUV components.


.. rubric:: Components Matrix

.. list-table::
   :header-rows: 1

   * - av.c Value
     - Component
   * - 0
     - None
   * - 1
     - Y
   * - 2
     - U
   * - 3
     - YU
   * - 4
     - V
   * - 5
     - YV
   * - 6
     - UV
   * - 7 (default)
     - YUV
   * - 8..15
     - repeat


.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Icons used here (remove comment indent to enable them for this document)
   
   .. |linux| image:: /images/icons/linux.png
   :width: 14px
   :alt: Linux
   :class: no-scaled-link

   .. |appimage| image:: /images/icons/kdenlive-appimage_3.svg
   :width: 14px
   :alt: appimage
   :class: no-scaled-link

   .. |windows| image:: /images/icons/windows.png
   :width: 14px
   :alt: Windows
   :class: no-scaled-link

   .. |apple| image:: /images/icons/apple.png
   :width: 14px
   :alt: MacOS
   :class: no-scaled-link