.. meta::

   :description: Kdenlive Video Effects - Erosion
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, image adjustment, erosion

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Erosion
=======

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-erosion.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-erosion

.. sidebar:: |kdenlive-show-video| Erosion

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      erosion
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter replaces the pixel by the local(3x3) minimum giving the source image an erosion effect.


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
     - Limits the maximum change for each :term:`plane`, default is 50. If 0, plane will remain unchanged.
   * - Coordinates
     - Integer
     - Flag which specifies the pixel to refer to. Default is 255, i.e. all eight pixels are used.
