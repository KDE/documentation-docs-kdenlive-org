.. meta::

   :description: Kdenlive Video Effects - Sharp/Unsharp
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, blur and sharpen, sharp, unsharp

   :authors: - Bernd Jordan

   :license: Creative Commons License SA 4.0


Sharp/Unsharp
=============

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-sharp_unsharp.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-sharp_unsharp

.. sidebar:: |kdenlive-show-video| Sharp/Unsharp

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      unsharp
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect is used to blur or sharpen a clip.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - | Luma
       | Chroma horizontal matrix
     - Integer
     - Set the matrix horizontal size. Odd integer between 3 and 23, default is 5
   * - | Luma
       | Chroma vertical matrix
     - Integer
     - Set the matrix vertical size. Odd integer between 3 and 23, default is 5
   * - | Luma
       | Chroma Strength
     - Float
     - Floating point number between -2.00 (blurry) and 5.00 (sharp). Reasonable values are between -1.5 and 1.5

