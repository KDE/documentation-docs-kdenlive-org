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
             - Chengkun Chen <serix2004@gmail.com>

   :license: Creative Commons License SA 4.0


.. _effects-subtitles:

=========
Subtitles
=========

.. .. versionadded:: 20.12.0

The subtitling tool allows you to add and edit subtitles directly in the timeline on a special subtitle track or by using the :ref:`subtitle-window`. You can also import (**ASS**/**SRT**/**VTT**/**SBV**) and export (**ASS**/**SRT**) subtitles.

.. .. versionadded:: 24.02

Kdenlive allows multiple subtitle files in the subtitle track (only one subtitle file loaded at a time). You can create, duplicate, and delete subtitle files and manage its components with the :ref:`subtitle-manager`.



.. image:: /images/subtitle-timeline-1.gif
   :alt: subtitle

.. tip::
   Kdenlive stores subtitles as .ass files, which means you might be interested in exploring some advanced ASS features. For more details, check out the `ASS File Format Guide <https://github.com/libass/libass/wiki/ASS-File-Format-Guide>`_ and `Aegisub's Documentation <https://aegisub.org/docs/latest/>`_.

Add Subtitles
-------------

* **Menu**

  * :menuselection:`Project --> Subtitle --> Add Subtitle`

* **Keyboard**

  * :kbd:`Shift + S` adds a subtitle.

* **Icon and Mouse**

  * Click :guilabel:`Add Subtitle` icon in the :ref:`timeline_toolbar` to open the subtitle track in the timeline.
  * Double-click in the subtitle track to add a subtitle.
  * Click :guilabel:`Add Subtitle` in the :ref:`timeline ruler <timeline_ruler>` context menu.

* **Import**

  * Import subtitles with the :ref:`import function <subtitle-import_export>`.

Edit Subtitles
--------------

You can add or editing text either directly into the subtitle clip or in the subtitle window.

.. _subtitle-spell_check:


.. _split_subtitle_after_first_line:

Split subtitle after first line
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tip::
   Use the escaped character `\\N` to insert a new line in the subtitle.

.. .. versionadded:: 23.04

With this feature, you can cut the selected subtitle with the Razor Tool after the first line of the current track position. The first line becomes the left subtitle before the track position, and the rest becomes the right subtitle after the track position. It then selects the right-hand subtitle.

.. .. figure:: /images/subtitle-split_at_line.png
   :scale: 75%
   :alt: subtitle split at line

   Subtitle split after first line or duplicate text

To enable this feature go to :menuselection:`Menu --> Settings --> Configure Kdenlive -->` :doc:`Tools</getting_started/configure_kdenlive/configuration_tools>` and switch to :guilabel:`Split after first line`

.. figure:: /images/subtitle-split_with_razor-tool.png
   :scale: 75%
   :alt: subtitle split with Razor-Tool

   Subtitle split with Razor-Tool

Select the subtitle in the timeline that contains two lines. Click on the subtitle with the Razor-Tool :kbd:`X`.

.. figure:: /images/subtitle-split_after.png
   :scale: 75%
   :alt: subtitle split after the split

   Subtitle after you have split it with the Razor-Tool

This makes it easier to split up subtitles, where you have a transcription with one subtitle per line. This comes from a couple of situations:

1. You have put the audio through an external transcription service

2. You are adding subtitles to a song that you have the lyrics for

Resize
~~~~~~

Grab the end of a subtitle with the mouse and lengthen or shorten it as needed.

Set subtitle in/out can be achieved with the same shortcut as to set clip in/out (left/right parenthesis shortcut).


Style Subtitles
---------------

.. figure:: /images/effects_and_compositions/subtitle-manager_style.png
   :alt: subtitle style

Creating, duplicating, deleting, and editing subtitle styles can be managed through the :ref:`subtitle-manager`.

:menuselection:`Menu --> Project --> Subtitles --> Manage Subtitles --> Styles`

Additionally, you can edit the assigned style directly using the edit button in the :ref:`subtitle-window`.

Create a style
~~~~~~~~~~~~~~

Subtitle styles can be created either within each subtitle file or globally.

1. Choose a subtitle file or the global space from the sidebar as the location for the new style.

2. Click :guilabel:`+ Add Style` in the :ref:`subtitle-manager`.

3. Enter the properties in the :ref:`subtitle-style-editor`.

Move/Copy a style
~~~~~~~~~~~~~~~~~

.. figure:: /images/effects_and_compositions/subtitle-move_styles.gif
   :alt: subtitle move copy

In the style section of the :ref:`subtitle-manager`, drag a style to the desired item in the sidebar to move or copy it.

.. note::
   You cannot move or delete the style **Default**.

Assign a style to a subtitle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can assign a style to the subtitle you are currently editing using the :guilabel:`Style` combobox in the :ref:`subtitle-window`. This style will be applied to **the entire subtitle**.

Override style with tags
~~~~~~~~~~~~~~~~~~~~~~~~

Kdenlive supports using ASS override tags to style **specific parts of the subtitle text**.

.. figure:: /images/effects_and_compositions/subtitle-window_page1.png
   :scale: 60%
   :alt: subtitle override tags

* A **highlighter** renders different parts of the tags in distinct styles, making them more distinguishable.

* An **auto-completer** automatically lists all valid presets as you start typing a tag name.

* The buttons above the text editor will automatically add or edit tags when pressed.

  - Tags like "Set Position," which affect the entire subtitle text, will be added **at the beginning of the subtitle text**.
  
  - Tags like "Toggle Bold," which affect only the text following them, will either be added **at the current cursor position** or **wrap the selected text in tags** if there is a selection.

* Additionally, you can use '\\r<style>' to reset the style of the subtitle after the tag.

.. _subtitle-multi-layer_subtitling:

Multi-layer Subtitling
----------------------

Kdenlive supports multiple subtitle layers. You can create, duplicate, and delete subtitle layers using the :guilabel:`Layer` tab in :ref:`subtitle-manager`.

.. figure:: /images/effects_and_compositions/subtitle-manager_event.png
   :alt: subtitle event

A new subtitle layer can also be created by :kbd:`Shift+drag` an existing subtitle down beyond the bottom of the subtitle track or by adjusting the layer indicator in the :ref:`subtitle-window`.

.. figure:: /images/effects_and_compositions/subtitle-add_new_layer_on_timeline.gif
   :alt: subtitle add new layer on timeline

Subtitles with a lower Layer value are placed behind those with a higher value.

Set the layer of a subtitle
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you create a new subtitle by double-clicking on the timeline, the subtitle will be placed on the layer under your cursor.

You can change a subtitle's layer value using the :guilabel:`Layer` indicator in the :ref:`subtitle-window`, or you can simply drag and drop the subtitle from one layer to another on the timeline.

.. figure:: /images/effects_and_compositions/subtitle-move_subtitles_between_layers.gif
   :alt: subtitle move subtitles between layers

If you set the layer value higher than the current maximum, Kdenlive will automatically add a new layer.

Copy/Move layer between files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can copy and move layers between different subtitle files using the :ref:`subtitle-manager`.

In the :guilabel:`Layer` tab, Simply drag a layer to the desired file in the sidebar. All events within the layer will be copied or moved to the new location.

.. figure:: /images/effects_and_compositions/subtitle-move_layer.gif
   :alt: subtitle move layer

Default style of layer
~~~~~~~~~~~~~~~~~~~~~~

You can assign each subtitle layer a default style. Any new subtitles created on that layer will automatically be assigned this style.

To set this, go to the :guilabel:`Layer` tab in the :ref:`subtitle-manager`. Click the :guilabel:`Style` column of a layer item and select the desired style from the pop-up menu.

This feature is particularly useful when working with multiple speakers in a subtitle file, as it allows each speaker to have a distinct style effortlessly.

.. _subtitle-import_export:

Import and Export Subtitles
---------------------------

.. .. versionadded:: 22.08

  Allows importing .vtt (Web Video Text Tracks) and .sbv (YouTube) files.

Importing **SRT**, **ASS**, **VTT** and **SBV** subtitle file: :menuselection:`Menu --> Project --> Subtitles --> Import Subtitle File`

Exporting **ASS** or **SRT** subtitles: :menuselection:`Menu --> Project --> Subtitles --> Export Subtitle File`

.. .. versionadded:: 23.04

.. figure:: /images/kdenlive2402_import_subtitle.webp
   :scale: 75%
   :alt: import_subtitle_23-04

:guilabel:`Encoding`: Allow overriding of detected codecs through a list of available codecs, and show a preview to make choice easier.

.. .. versionadded:: 24.02

:guilabel:`Create New Subtitle Track`: Importing an :file:`.srt` file in the project, you can create a new subtitle track (an entry in the subtitles combo list) instead of overwriting the current subtitle track.

.. _subtitle-window:

Subtitle Window
---------------

The subtitles window allows easier editing and also makes it possible to easily navigate between subtitles with the :guilabel:`<` and :guilabel:`>` buttons

.. figure:: /images/subtitle-widget.gif
   :alt: subtitle window

   Subtitle window

* **Add subtitles** with the :guilabel:`+` button

* **Cut subtitles** with the scissors button
  
  Let's say your subtitle text is too long and you want to make it two different subtitles. Put the cursor in the text widget where you want to cut and click the scissors, it will split the text between two different subtitle items. 

.. tip::
  The scissors only works when the playhead is positioned over the subtitle itself.

* **Apply changes** by clicking the check-mark button, or by pressing :kbd:`Enter`

.. _subtitle-char_count_and_zoom:

Character count and zoom
~~~~~~~~~~~~~~~~~~~~~~~~

.. .. versionadded:: 23.08

.. figure:: /images/effects_and_compositions/subtitle_character_count_and_zoom.gif
   :alt: subtitle_character_count_and_zoom

:guilabel:`Character`: Character number at cursor position

:guilabel:`Total`: Total number of Character

:guilabel:`Zoom in`: Zoom into the edit window

:guilabel:`Zoom out`: Zoom out of the edit window

:kbd:`Alt+Arrow`: jumps from subtitle to subtitle.

Spell check
~~~~~~~~~~~

.. .. versionadded:: 21.04.0

A spell check for subtitle is integrated and shows incorrect words by a red wiggly line. Right-click on the word and you get a list of possible words you can then choose by clicking on it.

To enable spell check, right-click the subtitle text widget in the :ref:`subtitle-window` and check the :guilabel:`Auto Spell Check` option.

.. warning::
   Please note that this feature conflicts with the ASS tag highlighter. To re-enable the highlighter, uncheck the :guilabel:`Auto Spell Check` option.

.. figure:: /images/Speech-to-text_Spell-Check.png
   :align: left
   :alt: Spell check

.. rst-class:: clear-both

Simple editor
~~~~~~~~~~~~~

A simple text editor that syncs with the normal editor, hides ASS override tag blocks, and translates '\N' into a new line.

.. warning::
   Due to the complexities of ASS tag rules, style editing in the Simple Editor can sometimes behave unpredictably. So it's best suited for simpler use cases before or after editing styles.

Scrolling
~~~~~~~~~

You can configure subtitle scrolling using the following options:

:menuselection:`Subtitle Window --> More Options --> Scroll`

.. figure:: /images/effects_and_compositions/subtitle-scroll.gif
   :alt: subtitle scroll

* Check the :guilabel:`Scrolling` checkbox to enable scrolling.

* Use the :guilabel:`Direction` combobox to set the scrolling direction.

* Adjust the speed by changing the value of :guilabel:`Speed`.

* **For vertical scrolling only**, set the :guilabel:`Upper Bound` and :guilabel:`Lower Bound` values to clip the text at the top and bottom of the screen.

.. _subtitle-manager:

Subtitle Manager
----------------

.. .. versionadded:: 24.02

You can create, duplicate, and delete subtitle files and manage its components with the subtitle manager: :menuselection:`Menu --> Project --> Subtitles --> Manage Subtitles` or on the timeline as drop-down menu in the subtitle track.

.. figure:: /images/kdenlive2402_drop-down_subtitle-manager.webp
   :align: left
   :alt: drop down menu to the subtitle manager

   Open the subtitle manager from the drop down menu 


.. figure:: /images/effects_and_compositions/subtitle-manager_file.png
   :alt: subtitle event

   Subtitle manager with 4 subtitle files 

.. rst-class:: clear-both

Click on |application-menu|:guilabel:`Options` and select :guilabel:`Import Subtitle` or :guilabel:`Export Subtitle` to reach :ref:`subtitle-import_export`. 

Only one subtitle file can be active. So, rendering will always render using the active subtitle only. 

.. _subtitle-style-editor:

Style editor
------------

.. figure:: /images/effects_and_compositions/subtitle-style_editor.png
   :alt: subtitle style editor

An editor that allows you to adjust style properties with a live preview.