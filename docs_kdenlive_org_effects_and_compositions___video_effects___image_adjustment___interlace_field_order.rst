.. meta::

   :description: Do your first steps with Kdenlive video editor, using interlace field order effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, image adjustment, interlace field order

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-interlace_field_order:

Interlace Field Order
=====================

This effect/filter transforms the :term:`field order` of the (interlaced) input video.

The transformation is done by shifting the picture content up or down by one line, and filling the remaining line with appropriate picture content. This method is consistent with most broadcast field order converters.

If the input video is not flagged as being :term:`interlaced`, or it is already flagged as being of the required output field order, then this filter does not alter the incoming video.

It is very useful when converting to or from PAL DV material, which is bottom field first.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-interlace_field_order.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-interlace_field_order

   Interlace Field Order effect

* **Field priority** - Specifies the output field order. Options are **Top field first** or **Bottom field first**.
