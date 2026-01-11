.. meta::

   :description: Kdenlive Video Effects - Nosync0r (broken TV)
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, nosync0r, broken tv

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |link| raw:: html

   <a href="link_URI" target="_blank">link_text</a>


Nosync0r (Broken TV)
====================

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-nosync0r.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Nosync0r

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      nosync0r
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter shifts the input frame by a set amount (1/1000\ :sup:`th` of the frame height) and wraps it around the bottom edge. This simulates a broken TV set where the horizontal synchronization signal (HSync) is off or faulty. Using keyframes allows you to simulate a continuous scrolling video.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - HSync
     - Integer
     - Offset amount (1/1000\ :sup:`th` of the frame height)
