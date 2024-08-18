.. meta::

   :description: Kdenlive Video Effects - Soft Glow
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, soft glow

.. metadata-placeholder

   :authors: - Roger (https://userbase.kde.org/User:Roger)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Soft Glow
=========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-soft_glow.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-soft_glow

.. sidebar:: |kdenlive-show-video| Soft Glow

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      softglow
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter creates a soft glow effect on highlights.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Blend mode
     - Selection
     - Defines how to blend highlight blur with input image
   * - Blur of the glow
     - Float
     - Set the blurriness of the glow
   * - Brightness
     - Float
     - Set the brightness of highlight areas
   * - Sharpness
     - Float
     - Set the sharpness of highlight areas

The following selection items are available:

:guilabel:`Blend mode`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Screen
     - default
   * - Overlay
     - 
   * - Add
     - 
