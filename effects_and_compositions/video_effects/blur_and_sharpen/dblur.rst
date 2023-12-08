.. meta::

   :description: Kdenlive Video Effects - Directional Blur (dblur)
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, blur and sharpen, dblur, directional blur

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0



Directional Blur (Dblur)
========================

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-dblur.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-dblur

.. sidebar:: |kdenlive-show-video| Directional Blur

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      dblur
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect applies a directional blur to the clip.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - av.angle
     - Float
     - Sets the angle for the direction. Range is from 0.000 to 360.000, default is 0.000.
   * - av.radius
     - Float
     - Sets the radius for the direction. Range is from 5.000 to 8192.000, default is 5.000.
   * - av.planes
     - Integer
     - Sets the color space plane the effect is applied to (see below)

:guilabel:`Planes`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - 0/8 - Alpha
     - Alpha channel
   * - 1/9 - Y
     - Luminance
   * - 2/10 - U
     - Chroma (U plane)
   * - 3/11 - V
     - Chroma (V plane)
   * - 4/12 - Red
     - Red channel
   * - 5/13 - Green
     - Green channel
   * - 6/14 - Blue
     - Blue channel
   * - 7/15 - All
     - All planes will be affected by the blur amount (default)

.. hint:: Using the slider or mouse wheel for :guilabel:`av.radius` results in large fixed increments and therefore overly strong blur effects. It is recommended to use direct input for better results.