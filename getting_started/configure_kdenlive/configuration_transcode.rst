.. meta::
   :description: Kdenlive Documentation - Configuration Transcode
   :keywords: KDE, Kdenlive, documentation, user manual, configuration, preferences, transcode, video editor, open source, free, learn, easy


.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |ffmpeg| raw:: html

   <a href="https://ffmpeg.org" target="_blank">ffmpeg</a>


Transcode
---------

This controls the :ref:`transcode` functionality. The parameters section are ffmpeg parameters. Find help on them by issuing ``ffmpeg -h`` at a command line.

.. figure:: /images/getting_started/configure_transcode_2412.webp
   :width: 700px
   :figwidth: 700px
   :alt: Kdenlive_Configure_transcode

   Configure section Transcode

:1: List of all available transcoding profiles

:2: :guilabel:`Description` shows the short description of the selected profile.

:3: :guilabel:`Audio only` indicates if this is an audio-only transcoding profile.

:4: :guilabel:`Extension` shows the file type / extension used for the transcoded video file.

:5: :guilabel:`Parameters` lists the |ffmpeg| parameters used in the selected profile. You can change and add parameters here.

:6: :guilabel:`Add profile` - create a new transcoding profile. :guilabel:`Update Profile` - to save changes made for the selected profile (see **5**). :guilabel:`Delete Profile` - deletes the selected profile.


.. .. rubric:: Transcode Options

.. not needed?
   .. list-table::
   :header-rows: 1
   :class: table-wrap

.. * -  Option 
    -  Description 
    -  Parameters 
    -  Meanings of Parameters
  * -  Wav 48000Hz 
    -  Extract audio as WAV file 
    -  :code:`-vn -ar 48000`
    -  | -vn = disable video,
       | -ar 48000 = set audio sampling rate to 48kHz
  * -  Remux with MKV 
    -  
    -  :code:`-vcodec copy -acodec copy -sn`
    -  copy the video and the audio; -sn = disable subtitles 
  * -  Remux MPEG-2 PS/VOB 
    -  Fix audio sync in MPEG-2 vob files 
    -  :code:`-vcodec copy -acodec copy`
    -  copy the video and the audio 