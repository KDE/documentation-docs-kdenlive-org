.. meta::

   :description: Kdenlive Video Effects - Gradfun
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, grain and noise, gradfun

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Gradfun
=======

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-gradfun.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-gradfun

.. sidebar:: |kdenlive-show-video| Gradfun

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      gradfun
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter de-bands video quickly by using gradients.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - av.strength
     - Float
     - The maximum amount by which the filter will change any one pixel
   * - av.radius
     - Integer
     - The neighborhood to fit the gradient to
