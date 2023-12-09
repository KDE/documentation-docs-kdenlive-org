.. meta::

   :description: Kdenlive Video Effects - Cairogradient
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, generate, cairogradient, gradient

.. metadata-placeholders

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Cairogradient
=============

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-cairogradient.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: denlive2304_effects-cairogradient

.. sidebar:: |kdenlive-show-video| Cairogradient

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      cairogradient
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter draws a gradient on top of the image source.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Pattern
     - Selection
     - Determines the pattern or direction of the gradient
   * - Blend Mode
     - Selection
     - Determines the mode used to composite  gradient and image source
   * - Start Color
     - Picker
     - First color of the gradient
   * - Start Opacity
     - Float
     - Opacity of the first color of the gradient
   * - End Color
     - Picker
     - Second color of the gradient
   * - End Opacity
     - Float
     - Opacity of the second color of the gradient
   * - Start / End X
     - Float
     - X position of the start and end point of the gradient
   * - Start / End Y
     - Float
     - Y position of the start and end point of the gradient
   * - Offset
     - Float
     - Position of the first color in the line connecting gradient ends. Really useful only for **radial** :guilabel:`Pattern`.

The following selection items are available:

:guilabel:`Pattern`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - Linear
     - Default
   * - Radial
     - 

:guilabel:`Blend Mode`\ [1]_

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - normal
     - This is the default attribute which specifies no blending. The blending formula simply selects the source color.
   * - add
     - 
   * - saturate
     - 
   * - multiply
     - The source color is multiplied by the destination color and replaces the destination. The resultant color is always at least as dark as either the source or destination color. Multiplying any color with black results in black. Multiplying any color with white preserves the original color.
   * - screen
     - Multiplies the complements of the backdrop and source color values, then complements the result. The result color is always at least as light as either of the two constituent colors. Screening any color with white produces white; screening with black leaves the original color unchanged. The effect is similar to projecting multiple photographic slides simultaneously onto a single screen.
   * - overlay
     - Multiplies or screens the colors, depending on the backdrop color value. Source colors overlay the backdrop while preserving its highlights and shadows. The backdrop color is not replaced but is mixed with the source color to reflect the lightness or darkness of the backdrop.
   * - darken
     - Selects the darker of the backdrop and source colors. The backdrop is replaced with the source where the source is darker; otherwise, it is left unchanged.
   * - lighten
     - Selects the lighter of the backdrop and source colors. The backdrop is replaced with the source where the source is lighter; otherwise, it is left unchanged.
   * - colordodge
     - Brightens the backdrop color to reflect the source color. Painting with black produces no changes.
   * - colorburn
     - Darkens the backdrop color to reflect the source color. Painting with white produces no change.
   * - hardlight
     - Multiplies or screens the colors, depending on the source color value. The effect is similar to shining a harsh spotlight on the backdrop.
   * - softlight
     - Darkens or lightens the colors, depending on the source color value. The effect is similar to shining a diffused spotlight on the backdrop.
   * - difference
     - Subtracts the darker of the two constituent colors from the lighter color. Painting with white inverts the backdrop color; painting with black produces no change.
   * - exclusion
     - Produces an effect similar to that of the Difference mode but lower in contrast. Painting with white inverts the backdrop color; painting with black produces no change.
   * - hslhue
     - Creates a color with the hue of the source color and the saturation and luminosity of the backdrop color.
   * - hslsaturation
     - Creates a color with the saturation of the source color and the hue and luminosity of the backdrop color. Painting with this mode in an area of the backdrop that is a pure gray (no saturation) produces no change.
   * - hslcolor
     - Creates a color with the hue and saturation of the source color and the luminosity of the backdrop color. This preserves the gray levels of the backdrop and is useful for coloring monochrome images or tinting color images.
   * - hslluminosity
     - Creates a color with the luminosity of the source color and the hue and saturation of the backdrop color. This produces an inverse effect to that of the Color mode.


----

.. |blending_modes| raw:: html

   <a href="https://www.w3.org/TR/compositing-1/#blending" target="_blank">blending modes</a>


.. [1] For more details see this W3 paper on |blending_modes|


.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Icons used here (remove comment indent to enable them for this document)
   
   .. |linux| image:: /images/icons/linux.png
   :width: 14px
   :alt: Linux
   :class: no-scaled-link

   .. |appimage| image:: /images/icons/kdenlive-appimage_3.svg
   :width: 14px
   :alt: appimage
   :class: no-scaled-link

   .. |windows| image:: /images/icons/windows.png
   :width: 14px
   :alt: Windows
   :class: no-scaled-link

   .. |apple| image:: /images/icons/apple.png
   :width: 14px
   :alt: MacOS
   :class: no-scaled-link