.. meta::

   :description: Kdenlive Video Effects - Despill
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, alpha, despill, greenscreen, bluescreen, keying

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Despill
=======

.. figure:: /images/effects_and_compositions/effects-despill-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-show-video| Despill

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      despill
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

Remove unwanted contamination of foreground colors caused by reflected color of greenscreen or bluescreen (avfilter.despill)


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Screen type
     - Selection
     - Sets what type of despill to use
   * - Spillmap Mix
     - Float
     - Sets how spillmap will be generated
   * - Spillmap Expand
     - Float
     - Sets how much to get rid of still remaining spill
   * - Set Red Scale
     - Float
     - Controls amount of red in spill area
   * - Set Green Scale
     - Float
     - Controls amount of green in spill area. Should be -1 for greenscreen.
   * - Set Blue Scale
     - Float
     - Controls amount of blue in spill area. Should be -1 for bluescreen.
   * - Brightness
     - Float
     - Controls brightness of spill area, preserving colors.

The following selection items are available:

:guilabel:`Screen type`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - green
     - Assumes a green screen
   * - blue
     - Assumes a blue screen

