.. meta::

   :description: Do your first steps with Kdenlive video editor, using contrast effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, contrast

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-contrast:

Contrast
========

This effect/filter adjusts the contrast of a source image.

This effect has keyframes

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-contrast.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-contrast

   Contrast effect

* **Contrast** - Set the contrast. Allowed values are from 0 to 1000, default value is 250.

.. rst-class:: clear-both

This filter controls the tonal range of the source which maps pixel values below a specified value to black, and those above a specified value to white. It is best used in conjunction with :ref:`view-rgb_parade` and the :ref:`view-histogram`. Values below 250 decrease the contrast between dark and light areas, values above 250 increase it.
