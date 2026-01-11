.. meta::

   :description: Kdenlive Video Effects - Analog Video Echo
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, analog, video, echo

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Analog Video Echo
=================

.. figure:: /images/effects_and_compositions/effects-aech0r-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Analog Video Echo

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      aech0r
   :**Available**:
      |appimage| |windows| |apple|
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

This effect/filter creates an analog video echo.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Fade Factor
     - Float
     - Disappearance rate of the echo
   * - Direction
     - Switch
     - Darker or Brighter echo
   * - Keep RED
     - Switch
     - Influence on Red channel
   * - Keep GREEN
     - Switch
     - Influence on Green channel
   * - Keep BLUE
     - Switch
     - Influence on Blue channel
   * - Strobe period
     - Float
     - Rate of the stroboscope: from 0 to 8 frames
