.. meta::

   :description: Kdenlive Video Effects - Burning TV
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, burning tv, burning

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Burning TV
==========

.. figure:: /images/effects_and_compositions/effects-burning_tv-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-burning_tv-2504.webp

.. sidebar:: |kdenlive-show-video| Burning TV

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      BurningTV
   :**Available**:
      |appimage| |windows| |apple|
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

This effect/filter simulates burning TV pixels.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Foreground Only
     - Switch
     - Whether to separate the background and burn only the foreground. The background is based upon the first frame received by the filter.
   * - Movement Threshold
     - Integer
     - The lower the threshold the more movement will be picked up and turned into burning pixels
