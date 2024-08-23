.. meta::

   :description: Kdenlive Video Effects - Oldfilm
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, oldfilm

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jack (https://userbase.kde.org/User:Jack)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Old Film
========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-oldfilm.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-oldfilm

.. sidebar:: |kdenlive-show-video| EFFECT_NAME

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

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter moves the video up and down and adds random brightness changes, making it look like old film footage. See also :doc:`/effects_and_filters/video_effects/grain_and_noise/dust` and :doc:`/effects_and_filters/video_effects/grain_and_noise/scratchlines` effects.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Y-Delta
     - Integer
     - Maximum delta value of up/down move (jitter)
   * - % of picture have delta
     - Percent
     - Set the %age of frames that have a Y-Delta (jitter)
   * - Brightness up
     - Integer
     - Sets the value by which the image will be made lighter
   * - Brightness down
     - Integer
     - Sets the value by which the image will be made darker
   * - Brightness every
     - Percent
     - Set the %age of frames that will have the brightness changed
   * - Unevendevelop up
     - Integer
     - Sets the value by which the image will be made lighter
   * - Unevendevelop down
     - Integer
     - Sets the value by which the image will be made darker
   * - Unevendevelop Duration
     - Integer
     - Sets the time in frames of an up/down cycle for uneven development


.. https://youtu.be/0g1xDo-pwm0

   https://youtu.be/PuQTd6D2Y2Y
