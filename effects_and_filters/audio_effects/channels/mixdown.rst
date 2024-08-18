.. meta::

   :description: Kdenlive Audio Effects - Mixdown
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, audio effects, mixdown

.. metadata-placeholders

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Mixdown
=======================

.. figure:: /images/effects_and_compositions/kdenlive2308_effects-mixdown.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-audio| Mixdown

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

Mixes all audio channels into a mono signal and outputs it as N channels.

.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: table-wrap

   * - Parameter
     - Value
     - Description

   * - **Number of output channels**
     - Selection
     - Select the number of output channels

.. rst-class:: clear-both


The following selection items are available:

.. list-table::
   :width: 100%
   :class: table-simple

   * - Mono
     - Mono output
   * - Stereo
     - Stereo output
   * - 2.1
     - 2.1 mixdown (stereo plus sub-woofer)
   * - 4 Channels
     - Quadraphonic
   * - 5.1
     - 5.1 (surround sound)
   * - 7.1
     - 7.1 (cinema and home theater surround sound)