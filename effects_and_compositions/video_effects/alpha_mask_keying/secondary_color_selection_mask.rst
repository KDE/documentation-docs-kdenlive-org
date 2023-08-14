.. metadata-placeholder

   :authors: - Bernd Jordan

   :license: Creative Commons License SA 4.0


.. _effects-sec_col_cor_area_selection_mask:

Secondary Color Correction Area Selection (Mask)
================================================

This filter makes a snapshot of the frame before it selects the specified color. Use it together with the :ref:`Mask Apply <effects-mask_apply>` effect, that uses a transition to composite the current frame's image over the snapshot. The typical use case is to add effects in the following sequence:

 Secondary Color Correction Area Selection Mask (this effect) -->  zero or more effects (e.g. Blur, Cartoon) -->  Mask Apply

