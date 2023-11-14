.. meta::

   :description: Kdenlive Audio Effects - Audio Pan
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, audio effects, audio pan, panning, balance

.. metadata-placeholders

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Audio Pan
=========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-audio_pan.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-audio| Audio Pan

   :**Status**:
      Maintained
   :**Keyframes**:
      No
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

Allows for each channel to be panned, or a simple balance adjustment to be made.

.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: table-wrap

   * - Parameter
     - Value
     - Description

   * - **Start**
     - Float
     - The position of the audio relative to its neighbor

   * - **End**
     - Float
     - Then ending value of the audio position

   * - **Channel**
     - Integer
     - Channel selector

   * - **Gang**
     - Switch
     - Whether to gang together front and back when using balance, or left and right when using fade

   * - **Split**
     - Float
     - The animated position of the audio relative to its neighbor channel
