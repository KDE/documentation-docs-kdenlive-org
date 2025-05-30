.. meta::

   :description: Kdenlive Video Effects - Rotoscoping (Mask)
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, alpha, mask, keying, rotoscoping, mask

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Rotoscoping (Mask)
==================

.. figure:: /images/effects_and_compositions/effects-rotoscoping_mask-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-rotoscoping_mask-2504.webp

.. sidebar:: |kdenlive-show-video| Rotoscoping (Mask)

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      rotoscoping
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This filter takes a snapshot of the frame before it draws the :doc:`Rotoscoping </effects_and_filters/video_effects/alpha_mask_keying/rotoscoping>` region/mask into the alpha channel. Use it together with the :doc:`Mask Apply </effects_and_filters/video_effects/alpha_mask_keying/mask_apply>` effect, that uses a transition to composite the current frame's image over the snapshot. The typical use case is to add effects in the following sequence:

 Rotoscoping Mask (this effect) -->  zero or more effects (e.g. :doc:`Blur </effects_and_filters/video_effects/blur_and_sharpen/gaussian_blur>`, :doc:`Cartoon </effects_and_filters/video_effects/stylize/cartoon>`) -->  Mask Apply


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 10 65
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Mode
     - Selection
     - Defines the channel to apply rotoscoping to
   * - Alpha Operation
     - Selection
     - Determines how compositing is done
   * - Invert
     - Switch
     - Inverts the rotoscoping selection
   * - Feathering width
     - Integer
     - Determines the amount of :abbr:`feathering (Smoothing or blurring the edges of a feature)`. Default is 0 (no feathering).
   * - Feathering passes
     - Integer
     - Sets the number of passes. The more passes the finer and more accurate the :abbr:`feathering (Smoothing or blurring the edges of a feature)` will be. Default is 1.

The following selection items are available:

:guilabel:`Mode`

.. list-table::
   :width: 100%
   :widths: 25 75
   :class: table-simple

   * - Alpha
     - The rotoscoped area will be the alpha channel (default)
   * - Luma
     - 
   * - RGB
     - 

:guilabel:`Alpha Operation`

.. list-table::
   :width: 100%
   :widths: 25 75
   :class: table-simple

   * - Write on clear
     - (default)
   * - Maximum
     - 
   * - Minimum
     - 
   * - Add
     - 
   * - Subtract
     - 


.. rubric:: Notes

See the :doc:`Rotoscoping </effects_and_filters/video_effects/alpha_mask_keying/rotoscoping>` effect for more details and examples.
