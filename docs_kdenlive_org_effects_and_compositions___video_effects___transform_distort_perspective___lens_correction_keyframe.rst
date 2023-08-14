.. meta::

   :description: Do your first steps with Kdenlive video editor, using lens correction (keyframable) effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, lens correction keyframable

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |avfilter.lc| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-lenscorrection/" target="_blank">avfilter.lenscorrection</a>

.. |frei0r.lc| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-lenscorrection/" target="_blank">frei0r.lenscorrection</a>


.. _effects-lens_correction_keyframable:

Lens Correction (keyframable)
=============================

This effect/filter allows compensation of lens distortion. It can be used to create an "old TV set or monitor" curving effect.

The effect has keyframes. See :ref:`effects-lens_correction` if you do not need to use keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-lens_correction_keyframable.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-lens_correction_keyframable

   Lens Correction (keyframable) effect

* **Horizontal Center** - Set relative center X

* **Vertical Center** - Set relative center Y

* **Center Correction** - Set correction near the center

* **Edges Correction** - Set correction near the edges

* **Brightness** - Set brightness increase

.. rst-class:: clear-both


.. note:: This effect may produce different results than :ref:`effects-lens_correction` although the name may suggest the only difference is the keyframes. **Lens Correction (keyframable)** uses |frei0r.lc|, whereas **Lens Correction** uses |avfilter.lc|.


.. https://youtu.be/axQdm482Uto

.. https://youtu.be/cEwZzNRiVks
