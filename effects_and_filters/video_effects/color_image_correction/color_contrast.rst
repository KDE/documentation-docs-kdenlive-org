.. meta::

   :description: Kdenlive Video Effects - Color Contrast
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, color contrast

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Color Contrast
==============

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-color_contrast.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-color_contrast

.. sidebar:: |kdenlive-show-video| Color Contrast

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      avfilter
   :**Source filter**:
      colorcontrast
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter adjusts the color contrast between RGB components.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 30 10 60
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Red-Cyan Contrast
     - Float
     - Set the red-cyan contrast. Default is 0.0. Allowed range is from -1.0 to 1.0.
   * - Green-Magenta Contrast
     - Float
     - Set the green-magenta contrast. Default is 0.0. Allowed range is from -1.0 to 1.0.
   * - Blue-Yellow Contrast
     - Float
     - Set the blue-yellow contrast. Default is 0.0. Allowed range is from -1.0 to 1.0.
   * - Red-Cyan Weight
     - Float
     - Set the weight for red-cyan option value. Default value is 0.0. Allowed range is from 0.0 to 1.0. If all weights are 0.0 filtering is disabled.
   * - Green-Magenta Weight
     - Float
     - Set the weight for green-magenta option value. Default value is 0.0. Allowed range is from 0.0 to 1.0. If all weights are 0.0 filtering is disabled.
   * - Blue-Yellow Weight
     - Float
     - Set the weight for blue-yellow option value. Default value is 0.0. Allowed range is from 0.0 to 1.0. If all weights are 0.0 filtering is disabled.
   * - Preserving lightness
     - Float
     - Set the amount of preserving lightness. Default value is 0.0. Allowed range is from 0.0 to 1.0.
