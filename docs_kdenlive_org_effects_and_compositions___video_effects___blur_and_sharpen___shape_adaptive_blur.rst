.. meta::

   :description: Do your first steps with Kdenlive video editor, using shape adaptive blur effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, blur and sharpen, shape adaptive blur

   :authors: - Bernd Jordan

   :license: Creative Commons License SA 4.0


.. _effects-shape_adaptive_blur:

Shape Adaptive Blur
===================

This effect blurs the clip while trying to keeping shape (edge).

This effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-shape_adaptive_blur.webp
   :align: left
   :width: 400px
   :figwidth: 400px
   :alt: kdenlive2304_effects-shape_adaptive_blur

   Shape Adaptive Blur effect

* **Luma Radius** - Set :term:`luma` blur filter strength. Range 0.1 - 4.0, default is 1. The higher the value the more blurring, and slower processing.

* **Luma pre-filter radius** - Set luma pre-filter radius. Range 0.1-2.0, default value is 1.0..

* **Luma Strength** - Set luma maximum difference between pixels to still be considered. Range 0.1-100.0, default value is 1.0.

* **Chroma Radius** - Set :term:`chroma` blur filter strength. Range -0.9 - 4.0, default is 0 (no blurring). The higher the value the more blurring, and slower processing.

* **Chroma pre-filter radius** - Set chroma pre-filter blur strength. Range -0.9 - 2.0, default is 1.

* **Chroma Strength** - Set chroma blur filter strength. Range -0.9 - 100.0, default is 0 (no blurring)
