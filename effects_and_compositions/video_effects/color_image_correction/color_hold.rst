.. meta::

   :description: Do your first steps with Kdenlive video editor, how to use color_hold effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, color hold

   :authors: - Bernd Jordan

   :license: Creative Commons License SA 4.0


.. _effects-color_hold:

Color Hold
==========

This effect/filter removes all color information for all RGB colors except for the selected one.

This effect has keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-color_hold.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-color_hold

   Color Hold effect

* **Similarity** - Similarity percentage with the above color. 0.01 matches only the exact key color, while 1.0 matches everything.

* **Blend** - Blend percentage. 0.0 makes pixels fully gray. Higher values result in more preserved color.

* **Color key** - The color which will not be replaced with neutral gray. Use the color picker or the color button to select the color to hold.
