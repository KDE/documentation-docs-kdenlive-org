.. meta::

   :description: Kdenlive Video Effects - Sharp/Unsharp
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, blur and sharpen, smartblur

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Smartblur
=========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-smartblur.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-smartblur

.. sidebar:: |kdenlive-show-video| Smartblur

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      smartblur
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect blurs the clip without impacting the outlines.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Luma Radius
     - Float
     - Number in the range [0.1,5.0] that specifies the variance of the gaussian filter used to blur the image (slower if larger). Default value is 1.0.
   * - Luma Strength
     - Float
     - Number in the range [-1.0,1.0] that configures the blurring. A value included in [0.0,1.0] will blur the image whereas a value included in [-1.0,0.0] will sharpen the image. Default value is 1.0.
   * - Luma Threshold
     - Integer
     - Used as a coefficient to determine whether a pixel should be blurred or not. The value must be an integer in the range [-30,30]. A value of 0 will filter all the image, a value included in [0,30] will filter flat areas and a value included in [-30,0] will filter edges. Default value is 0.
   * - Chroma Radius
     - Float
     - Same as Luma Radius. Default value is what is defined for Luma Radius.
   * - Chroma Strength
     - Float
     - Same as Luma Strength. Default value is what is defined for Luma Strength.
   * - Chroma Threshold
     - Integer
     - Same as Luma Threshold. Default value is what is defined for Luma Threshold.
