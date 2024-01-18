.. meta::

   :description: Kdenlive Video Effects - Video Values
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, utility, video values

.. metadata-placeholder

   :authors: - Roger (https://userbase.kde.org/User:Roger)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Video Values
============

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-video_values.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-video_values

.. sidebar:: |kdenlive-show-video| Video Values

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      pr0be
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter draws and overlays a window in the clip that shows a zoomed version of the area covered by a small crosshair, and specific values of the covered area of the video stream.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Measurement
     - Selection
     - Select what will be measured.
   * - 256 scale
     - Switch
     - Use the scale 0..256 instead of 0.0..1.0 (default)
   * - Show alpha
     - Switch
     - Show the Alpha channel
   * - Big window
     - Switch
     - Show a bigger version of the video values window
   * - X / Y / X size / Y size
     - Integer
     - Set the position (X / Y) and the size (X size / Y size) of the crosshair (determines the area covered and analyzed)


The following selection items are available:

:guilabel:`Measurement`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - RGB
     - default
   * - Y'PbPr - rec.601
     - 
   * - Y'PbPr - rec.709
     - 
   * - HSV
     - Hue, Saturation, Value
   * - HSL
     - Hue, Saturation, :term:`Luma`

