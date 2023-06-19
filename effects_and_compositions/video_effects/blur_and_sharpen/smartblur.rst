.. metadata-placeholder

   :authors: - Bernd Jordan

   :license: Creative Commons License SA 4.0

.. _effects-smartblur:

Smartblur
=========

This effect blurs the clip without impacting the outlines.

This effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effect_smartblur.webp
   :align: left
   :width: 400px
   :figwidth: 400px
   :alt: kdenlive2304_effect_smartblur

   Smartblur effect

* **Luma Radius** - The option value must be a float number in the range [0.1,5.0] that specifies the variance of the gaussian filter used to blur the image (slower if larger). Default value is 1.0.

* **Luma Strength** - The option value must be a float number in the range [-1.0,1.0] that configures the blurring. A value included in [0.0,1.0] will blur the image whereas a value included in [-1.0,0.0] will sharpen the image. Default value is 1.0.

* **Luma Threshold** - Used as a coefficient to determine whether a pixel should be blurred or not. The option value must be an integer in the range [-30,30]. A value of 0 will filter all the image, a value included in [0,30] will filter flat areas and a value included in [-30,0] will filter edges. Default value is 0.

* **Chroma Radius** - Same as Luma Radius. Default value is what is defined for Luma Radius.

* **Chroma Strength** - Same as Luma Strength. Default value is what is defined for Luma Strength.

* **Chroma Threshold** - Same as Luma Threshold. Default value is what is defined for Luma Threshold.
