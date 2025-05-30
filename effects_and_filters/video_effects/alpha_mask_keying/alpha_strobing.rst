.. meta::

   :description: Kdenlive Video Effects - Alpha Strobing
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, alpha strobing

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Alpha Strobing
==============

.. figure:: /images/effects_and_compositions/effects-alpha_strobing-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-show-video| Alpha Strobing

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      strobe
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

Strobes the alpha channel to 0. Many other filters overwrite the alpha channel, in that case this needs to be last.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Invert
     - Switch
     - Inverts the operation
   * - Interval
     - Integer
     - Defines the strobing interval. Higher numbers mean less frequent strobing.


.. rubric:: Notes

An :guilabel:`Interval` of 1 alternates the alpha channel every frame; a value of 100 alternates every 50 frames