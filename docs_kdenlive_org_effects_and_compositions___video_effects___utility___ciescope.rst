.. meta::

   :description: Do your first steps with Kdenlive video editor, using ciescope effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, utility, ciescope

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |link| raw:: html

   <a href="link_URI" target="_blank">link_text</a>


.. _effects-ciescope:

CIE Scope
=========

This effect/filter displays a CIE color diagram with overlaid input pixels.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-ciescope.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-ciescope

   CIE Scope effect

* **av.size / av.s** - Set CIE Scope size, by default set to 512. [1]_

* **av.intensity / av.i** - Set intensity used to map input pixel values to CIE diagram [2]_

* **av.contrast** - Set contrast used to draw tongue colors that are out of active color system gamut

* **av.gamma** - Correct gamma displayed on scope, by default enabled [3]_

.. rst-class:: clear-both


**Notes**

 .. [1] Only **av.s** is taken into account

 .. [2] Only **av.i** is taken into account

 .. [3] At the moment this parameter has no effect
