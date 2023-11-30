.. meta::

   :description: Do your first steps with Kdenlive video editor, using pixelize effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, pixelize

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-pixelize:

Pixelize
========

This effect/filter pixelizes the input image. It works similar to the :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/obscure` effect but allows you to control the block size individually and independently from the image size, but by contrast applies it to the entire frame. In order to apply the **Pixelize** effect only to a certain region use it in combination with the :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/alpha_shapes_mask` effect.

The effect has keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-pixelize.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-pixelize

   Pixelize effect

* **Block Size X** - Horizontal size of one "pixel"

* **Block Size Y** - Vertical size of one "pixel"

.. rst-class:: clear-both


.. note:: The :guilabel:`Block Size` takes the aspect ratio into account. That means that in a 16:9 project the ratio of the two values has to be 16:9 in order to produce square pixels. Otherwise, identical values will produce rectangles.
