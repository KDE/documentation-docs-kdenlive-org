.. meta::

   :description: Kdenlive Video Effects - Curves
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, curves

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Curves
======

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-curves.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-curves

.. sidebar:: |kdenlive-show-video| Curves

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      frei0r
   :**Source filter**:
      curves
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter adjusts shadows, midtones and highlights of an image using curves. It is similar to the :doc:`/effects_and_filters/video_effects/color_image_correction/color_levels` or :doc:`/effects_and_filters/video_effects/color_image_correction/levels` effects but with the option to create additional points along the curve allowing for pinpoint accuracy when adjusting brightness values.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Channel
     - Selection
     - Set the channel to which the curve applies.
   * - Luma formula
     - Selection
     - Set the color space in which the application takes place
   * - In
     - Float
     - Set the Input value
   * - Out
     - Float
     - Set the Output value
   * - Show graph in picture
     - Switch
     - Check this box to overlay the graph onto the image in the Project Monitor. Note that this influences the :ref:`view-rgb_parade` and :ref:`view-histogram` :term:`widgets<widget>`.
   * - Graph position
     - Selection
     - Select the position for the graph

The following selection items are available:

:guilabel:`Channel`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - RGB
     - Default
   * - Red
     - 
   * - Green
     - 
   * - Blue
     - 
   * - Alpha
     - 
   * - Luma
     - 
   * - Saturation
     - 

:guilabel:`Luma formula`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Rec. 709
     - Default
   * - Rec. 601
     - 

:guilabel:`Graph position`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Top left
     - 
   * - Top right
     - 
   * - Bottom left
     - 
   * - Bottom right
     - Default

.. rst-class:: clear-both

.. hint:: 
  It is recommended to use this effect while in Color layout as this comes with :ref:`RGB Parade <view-rgb_parade>` and :ref:`view-histogram` already switched on. If you want to use the effect while in Editing or Effects layout, turn on the Histogram :term:`widget` with :menuselection:`Menu --> View --> Histogram`.
