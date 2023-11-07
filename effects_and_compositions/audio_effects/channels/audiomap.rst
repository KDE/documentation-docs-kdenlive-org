.. meta::

   :description: Kdenlive Audio Effects - Audiomap
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, audio effects, audiomap, mapping, balance

.. metadata-placeholders

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Audiomap
=========

.. figure:: /images/effects_and_compositions/kdenlive2308_effects-audiomap.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-audio| Audiomap

   | **Status**: Maintained
   | **Keyframes**: No
   | **Source library**: avfilter.audiomap
   | **Available**: |linux| |appimage| |windows| |apple|
   | **On Master only**: No
   | **Known bugs**: No


.. .. list-table::
   :class: table-rows
   :width: 45%
   :widths: 100
   :header-rows: 1

   * - | |kdenlive-audio| **Audiomap**
       | **Status**: Maintained
       | **Keyframes**: No
       | **Source library**: avfilter.audiomap
       | **Available**: |linux| |appimage| |windows| |apple|
       | **On Master only**: No
       | **Known bugs**: No

.. rst-class:: clear-both

.. rubric:: Description

Allows for up to six audio source channels to be mapped to up to 32 channels.

.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: table-wrap

   * - Parameter
     - Value
     - Description

   * - **CH x source**
     - Selection
     - Maps source channel CH x to the selected channel (CH 1 .. CH32)