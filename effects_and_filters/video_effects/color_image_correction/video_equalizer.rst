.. meta::

   :description: Kdenlive Video Effects - Video Equalizer
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, video equalizer

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Video Equalizer
===============

.. figure:: /images/effects_and_compositions/effects-video_equalizer-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-video_equalizer-2504.webp

.. sidebar:: |kdenlive-show-video| Video Equalizer

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      
   :**Source filter**:
      
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter sets brightness, contrast, :term:`saturation` and approximate :term:`gamma` adjustment.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Contrast
     - Float
     - Set the contrast expression. Negative values give a negative image. The value must be a float value in range -3.00 to 3.00. The default value is 1.00.
   * - Brightness
     - Float
     - Set the brightness expression. The value must be a float value in range -1.00 to 1.00. The default value is 0.00.
   * - Saturation
     - Float
     - Set the saturation expression. The value must be a float in range 0.00 to 5.00. The default value is 1.00.
   * - Gamma
     - Float
     - Set the gamma expression. The value must be a float in range 0.00 to 3.00. The default value is 1.00.
   * - Red / Green / Blue Gamma
     - Float
     - Set the gamma expression for red, green or blue. The value must be a float in range 0.00 to 3.00. The default value is 1.00.
   * - Gamma Weight
     - Float
     - Set the gamma weight expression. It can be used to reduce the effect of a high gamma value on bright image areas, e.g. keep them from getting over amplified and just plain white. The value must be a float in range 0.00 to 1.00. A value of 0.0 turns the gamma correction all the way down while 1.00 leaves it at its full strength. Default is 1.00.
