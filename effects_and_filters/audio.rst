.. meta::
   :description: Mix audio in Kdenlive video editor
   :keywords: KDE, Kdenlive, timeline, audio mixer, multiple audio streams, audio recording, documentation, user manual, video editor, open source, free, learn, easy


.. metadata-placeholder

   :authors: - Eugen Mohr


   :license: Creative Commons License SA 4.0

.. _effects-audio_tools:

===========
Audio Tools
===========

Kdenlive has some tools for handling audio. Beside the audio spectrum viewer and some audio effects, you have following possibilities:

.. _audio_mixer:

Audio Mixer
~~~~~~~~~~~

.. versionadded:: 19.12.0

.. versionchanged:: 22.08

.. figure:: /images/audio-mixer_23-08.webp
   :alt: Audio-Mixer

The audio mixer has following functions for each channel:

1.	Channel number (audio track number) or Master channel
2.	Mute an audio channel
3.	Solo an audio channel
4.	:ref:`Record audio <audio-recording>` direct on the track of the related audio channel
5.	Opens the effect stack of the related audio channel
6.	Balance the audio channel. Either with the slider or with values
7.	Adjustment of the volume

Multiple audio streams
~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 20.08.0

Multiple audio streams of a video clip. In clip properties on the tab audio you can adjust and manipulate each audio stream. For more details see the chapter :ref:`audio_properties`
  
.. _audio-recording:

Audio recording
~~~~~~~~~~~~~~~

.. versionchanged:: 22.08

.. figure:: /images/kdenlive2405_show-record-controls.webp
   :align: left
   :alt: sow recording controls

.. rst-class:: clear-both

Right click the track head and enable :guilabel:`Show Record Controls` or pressing the :guilabel:`mic` button in the mixers (number 4 in above picture) displays the track head record control which get colorized. It's now in audio monitoring mode (levels show mic input and volume slider selects the mic level).


.. image:: /images/audio-record.png
   :alt: audio-record

.. rst-class:: clear-both

While recording you see a live waveform appearing on timeline.


.. figure:: /images/audio-countdown.png
   :width: 40%
   :alt: audio-countdown

   Disable countdown see :ref:`Configure Capture Audio<configure_capture_audio>` settings

.. .. versionchanged:. 24.05

**Recording while timeline is playing** 

- Hit :kbd:`spacebar` to start timeline playback when monitoring.

- Press :kbd:`r` or click the :guilabel:`record` button will pause timeline playback. :kbd:`Spacebar` start recording.

**Direct recording** 

- *Start record:* press :kbd:`r` or click the :guilabel:`record` button on the track head. A countdown start in project monitor (disable countdown see :ref:`Configure Capture Audio<configure_capture_audio>` settings).

- *Pause:* press :kbd:`spacebar`

- *To resume:* press :kbd:`spacebar` again

- *Stop record:* press :kbd:`esc` or click the :guilabel:`record` button in the track head. The audio clip get added in the timeline and project bin.

After the recording is finished the audio file get created and stored in the project bin or :doc:`folder you have defined </project_and_asset_management/capturing_audio>`. The "focus" is still on the timeline. You can continue to use keyboard shortcuts to move around the newly inserted recording, like jumping to the end of it or the beginning, or the next clip.