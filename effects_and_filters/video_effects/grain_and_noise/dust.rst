.. meta::

   :description: Kdenlive Video Effects - Dust
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, grain and noise, dust

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Dust
====

.. figure:: /images/effects_and_compositions/effects-dust-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-dust-2504.webp

.. sidebar:: |kdenlive-show-video| Dust

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      dust
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter makes random dust particles appear across the image source. This gives the video an old film look. See also the :doc:`/effects_and_filters/video_effects/stylize/oldfilm`, :doc:`/effects_and_filters/video_effects/grain_and_noise/filmgrain`, and :doc:`/effects_and_filters/video_effects/grain_and_noise/scratchlines` effects.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 30 10 60
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Maximum diameter
     - Percentage
     - Sets the maximum size of (the underlying .png file for) the dust particles
   * - Maximum number of particles
     - Integer
     - Sets the maximum number of dust particles
