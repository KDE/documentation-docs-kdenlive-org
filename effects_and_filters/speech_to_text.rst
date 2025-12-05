.. meta::
   :description: Kdenlive Documentation - Speech to Text
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, help, speech to text, silence detection

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Jean-Baptiste Mardelle <jb@kdenlive.org>
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Vincent Pinon <vpinon@kde.org>
             - Jessej (https://userbase.kde.org/User:Jessej)
             - Jack (https://userbase.kde.org/User:Jack)
             - Roger (https://userbase.kde.org/User:Roger)
             - TheMickyRosen-Left (https://userbase.kde.org/User:TheMickyRosen-Left)
             - Eugen Mohr
             - Smolyaninov (https://userbase.kde.org/User:Smolyaninov)
             - Tenzen (https://userbase.kde.org/User:Tenzen)
             - Anders Lund
             - Bernd Jordan  (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. .. versionadded:: 21.04.0

.. _effects-speech_to_text:

Speech to Text
==============

.. warning:: Speech to text does not work with version 21.04.2 due to `Vosk API <https://github.com/alphacep/vosk-api>`_ issues. Use version 21.04.1 or 21.04.3 and later versions.


Before you can use Speech to Text, it must be properly configured and speech models installed. Please refer to the chapter :doc:`Configure Speech to Text</getting_started/configure_kdenlive/configuration_plugins>`.

.. hint:: While you can configure and set up both, VOSK and Whisper, for speech recognition, the engine that is selected in the :doc:`Speech to Text</getting_started/configure_kdenlive/configuration_plugins>` configuration section is being used for speech recognition the next time you use this feature. You can switch back and forth during editing, of course, and use different engines for different purposes. The Speech Editor widget has a menu entry to quickly access the configuration section bypassing the :menuselection:`Menu --> Settings --> Configure Kdenlive -->` :doc:`Speech to Text</getting_started/configure_kdenlive/configuration_plugins>` route.


Speech Recognition
------------------

There are two use cases for speech recognition:

1. Creating subtitles automatically
2. Creating :ref:`transcripts<creating_clips_by_speech_recognition>` and the ability to :ref:`add clips to the timeline<creating_clips_by_speech_recognition>` based on the transcript

.. Select the Speech Engine
   ~~~~~~~~~~~~~~~~~~~~~~~~

.. .. versionadded:: 23.04

..   If not already part of your workspace layout, enable the Speech Editor via :menuselection:`Menu --> View --> Speech Editor`.

..   .. figure:: /images/Speech-to-text_select_speech-engine.png
   :align: left
   :width: 500px
   :figwidth: 500px
   :alt: change the speech engine

   .. rst-class:: clear-both

   Click on the |application-menu|:guilabel:`Hamburger Menu` and select :guilabel:`Configure Speech Recognition`. This brings you to :ref:`Configure Speech to Text <configure_speech_to_text>`, select the engine and click :guilabel:`OK.`

   :guilabel:`Translate to english` is only available with the Whisper speech engine. It translates non-English text to English during recognition.

   .. figure:: /images/kdenlive2405_speech-to-text_Show-log.webp
   :align: left
   :width: 300px
   :figwidth: 300px
   :alt: Speech to text show log

   .. rst-class:: clear-both

   If an error occurs or an important message happens, click on the :guilabel:`Show log` to open the log file.


Creating Subtitles using VOSK Speech Recognition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. .. versionchanged:: 24.05

If not yet created, add a subtitle track by clicking on the |add-subtitle|\ :guilabel:`Edit Subtitle Tool` icon in the Timeline tool bar (**6**).

.. figure:: /images/effects_and_compositions/s2t_subs_vosk_2412.webp
   :width: 700px
   :figwidth: 700px
   :alt: Speech to text subtitle

   Automatic subtitle generation using the VOSK engine

:1: |tools-wizard|\ :guilabel:`Speech recognition`. Click here to open the **Automatic Subtitling** dialog window.

:2: Timeline Zone. More details about Timeline Zones can be found in the chapter :ref:`timeline_ruler`.

:3: Choose which part of the timeline should be used for speech recognition

:4: :guilabel:`Process`. Click to start the recognition

:5: :guilabel:`Model`. Select the model for the language of the subtitles. You can install more models in the Configuration section :doc:`Speech to Text</getting_started/configure_kdenlive/configuration_plugins>`.

:6: |add-subtitle|\ :guilabel:`Edit Subtitle Tool`. Click to open or close the subtitle track.

.. rubric:: Steps to create subtitles using VOSK speech recognition
   
(numbers in brackets point to the GUI element in the screenshot above):

#. |tools-wizard|\ :guilabel:`Speech recognition` (**1**). Click here to open the **Automatic Subtitling** dialog window.

#. If needed, define a timeline zone (**2**) for which you want to use speech recognition. More details about Timeline Zones can be found in the chapter :ref:`timeline_ruler`.

#. :guilabel:`Model` (**5**). Select the model for the language of the subtitles. You can install more models in the Configuration section :doc:`Speech to Text</getting_started/configure_kdenlive/configuration_plugins>`.

#. Choose which part of the timeline should be used for speech recognition (**3**)

#. :guilabel:`Process` (**4**). Click to start the subtitle creation.

The subtitle is created and inserted automatically.

Remark to step **4**: The default is to analyze only the :guilabel:`Timeline zone (all tracks)` (**2** in the screenshot above). Set the timeline zone to what you want to analyze (use :kbd:`I` and :kbd:`O` to set in and out points). :guilabel:`Selected clips` option analyses the selected clip only.


Creating Subtitles using WHISPER Speech Recognition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. .. versionchanged:: 24.05

If not yet created, add a subtitle track by clicking on the |add-subtitle|\ :guilabel:`Edit Subtitle Tool` icon in the Timeline tool bar (**11**).

.. figure:: /images/effects_and_compositions/s2t_subs_whisper_2412.webp
   :width: 700px
   :figwidth: 700px
   :alt: Speech to text subtitle Whisper

   Automatic subtitle generation using the Whisper engine

:1: |tools-wizard|\ :guilabel:`Speech recognition`. Click here to open the **Automatic Subtitling** dialog window.

:2: Timeline Zone. More details about Timeline Zones can be found in the chapter :ref:`timeline_ruler`.

:3: Choose which part of the timeline should be used for speech recognition

:4: :guilabel:`Model`. Select the model for the language of the subtitles. You can install more models in the Configuration section :doc:`Speech to Text</getting_started/configure_kdenlive/configuration_plugins>`.

:5: :guilabel:`Process`. Click to start the recognition

:6: :guilabel:`Language`. Default is **Autodetect**. Change to the correct language if not detected properly.

:7: :guilabel:`Maximum character per line`. Define how many characters per line are allowed before a line break is inserted.

:8: :guilabel:`Translate with SeamlessM4T`. Checking this opens adds two more selection fields: One for the :guilabel:`Input language`, and one for the :guilabel:`Output language`. This requires that translation with SeamlessM4T is enabled in the settings (:menuselection:`Menu --> Settings --> Configure Kdenlive --> Speech To Text`). Please refer to the chapter about :doc:`Speech to Text</getting_started/configure_kdenlive/configuration_plugins>`.

:9: :guilabel:`Translate to English`. Select this to use *Whisper* for the translation to English.

:10: |add-subtitle|\ :guilabel:`Edit Subtitle Tool`. Click to open or close the subtitle track.

.. rubric:: Steps to create subtitles using VOSK speech recognition
   
(numbers in brackets point to the GUI element in the screenshot above):

#. |tools-wizard|\ :guilabel:`Speech recognition` (**1**). Click here to open the **Automatic Subtitling** dialog window.

#. If needed, define a timeline zone (**2**) for which you want to use speech recognition. More details about Timeline Zones can be found in the chapter :ref:`timeline_ruler`.

#. :guilabel:`Model` (**5**). Select the model for the language of the subtitles. You can install more models in the Configuration section :doc:`Speech to Text</getting_started/configure_kdenlive/configuration_plugins>`.

#. Choose which part of the timeline should be used for speech recognition (**3**)

#. :guilabel:`Process` (**4**). Click to start the subtitle creation.

The subtitle is created and inserted automatically.

Remark to step **4**: The default is to analyze only the :guilabel:`Timeline zone (all tracks)` (**2** in the screenshot above). Set the timeline zone to what you want to analyze (use :kbd:`I` and :kbd:`O` to set in and out points). :guilabel:`Selected clips` option analyses the selected clip only.


.. _Translate_with_SeamlessM4T:

.. rubric:: Translate with SeamlessM4T

.. figure:: /images/effects_and_compositions/s2t_subs_whisper_SM4T_1_2412.webp
   :align: left
   :width: 300px
   :figwidth: 300px
   :alt: Whisper SeamlessM4T: Choose input and output language

   Translating with SeamlessM4T

Select :guilabel:`Input Language` and :guilabel:`Output Language` and click :guilabel:`Process`.

This will first process the audio using *Whisper*, then start the *SeamlessM4T* translation. Translation can occupy 100% RAM, 100% CPU and 100% disk access.

.. rst-class:: clear-both

.. attention::
   If the 9GB model has not yet been downloaded, it will be downloaded now. With a 100MB/s download speed this will take about 12 minutes!

   During download Kdenlive will react as normal. Do not click on :guilabel:`Close`, otherwise the download is stopped. 

.. figure:: /images/effects_and_compositions/s2t_subs_whisper_SM4T_2_2412.webp
   :align: left
   :width: 300px
   :figwidth: 300px
   :alt: Whisper SeamlessM4T choose input and output language

Don't worry if you see such a message on the box below :guilabel:`Initializing translation model` while the download is running.

Depending on your internet connection and bandwidth, downloading the model can take quite some time (about 12 minutes with 100MB/s download speed). 

Once the translation model is downloaded, translation will start.

.. rst-class:: clear-both

.. This has been moved to the Configure Kdenlive section
.. .. figure:: /images/kdenlive2405_speech-to-text_Whisper_SeamlessM4T.webp
   :width: 500px
   :figwidth: 500px
   :alt: On Whisper SeamlessM4T installed

   SeamlessM4T is enabled and downloaded successful

   The SeamlessM4T models are stored here:

   :Linux: :file:`$HOME/.cache/huggingface`

   :Windows: :file:`C:\\Users\\<username>\\.cache\\huggingface`


.. _creating_clips_by_speech_recognition:

.. .. versionadded:: 24.02
   Create new sequence with edit
   Zoom in Zoom out

.. .. versionchanged:: 24.12
   Zoom in/out changed to increase/decrease font and moved to tool bar


.. _effect_s2t_transcribing_speech:

Creating Clips using Speech Recognition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is useful for interviews and other speech-related footage. Go to the Speech Editor widget. If not yet enabled, do so via :menuselection:`Menu --> View --> Speech Editor`.

.. note:: Using speech recognition to create transcripts and create clips from that, is only possible with clips in the **Project Bin**.

.. figure:: /images/effects_and_compositions/speech_editor_2412.webp
   :width: 700px
   :figwidth: 700px
   :alt: Speech editor

   Shown with the VOSK engine and Search (10) enabled

Select a clip in the **Project Bin**.

:1: If needed, set in and out points in the **Clip Monitor** and check :guilabel:`Selected zone only`. This will only transcribe text inside that zone.

:2: Click on |application-menu|\ :guilabel:`Hamburger Menu` and choose the model for the correct language when the *VOSK* engine is set for speech recognition. If the *Whisper* engine is selected, you can select :guilabel:`Translate to English` if needed. You select the speech recognition engine in :menuselection:`Menu --> Settings --> Configure Kdenlive --> Speech to Text`. Click on :guilabel:`Configure Speech Recognition` to open the configuration section for Speech to Text. For more details about the configuration refer to the chapter :doc:`Configure Speech to Text</getting_started/configure_kdenlive/configuration_plugins>`.

:3: Press the :guilabel:`Transcribe` button.

:4: Select the text you want. Holding :kbd:`CTRL` or :kbd:`Shift` to select several texts.

:5: :guilabel:`Create new sequence with edit` creates a new sequence with each timecode-text as a single clip. :guilabel:`Insert selection in timeline` creates clips for each selected timecode-text starting at the playhead's position. :guilabel:`Save edited text in a playlist file` creates an asset in the project bin with the entire transcribed text. 

:6: |format-font-size-more|\ :guilabel:`Increase font size` and |format-font-size-less|\ :guilabel:`Decrease font size` decrease, respectively, increase the font size.

:7: |bookmark-new|\ :guilabel:`Add marker` adds a marker for the timecode of the selected text. More details about *Guides* and *Markers* are available in the chapter about :doc:`/cutting_and_assembling/guides`.

:8: |edit-delete|\ :guilabel:`Delete selection` deletes the selected text.

:9: :guilabel:`Remove non speech zones` deletes all "No speech" entries at once.

:10: |edit-find|\ :guilabel:`Search in text` toggles the search field. Enter text you want to find in the transcribed text. Search is not case sensitive and finds all occurrences of the string even within words. |go-up| and |go-down| navigate to the next occurrence of the search term. If the search field turns reddish you have reached the last occurrence of the search term in the text.


.. _effects-s2t_silence_detection:

Silence Detection
-----------------

.. note:: This works with the VOSK engine only.

Select the clip in the **Project Bin** and open the speech editor window (:menuselection:`Menu --> View --> Speech Editor`) .

Click on |application-menu|:guilabel:`Hamburger Menu` and choose the model for your language. If the right model is not listed, click on :guilabel:`Configure Speech Recognition`. For details about how to add models for the *VOSK* engine refer to the chapter about :doc:`/getting_started/configure_kdenlive/configuration_plugins`.

Then click :guilabel:`Start Recognition` button.

Once this is done, choose under point 6 from above to :guilabel:`Remove non speech zones` at once. Or click on the time-code where "No speech" is indicated (hold :kbd:`Ctrl` to select several items at once) and just hit the :kbd:`Delete` key. 

Repeat the operation for all the parts you want to remove, including where someone says what you do not want to include in your final edit.

Once finished, make sure :guilabel:`Selected zone only` is disabled, click on the :guilabel:`Save edited text in a playlist file` button (above under point 5) and after few seconds a new playlist is added in the Project Bin without silence and without the text you do not want.
