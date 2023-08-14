.. meta::

   :description: Do your first steps with Kdenlive video editor, using elbg posterizer effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, elbg posterizer

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-elbg_posterizer:

ELBG Posterizer
===============

This effect/filter applies a :term:`posterize` effect using the ELBG (Enhanced LBG) algorithm.

For each input image, the filter will compute the optimal mapping from the input to the output given the :guilabel:`Codebook length`, that is the number of distinct output colors.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-elbg_posterizer.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-elbg_posterizer

   ELBG Posterizer effect

* **Codebook Length** - Set codebook length. The value must be a positive integer, and represents the number of distinct output colors. Default value is 50.

* **Steps** - Set the maximum number of iterations to apply for computing the optimal mapping. The higher the value the better the result and the higher the computation time. Default value is 1.
