.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Bernd Jordan

   :license: Creative Commons License SA 4.0


.. _effects-alpha_shapes_mask:

Alpha Shapes (Mask)
-------------------

This filter takes a snapshot of the frame before it draws simple shapes into the alpha channel. Use it together with the :ref:`Mask Apply <effects-mask_apply>` effect that uses a transition to composite the current frame's image over the snapshot. The typical use case is to add effects in the following sequence:

 Alpha Shapes Mask (this effect) -->  zero or more effects (e.g. Blur, Cartoon) -->  Mask Apply [--> more effects if needed]

For a more detailed description of the Alpha Shapes effect refer to the :ref:`Alpha Shapes <effects-alpha_shapes>` section of the documentation.
