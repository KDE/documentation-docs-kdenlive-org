.. meta::
   :description: Kdenlive Tips & Tricks - Render Profile Parameters and How to Read Them
   :keywords: KDE, Kdenlive, render, parameter, documentation, user manual, video editor, open source, free, help, learn, render, render profile, render parameter

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jack (https://userbase.kde.org/User:Jack)
             - Roger (https://userbase.kde.org/User:Roger)
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |ffmpeg_project| raw:: html

   <a href="https://ffmpeg.org/about.html" target="_blank">ffmpeg project</a>

.. |ffmpeg_options| raw:: html

   <a href="https://ffmpeg.org/ffmpeg.html#Options" target="_blank">ffmpeg options</a>

.. |mlt_presets| raw:: html

   <a href="https://www.mltframework.org/docs/presets/" target="_blank">MLT Presets</a>

  
.. _render_profile_parameters:

Render Profile Parameters Explained
===================================

.. .. versionchanged:: 22.04

.. |image_1| image:: /images/tips_and_tricks/render_parameters_1.webp
   :width: 200px

.. |image_2| image:: /images/tips_and_tricks/render_parameters_2.webp
   :width: 200px

.. |image_3| image:: /images/tips_and_tricks/render_parameters_3.webp
   :width: 200px
   
|image_1| |image_2| |image_3|

Property Presets
----------------

Kdenlive now makes use of *property presets* delivered by the **melt** project (see |mlt_presets|). These presets are referenced by the *properties=<preset>* syntax. In the example illustrated, the render profile is referencing *lossless/H.264*. This refers to a property preset found in file H.264 found on the system at

:Windows: :file:`C:\\Program Files\\kdenlive\\share\\mlt\\presets\\consumer\\avformat\\lossless`
:Linux: :file:`/usr/share/mlt/presets/consumer/avformat/lossless`

On a default install, all the *<presets>* referenced in the render settings in Kdenlive will be referring to presets found in

:Windows: :file:`C:\\Program Files\\kdenlive\\share\\mlt\\presets\\consumer\\avformat\\`
:Linux: :file:`/usr/share/mlt/presets/consumer/avformat/`

You reference presets found in subdirectories of this folder using a ``<subdirname>/<profile>`` syntax as shown in the example above.

.. code-block:: cfg
  :emphasize-lines: 1

  properties=lossless/H.264
  g=120
  crf=%quality
  ab=%audiobitrate+'k'

The preset files found at :file:`/usr/share/mlt/presets/consumer/avformat/` and :file:`C:\\Program Files\\kdenlive\\share\\mlt\\presets\\consumer\\avformat\\`, respectively, are simple text files that contain the *melt* parameters that define the rendering. An example is shown below. These are the same parameters that were used in earlier versions of Kdenlive.

Contents of :file:`lossless/H.264`:

.. code-block:: cfg

  f=mp4
  acodec=aac
  ab=384k
  vcodec=libx264
  intra=1
  vb=0
  g=0
  bf=0
  preset=medium
  qscale=1
  qp=0
  coder=ac

  <!--T:28-->
  meta.preset.extension=mp4
  meta.preset.note=Intra-frame only, lossless compressed MPEG-4 AVC with AAC audio

.. not sure why this section is here:
   Scanning Dropdown
   -----------------

   .. figure:: /images/glossary/render_dialog_21-08_scanning.png
         :align: left

   This option controls the frame scanning setting the rendered file will have.
   Options are *Force Progressive*, *Force Interlaced* and *Auto*.

   :menuselection:`Auto` causes the rendered file to take the scanning settings that are defined in the :ref:`project_settings`. Use the other options to override the setting defined in the project settings.


How to Read Them
----------------

Essentially, the parameters are instructions for ffmpeg which is used for encoding the video and audio streams. Hence it should not come as a surprise that the parameters are well documented by the |ffmpeg_project|.

In the example above the parameters are:

.. code-block:: cfg

  f=mp4
  acodec=aac
  ab=384k
  vcodec=libx264
  intra=1
  vb=0
  g=0
  bf=0
  preset=medium
  qscale=1
  qp=0
  coder=ac

Another example for DVD output:

.. code-block:: cfg

  f=dvd
  vcodec=mpeg2video
  acodec=mp2
  b=5000k
  maxrate=8000k
  minrate=0
  bufsize=1835008
  mux_packet_s=2048
  mux_rate=10080000
  ab=192k
  ar=48000
  s=720x576
  g=15
  me_range=63
  trellis=1
  profile=dv_pal_wide
  pass=2

Looking up the |ffmpeg_options| translates these parameters as follows:

Main option is:

.. code:: cfg

  -f fmt            force format

Video options are:

.. code:: cfg

  -vcodec codec     force video codec ('copy' to copy stream)
  -pass n           select the pass number (1 or 2)
  -b bitrate        set bitrate (in bits/s)
  -vb bitrate       set video bitrate (in bits/s)
  -s size           set frame size (WxH or abbreviation)
  -me_range         limit motion vectors range (1023 for DivX player)
  -trellis          rate-distortion optimal quantization

Audio options are:

.. code-block:: cfg

  -acodec codec     force audio codec ('copy' to copy stream)
  -ab bitrate       set audio bitrate (in bits/s)
  -ar rate          set audio sampling rate (in Hz)

The AVCodecContext AVOptions include:

.. code-block:: cfg

  -b                set bitrate (in bits/s)
  -maxrate          set max video bitrate tolerance (in bits/s)
  -minrate          set min video bitrate tolerance (in bits/s)
  -g                set the group of picture size

All the render profile options are documented in the **ffmpeg** documentation.

See also |mlt_presets| for more details on the MLT preset property.