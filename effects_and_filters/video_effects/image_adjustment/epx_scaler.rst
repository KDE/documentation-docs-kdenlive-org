.. meta::

   :description: Kdenlive Video Effects - EPX Scaler
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, image adjustment, epx scaler

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


EPX Scaler
==========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-epx_scaler.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| EPX Scaler

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      epx
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter applies the EPX\ [1]_ magnification filter which is designed for pixel art.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Scale factor
     - Selection
     - Sets the scaling dimension

The following selection items are available:

:guilabel:`Scale factor`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - 2x
     - 
   * - 3x
     - Default

----

.. |epx| raw:: html

   <a href="https://en.wikipedia.org/wiki/Pixel-art_scaling_algorithms#EPX/Scale2%C3%97/AdvMAME2%C3%97" target="_blank">Eric's Pixel Expansion (EPX)</a>

.. [1] See the article in Wikipedia about |epx| algorithm.
