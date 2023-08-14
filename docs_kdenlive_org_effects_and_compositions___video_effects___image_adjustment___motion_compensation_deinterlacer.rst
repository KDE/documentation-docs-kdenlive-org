.. meta::

   :description: Do your first steps with Kdenlive video editor, using motion compensation deinterlacer effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, image adjustment, motion compensation deinterlacer

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-motion_compensation_deinterlacer:

Motion Compensation Deinterlacer
================================

This effect/filter applies motion-compensation deinterlacing.

It needs one field per frame as input and must thus be used together with yadif=1/3 or equivalent.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-motion_compensation_deinterlacer.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-motion_compensation_deinterlacer

   Motion Compensation Deinterlacer effect

* **Mode** - Sets the deinterlacing mode. Options are **Fast**, **Medium** (default) and **Slow** for iterative motion estimation, **Extra_slow** like **Slow** but using multiple reference frames.

* **Picture field parity** - Sets the picture field parity assumed for the input video. Options are **Top field first** and **Bottom field first**.

**QP** - Sets the per-block quantizing parameter (QP) used by the internal encoder. Higher values should result in a smoother motion vector field but less optimal individual vectors. Default value is 1.
