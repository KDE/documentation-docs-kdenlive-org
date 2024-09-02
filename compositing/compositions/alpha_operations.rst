.. meta::
   :description: Kdenlive Documentation - Compositing: Compositions Alpha Operations
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, compositing, composition, compositions, alpha, operations

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0



.. _compositions-alpha_operations:

Alpha Operations
----------------

The **Alpha Operations** composition types require an alpha channel in the clips on the blend and base track. If the clips do not have an :doc:`alpha channel </compositing/alpha_channels>`, you can add one by using effects from the :doc:`/effects_and_filters/video_effects/alpha_mask_keying` effects category.

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/compositions-alpha_ops-timeline.gif
      :width: 360px
      :figwidth: 360px
      :align: left

      Changing the composition type **Alpha operation**

   You can change the **Alpha Operation** by selecting from the :guilabel:`Composition Type` drop-down list.

.. rst-class:: clear-both


For this comparison, :doc:`title clips </titles_and_graphics/titles/titles>` were used for the orange square on the blend track, and for a blue circle in the base track.

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 30 30 40
   :class: table-wrap

   * - Composition Type
     - Example
     - Notes
   * - Default composite
     - .. image:: /images/effects_and_compositions/composition_method-alpha_baseline.webp
     - The square on the upper track (blend track) covers part of the circle on the lower track (base track)
   * - Alpha ATOP
     - .. image:: /images/effects_and_compositions/composition_method-alpha_atop.webp
     - Draw a pixel from the base layer on top of the blend layer if both layers have a non-alpha pixel (|frei0r.alphaatop|)
   * - Alpha IN
     - .. image:: /images/effects_and_compositions/composition_method-alpha_in.webp
     - Draw a pixel from the base layer only where both layers have a non-alpha pixel. This is the alpha equivalent of clipping. (|frei0r.alphain|)
   * - Alpha OUT
     - .. image:: /images/effects_and_compositions/composition_method-alpha_out.webp
     - Draw an alpha pixel only where both layers have a non-alpha pixel, otherwise draw the pixel from the base layer. This is the alpha equivalent of clipping. (|frei0r.alphaout|)
   * - Alpha OVER
     - .. image:: /images/effects_and_compositions/composition_method-alpha_over.webp
     - Overlay the blend layer with the base layer (|frei0r.alphaover|)
   * - Alpha XOR
     - .. image:: /images/effects_and_compositions/composition_method-alpha_xor.webp
     - Draw a pixel only where either layer has a pixel, and no pixel (alpha) where both layers have a pixel (|frei0r.alphaxor|)


.. ===========================================================================
   Link listcompositing/compositions.rst

.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Compositions
   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. |frei0r.alphaatop| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-alphaatop/" target="_blank">frei0r.alphaatop</a>

.. |frei0r.alphain| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-alphain/" target="_blank">frei0r.alphain</a>

.. |frei0r.alphaout| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-alphaout/" target="_blank">frei0r.alphaout</a>

.. |frei0r.alphaover| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-alphaover/" target="_blank">frei0r.alphaover</a>

.. |frei0r.alphaxor| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-alphaxor/" target="_blank">frei0r.alphaxor</a>
