.. metadata-placeholder

   :authors: - Bernd Jordan

   :license: Creative Commons License SA 4.0


.. _effects-shape_alpha:

Shape Alpha
===========

This effect creates an alpha channel (transparency) based on a file (e.g. PNG with alpha, PGM with luma information)

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-shape_alpha.webp
   :align: left
   :width: 400px
   :figwidth: 400px
   :alt: kdenlive2304_effects-shape_alpha

   Shape Alpha effect panel

You can use a static image file or a video for animated masks

.. container:: clear_both

   .. figure:: /images/effects_and_compositions/kdenlive2304_effects-shape_alpha_resource.webp
      :align: left
      :width: 400px
      :figwidth: 400px
      :alt: kdenlive2304_effects-shape_alpha_resource

      Shape Alpha selecting the resource

   Select the file you want to use for the mask

.. container:: clear_both

   .. figure:: /images/effects_and_compositions/kdenlive2304_effects-shape_alpha_error.webp
      :align: left
      :width: 400px
      :figwidth: 400px
      :alt: kdenlive2304_effects-shape_alpha_error

      Shape Alpha error message in case no alpha

   If the selected image or video file does not have an alpha channel, Kdenlive displays this warning message

.. container:: clear_both

   .. figure:: /images/effects_and_compositions/kdenlive2304_effects-shape_alpha_luma.webp
      :align: left
      :width: 400px
      :figwidth: 400px
      :alt: kdenlive2304_effects-shape_alpha_luma

      Shape Alpha using Luma information

   Instead of the alpha channel you can use the Luma information in the file

.. rst-class:: clear_both

This is an example for how the Shape Alpha effect looks like when using an :file:`PGM` with Luma:

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-shape_alpha_result.webp
   :alt: kdenlive2304_effects-shape_alpha_result

   Shape Alpha effect applied
