.. meta::

   :description: Do your first steps with Kdenlive video editor, using lens correction effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, lens correction

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |avfilter.lc| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-lenscorrection/" target="_blank">avfilter.lenscorrection</a>

.. |frei0r.lc| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-lenscorrection/" target="_blank">frei0r.lenscorrection</a>


.. _effects-lens_correction:

Lens Correction
===============

This effect/filter corrects radial lens distortion. It can be used to create an "old TV set or monitor" curving effect.

The effect does not have keyframes. See :ref:`effects-lens_correction_keyframable` if you need to use keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-lens_correction.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-lens_correction

   Lens Correction effect

* **Focal point relative-X coord** - Set relative center X

* **Focal point relative-Y coord** - Set relative center Y

* **Quadratic correction coeff.** - Set quadratic distortion factor

* **DoubleQuadratic correction coeff.** - Set double quadratic distortion factor

.. rst-class:: clear-both


.. note:: This effect may produce different results than :ref:`effects-lens_correction_keyframable` although the name may suggest the only difference is the keyframes. **Lens Correction** uses |avfilter.lc|, whereas **Lens Correction (keyframable)** uses |frei0r.lc|.


.. https://youtu.be/axQdm482Uto

.. https://youtu.be/cEwZzNRiVks
