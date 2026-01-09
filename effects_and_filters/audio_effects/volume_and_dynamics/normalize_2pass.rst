.. meta::
   :description: Kdenlive Audio Effects - Normalize (2 Pass)
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, audio effects, volume, dynamics, normalize
   
.. metadata-placeholder

   :authors: - Bushuev (https://userbase.kde.org/User:Bushuev)
             - TheMickyRosen-Left (https://userbase.kde.org/User:TheMickyRosen-Left)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Normalize (2 Pass)
==================

.. figure:: /images/effects_and_compositions/kdenlive2308_effects-normalize_2pass.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-audio| Normalize (2 Pass)

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

This filter requires two passes. It is designed to analyze and apply the normalization based on an entire audio file or an entire track. Click :guilabel:`Analyse to Apply Effect` to start the first pass which performs the analysis and stores the result in the "results" property. The second pass applies the results to the audio in order to achieve the desired loudness over the range of the filter.

If you like to normalize a live stream then use :doc:`Normalize <normalize>`

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


.. rubric:: Notes

The objective of a normalization is to raise the audio level to its set maximum while the loudest part of the audio must not be exceeded. Normally, normalization is useful if the audio signal was low already during recording due to wrong or faulty settings in the recording device or too big of a distance between microphone and audio source.