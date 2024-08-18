.. meta::

   :description: Kdenlive Video Effects - Dilation 
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, image adjustment, dilation

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Dilation
========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-dilation.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-dilation

.. sidebar:: |kdenlive-show-video| Dilation

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      dilation
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter replaces the pixel by the local(3x3) maximum.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - 1st / 2nd / 3rd / 4th Plane Threshold
     - Integer
     - Limit the maximum change for each :term:`plane`, default is 50. If 0, plane will remain unchanged.
   * - Coordinates
     - Integer
     - Flag which specifies the pixel to refer to. Default is 255, i.e. all eight pixels are used.
