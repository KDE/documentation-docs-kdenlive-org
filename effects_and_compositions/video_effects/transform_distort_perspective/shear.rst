.. meta::

   :description: Do your first steps with Kdenlive video editor, using shear effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, shear

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |link| raw:: html

   <a href="link_URI" target="_blank">link_text</a>


.. _effects-shear:

Shear
=====

This effect/filter applies a shear transformation to the clip.

The effect has keyframes but only for the :guilabel:`Background fill color`.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-shear.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-shear

   Shear effect

* **X shear factor** - Set the shear factor. Range is from -2 to 2.

* **Y shear factor** - Set the shear factor. Range is from -2 to 2.

* **Interpolation mode** - Set the interpolation mode. Options are **Nearest** (default) and **Bilinear**.

* **Background fill color** - Set the background fill color if the shear reveals the background. Default is **black**.

.. rst-class:: clear-both


.. note:: As of this writing and version 23.04 the shear parameters are integer values, not float, hence the very much limited use of the effect. A bug report has been created. Until this is fixed use the :ref:`effects-rotate_and_shear` effect.
