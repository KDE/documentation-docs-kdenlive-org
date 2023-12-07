.. meta::

   :description: Kdenlive Video Effects - Edge Crop
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, edge crop

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Edge Crop
=========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-edge_crop.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-edge_crop

.. sidebar:: |kdenlive-show-video| Edge Crop

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      MLT
   :**Source filter**:
      crop
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      Yes (see warning)

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter removes pixels from the edges of the video (cropping).

.. note:: 
   This filter is meant to be included as a normalizing filter attached automatically by the loader so that cropping occurs early in the processing stack and can request the full resolution of the source image. Then, a second instance of the filter may be applied to set the parameters of the crop operation.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Top
     - Integer
     - Number of pixels to be removed from the top edge
   * - Left
     - Integer
     - Number of pixels to be removed from the left edge
   * - Bottom
     - Integer
     - Number of pixels to be removed from the bottom edge
   * - Right
     - Integer
     - Number of pixels to be removed from the right edge
   * - Automatic center-crop
     - Switch
     - Whether to automatically crop whatever is needed to fill the output frame and prevent padding
   * - Center balance
     - Integer
     - When center crop is enabled, offset the center point
   * - Use project resolution
     - Switch
     - This is useful for proxy editing. Normally all crop values are expressed in terms of pixels of the source footage, but this option makes them relative to the profile resolution.


.. warning:: 
   As of this writing and in version 23.04 this effect still behaves strangely. The parameter values seem to interfere with each other and it is not possible to have all four sides being cropped. It is either top/bottom or left/right and only the last value entered is applied (and then on both sides). Until this is fixed it is recommended to use the :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/crop_scale_tilt` effect.
