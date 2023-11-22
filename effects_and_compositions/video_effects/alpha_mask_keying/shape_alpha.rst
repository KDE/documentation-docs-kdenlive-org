.. meta::

   :description: Kdenlive Video Effects - Shape Alpha
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, alpha, mask, keying, shape

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Shape Alpha
===========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-shape_alpha.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-shape_alpha

.. sidebar:: |kdenlive-show-video| Shape Alpha

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      MLT
   :**Source filter**:
      shape
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect creates an alpha channel (transparency) based on a file (e.g. PNG with alpha, PGM with :term:`luma` information).


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 30 20 50
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Image or video resource
     - File Selection
     - Select the file (image or video) to be used as the mask
   * - Threshold
     - Percentage
     - Sets the threshold for making opaqueness and transparency. Values below the value are made opaque, values above transparent.
   * - Softness
     - Float
     - When using Threshold determines how soft to make the edge around the threshold. Similar to :abbr:`feathering (Smoothing or blurring the edges of a feature)`. 0.0 means no softness (hard edge), 1.0 means very soft (default is 0.10).
   * - Invert
     - Switch
     - Invert the alpha channel
   * - Use Luma
     - Switch
     - Use the Luma information instead of the alpha channel
   * - Use Threshold
     - Switch
     - Use the Threshold value


.. rubric:: Notes

You can use a static image file or a video for animated masks


.. rubric:: Examples

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

This is an example for how the Shape Alpha effect looks like when using a :file:`PGM` image file with :term:`Luma`:

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-shape_alpha_result.webp
   :alt: kdenlive2304_effects-shape_alpha_result

   Shape Alpha effect applied
