.. meta::

   :description: Kdenlive Video Effects - Directional Blur (dblur)
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, blur and sharpen, dblur, directional blur

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0



Directional Blur (Dblur)
========================

.. figure:: /images/effects_and_compositions/effects-dblur-2412.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-dblur_2412

.. sidebar:: |kdenlive-show-video| Directional Blur

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
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
   * - Planes to filter
     - List
     - Sets the color space plane the effect is applied to (see below)
   * - Angle
     - Float
     - Sets the angle for the direction. Range is from 0.0 to 360.0, default is 45.0.
   * - Radius
     - Integer
     - Sets the radius for the direction. Range is from 0 to 8192, default is 5.

:guilabel:`Planes to filter`

.. list-table::
   :width: 100%
   :widths: 25 75
   :class: table-wrap

   * - Alpha
     - Alpha channel
   * - Luminance (Y plane)
     - 
   * - Chroma (U plane)
     - 
   * - Chroma (V plane)
     - 
   * - Red
     - Red channel
   * - Green
     - Green channel
   * - Blue
     - Blue channel
   * - All
     - All planes will be affected by the blur amount (default)

.. hint:: Using the slider or mouse wheel for :guilabel:`av.radius` results in large fixed increments and therefore overly strong blur effects. It is recommended to use direct input for better results.