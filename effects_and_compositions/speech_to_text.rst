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

   :license: Creative Commons License SA 4.0



..  Please use level 3 top heading, i.e. "===" 

.. _speech_to_text:

Speech to text
==============

.. versionadded:: 21.04.0


Install Python
~~~~~~~~~~~~~~

Python needs to be installed on your computer. Download it from here https://www.python.org/downloads/ for installation on your computer.  


Speech recognition requires the vosk and srt python modules
 
-	On Linux open a terminal and put in and run: "pip3 install vosk;pip3 install srt".   

-	On Windows, you can download this batch file (`Archive File: Install_vosk_srt.zip <Install_vosk_srt.zip>`_). After download double click starts the installations.
  
Install a language
~~~~~~~~~~~~~~~~~~

Goto :menuselection:`Settings --> Configure Kdenlive --> Speech to Text` 

Click on the link to get a language model

.. image:: /images/Speech-to-text_Download-link.png
   :align: left
   :alt: download link

Drag &  drop the language you want from the vosk-model download page to the model window, and it will download and extract it for you.

.. image:: /images/Speech-to-text_Download-model.png
   :align: left
   :alt: download model


If you have problems click on "Check configuration" button. 


Speech recognition
~~~~~~~~~~~~~~~~~~

**Creating subtitle by speech recognition**


1.	Mark the timeline zone you want to recognize (adjust the blue line).


2.	Click on the "Speech recognition" icon.


3.	Choose the language.


4.	Choose how the selected zone should be applied.


5.	Click "Process"


The subtitle gets created and inserted automatically.


Remark: Only timeline zone is implemented for now in automatic subtitles.


.. image:: /images/Speech-to-text_Subtitle.png
   :align: left
   :alt: Speech to text subtitle

**Creating clips by speech recognition**
This is useful for interviews and other speech-related footage.
Enable :menuselection:`View --> Text Edit`


Select a clip in the project bin.


1.	If needed set in/out point in the clip monitor and enable "selected zone only". This will only recognize the text inside the zone.


2.	Choose the correct language


3.	Click "start recognition"


4.	Selecting the text you want to either


5.	Put into the timeline


6.	Save as a new clip


7.	Add a Bookmark. You can jump to these bookmarks in the timeline with :kbd:`alt + arrow` or edit the bookmark by double click.


8.	Delete the selection.


9.	Here you can search in the text.


10.	And navigate up


11.	Or down in the text.


.. image:: /images/Speech-to-text_Text-Edit.png
   :align: left
   :alt: Text edit


.. warning::

  Speech to text doesn't work with version 21.04.2 due to vosk API issues. Use version 21.04.1 or 21.04.3 and later versions.