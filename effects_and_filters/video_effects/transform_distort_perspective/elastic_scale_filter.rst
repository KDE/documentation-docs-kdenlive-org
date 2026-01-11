.. meta::

   :description: Kdenlive Video Effects - Elastic Scale
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, elastic scale

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Elastic Scale
=============

.. figure:: /images/effects_and_compositions/effects-elastic_scale-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Elastic Scale

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
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
   :**Color depth**:
      8bit
   :**Tutorial**:
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
     - Integer
     - Horizontal center position of the linear area
   * - Linear Width
     - Integer
     - Width of the linear area
   * - Linear Scale Factor
     - Float
     - Amount how much the linear area is scaled
   * - Non-Linear Scale Factor
     - Float
     - Amount how much the outer left and outer right areas are scaled non-linearly
