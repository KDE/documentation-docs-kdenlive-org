.. meta::

   :description: Kdenlive Video Effects - Old Film Simulator
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, oldfilm, old, film, simulator

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jack (https://userbase.kde.org/User:Jack)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Old Film Simulator
==================

.. figure:: /images/effects_and_compositions/effects-oldfilm-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-oldfilm-2504.webp

.. sidebar:: |kdenlive-show-video| Old Film Simulator

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      oldfilm
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

This effect/filter moves the video up and down and adds random brightness changes, making it look like old film footage. See also :doc:`/effects_and_filters/video_effects/grain_and_noise/dust`, :doc:`/effects_and_filters/video_effects/grain_and_noise/scratchlines`, :doc:`/effects_and_filters/video_effects/motion/gate_weave`, and :doc:`/effects_and_filters/video_effects/grain_and_noise/filmgrain` effects.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 10 65
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Maximum Up/Down Move
     - Integer
     - Determines the maximum vertical movement in pixels (jitter)
   * - Frames With Movement
     - Percent
     - Set the %age of frames that have a vertical movement (jitter)
   * - Brightness Up
     - Integer
     - Sets the value by which the image will be made lighter
   * - Brightness Down
     - Integer
     - Sets the value by which the image will be made darker
   * - Brightness Every
     - Percent
     - Set the %age of frames that will have the brightness changed
   * - Uneven Develop Up
     - Integer
     - Sets the value by which the image will be made lighter
   * - Uneven Develop Down
     - Integer
     - Sets the value by which the image will be made darker
   * - Uneven Develop Duration
     - Integer
     - Sets the time in frames of an up/down cycle for uneven development


.. https://youtu.be/0g1xDo-pwm0

   https://youtu.be/PuQTd6D2Y2Y
