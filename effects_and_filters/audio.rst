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

.. .. versionadded:: 19.12.0

.. .. versionchanged:: 22.08

..  .. versionchanged:: 22.08
   Revamp audio mixer and levels

.. figure:: /images/effects-and-filer_audio-mixer_2508.webp
   
The audio mixer has following functions for each channel:

:1:	Channel number (audio track number or name) and Master channel
:2:	Mute an audio channel
:3:	Solo an audio channel
:4:	:ref:`Record audio <audio-recording>` directly on the track of the related audio channel
:5:	Opens the effect stack of the related audio channel
:6:   Toggles the audio track controls on and off
:7:	Change the balance of the audio channel. You can use the slider or enter values.
:8:	Adjustment of the volume
:9:   :kbd:`RMB` shows the menu where you can adjust the audio level appearance. These settings control the level appearance on clip and project monitor simultaneously.
:10:  Hovering over the level shows the dB value of each channel

.. figure:: /images/effects-and-filer_monitor-level_2508.webp
   
   Monitor level. When 6 channels are playing the dB value are hidden.

Monitors. If you have more than 2 audio channels, the audio dB value is not shown (ticks will still be shown). Hover over the widget and it shows the meter and the dB value per channel.


Multiple audio streams
~~~~~~~~~~~~~~~~~~~~~~

.. .. versionadded:: 20.08.0

Multiple audio streams of a video clip. In clip properties on the tab audio you can adjust and manipulate each audio stream. For more details see the chapter :ref:`audio_properties`
  
.. _audio-recording:

Audio recording
~~~~~~~~~~~~~~~

.. .. versionchanged:: 22.08

.. figure:: /images/kdenlive2405_show-record-controls.webp
   :align: left
   
.. rst-class:: clear-both

Right click the track head and enable :guilabel:`Show Record Controls` or pressing the :guilabel:`mic` button in the mixers (number 4 in above picture) displays the track head record control which get colorized. It's now in audio monitoring mode (levels show mic input and volume slider selects the mic level).


.. figure:: /images/audio-record.png
   
.. rst-class:: clear-both

While recording you see a live waveform appearing on timeline.


.. figure:: /images/audio-countdown.png
   :width: 40%
   
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