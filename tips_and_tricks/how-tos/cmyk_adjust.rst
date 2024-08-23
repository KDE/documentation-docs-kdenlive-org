.. meta::
   :description: Kdenlive Tips & Tricks - CMYK Adjust
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, color correction, useful information, tutorial, how-to, white balance (LMS)

.. metadata-placeholder

   :authors: - micha  (https://discuss.kde.org/u/micha)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


CMYK Adjust
===========

This how-to is about applying :term:`CMYK` correction to specific color ranges using the :doc:`/effects_and_filters/video_effects/color_image_correction/CMYK_adjust` effect.

:term:`Color Correction` is an important process when dealing with footage that was shot with different equipment or in different lighting conditions. See also the how-to about :doc:`white balance </tips_and_tricks/how-tos/tutorial-white_balance_lms>`. CMYK Adjust is an interesting filter for some special tasks in color correction.

Naturally, digital video footage uses the :abbr:`RGB (Red Green Blue)` :term:`color space`. But :doc:`/effects_and_filters/video_effects/color_image_correction/CMYK_adjust` in addition has parameters (or sliders) for Cyans, Magentas, Yellows, and Whites, Neutrals and Blacks.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-cmyk_adjust.webp
   :align: left
   :width: 350px
   :alt: kdenlive2304_effects-cmyk_adjust.webp

   CMYK Adjust effect

The effect works by changing the color intensity (or saturation) of the color individually with the respective slider - all the other colors are not affected. For example, you can increase or decrease the intensity (or saturation) of the color *red* using the slider :guilabel:`Reds` without changing other pixels (i.e. those parts of the image that are not red). Most important is that neutral color tones remain unchanged. So this effect/filter is very useful for reducing redishness in skin tones.

Using the :guilabel:`Whites` slider you can make bright color tones more redish (move the color tone more toward red-magenta) or blueish (move the color tone more towards blue-cyan). The same applies for :guilabel:`Neutrals` to change the mid-tones and :guilabel:`Blacks` for the dark tones.

The effect works like a mask for a specific color tone but limited to one of the six basic colors. The advantage is that you do not have to create a precise selection and that you can directly change the intensity (saturation).

.. attention:: When moving the :guilabel:`Reds`, :guilabel:`Yellows` or :guilabel:`Magentas` slider to the right (increases the value) the intensity (saturation) decreases; moving it to the left (decreasing the value) increases the intensity (saturation). All other sliders work as one might expect: higher values increase intensity (saturation).