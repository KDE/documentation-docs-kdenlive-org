.. meta::

   :description: Kdenlive Video Effects - Gate Weave 
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, motion, gate weave, film, gate, weave

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. .. versionadded:: 25.04

   
Gate Weave
==========

.. figure:: /images/effects_and_compositions/effects-gate_weave-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-gate_weave-2504.webp

.. sidebar:: |kdenlive-show-video| Gate Weave

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

Randomly moves frame around to simulate film gate weave. For other film effects see also :doc:`/effects_and_filters/video_effects/grain_and_noise/filmgrain`, :doc:`/effects_and_filters/video_effects/grain_and_noise/dust`, :doc:`/effects_and_filters/video_effects/grain_and_noise/scratchlines`, and the vignette effects (:doc:`/effects_and_filters/video_effects/generate/vignette`, :doc:`/effects_and_filters/video_effects/generate/vignette_effect`).


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 10 65
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Interval
     - Integer
     - The amount of time before the position is randomized again. The larger the number the slower the picture will move.
   * - Maximum Horizontal Movement
     - Float
     - The maximum distance the picture could move left or right. The larger the number the more the picture moves and the less subtle the effect. Maximum is 10, but it takes fractions (results in subtle pixel color mixes).
   * - Maximum Vertical Movement
     - Float
     - The maximum distance the picture could move up or down. The larger the number the more the picture moves and the less subtle the effect. Maximum is 10, but it takes fractions (results in subtle pixel color mixes).
