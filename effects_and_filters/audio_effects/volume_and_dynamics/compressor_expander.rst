.. meta::
   :description: Kdenlive Audio Effects - Compressor/Expander
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, audio effects, volume, dynamics, compressor, expander
   
.. metadata-placeholder

   :authors: - Bushuev (https://userbase.kde.org/User:Bushuev)
             - TheMickyRosen-Left (https://userbase.kde.org/User:TheMickyRosen-Left)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Compressor/Expander
===================

.. figure:: /images/effects_and_compositions/kdenlive2308_effects-compressor_expander.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-audio| Compressor/Expander

   :Status:
      Maintained
   :Keyframes:
      No
   :Source library:
      avfilter 
   :Available:
      |linux| |appimage| |windows| |apple|
   :On Master only:
      No
   :Known bugs:
      No

.. rst-class:: clear-both


.. rubric:: Description

Compresses or expands the audio's dynamic range.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description

   * - **Attacks**
     - Float
     - Sets time in fractions of a second over which increase of volume is determined
   * - **Decays**
     - Float
     - Sets time in fractions of a second over which decrease of volume is determined
   * - **Soft-Knee**
     - Float
     - Reduces maximum volume peaks (:abbr:`dB (decibels)`)
   * - **Gain**
     - Float
     - Increases the overall volume  (:abbr:`dB (decibels)`)
   * - **Initial Volume**
     - Float
     - Sets the initial volume (:abbr:`dB (decibels)`)


.. rubric:: Notes

Compressor/Expander amplifies audio signals depending on their initial volume: low volume signals are left as is or are amplified, high volume signals are reduced. The objective is to level out peaks and valleys in the audio's volume range. This allows to increase the overall volume because the effect will prevent any clipping and hence distortion, which in turn elevates quiet sections. This is an important effect when dealing with voice recording where :guilabel:`Soft-Knee` and :guilabel:`Gain` play an important role. :guilabel:`Soft-Knee` reduces the peaks, and :guilabel:`Gain` raises the overall volume. In most cases the two values are the same or very close. It is not unusual to use values between 4 and up to 10 dB for voice recordings as this is depending on the dynamic range of the speaker.
