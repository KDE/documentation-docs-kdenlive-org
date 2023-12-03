.. meta::

   :description: Kdenlive Video Effects - Dance
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, on master, dance

.. metadata-placeholder

   :authors: - Roger (https://userbase.kde.org/User:Roger)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Dance
=====

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-dance.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: denlive2304_effects-dance

.. sidebar:: |kdenlive-show-video| Dance

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      MLT
   :**Source filter**:
      dance
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      Yes
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter is an audio visualization effect that zooms, moves and rotates the image proportional to the magnitude of the audio spectrum.

Using the :guilabel:`Zoom` alone creates a cool pump effect in sync with the beats.


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
     - The low end of the frequency range to be used to influence the image motion (:abbr:`Hz (Hertz)`)
   * - High Frequency
     - Integer
     - The high end of the frequency range to be used to influence the image motion (:abbr:`Hz (Hertz)`)
   * - Level Threshold
     - Integer
     - The minimum amplitude of sound that must occur within the frequency range to cause the image to move (:abbr:`dB (decibel)`)
   * - Oscillation
     - Integer
     - Oscillation can be useful to make the image move back and forth during long periods of sound (:abbr:`Hz (Hertz)`). A value of 0 specifies no oscillation.
   * - Initial Zoom
     - Percent
     - The amount to zoom the image before any motion occurs. This can be used to avoid black on the sides of the image when it moves.
   * - Zoom
     - Percent
     - The amount that the audio affects the zoom of the image.
   * - Left / Right
     - Percent
     - The amount that the audio affects the left / right offset of the image.
   * - Up / Down
     - Percent
     - The amount that the audio affects the up / down offset of the image.
   * - Clockwise / Counter Clockwise
     - Degree
     - The amount that the audio affects the rotation of the image.
   * - Window Size
     - Integer
     - The number of samples that the FFT\ [1]_ will be performed on. If :guilabel:`Window Size` is less than the number of samples in a frame, extra samples will be ignored. If :guilabel:`Window Size` is more than the number of samples in a frame, samples will be buffered from previous frames to fill the window. The buffering is performed as a sliding window so that the most recent samples are always transformed.


:guilabel:`Initial Zoom`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - 100%
     - no zoom
   * - < 100%
     - zoom out (make the image smaller)
   * - > 100%
     - zoom in (make the image larger)


:guilabel:`Zoom`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - < 0%
     - Image will zoom out (get smaller) with more sound
   * - 0%
     - no zoom
   * - > 0%
     - Image will zoom in (get larger) with more sound


:guilabel:`Left / Right`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - 0%
     - no offset
   * - > 0%
     - Image will move left / right with more sound


:guilabel:`Up / Down`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - 0%
     - no offset
   * - > 0%
     - Image will move up / down with more sound


:guilabel:`Clockwise / Counter Clockwise`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - 0%
     - no rotation
   * - > 0%
     - Image will rotate with more sound


----

.. [1] FFT := Fast Fourier Transform


.. https://youtu.be/gqxU1nvh6JI

