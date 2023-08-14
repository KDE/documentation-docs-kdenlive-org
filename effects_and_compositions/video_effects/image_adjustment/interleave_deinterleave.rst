.. meta::

   :description: Do your first steps with Kdenlive video editor, using interleave - deinterleave effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, image adjustment, interleave - deinterleave

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-interleave:

Interleave - Deinterleave
=========================

This effect/filter interleaves or deinterleave fields.

This filter allows one to process interlaced images fields without deinterlacing them. Deinterleaving splits the input frame into 2 fields (so-called half pictures). Odd lines are moved to the top half of the output image, even lines to the bottom half. You can process (filter) them independently and then re-interleave them.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-interleave.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-interleave

   Interleave - Deinterleave effect

* **Luma / Chroma / Alpha Mode** - Options are **None** (do nothing), **Deinterleave** (deinterleave fields, placing one above the other), or **Interleave** (interleave fields; reverse the effect of deinterleaving).

* **Swap Luma / Chroma / Alpha fields** - Swap :term:`luma`, :term:`chroma` or alpha fields, Exchanges even and odd lines. Default is off.
