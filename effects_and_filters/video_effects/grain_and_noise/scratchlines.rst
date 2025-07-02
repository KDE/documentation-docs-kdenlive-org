.. meta::

   :description: Kdenlive Video Effects - Scratchlines
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, grain and noise, scratchlines

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Scratch Lines
=============

.. figure:: /images/effects_and_compositions/effects-scratchlines-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-scratchlines-2504.webp

.. sidebar:: |kdenlive-show-video| Scratch Lines

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      lines
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

This effect/filter generates scratch lines over the image source. Can be used in conjunction with :doc:`/effects_and_filters/video_effects/stylize/oldfilm` and :doc:`/effects_and_filters/video_effects/grain_and_noise/dust` to simulate vintage film footage.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 10 65
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Width of line
     - Integer
     - Sets the width of the scratch lines
   * - Max number of lines
     - Integer
     - Defines the maximum number of lines
   * - Max darker
     - Integer
     - Defines how much darker the image will be behind the line
   * - Max lighter
     - Integer
     - Defines how much lighter the image will be behind the line
