.. meta::

   :description: Kdenlive Video Effects - Lag Fun
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, motion, lagfun, lag fun, lag, fun, motion blur

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0

.. .. versionadded:: 26.08


Lag Fun
=======

.. figure:: /images/effects_and_compositions/effects-lagfun-2608.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Lag Fun

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      lagfun
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter slowly updates darker pixels.


.. note:: 
   This effect does not reset during playback due to frame buffer issues but renders correctly.

.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Decay 
     - Float
     - Sets the decay from 0 to 1
     