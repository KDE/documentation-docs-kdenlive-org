.. meta::

   :description: Do your first steps with Kdenlive video editor, using vertigo effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, motion, vertigo

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-vertigo:

Vertigo
=======

This effect/filter uses alpha blend with zoomed and rotated and phase-shifted copies of the source video to create a somewhat nauseating effect similar to suffering from vertigo (or whatever Hitchcock tried to achieve in his movie of the same name).

The effect has keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-vertigo.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-vertigo

   Vertigo effect

* **Phase Increment** - Sets the frequency of the rotation. The higher the number the more jittery the rotation.

* **Zoom Rate** - Sets the zoom factor for the copies. The higher the number the more copies are visible. Values below 100 lead to black banding at the edges of the video due to the rotation of the video and its copies.
