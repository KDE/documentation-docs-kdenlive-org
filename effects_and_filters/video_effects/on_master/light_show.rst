.. meta::

   :description: Kdenlive Video Effects - Light Show
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, misc, miscellaneous, light show

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Light Show
==========

.. figure:: /images/effects_and_compositions/effects-light_show-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-light_show-2504.webp

.. sidebar:: |kdenlive-show-video| Light Show

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      lightshow
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      Yes
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter is an audio visualization effect that colors the image proportional to the magnitude of the audio spectrum.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Low Frequency
     - Integer
     - The low end of the frequency range to be used to influence the image changes (:abbr:`Hz (Hertz)`)
   * - High Frequency
     - Integer
     - The high end of the frequency range to be used to influence the image changes (:abbr:`Hz (Hertz)`)
   * - Level Threshold
     - Integer
     - The minimum amplitude of sound that must occur within the frequency range to cause the image to be changed (:abbr:`dB (decibel)`)
   * - Oscillation
     - Integer
     - Oscillation can be useful to make the image move back and forth during long periods of sound (:abbr:`Hz (Hertz)`). A value of 0 specifies no oscillation.
   * - 1st / 2nd Color
     - Picker
     - The color of the gradient used for lightening or darkening the image
