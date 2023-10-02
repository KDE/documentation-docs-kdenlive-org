.. meta::
   :description: The Kdenlive User Manual - Notes for Earlier Versions
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, help, learn, easy, earlier version

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

==========================
Notes for Earlier Versions
==========================

This section contains documentation of features from earlier versions that have been changed or even deprecated. It is here for reference in case you are running an earlier version. As such, the paragraphs below are not being maintained.


.. _rendering-vbr:

Variable Bit Rate (earlier version)
-----------------------------------

.. image:: /images/glossary/Kdenlive_Render_dialog_vbr_0.9.10.png
   :width: 400px
   :alt: File rendering dialog Variable Bit Rate - ver 0.9.10

When a variable bitrate (VBR) profile is selected, the :guilabel:`File Size` section displays a drop down for choosing the **Video quality** you want. This quality figure is a codec-dependent number representing the quality of the video that will be rendered. Generally, lower numbers mean higher quality video and larger file sizes (e.g. x264, MPEG2, VPx), but some codecs use opposite order (e.g. Theora). Profiles provided with **Kdenlive** offer these numbers ordered from best quality (almost lossless) to lower quality (still not degrading too much). The exact file size that is produced can not be predicted when using the VBR method. The idea behind this is that you specify a certain quality of video that you want through the entire video and the encoding optimizes bitrate to give you that constant quality, lowering data size for low action scenes and using more bits for high action scenes.

Example: 1min 55 seconds of 720 x 576 H.264 iPhone footage rendered at quality 15 with the H.264/AAC High Profile would produce a file size of 186 Mb. Whereas rendering the same footage at quality quality 20 produced an 83Mb file.

.. _rendering-cbr:

Constant Bit Rate (earlier version)
-----------------------------------

.. note:: |outdated|

.. image:: /images/glossary/Kdenlive_Render_dialog_cbr_0.9.10.png
   :width: 400px
   :alt: File rendering dialog Constant Bit Rate - ver 0.9.10

When a constant bitrate (CBR) profile is selected, the :menuselection:`File Size` section displays a drop down for choosing the **Video bitrate** you want. This is similar to the version <=0.9.8 behaviour of **Kdenlive**. You select the video bitrate you want and the video is encoded at that video bitrate across its entire length.

.. image:: /images/glossary/Kdenlive_Render_dialog_0.9.8.png
   :width: 400px
   :alt: File rendering dialog - ver 0.9.8


.. _rendering-audio_automatic:

Rendering Audio Track Automatically
-----------------------------------

Admittedly, this is an unusual one. Instead of a normal on/off checkbox toggle, the :guilabel:`Export Audio` checkbox cycles among three choices.

.. note:: As if that weren't confusing enough, the :guilabel:`Export audio (automatic)` option may appear different depending on your combination of distribution, desktop environment and theme. See three examples below.

   Regardless of how the checkbox on the :guilabel:`Export audio (automatic)` option may appear on your installation, rest assured that when that option is showing, it is enabled.

So what do the three options mean?

.. image:: /images/glossary/kdenlive2108_rendering-audio_automatic.webp
   :align: left
   :alt: kdenlive2108_rendering-audio_automatic

*Export audio (automatic)* means detect if an audio track is present and write the audio track if found

.. container:: clear-both

   .. image:: /images/glossary/kdenlive2108_rendering-audio_checked.webp
      :align: left
      :alt: kdenlive2108_rendering-audio_checked

   *Export audio*, when checked, means write an audio track in the rendered file even if there is no audio track to write.

.. container:: clear-both

   .. image:: /images/glossary/kdenlive2108_rendering-audio_unchecked.webp
      :align: left
      :alt: kdenlive2108_rendering-audio_unchecked

   *Export audio*, when unchecked, means do not write an audio track in the rendered file.

.. rst-class:: clear-both

The difference in behavior between enabling *Export audio* versus *Export audio (automatic)* can be seen in the situation where you have a video on the timeline but there is no audio track on the timeline and the video in the video track also does not have an audio track. An example of such a situation is shown in the screenshot below.

.. image:: /images/glossary/Kdenlive_Video_with_no_audio.png
   :alt: Kdenlive_Video_with_no_audio

In this situation, if you render with *Export audio (automatic)*, the rendered file will not have an audio track (Result 1 on screenshot below). But if you render with *Export Audio* checked, then the rendered file will contain an audio track – the track will however be empty (Result 2 on screenshot below).

.. image:: /images/glossary/Kdenlive_Render_export_audio_auto_vs_just_checked2.png
   :alt: Kdenlive_Render_export_audio_auto_vs_just_checked2

FFprobe on file generated from an audio-less track using *Export audio (automatic)*. Note only one stream – Stream #0.0 – a video stream. **Kdenlive** automatically detected there was not an audio track and so it did not write one.

.. code-block:: bash

  $ ffprobe dog_rotated_exp_audio_auto.mp4

.. code-block:: bash

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

.. code-block:: bash

    Metadata:
      major_brand     : isom
      minor_version   : 512
      compatible_brands: isomiso2avc1mp41
      encoder         : Lavf53.21.1
    Duration: 00:00:03.62, start: 0.000000, bitrate: 12598 kb/s

  Stream #0.0(und): Video: h264 (High), yuv420p, 1280x720 [PAR 1:1 DAR 16:9], 12587 kb/s, 27.83 fps, 27.83 tbr, 30k tbn, 55.66 tbc
  Stream #0.1(und): Audio: aac, 48000 Hz, stereo, s16, 2 kb/s

In cases where there is an audio track ...

.. image:: /images/glossary/Kdenlive_Video_plus_Audio_in_seperate_tracks.png
   :align: left
   :alt: Kdenlive_Video_plus_Audio_in_seperate_tracks

Rendering with :guilabel:`Export audio` unchecked will produce a file with no audio track – result 4 in the screenshot above.
Rendering with :guilabel:`Export audio (automatic)` (result 3 in the screenshot above) or with *Export audio* checked will produce files with Audio tracks.
