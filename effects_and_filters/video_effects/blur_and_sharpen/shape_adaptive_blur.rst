.. meta::

   :description: Kdenlive Video Effects - Planes Blur
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, blur and sharpen, shape adaptive blur

   :authors: - Bernd Jordan

   :license: Creative Commons License SA 4.0


Shape Adaptive Blur
===================

.. figure:: /images/effects_and_compositions/effects-shape_adaptive_blur-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-shape_adaptive_blur-2504.webp

.. sidebar:: |kdenlive-show-video| Shape Adaptive Blur

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      sab
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect blurs the clip while trying to keeping shape (edge).


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 10 65
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - | Luma
       | Chroma Radius
     - | Float
       | Integer
     - Set blur filter strength. Range 0.1 - 4.0, default is 1.0 for :guilabel:`Luma`, and 0 (no blurring) for :guilabel:`Chroma`. The higher the value the more blurring, and slower processing.
   * - | Luma
       | Chroma pre-filter radius
     - Float
     - Set pre-filter radius. Range 0.1-2.0, default value is 1.0.
   * - | Luma
       | Chroma Strength
     - | Float
       | Integer
     - Set maximum difference between pixels to still be considered. Range 0.1-100.0, default value is 1.0 for :guilabel:`Luma`, and 0 (no blurring) for :guilabel:`Chroma`.
