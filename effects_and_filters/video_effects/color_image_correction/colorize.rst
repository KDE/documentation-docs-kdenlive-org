.. meta::

   :description: Kdenlive Video Effects - Colorize
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, colorize

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Colorize
========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-colorize.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-colorize

.. sidebar:: |kdenlive-show-video| Colorize

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
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

This effect/filter colorizes an image to the selected :term:`hue`, :term:`saturation` and :term:`lightness`.


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
     - Integer
     - Set the color :term:`hue`. Allowed values are from 0 to 360, default value is 0.
   * - Saturation
     - Integer
     - Set the color :term:`saturation`. Allowed values are from 0 to 1, default value is 0.5.
   * - Lightness
     - Integer
     - Set the color :term:`lightness`. Allowed values are from 0 to 1, default value is 0.5.

.. note::
   This effect works similar to the :doc:`/effects_and_filters/video_effects/color_image_correction/color_overlay` effect but produces slightly different results for crispiness and detail.
