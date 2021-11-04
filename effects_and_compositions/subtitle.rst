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




.. _subtitle:

Subtitle
========

.. versionadded:: 20.12.0

.. image:: /images/subtitle-timeline-1.gif
   :alt: subtitle
  
The subtitling tool allows you to add and edit subtitles directly in the timeline on a special subtitle track or by using the new subtitle window. You can also import (SRT/ASS) and export (SRT) subtitles.   


There are 3 ways to add subtitle: 


* **Menu**


  * :menuselection:`Project --> Subtitle --> Add Subtitle`


* **Keyboard**   


  * :kbd:`Shift + S` adds a subtitle.  


* **Icon and Mouse**  


  * Click the "subtitle" icon in the timeline toolbar to open the subtitle track in the timeline.


  * Double-click in the subtitle track to add a subtitle.


**Adding and editing text**


Add or editing text either directly into the subtitle clip or in the subtitle window.


**Adjust the length of subtitle**


Grab the end of a subtitle with the mouse and lengthen or shorten it as needed.
Set subtitle in/out can be achieved with the same shortcut as to set clip in/out (left/right parenthesis shortcut). 


**Subtitle window**


.. image:: /images/subtitle-widget.gif
   :alt: subtitle window
  
* The subtitles window allows easier editing and also makes it possible to easily navigate between subtitles with the left/right button.   


* With the plus sign, you can add subtitles.


* The scissors are mostly here for divide subtitles: let's say your subtitle text is too long and you want to make it 2 different subtitles. Put the cursor in the text widget where you want to cut and click the scissors, it will split the text between 2 different subtitle items. The scissors are only working when the playhead is over the subtitle itself.  


* The tick adds the text to the subtitle.


**Import and export subtitle**


Importing SRT and ASS subtitle file: :menuselection:`Project --> Subtitles --> Import subtitles file` 


Exporting SRT subtitles only: :menuselection:`Project --> Subtitles --> Export subtitles file`   


.. tip::

  SRT supports markup for: bold, italic, underline, text color and line break.

  * ``<b>text in boldface</b>``
  * ``<i>text in italics</i>``
  * ``<u>text underlined</u>``
  * ``<font color="#00ff00"> text in green</font>`` you can use the font tag only to change color.
  * And all combined: ``<font color="#00ff00"><b><i><u>All combined</u></i></b></font>``     
  * **Line break:** Add on the end of each line a ``<br>`` (for break). Now the srt file is stored correct and reopened with the line break. The subtitle in the subtitle window will be all in 1 line after several save but the breaks is working.
  
  :kbd:`Alt + arrow` jumps from subtitle to subtitle.

.. versionadded:: 21.04.0


**Spelling check**

Spelling check for subtitle is integrated and shows incorrect words by a red wiggly line. Right-click on the word and you get a list of possible words you can choose by click on it.


.. image:: /images/Speech-to-text_Spell-Check.png
   :align: left
   :alt: Spell check