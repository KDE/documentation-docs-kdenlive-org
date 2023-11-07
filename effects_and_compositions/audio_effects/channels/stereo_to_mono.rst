.. meta::

   :description: Kdenlive Audio Effects - Stereo to Mono
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, audio effects, stereo to mono, stereo, mono

.. metadata-placeholders

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Stereo to Mono
==============

.. figure:: /images/effects_and_compositions/kdenlive2308_effects-stereo_to_mono.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-audio| Stereo to Mono

   | **Status**: Maintained
   | **Keyframes**: No
   | **Source library**: avfilter.channelcopy
   | **Available**: |linux| |appimage| |windows| |apple|
   | **On Master only**: No
   | **Known bugs**: No


.. .. list-table::
   :class: table-rows
   :width: 45%
   :widths: 100
   :header-rows: 1

   * - | |kdenlive-audio| **Stereo to Mono**
       | **Status**: Maintained
       | **Keyframes**: No
       | **Source library**: avfilter.channelcopy
       | **Available**: |linux| |appimage| |windows| |apple|
       | **On Master only**: No
       | **Known bugs**: No

.. rst-class:: clear-both

.. rubric:: Description

Copies one channel to another.

.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: table-wrap

   * - Parameter
     - Value
     - Description

   * - **From**
     - Selection
     - Selects the source channel for the operation

   * - **To**
     - Selection
     - Selects the target channel for the operation
   
   * - **Swap channels**
     - Switch
     - Swaps the channels for the operation