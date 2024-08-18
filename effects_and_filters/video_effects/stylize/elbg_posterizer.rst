.. meta::

   :description: Kdenlive Video Effects - ELBG Posterizer
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, elbg posterizer

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


ELBG Posterizer
===============

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-elbg_posterizer.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-elbg_posterizer

.. sidebar:: |kdenlive-show-video| EFFECT_NAME

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      elbg 
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter applies a :term:`posterize` effect using the ELBG (Enhanced LBG) algorithm.

For each input image, the filter will compute the optimal mapping from the input to the output given the :guilabel:`Codebook length`, that is the number of distinct output colors.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Codebook Length
     - Integer
     - Set codebook length. The value must be a positive integer, and represents the number of distinct output colors. Default value is 50.
   * - Steps
     - Integer
     - Set the maximum number of iterations to apply for computing the optimal mapping. The higher the value the better the result and the higher the computation time. Default value is 1.
