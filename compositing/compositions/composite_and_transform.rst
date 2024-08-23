.. meta::
   :description: Kdenlive Documentation - Compositing: Composition Type "Composite and Transform"
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, compositing, composition type, composite and transform

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _composition-composite_and_transform:

Composite and Transform
=======================

The composition type **Composite and Transform** combines :doc:`/compositing/blending_modes` and a :doc:`Transform </effects_and_filters/video_effects/transform_distort_perspective/transform>` effect. It is not animated by default but has keyframes which gives you fine control over what is happening when. The :guilabel:`Opacity` parameter controls the level of compositing with the selected :guilabel:`Compositing` method.

.. hint:: This is the only composition that gives you :code:`bitwise` and :code:`Destination in` and :code:`Destination out` operations.

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/composition_type-composite_and_transform.webp
     :width: 360px
     :figwidth: 360px
     :align: left

     Settings for the Composite and Transform composition

   Only the parameters below the keyframe ruler can be animated via keyframes. By default, this composition just applies the selected :guilabel:`Compositing` method. You can use the keyframes to move, scale, and rotate the clip. Use :guilabel:`Opacity` to control the amount of compositing.

.. rst-class:: clear-both

This list shows the available :guilabel:`Compositing` methods (see the timeline setup above):

.. list-table:: 
   :header-rows: 1
   :widths: 20 30 50
   :class: table-wrap

   * - Wipe Method
     - Example
     - Notes
   * - Alpha blend
     - .. image:: /images/effects_and_compositions/compositing-alpha_blend.webp
     - A clip with an alpha channel (or an :doc:`alpha mask effect </effects_and_filters/video_effects/alpha_mask_keying>`)\ [1]_ is required. The alpha channel lets show through the clip in the :guilabel:`Composition track`.
   * - Xor
     - .. image:: /images/effects_and_compositions/compositing-destination_out.webp
     - A clip with an alpha channel (or an :doc:`alpha mask effect </effects_and_filters/video_effects/alpha_mask_keying>`)\ [1]_ is required. Has the same effect as the :guilabel:`Compositing` **Destination in**.
   * - Plus
     - .. image:: /images/effects_and_compositions/compositing-plus.webp
     - 
   * - Multiply
     - .. image:: /images/effects_and_compositions/compositing-multiply.webp
     - 
   * - Screen
     - .. image:: /images/effects_and_compositions/compositing-screen.webp
     - 
   * - Overlay
     - .. image:: /images/effects_and_compositions/compositing-overlay.webp
     - 
   * - Darken
     - .. image:: /images/effects_and_compositions/compositing-darken.webp
     - 
   * - Lighten
     - .. image:: /images/effects_and_compositions/compositing-lighten.webp
     - 
   * - Color dodge
     - .. image:: /images/effects_and_compositions/compositing-color_dodge.webp
     - 
   * - Color burn
     - .. image:: /images/effects_and_compositions/compositing-color_burn.webp
     - 
   * - Hard light
     - .. image:: /images/effects_and_compositions/compositing-hard_light.webp
     - 
   * - Soft light
     - .. image:: /images/effects_and_compositions/compositing-soft_light.webp
     - 
   * - Difference
     - .. image:: /images/effects_and_compositions/compositing-difference.webp
     - 
   * - Exclusion
     - .. image:: /images/effects_and_compositions/compositing-exclusion.webp
     - 
   * - Bitwise or
     - .. image:: /images/effects_and_compositions/compositing-bitwise_or.webp
     - 
   * - Bitwise and
     - .. image:: /images/effects_and_compositions/compositing-bitwise_and.webp
     - 
   * - Bitwise xor
     - .. image:: /images/effects_and_compositions/compositing-bitwise_xor.webp
     - 
   * - Bitwise nor
     - .. image:: /images/effects_and_compositions/compositing-bitwise_nor.webp
     - 
   * - Bitwise nand
     - .. image:: /images/effects_and_compositions/compositing-bitwise_nand.webp
     - 
   * - Bitwise not xor
     - .. image:: /images/effects_and_compositions/compositing-bitwise_not_xor.webp
     - 
   * - Destination in
     - .. image:: /images/effects_and_compositions/compositing-destination_in.webp
     - A clip with an alpha channel (or an :doc:`alpha mask effect </effects_and_filters/video_effects/alpha_mask_keying>`) is required. The clip in the :guilabel:`Composition track` is essentially clipped by the alpha channel.
   * - Destination out
     - .. image:: /images/effects_and_compositions/compositing-destination_out.webp
     - A clip with an alpha channel (or an :doc:`alpha mask effect </effects_and_filters/video_effects/alpha_mask_keying>`) is required. The clip in the :guilabel:`Composition track` is essentially clipped by the alpha channel.


----

.. [1] In this context, an alpha mask effect could be any effect from the :doc:`/effects_and_filters/video_effects/alpha_mask_keying` effects category that creates an alpha channel. For example, :doc:`/effects_and_filters/video_effects/alpha_mask_keying/alpha_shapes`, :doc:`/effects_and_filters/video_effects/alpha_mask_keying/chroma_key`, or :doc:`/effects_and_filters/video_effects/alpha_mask_keying/rotoscoping`.