.. meta::
   :description: Kdenlive Documentation - Compositing: Blending Modes
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, compositing, blending modes

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _compositing-blending_modes:

==============
Blending Modes
==============

Blending modes (or **blend modes** or **mixing modes**) are also called **Composition Type** in Kdenlive. They determine how two images are blended together. The default blending mode is simply to cover whatever is in the lower track by whatever is in the upper track, while taking any :ref:`alpha channel <compositing-alpha_channels>` information into account.

In this section, we are using the :guilabel:`Composition Type` **Cairo Blend** to explain the different blend modes.

Compositing/blending needs at least two tracks: The top track or "layer", also called the *blend layer* or *active layer*; and the "bottom" track or layer, also called the *base layer*. In a blending composition, the *blend layer* is always the track where the composition originates, whereas the *base layer* can be specified with the :guilabel:`Composition track`. By default it is set to :guilabel:`Automatic` which uses the track immediately below.

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/cairo_blend-blend_mode.gif
     :width: 360px
     :figwidth: 360px
     :align: left

     Selecting the composition track and blend mode

   If you want to blend with a different base layer, select the correct one from the :guilabel:`Composition track`.
   
   Select the blend mode by clicking on the :guilabel:`Blend mode` drop-down list.

   Blending can be controlled and keyframed by using the :guilabel:`Opacity` slider.

.. rst-class:: clear-both

To better understand how blending modes work, read the :doc:`/tips_and_tricks/index` :doc:`/tips_and_tricks/how-tos/index` sections about :doc:`/tips_and_tricks/how-tos/lift_gamma_gain`, :doc:`White Balance </tips_and_tricks/how-tos/tutorial-white_balance_lms>`, and familiarize yourself with the :doc:`/effects_and_filters/video_effects/color_image_correction/color_levels` effect.

Blending Modes can be grouped by their result:

* Normal_
* Darker_
* Lighter_
* Contrast_
* Comparative_
* Color_

.. _blending_modes-normal:

Normal
======

This is the standard blending mode. The blend layer simply covers everything in the base layer, except if there is an alpha channel in the blend layer.

.. _blending_modes-dissolve:

.. Dissolve
  ========

  While this is one of the compositions mostly used for a transition, it is considered a blend mode. It takes random pixels from both layers, where most pixels are taken from the blend layer if it has a higher opacity than the base layer, while most pixels are taken from the base layer if it has a lower opacity than the blend layer. Since there will be no anti-aliasing, the resulting image may look grainy and harsh.


.. _blending_modes-group_darker:

Darker
======

The following blending modes all darken or amplify dark colors in the image:

:Darken:
   Keeps the darkest colors between the blend and base layers.

:Multiply:
   Keeps the darker colors of the blend layer and makes light colors less opaque. This is done by taking the :abbr:`RGB(Red Green Blue)` channel values from 0 to 1 of the pixel in the blend layer and multiplying it with the values of the corresponding pixel in the base layer. The resulting color is always darker, except for where it is pure white, since each value is less than 1.

:Color Burn:
   The color from the blend layer is used to darken the base layer, and increases the contrast between the two. This is done by dividing the inverted base layer by the blend layer, and then inverting the result. Blending with white produces no change. Note that when the blend layer is a homogeneous color, this effect is equivalent to changing the black point to the inverted color.

.. list-table:: 
   :widths: 33 33 33
   :class: table-wrap

   * - .. figure:: /images/effects_and_compositions/blending_modes-darken.webp
          :width: 100%
          :align: center

          Darken

     - .. figure:: /images/effects_and_compositions/blending_modes-multiply.webp
          :width: 100%
          :align: center

          Multiply
          
     - .. figure:: /images/effects_and_compositions/blending_modes-color_burn.webp
          :width: 100%
          :align: center

          Color Burn


.. _blending_modes-group_lighter:

Lighter
=======

The following blending modes lighten or amplify light colors in the image:

:Add / Addition:
   The color values of both layers are simply added (hence the name). Since this always produces the same or lighter colors than the input (base layer) it is also known as *Plus Lighter*.

:Lighten:
   Keeps the lightest colors between the blend and base layers. It will only lighten of the blend layer is lighter than the brightness (or luminance) of the base layer.

:Screen:
   In this blending mode, the color values of the image of both layers are inverted, multiplied, and then inverted again. This is the opposite of **Multiply**: Wherever either layer was darker than white, the composite is brighter.

:Color Dodge:
   This blending mode divides the base layer by the inverted blend layer. It lightens the base layer depending on the value of the blend layer: the brighter the blend layer, the more it affects the base layer. If you use white in the blend layer, the color in the base layer will become white; using black in the blend layer does not change the base layer. Note that when the blend layer is a homogeneous color, this blending mode essentially changes the output black point to this color, and (input) white point to the inverted color.

.. list-table:: 
   :widths: 25 25 25 25
   :class: table-wrap

   * - .. figure:: /images/effects_and_compositions/blending_modes-add.webp
          :width: 100%
          :align: center

          Add

     - .. figure:: /images/effects_and_compositions/blending_modes-lighten.webp
          :width: 100%
          :align: center

          Lighten
          
     - .. figure:: /images/effects_and_compositions/blending_modes-screen.webp
          :width: 100%
          :align: center

          Screen
          
     - .. figure:: /images/effects_and_compositions/blending_modes-color_dodge.webp
          :width: 100%
          :align: center

          Color Dodge
 

.. _blending_modes-group_contrast:

Contrast
========

The following blending modes are great for adding depth and dynamics to images by having the two layers play off of each other:

:Overlay:
   This blending mode works like **Multiply** if the base layer is darker, or like **Screen** if it's lighter. In other words: where the base layer is light, the blend layer becomes lighter; where the base layer is dark, the blend layer becomes darker; mid-tones do not affect the blend layer.

:Hard Light:
   This blending mode is a combination of **Multiply** and **Screen**. It works similar to **Overlay** but uses the brightness of the blend layer where **Overlay** uses the base layer.

:Soft Light:
   Similar to **Overlay**, it uses luminance values to either darken or lighten the image.

.. list-table:: 
   :widths: 33 33 33
   :class: table-wrap

   * - .. figure:: /images/effects_and_compositions/blending_modes-overlay.webp
          :width: 100%
          :align: center

          Overlay

     - .. figure:: /images/effects_and_compositions/blending_modes-hard_light.webp
          :width: 100%
          :align: center

          Hard Light
          
     - .. figure:: /images/effects_and_compositions/blending_modes-soft_light.webp
          :width: 100%
          :align: center

          Soft Light


.. _blending_modes-group_comparative:

Comparative
===========

The following blending modes basically invert white or light colors:

:Difference:
   This blending mode subtracts the base layer from the blend layer, or the other way around to avoid negative numbers. Blending with black (:abbr:`RGB(Red Green Blue)` value is 0,0,0) results in no change, whereas blending with white (:abbr:`RGB(Red Green Blue)` value is 255, 255, 255) inverts the picture.
   During the editing process this can be used to verify alignment of images with similar content: is the pixel values are the same, the result is black.

:Exclusion:
   This blending mode is essentially the same as **Difference** but with less contrast as it does not invert mid-tones.

.. list-table:: 
   :widths: 50 50
   :class: table-wrap

   * - .. figure:: /images/effects_and_compositions/blending_modes-difference.webp
          :width: 100%
          :align: center

          Difference

     - .. figure:: /images/effects_and_compositions/blending_modes-exclusion.webp
          :width: 100%
          :align: center

          Exclusion
          

.. _blending_modes-group_color:

Color
=====

The following blending modes play with :term:`hues<hue>`, :term:`saturation`, and brightness (aka :term:`luminance`, hence the acronym HSL):

:HSL hue:
   This blending mode preserves the luma and saturation (:term:`chroma`) of the base layer, while taking the hue of the blend layer.

:HSL saturation:
   This blending mode preserves the luma and hue from the base layer, while adopting the saturation from the blend layer.

:HSL color:
   This blending mode preserves the luma from the base layer, while taking the hue and saturation from the blend layer.

:HSL luminosity:
   This blending mode preserves the hue and saturation from the base layer, while adopting the luma from the blend layer.

.. list-table:: 
   :widths: 25 25 25 25
   :class: table-wrap

   * - .. figure:: /images/effects_and_compositions/blending_modes-hsl_hue.webp
          :width: 100%
          :align: center

          Hue

     - .. figure:: /images/effects_and_compositions/blending_modes-hsl_saturation.webp
          :width: 100%
          :align: center

          Saturation
          
     - .. figure:: /images/effects_and_compositions/blending_modes-hsl_color.webp
          :width: 100%
          :align: center

          Color
          
     - .. figure:: /images/effects_and_compositions/blending_modes-hsl_luminosity.webp
          :width: 100%
          :align: center

          Luminosity

