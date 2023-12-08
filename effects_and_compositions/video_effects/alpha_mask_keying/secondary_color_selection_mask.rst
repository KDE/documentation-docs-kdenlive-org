.. meta::

   :description: Kdenlive Video Effects - Secondary Color Correction Area Selection (Mask)
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, alpha, mask, keying, secondary, color correction, area selection

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Secondary Color Correction Area Selection (Mask)
================================================

.. figure:: /images/effects_and_compositions/kdenlive2308_effects-sec_color_corr_area_select_mask.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2308_effects-sec_color_corr_area_select_mask

.. sidebar:: |kdenlive-show-video| Secondary Color Correction Area Selection (Mask)

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      mask_start
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This filter takes a snapshot of the frame before it selects the specified color. Use it together with the :doc:`Mask Apply </effects_and_compositions/video_effects/alpha_mask_keying/mask_apply>` effect, that uses a transition to composite the current frame's image over the snapshot. The typical use case is to add effects in the following sequence:

 Secondary Color Correction Area Selection Mask (this effect) -->  zero or more effects (e.g. :doc:`Blur </effects_and_compositions/video_effects/blur_and_sharpen/gaussian_blur>`, :doc:`Cartoon </effects_and_compositions/video_effects/stylize/cartoon>`) -->  Mask Apply

