.. meta::

   :description: Kdenlive Video Effects - Color Overlay
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, color overlay, colorize

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Color Overlay
=============

.. figure:: /images/effects_and_compositions/effects-color_overlay-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-color_overlay-2504.webp

.. sidebar:: |kdenlive-show-video| Color Overlay

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      avfilter
   :**Source filter**:
      colorize
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter overlays a solid color on the video stream.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Hue
     - Float
     - Set the color :term:`hue`. Allowed values are from 0 to 360, default value is 0.
   * - Saturation
     - Float
     - Set the color :term:`saturation`. Allowed values are from 0 to 1, default value is 0.5.
   * - Lightness
     - Float
     - Set the color :term:`lightness`. Allowed values are from 0 to 1, default value is 0.5.
   * - Mix
     - Float
     - Set the mix of source lightness. Allowed values are from 0.0 to 1.0, default value is 1.0.
