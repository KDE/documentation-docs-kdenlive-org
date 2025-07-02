.. meta::

   :description: Kdenlive Video Effects - Oscilloscope
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, utility, oscilloscope

.. metadata-placeholder

   :authors: - Roger (https://userbase.kde.org/User:Roger)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Oscilloscope (simple)
=====================

.. figure:: /images/effects_and_compositions/effects-oscilloscope-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-oscilloscope-2504.webp

.. sidebar:: |kdenlive-show-video| Oscilloscope (simple)

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
   :**Color depth**:
      10bit |color-management|
   :**Tutorial**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter creates a 2D video oscilloscope overlay. Useful to measure spatial impulse, step responses, chroma delays, etc. If you need more parameters to control, use the :doc:`/effects_and_filters/video_effects/utility/oscilloscope_advanced` effect.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 10 65
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Components
     - Selection
     - Set which components to trace. By default it traces **All** components (YUV).
   * - Draw Scope Grid
     - Switch
     - Set scope size, relative to frame diagonal
   * - Print Statistics
     - Switch
     - Set scope size, relative to frame diagonal
   * - Draw Trace Profile Line
     - Switch
     - 
   * - Trace X Position
     - Integer
     - Set trace center X position
   * - Trace Y Position
     - Integer
     - Set trace center Y position
   * - Size
     - Integer
     - Set scope size, relative to frame diagonal
   * - Tilt
     - Integer
     - Set scope tilt/rotation
   * - Opacity
     - Integer
     - Set scope opacity
   * - Scope X Position
     - Integer
     - Set scope center X position
   * - Scope Y Position
     - Integer
     - Set scope center Y position
   * - Scope Width
     - Integer
     - Set trace width, relative to width of frame
   * - Scope Height
     - Integer
     - Set trace height, relative to height of frame


The following selection items are available:

:guilabel:`Components`

.. list-table::
   :width: 100%
   :widths: 25 75
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