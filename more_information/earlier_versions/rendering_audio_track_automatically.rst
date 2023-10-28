.. meta::
   :description: The Kdenlive User Manual - Notes for Earlier Versions - Rendering Audio Track Automatically
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, help, learn, easy, rendering audio track automatically

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Nikerabbit (https://userbase.kde.org/User:Nikerabbit)
             - Simon Eugster <simon.eu@gmail.com>
             - Jean-Baptiste Mardelle <jb@kdenlive.org>
             - Earl fx (https://userbase.kde.org/User:Earl fx)
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Vincent Pinon <vpinon@kde.org>
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jessej (https://userbase.kde.org/User:Jessej)
             - Dbolton (https://userbase.kde.org/User:Dbolton)
             - Jack (https://userbase.kde.org/User:Jack)
             - Roger (https://userbase.kde.org/User:Roger)
             - KGHN (https://userbase.kde.org/User:KGHN)
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _rendering-audio_automatic:

.. attention:: This page is not maintained anymore and contains information referring to features or functions from earlier versions of Kdenlive that are deprecated or have been superseded by something else.

Rendering Audio Track Automatically
===================================

Admittedly, this is an unusual one. Instead of a normal on/off checkbox toggle, the :guilabel:`Export Audio` checkbox cycles among three choices.

.. note:: As if that weren't confusing enough, the :guilabel:`Export audio (automatic)` option may appear different depending on your combination of distribution, desktop environment and theme. See three examples below.

   Regardless of how the checkbox on the :guilabel:`Export audio (automatic)` option may appear on your installation, rest assured that when that option is showing, it is enabled.

So what do the three options mean?

.. image:: /images/earlier_versions/kdenlive2108_rendering-audio_automatic.webp
   :align: left
   :alt: kdenlive2108_rendering-audio_automatic

*Export audio (automatic)* means detect if an audio track is present and write the audio track if found

.. container:: clear-both

   .. image:: /images/earlier_versions/kdenlive2108_rendering-audio_checked.webp
      :align: left
      :alt: kdenlive2108_rendering-audio_checked

   *Export audio*, when checked, means write an audio track in the rendered file even if there is no audio track to write.

.. container:: clear-both

   .. image:: /images/earlier_versions/kdenlive2108_rendering-audio_unchecked.webp
      :align: left
      :alt: kdenlive2108_rendering-audio_unchecked

   *Export audio*, when unchecked, means do not write an audio track in the rendered file.

.. rst-class:: clear-both

The difference in behavior between enabling *Export audio* versus *Export audio (automatic)* can be seen in the situation where you have a video on the timeline but there is no audio track on the timeline and the video in the video track also does not have an audio track. An example of such a situation is shown in the screenshot below.

.. image:: /images/earlier_versions/Kdenlive_Video_with_no_audio.png
   :alt: Kdenlive_Video_with_no_audio

In this situation, if you render with *Export audio (automatic)*, the rendered file will not have an audio track (Result 1 on screenshot below). But if you render with *Export Audio* checked, then the rendered file will contain an audio track – the track will however be empty (Result 2 on screenshot below).

.. image:: /images/earlier_versions/Kdenlive_Render_export_audio_auto_vs_just_checked2.png
   :alt: Kdenlive_Render_export_audio_auto_vs_just_checked2

FFprobe on file generated from an audio-less track using *Export audio (automatic)*. Note only one stream – Stream #0.0 – a video stream. **Kdenlive** automatically detected there was not an audio track and so it did not write one.

.. code-block:: bash

  $ ffprobe dog_rotated_exp_audio_auto.mp4

.. code-block:: cfg

    Metadata:
      major_brand     : isom
      minor_version   : 512
      compatible_brands: isomiso2avc1mp41
      encoder         : Lavf53.21.1
  Duration: 00:00:03.62, start: 0.000000, bitrate: 12592 kb/s
  Stream #0.0(und): Video: h264 (High), yuv420p, 1280x720 [PAR 1:1 DAR 16:9], 12587 kb/s, 27.83 fps, 27.83 tbr, 30k tbn, 55.66 tbc

FFprobe on file generated from an audio-less track using *Export audio* checked. Note two streams – Stream #0.0 and Stream #0.1 – the latter being an aac audio track. We forced **Kdenlive** to write an audio track even though there was not any source audio to write.

.. code-block:: bash

  $ ffprobe dog_rotated_exp_audio.mp4

.. code-block:: cfg

    Metadata:
      major_brand     : isom
      minor_version   : 512
      compatible_brands: isomiso2avc1mp41
      encoder         : Lavf53.21.1
    Duration: 00:00:03.62, start: 0.000000, bitrate: 12598 kb/s

  Stream #0.0(und): Video: h264 (High), yuv420p, 1280x720 [PAR 1:1 DAR 16:9], 12587 kb/s, 27.83 fps, 27.83 tbr, 30k tbn, 55.66 tbc
  Stream #0.1(und): Audio: aac, 48000 Hz, stereo, s16, 2 kb/s

In cases where there is an audio track ...

.. image:: /images/earlier_versions/Kdenlive_Video_plus_Audio_in_seperate_tracks.png
   :align: left
   :alt: Kdenlive_Video_plus_Audio_in_seperate_tracks

Rendering with :guilabel:`Export audio` unchecked will produce a file with no audio track – result 4 in the screenshot above.
Rendering with :guilabel:`Export audio (automatic)` (result 3 in the screenshot above) or with *Export audio* checked will produce files with Audio tracks.