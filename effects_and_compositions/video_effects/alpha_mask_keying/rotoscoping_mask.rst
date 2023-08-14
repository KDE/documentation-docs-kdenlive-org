.. metadata-placeholder

   :authors: - Bernd Jordan

   :license: Creative Commons License SA 4.0


.. _effects-rotoscoping_mask:

Rotoscoping (Mask)
------------------

This filter makes a snapshot of the frame before it draws the :ref:`Rotoscoping <effects-rotoscoping>` region/mask into the alpha channel. Use it together with the :ref:`Mask Apply <effects-mask_apply>` effect, that uses a transition to composite the current frame's image over the snapshot. The typical use case is to add effects in the following sequence:

 Rotoscoping Mask (this effect) -->  zero or more effects (e.g. Blur, Cartoon) -->  Mask Apply
