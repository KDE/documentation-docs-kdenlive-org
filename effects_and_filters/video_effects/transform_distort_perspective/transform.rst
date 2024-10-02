.. meta::

   :description: Kdenlive Video Effects - Transform 
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, transform

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Roger (https://userbase.kde.org/User:Roger)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |rotate| replace:: on the **rotate** icon

Transform
=========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-transform.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-transform

.. sidebar:: |kdenlive-show-video| Transform

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      qtblend
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter allows transformation and compositing of the clip at the same time. It can be :ref:`controlled directly on the monitor <ui-monitors_effect_direct_control>`.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Compositing
     - Selection
     - Defines which composition operation will be performed. See below for available options.
   * - Distort
     - Switch
     - If checked, allows the non-uniform stretching of the clip
   * - Rotate from center
     - Switch
     - If checked, process the rotation from center, otherwise from top left corner
   * - X / Y / W / H / Size
     - Various
     - This is where the action is for the transformation
   * - Rotation
     - Integer
     - Angle for rotation. Clicking |rotate| increments the value by 90 degrees. After reaching 360 it wraps to -360 and continues counting up with each click.

The following selection items are available:

:guilabel:`Compositing`\ [1]_

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - Alpha blend
     - This is the default attribute which specifies no blending. The blending formula simply selects the source color.
   * - Plus
     - 
   * - Xor
     - 
   * - Multiply
     - The source color is multiplied by the destination color and replaces the destination. The resultant color is always at least as dark as either the source or destination color. Multiplying any color with black results in black. Multiplying any color with white preserves the original color.
   * - Screen
     - Multiplies the complements of the backdrop and source color values, then complements the result. The result color is always at least as light as either of the two constituent colors. Screening any color with white produces white; screening with black leaves the original color unchanged. The effect is similar to projecting multiple photographic slides simultaneously onto a single screen.
   * - Overlay
     - Multiplies or screens the colors, depending on the backdrop color value. Source colors overlay the backdrop while preserving its highlights and shadows. The backdrop color is not replaced but is mixed with the source color to reflect the lightness or darkness of the backdrop.
   * - Darken
     - Selects the darker of the backdrop and source colors. The backdrop is replaced with the source where the source is darker; otherwise, it is left unchanged.
   * - Lighten
     - Selects the lighter of the backdrop and source colors. The backdrop is replaced with the source where the source is lighter; otherwise, it is left unchanged.
   * - Color dodge
     - Brightens the backdrop color to reflect the source color. Painting with black produces no changes.
   * - Color burn
     - Darkens the backdrop color to reflect the source color. Painting with white produces no change.
   * - Hard light
     - Multiplies or screens the colors, depending on the source color value. The effect is similar to shining a harsh spotlight on the backdrop.
   * - Soft light
     - Darkens or lightens the colors, depending on the source color value. The effect is similar to shining a diffused spotlight on the backdrop.
   * - Difference
     - Subtracts the darker of the two constituent colors from the lighter color. Painting with white inverts the backdrop color; painting with black produces no change.
   * - Exclusion
     - Produces an effect similar to that of the Difference mode but lower in contrast. Painting with white inverts the backdrop color; painting with black produces no change.
   * - Bitwise or
     - 
   * - Bitwise and
     - 
   * - Bitwise xor
     - 
   * - Bitwise nor
     - 
   * - Bitwise nand
     - 
   * - Bitwise not xor
     - 
   * - Destination in
     - 
   * - Destination out
     - 

:Bitwise:
 The top track's alpha controls interpolation between the lower track and the combined tracks

:Destination:
 Can be used as a mask where overlapping non transparent pixels are drawn or not

----

.. |blending_modes| raw:: html

   <a href="https://www.w3.org/TR/compositing-1/#blending" target="_blank">blending modes</a>


.. [1] For more details see this W3 paper on |blending_modes|


.. **Examples of compositing options:**

   .. image:: /images/effects_and_compositions/kdenlive2304_effects-transform_compositions_1.webp
   :align: left
   :alt: kdenlive2304_effects-transform_compositions_1

   .. image:: /images/effects_and_compositions/kdenlive2304_effects-transform_compositions_2.webp
   :align: left
   :alt: kdenlive2304_effects-transform_compositions_2


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