.. meta::

   :description: Kdenlive Video Effects - Contrast Adaptive Sharpen (CAS)
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, blur and sharpen, contrast adaptive sharpen, CAS

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Contrast Adaptive Sharpen (CAS)
===============================

.. figure:: /images/effects_and_compositions/effects-CAS-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-CAS-2504.webp

.. sidebar:: |kdenlive-show-video| Contrast Adaptive Sharpen (CAS)

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      avfilter
   :**Source filter**:
      cas
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

Helps increase visual quality by providing natural sharpness without artifacts.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Planes 
     - Selection
     - Sets the color space plane the effect is applied to
   * - Strength
     - Float
     - Set the sharpening strength. Range is from 0.000 to 1.000, default is 0.000.

The following selection items are available:

:guilabel:`Planes`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Alpha
     - Alpha channel
   * - Y
     - Luminance
   * - U
     - Chroma (U plane)
   * - V
     - Chroma (V plane)
   * - Red
     - Red channel
   * - Green
     - Green channel
   * - Blue
     - Blue channel
   * - All
     - All planes will be affected by the blur amount (default)
 
