.. meta::
   :description: The Kdenlive User Manual
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
             - Bernd Jordan

   :license: Creative Commons License SA 4.0


.. _effects-speech_to_text:

Speech to Text
==============

.. versionadded:: 21.04.0

.. warning:: Speech to text does not work with version 21.04.2 due to `Vosk API <https://github.com/alphacep/vosk-api>`_ issues. Use version 21.04.1 or 21.04.3 and later versions.


Install Python
--------------
.. |python_download| raw:: html

   <a href="https://www.python.org/downloads/" target="_blank">https://www.python.org/downloads/</a>

Python 3 needs to be installed on your computer (details see below for Linux and Windows). Once Python is installed, :ref:`follow these steps <settings_environment_python>` to put Python into a virtual environment (afterwards Python is copied to the :file:`venv` folder) 

**De-install Python**

To remove the installed :file:`venv` package got to :menuselection:`Settings --> Kdenlive Settings --> Environment --> Python` and :guilabel:`Delete` :file:`venv`.

It will completely remove the :file:`venv` folder with all installed packages. Note that this does not remove the downloaded models (vosk/whisper) that can still take quite some HD space

Linux
~~~~~

On most Linux distributions python is installed by default. You can check if that is the case for you too by running ``python3 -V`` in a terminal. If python is missing just search the internet, there are lots of instructions around.

Windows
~~~~~~~

Download python from |python_download| for installation on your computer.


.. _effects-s2t_install_language:

Speech Engines
--------------

To install the speech engines go to :menuselection:`Settings --> Configure Kdenlive --> Speech to Text`.

VOSK
----

.. Pre 24.02
   **Linux**

   To install VOSK and srt open a terminal and run: ``pip3 install vosk srt``

   **Windows**

   Download this batch file (:download:`Install_vosk_srt.zip </files/Install_vosk_srt.zip>`). After download a double click starts the installations.

.. figure:: /images/kdenlive2402_speech-to-text_vosk_download.webp
   :align: left
   :width: 500px
   :figwidth: 500px
   :alt: Vosk download dependencies

   Vosk is not installed

.. rst-class:: clear-both

When you switch to VOSK for the first time you have to install the missing dependencies first.

Path where VOSK is installed:

- Linux: :file:`~/.local/share/kdenlive/venv/Lib`
- Windows: :file:`%LocalAppData%\\kdenlive\\venv\\Lib`

If you have installed VOSK in an earlier Kdenlive version already and now you have chosen the :file:`venv` folder for Python, you can delete the past installed VOSK libraries by using following command in a console: :file:`pip uninstall vosk srt`

Install a Language
~~~~~~~~~~~~~~~~~~

Goto :menuselection:`Settings --> Configure Kdenlive... --> Speech to Text page` and select the speech engine VOSK.

Click on the link :guilabel:`Download speech models from:` to get a language model.

.. figure:: /images/kdenlive2405_Speech-to-text_Download-link.webp
   :align: left
   :width: 500px 
   :figwidth: 500px
   :alt: download link

.. rst-class:: clear-both

Drag & drop the language you want from the vosk-model download page to the model window, and it will download and extract it for you.

.. figure:: /images/kdenlive2405_Speech-to-text_Download-model.webp
   :align: left
   :width: 500px
   :figwidth: 500px
   :alt: download model

.. rst-class:: clear-both

If you have problems or check for updates click on the :guilabel:`Check configuration` button.

.. .. versionchanged:: 24.05

:guilabel:`Models folder` Show the size of the installed models. Click on the link opens the model folder.

The VOSK speech models are stored here:

Linux: :file:`~/.local/share/kdenlive/speechmodels`

Windows: :file:`%AppData%\\kdenlive\\speechmodels`

Whisper
-------

.. |whisper_source| raw:: html

   <a href="https://github.com/openai/whisper" target="_blank">Whisper source code page</a>

.. versionadded:: 23.04

OpenAI-Whisper is a speech recognition model for general use. It is trained on a large dataset of diverse audio and is capable of performing speech translation, and language identification.

Whisper is slower than VOSK on CPU, but it is more accurate than VOSK. Whisper creates sentences with punctuation marks, even in Base mode.

.. figure:: /images/kdenlive2402_speech-to-text_whisper_download.webp
   :align: left
   :width: 500px
   :figwidth: 500px
   :alt: Whisper download dependencies

   Whisper is not installed

.. rst-class:: clear-both

When you switch to Whisper for the first time you have to install the missing dependencies first (about 2GB to download).

.. .. versionchanged:: 24.05

.. figure:: /images/kdenlive2405_speech-to-text_whisper_installed.webp
   :align: left
   :width: 500px
   :figwidth: 500px
   :alt: Whisper installed

   When all is correct configured, you get this screen.

.. rst-class:: clear-both

Path where Whisper is installed:

- Linux: :file:`~/.local/share/kdenlive/venv/Lib`
- Windows: :file:`%LocalAppData%\\kdenlive\\venv\\Lib`

The Whisper speech models are stored here:

Linux: :file:`~/.local/share/kdenlive/opencvmodels`

Windows: :file:`%AppData%\\kdenlive\\opencvmodels`


:guilabel:`Model` Select the model. More details on the |whisper_source| (default: Base).

:guilabel:`Language` Select the language if Autodetect is not accurate (default: Autodetect)

:guilabel:`Device` For compatibility purposes only CPU is available

:guilabel:`Disable half precision (FP16)` Only for GPU. When Kdenlive detects a NVIDIA GTX 16xx graphic card it disables half precision (FP16) automatically. If you have issues with using GPU you can switch off half precision.

:guilabel:`Translate text to english` This translates non-English text to English during recognition

:guilabel:`Enable translation through SeamlessM4T` This will only enable/disable ``facebook/seamless-m4t-v2-large``. To download and start subtitle translation :ref:`follow these steps <Translate_with_SeamlessM4T>`.  

You can check for updates by clicking on :guilabel:`Check configuration`

If you have installed Whisper in an earlier Kdenlive version already and now you have chosen the :file:`venv` folder for Python, you can delete the past installed Whisper libraries by using following command in a console: :file:`pip uninstall openai-whisper`


Speech recognition
------------------

Select the speech engine
~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 23.04

Enable :menuselection:`Menu --> View --> Speech Editor` menu item.

.. figure:: /images/Speech-to-text_select_speech-engine.png
   :align: left
   :width: 500px
   :figwidth: 500px
   :alt: change the speech engine

.. rst-class:: clear-both

Click on the :guilabel:`Hamburger Menu` |application-menu| and select :guilabel:`Configure Speech Recognition`. This brings you to :ref:`Configure Speech to Text <configure_speech_to_text>`, select the engine and click :guilabel:`OK.`

:guilabel:`Translate to english` is only available with the Whisper speech engine. It translates non-English text to English during recognition.

.. figure:: /images/kdenlive2405_speech-to-text_Show-log.webp
   :align: left
   :width: 300px
   :figwidth: 300px
   :alt: Speech to text show log

.. rst-class:: clear-both

If some error or important message happen. Click on the :guilabel:`Show log` and the log get visible.


Creating subtitle by VOSK speech recognition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. .. versionchanged:: 24.05

.. figure:: /images/kdenlive2405_speech-to-text_subtitle_VOSK.webp
   :align: left
   :width: 500px
   :figwidth: 500px
   :alt: Speech to text subtitle

   Shown with the VOSK engine

.. rst-class:: clear-both

1. Mark the timeline zone you want to recognize (adjust the blue line) (**1**)

2. Click on the :guilabel:`Speech recognition` icon (**2**)

3. Choose the :guilabel:`Language` (**3**)

4. Choose which part of the timeline should be applied for recognition (**4**)

5. :guilabel:`Process` Start the recognition (**5**)

The subtitle gets created and inserted automatically.

Remark to **4**: The default is to analyze only the :guilabel:`Timeline zone (all tracks)` (the blue bar in the timeline ruler). Set the zone in the timeline to what you want to analyze (use :kbd:`I` and :kbd:`O` to set in and out points). :guilabel:`Selected clips` option analyses the selected clip only.


Creating subtitle by WHISPER speech recognition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. .. versionchanged:: 24.05

.. figure:: /images/kdenlive2405_speech-to-text_subtitle_Whisper.webp
   :align: left
   :width: 500px
   :figwidth: 500px
   :alt: Speech to text subtitle Whisper

   Shown with the Whisper engine

.. rst-class:: clear-both

1. Mark the timeline zone you want to recognize (adjust the blue line) (**1**)

2. Click on the :guilabel:`Speech recognition` icon (**2**)

3. Choose the :guilabel:`Model` (**3**)

4. Choose which part of the timeline should be applied for recognition (**4**)

5. :guilabel:`Process` Start the recognition (**5**)

The subtitle gets created and inserted automatically.

Remark to **4**: The default is to analyze only the :guilabel:`Timeline zone (all tracks)` (the blue bar in the timeline ruler). Set the zone in the timeline to what you want to analyze (use :kbd:`I` and :kbd:`O` to set in and out points). :guilabel:`Selected clips` option analyses the selected clip only.

:guilabel:`Language` If :guilabel:`Autodetect` doesn't choose the correct language you can manually set the language

:guilabel:`Maximum character per line` Adjust the number of character per line in the subtitle

.. _Translate_with_SeamlessM4T:

:guilabel:`Translate with SeamlessM4T` First you have to enable :guilabel:`Enable translation through SeamlessM4T` in :menuselection:`Settings --> Configure Kdenlive --> Speech To Text`.

.. figure:: /images/kdenlive2405_speech-to-text_Whisper_SeamlessM4T_input-output_language.webp
   :align: left
   :width: 300px
   :figwidth: 300px
   :alt: Whisper SeamlessM4T choose input and output language

   **Attention** If you use SeamlessM4T the first time it downloads about 9GB of data in the background

.. rst-class:: clear-both

Select :guilabel:`Input Language` and :guilabel:`Output Language` and click :guilabel:`Process`. This will first process the audio using whisper, then start the SeamlessM4T translation. Translation can occupy 100% RAM, 100% CPU and 100% disk access.

.. attention::
   If the 9GB model has not yet been downloaded, it will be downloaded now. With a 100MB/s download speed this will take about 12 minutes!

   During download Kdenlive will react as normal. Don't click on :guilabel:`Close` otherwise download get stopped. 

Don't worry if you see such a message on the box below :guilabel:`Initializing translation model` while downloading is running.

.. figure:: /images/kdenlive2405_speech-to-text_Whisper_SeamlessM4T_download.webp
   :align: left
   :width: 300px
   :figwidth: 300px
   :alt: Whisper SeamlessM4T choose input and output language

.. rst-class:: clear-both

Once the translation model is downloaded translation will happen (be patient as download the model takes about 12 minutes with 100MB/s download speed). 

.. figure:: /images/kdenlive2405_speech-to-text_Whisper_SeamlessM4T.webp
   :align: left
   :width: 500px
   :figwidth: 500px
   :alt: On Whisper SeamlessM4T installed

   SeamlessM4T is enabled and downloaded successful

The SeamlessM4T models are stored here:

Linux: :file:`$HOME/.cache/hugginface`

Windows: :file:`C:\\Users\\<username>\\.cache\\huggingface`


.. _creating_clips_by_speech_recognition:

Creating clips by speech recognition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is useful for interviews and other speech-related footage.
Enable the :menuselection:`Menu --> View --> Speech Editor` menu item.

.. figure:: /images/kdenlive2402_speech-to-text_text-edit.webp
   :align: left
   :width: 500px
   :figwidth: 500px
   :alt: Speech editor

   Shown with the VOSK engine and search enabled

.. rst-class:: clear-both

Select a clip in the **Project Bin**.

1. If needed set in/out point in the clip monitor and enable :guilabel:`Selected zone only` selection box. This will only recognize the text inside the zone.

2. Choose the correct language when the VOSK engine is selected. Or choose the Whisper engine by click on :guilabel:`Configure Speech Recognition` (:ref:`see configure speech to text <configure_speech_to_text>`)

3. Press the :guilabel:`Start Recognition` button.

4. Select the text you want. Holding :kbd:`CTRL` or :kbd:`Shift` to select several texts.

.. .. versionadded:: 24.02

5. Choose: :guilabel:`Create new sequence with edit` creates a new sequence with each timecode-text as a single clip, or :guilabel:`Insert selection in timeline` at playhead position, or to :guilabel:`Save edited text in a playlist file` which appears in the project bin. 

.. .. versionadded:: 24.02

6. :guilabel:`Zoom in` or :guilabel:`Zoom out` of the text. :guilabel:`Remove non speech zones` deletes all "No speech" entries at once.

7. Add a Bookmark. You can jump to these bookmarks in the timeline with the :kbd:`Alt + arrow` shortcut or edit the bookmark by double click.

8. Delete the selected text.

9. Here you can search in the text.

10. And navigate up or down in the text.


.. _effects-s2t_silence_detection:

Silence detection
-----------------

This works with the VOSK engine only.

Open the clip in the clip monitor and open the speech editor window (:menuselection:`Menu --> View --> Speech Editor`) .

Select your language or :ref:`effects-s2t_install_language` and download the model for it.

Then click :guilabel:`Start Recognition` button.

Once this is done, choose under point 6 from above to :guilabel:`Remove non speech zones` at once. Or click on the time-code where "No speech" is indicated (hold :kbd:`Ctrl` to select several items at once) and just hit the :kbd:`Delete` key. 

Repeat the operation for all the parts you want to remove, including where someone says what you do not want to include in your final edit.

Once finished, make sure :guilabel:`Selected zone only` is disabled, click on the :guilabel:`Save edited text in a playlist file` button (above under point 5) and after few seconds a new playlist is added in the Project Bin without silence and without the text you do not want.
