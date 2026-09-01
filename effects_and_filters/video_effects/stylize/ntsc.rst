.. meta::

   :description: Kdenlive Video Effects - NTSC
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, ntsc filter

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0

.. .. versionadded:: 26.08


NTSC
====

.. figure:: /images/effects_and_compositions/effects-ntsc-2608.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| NTSC

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      frei0r
   :**Source filter**:
      ntsc
   :**Available**:
      |linux| |appimage| |windows| |apple|
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

This effect/filter simulates NTSC\ [1]_ analog video.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Progressive Scan
     - Switch
     - Toggles progressive scan (Interlaced if off)
   * - Scanlines
     - Switch
     - Draw borders between scanlines
   * - Signal Noise
     - Percent
     - Amount of noise introduced into the NTSC signal


----

.. |ntsc| raw:: html

   <a href="https://en.wikipedia.org/wiki/NTSC" target="_blank">NTSC</a>

.. [1] For more information about NTSC refer to the |ntsc| article in Wikipedia
