.. meta::

   :description: Do your first steps with Kdenlive video editor, using vignette_effect effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, generate, vignette_effect

.. metadata-placeholders

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-vignette_effect:

Vignette Effect
===============

This effect/filter creates an adjustable vignette. It is similar to the :ref:`effects-vignette` effect but lacks the adjustment of the aspect ratio.

The effect has keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-vignette_effect.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-vignette_effect

   Vignette effect

* **use cos instead of linear** - If selected makes the fall-off area appear denser by applying a cosine curve instead of a linear function

* **smooth** - Set the size of the fall-off area. Higher values make the center darker and the edges lighter. If **smooth** is set to zero, the vignette is like a black matte with a distinct edge.

* **radius** - Set the radius of the vignette

* **x / y** - Define the X and Y coordinates for the center point of the vignette (X = 0, Y = 0 defines the top-left corner of the screen)

* **opacity** - Set the :term:`opacity` of the black parts of the vignette
