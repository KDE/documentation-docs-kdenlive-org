.. meta::

   :description: Do your first steps with Kdenlive video editor, using the color correct effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, color correct

   :authors: - Bernd Jordan

   :license: Creative Commons License SA 4.0

.. _effects-color_correct:

Color Correct
=============

This effect/filter adjusts the color white balance selectively for blacks and whites. This filter operates in YUV color space.

This effect has keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-color_correct.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-color_correct

   Color Correct effect

* **Analyze mode** - If set to anything other than *manual* it will analyze every frame and use derived parameters for filtering the output frame. Possible values are *manual*, *average*, *minmax* and *median*. Default is *manual*.

* **Red shadow spot** - Set the red shadow spot. Default is 0.0. Allowed range is from -1.0 to 1.0.

* **Blue shadow spot** - Set the blue shadow spot. Default is 0.0. Allowed range is from -1.0 to 1.0.

* **Red highlight spot** - Set the red highlight spot. Default is 0.0. Allowed range is from -1.0 to 1.0.

* **Blue highlight spot** - Set the blue highlight spot. Default is 0.0. Allowed range is from -1.0 to 1.0.

* **Saturation** - Set the amount of sturation. Default value is 0.0. Allowed range is from -3.0. to 3.0. Default value is 1.0.
