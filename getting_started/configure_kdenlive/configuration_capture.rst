.. meta::
   :description: Kdenlive Documentation - Configuration Capture
   :keywords: KDE, Kdenlive, documentation, user manual, configuration, preferences, capture, screengrab, screen grab, decklink, audio capture, video capture, video editor, open source, free, learn, easy


.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |blackmagic| raw:: html

   <a href="https://www.blackmagicdesign.com" target="_blank">Blackmagic</a>

.. |decklink| raw:: html

   <a href="https://www.blackmagicdesign.com/products/decklink" target="_blank">Decklink</a>


Capture
-------

This section configures the capturing of audio and video. Kdenlive allows to capture video using :doc:`ScreenGrab</project_and_asset_management/capturing_video>` and a |blackmagic| |decklink| card, and :doc:`audio</project_and_asset_management/capturing_audio>` with the devices available on your system.


.. _configure_capture_screengrab:

ScreenGrab
~~~~~~~~~~

.. figure:: /images/getting_started/configure_capture_screengrab_2412.webp
   :width: 700px
   :figwidth: 700px
   
   Configure section Capture: ScreenGrab with Rectangular Region selected

:1: :guilabel:`Region to Capture`. Default is **Full screen**. Selecting **Rectangular Region** opens a panel with additional parameters (as shown in the figure above).

:2: :guilabel:`Follow mouse`. If checked, the defined rectangular follows the mouse. :guilabel:`Hide Frame`. If checked, makes the frame defined by the parameters below invisible.

:3: :guilabel:`Offset` - Distance along the x (first parameter) and y axis (second parameter) from the top left corner of the screen. :guilabel:`Size` - Width (first parameter) and height (second parameter) of the rectangle.

:4: :guilabel:`Mouse cursor`. If checked, the mouse pointer will not be recorded.

:5: :guilabel:`Frame rate`. Set the frame rate (fps) for the recording.

:6: :guilabel:`Encoding profile`. Clicking on |configure|\ :guilabel:`Show profile parameters` opens the **Manage Encoding profiles** dialog window (see yellow arrow) to manage the available profiles. Click on |help-about| to display the ffmpeg parameters used in the selected profile.


.. _configure_capture_blackmagic:

Blackmagic
~~~~~~~~~~

If you have a |blackmagic| |decklink| video capture card you can set here the import parameter.

.. figure:: /images/getting_started/configure_capture_blackmagic_2412.webp
   :width: 700px
   :figwidth: 700px
   
   Configure section Capture: Blackmagic DeckLink (encoding parameter window open)

:1: :guilabel:`Detected devices`. Lists the devices you can choose from.

:2: :guilabel:`Encoding profile`. Select the profile to be used for encoding the recording. Clicking on |configure|\ :guilabel:`Show profile parameters` opens the **Manage Encoding profiles** dialog window (see yellow arrow) to manage the available profiles. Click on |help-about| to display the ffmpeg parameters used in the selected profile.

:3: :guilabel:`Capture file name`. Enter the name under which the recording shall be saved to the folder defined in the Environment section.

:4: List of available encoding profile for DeckLink Capture.

:5: ffmpeg parameters for the selected profile

:6: Click on |list-add| to create a new profile based on the selected one, |document-edit| to edit the selected profile, |edit-delete| to delete the selected profile. |edit-download| does not have a function yet. 


.. _configure_capture_audio:

.. .. versionadded:: 22.12
   Disable countdown before recording

Audio
~~~~~

These settings are for configuring the audio device that is used during screen recording and for recording of voice overs. See the chapter about :doc:`Capturing Audio</project_and_asset_management/capturing_audio>`.

.. figure:: /images/getting_started/configure_capture_audio_2412.webp
   :width: 700px
   :figwidth: 700px
   

:1: :guilabel:`Device`. Select the device to be used for recording audio.

:2: :guilabel:`Capture volume`. Use the slider to adjust the volume for the recording.

:3: :guilabel:`Channels`. Select how many channels you want to record. Options are **Stereo (2 channels)** (default), and **Mono (1 channel)**.

:4: :guilabel:`Sample rate`. Select the sample rate for the recording. Options are **48,000Hz** (default) and **44,100Hz**.

:5: :guilabel:`Disable countdown before recording`. If checked, recording will start immediately upon pressing the record button in the audio track (see :doc:`Capturing Audio</project_and_asset_management/capturing_audio>`). By default, a three-second countdown will be used and displayed in the project monitor.