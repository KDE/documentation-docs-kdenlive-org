.. meta::
   :description: Add Subtitle in the timeline with Kdenlive video editor
   :keywords: KDE, Kdenlive, subtitle, styling, SRT, ASS, VTT, SBV, editing, timeline, documentation, user manual, video editor, open source, free, learn, easy


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


.. _effects-subtitles:

=========
Subtitles
=========

.. .. versionadded:: 20.12.0

The subtitling tool allows you to add and edit subtitles directly in the timeline on a special subtitle track or by using the new subtitle window. You can also import (**SRT**/**ASS**) and export (**SRT**) subtitles.

.. image:: /images/subtitle-timeline-1.gif
   :alt: subtitle

Three ways to add subtitle
--------------------------

* **Menu**

  * :menuselection:`Project --> Subtitle --> Add Subtitle`

* **Keyboard**

  * :kbd:`Shift + S` adds a subtitle.

* **Icon and Mouse**

  * Click :guilabel:`Add Subtitle` icon in the :ref:`timeline_toolbar` to open the subtitle track in the timeline.
  * Double-click in the subtitle track to add a subtitle.
  * Click :guilabel:`Add Subtitle` in the :ref:`timeline ruler <timeline_ruler>` context menu.

Adding and editing text
-----------------------

Add or editing text either directly into the subtitle clip or in the subtitle window.

Adjust the length of subtitle
-----------------------------

Grab the end of a subtitle with the mouse and lengthen or shorten it as needed.
Set subtitle in/out can be achieved with the same shortcut as to set clip in/out (left/right parenthesis shortcut).


.. _split_subtitle_after_first_line:

Split subtitle after first line
-------------------------------

.. .. versionadded:: 23.04

With this feature, you can cut the selected subtitle with the Razor Tool after the first line of the current track position. The first line becomes the left subtitle before the track position, and the rest becomes the right subtitle after the track position. It then selects the right-hand subtitle.

.. image:: /images/subtitle-split_at_line.png
   :scale: 75%
   :alt: subtitle split at line

To enable this feature go to :menuselection:`Menu --> Settings --> Configure Kdenlive... --> Tools` switch to :guilabel:`Split after first line`

.. image:: /images/subtitle-split_with_razor-tool.png
   :scale: 75%
   :alt: subtitle split with Razor-Tool

Select the subtitle in the timeline that contains two lines. Click on the subtitle with the Razor-Tool :kbd:`X`.

.. figure:: /images/subtitle-split_after.png
   :scale: 75%
   :alt: subtitle split after the split

   Subtitle after you have split it with the Razor-Tool

This makes it easier to split up subtitles, where you have a transcription with one subtitle per line. This comes from a couple of situations:

1. You have put the audio through an external transcription service

2. You are adding subtitles to a song that you have the lyrics for

Subtitle window
---------------

.. image:: /images/subtitle-widget.gif
   :alt: subtitle window

* The subtitles window allows easier editing and also makes it possible to easily navigate between subtitles with the :guilabel:`<` and :guilabel:`>` buttons

* With the :guilabel:`+` button you can add subtitles

* The scissors are mostly here for dividing subtitles: let's say your subtitle text is too long and you want to make it two different subtitles. Put the cursor in the text widget where you want to cut and click the scissors, it will split the text between two different subtitle items. The scissors are only working when the playhead is over the subtitle itself.

* The check-mark button adds the text to the subtitle

.. _subtitle-char_count_and_zoom:

Character count and zoom
~~~~~~~~~~~~~~~~~~~~~~~~

.. .. versionadded:: 23.08

.. figure:: /images/effects_and_compositions/subtitle_character_count_and_zoom.gif
   :alt: subtitle_character_count_and_zoom

:guilabel:`Character:`: Character number at cursor position

:guilabel:`total:`: Total number of Character

:guilabel:`Zoom in`: Zoom into the edit window

:guilabel:`Zoom out`:Zoom out of the edit window


.. _subtitle-style:

Style subtitle
--------------

.. .. versionadded:: 22.08

.. image:: /images/subtitle-style.png
   :alt: subtitle style

This is a global, simple subtitle styling possibility. It only allows one style for all subtitles of the project. Accessible through the "T drop" icon in the subtitle edit widget.

.. tip::

  **SRT** supports markup for: bold, italic, underline, text color and line break.

  * ``<b>text in boldface</b>``
  * ``<i>text in italics</i>``
  * ``<u>text underlined</u>``
  * ``<font color="#00ff00"> text in green</font>`` you can use the font tag only to change color.
  * And all combined: ``<font color="#00ff00"><b><i><u>All combined</u></i></b></font>``
  * **Line break:** Add on the end of each line a ``<br>`` (for break). Now the :file:`.srt` file is stored correct and reopened with the line break. The subtitle in the subtitle window will be all in 1 line after several save but the breaks is working.

  :kbd:`Alt+Arrow` jumps from subtitle to subtitle.


.. _subtitle-import_export:

Import and export subtitle
--------------------------

.. .. versionadded:: 22.08

  Allows importing .vtt (Web Video Text Tracks) and .sbv (YouTube) files.

Importing **SRT**, **ASS**, **VTT** and **SBV** subtitle file: :menuselection:`Menu --> Project --> Subtitles --> Import Subtitle File`

Exporting **SRT** subtitles only: :menuselection:`Menu --> Project --> Subtitles --> Export Subtitle File`

.. .. versionadded:: 23.04

.. image:: /images/import_subtitle_23-04.png
   :scale: 75%
   :alt: import_subtitle_23-04

Allow overriding of detected codecs through a list of available codecs, and show a preview to make choice easier.


.. _subtitle-spell_check:

Spell check
-----------

.. .. versionadded:: 21.04.0

A spell check for subtitle is integrated and shows incorrect words by a red wiggly line. Right-click on the word and you get a list of possible words you can then choose by clicking on it.

.. image:: /images/Speech-to-text_Spell-Check.png
   :align: left
   :alt: Spell check
