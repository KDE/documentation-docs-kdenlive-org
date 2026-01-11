.. meta::

   :description: Kdenlive Video Effects - Vertigo 
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, motion, vertigo

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Vertigo
=======

.. figure:: /images/effects_and_compositions/effects-vertigo-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Vertigo

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      vertigo
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter uses alpha blend with zoomed and rotated and phase-shifted copies of the source video to create a somewhat nauseating effect similar to suffering from vertigo (or whatever Hitchcock tried to achieve in his movie of the same name).


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 10 65
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Phase Increment
     - Integer
     - Sets the frequency of the rotation. The higher the number the more jittery the rotation.
   * - Zoom Rate
     - Integer
     - Sets the zoom factor for the copies. The higher the number the more copies are visible. Values below 100 lead to black banding at the edges of the video due to the rotation of the video and its copies.
