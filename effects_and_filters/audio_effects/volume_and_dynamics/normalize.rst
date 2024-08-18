.. meta::
   :description: Kdenlive Audio Effects - Normalize
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, audio effects, volume, dynamics, normalize
   
.. metadata-placeholder

   :authors: - Bushuev (https://userbase.kde.org/User:Bushuev)
             - TheMickyRosen-Left (https://userbase.kde.org/User:TheMickyRosen-Left)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Normalize
=========

.. figure:: /images/effects_and_compositions/kdenlive2308_effects-normalize.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-audio| Normalize

   :Status:
      Maintained
   :Keyframes:
      No
   :Source library:
      mlt 
   :Available:
      |linux| |appimage| |windows| |apple|
   :On Master only:
      No
   :Known bugs:
      No

.. rst-class:: clear-both


.. rubric:: Description

This filter adjusts the level of the audio based on the loudness of the input. It performs loudness measurement over a specified sliding window of time. Then, it adjusts the gain on the output based on the difference between the measured loudness and the target loudness in order to achieve the desired loudness.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description

   * - **Target Program Loudness**
     - Float
     - The target program loudness in :abbr:`LUFS (Loudness Units Full Scale)`
   * - **Measurement Window**
     - Integer
     - The duration of time in seconds over which the loudness is calculated
   * - **Maximum Gain Increase**
     - Integer
     - The maximum amount that the gain will be increased by the filter (:abbr:`dB (decibels)`)
   * - **Maximum Gain Decrease**
     - Integer
     - The maximum amount that the gain will be decreased by the filter (:abbr:`dB (decibels)`)
   * - **Maximum Rate Change**
     - Float
     - (:abbr:`dB (decibels)` per second)


.. rubric:: Notes

The objective of a normalization is to raise the audio level to its set maximum while the loudest part of the audio must not be exceeded. Normally, normalization is useful if the audio signal was low already during recording due to wrong or faulty settings in the recording device or too big of a distance between microphone and audio source.