.. meta::

   :description: Kdenlive Video Effects - Scroll
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, scroll

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Scroll
======

.. figure:: /images/effects_and_compositions/effects-scroll-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Scroll

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      avfilter
   :**Source filter**:
      scroll
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No
   :**Color depth**:
      10bit |color-management|
   :**Tutorial**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter scrolls the clip horizontally and/or vertically. Negative values make the scrolling go from left to right. The higher the value the faster the scrolling. A value of 1000 renders the effect useless.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Horizontal scrolling speed
     - Integer
     - Set the horizontal scrolling speed
   * - Vertical scrolling speed
     - Integer
     - Set the vertical scrolling speed
   * - Initial horizontal position
     - Integer
     - Set the initial horizontal position
   * - Initial vertical position
     - Integer
     - Set the initial vertical position
