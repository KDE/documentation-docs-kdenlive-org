.. meta::

   :description: Kdenlive Video Effects - squigglevision
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, squigglevision, squiggle, cartoon, wobble, hand-drawn, hand, drawn

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0

.. .. versionadded:: 26.08


Squigglevision
==============

.. figure:: /images/effects_and_compositions/effects-squigglevision-2608.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| squigglevision

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      squigglevision
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter creates a hand-drawn wobble effect.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 30 10 60
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Strength
     - Percent
     - Displacement amount
   * - FPS
     - Integer
     - Squiggle updates per second (capped at 30 fps)
   * - Scale
     - Integer
     - Noise cell size between 4 and 128 pixels
