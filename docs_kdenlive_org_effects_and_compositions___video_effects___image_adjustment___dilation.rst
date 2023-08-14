.. meta::

   :description: Do your first steps with Kdenlive video editor, using dilation effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, image adjustment, dilation

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-dilation:

Dilation
========

This effect/filter replaces the pixel by the local(3x3) maximum.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-dilation.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-dilation

   Dilation effect

* **1st / 2nd / 3rd / 4th Plane Threshold** - Limit the maximum change for each :term:`plane`, default is 50. If 0, plane will remain unchanged.

* **Coordinates** - Flag which specifies the pixel to refer to. Default is 255, i.e. all eight pixels are used.
