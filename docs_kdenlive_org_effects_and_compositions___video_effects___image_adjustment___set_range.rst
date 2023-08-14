.. meta::

   :description: Do your first steps with Kdenlive video editor, using set range effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, image adjustment, set range

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-set_range:

Set Range
=========

This effect/filter forces color range for the output video frame.

The filter marks the color range property for the output frames. It does not change the input frame, but only sets the corresponding property, which affects how the frame is treated by following filters.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-set_range.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-set_range

   Set Range effect

* **Set range** - Options are **auto** (keep the same color range property), **unspecified / unknown** (set the color range as unspecified), **limited / tv /mpeg** (set the color range as limited), and **full / pc / jpeg** (set the color range as full).
