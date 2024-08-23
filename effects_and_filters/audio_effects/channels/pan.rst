.. meta::

   :description: Kdenlive Audio Effects - Pan
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, audio effects, pan, panning

.. metadata-placeholders

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Pan
===

.. figure:: /images/effects_and_compositions/kdenlive2308_effects-pan.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-audio| Pan

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      avfilter
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No


.. rst-class:: clear-both

.. rubric:: Description

Adjusts the left/right spread of a channel.

.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: table-wrap

   * - Parameter
     - Value
     - Description

   * - **Channel**
     - Selection
     - Selects the channel for the operation

   * - **Pan**
     - Integer
     - Adjusts the balance: 0 - 1000 (default is 500)