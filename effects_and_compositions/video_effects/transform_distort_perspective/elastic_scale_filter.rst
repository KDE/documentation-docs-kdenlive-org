.. meta::

   :description: Kdenlive Video Effects - Elastic Scale Filter
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, elastic scale filter

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Elastic Scale Filter
====================

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-elastic_scale_filter.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-elastic_scale_filter

.. sidebar:: |kdenlive-show-video| Elastic Scale Filter

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      frei0r
   :**Source filter**:
      elastic_scale
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter allows to scale the video sources non-linearly.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Center
     - Float
     - Horizontal center position of the linear area
   * - Linear Width
     - Float
     - Width of the linear area
   * - Linear Scale Factor
     - Float
     - Amount how much the linear area is scaled
   * - Non-Linear Scale Factor
     - Float
     - Amount how much the outer left and outer right areas are scaled non linearly
