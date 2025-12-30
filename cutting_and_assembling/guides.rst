.. meta::
   :description: Set timeline markers
   :keywords: KDE, Kdenlive, set timeline marker, DVD, youtube, editing, timeline, documentation, user manual, video editor, open source, free, learn, easy


.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Gallaecio (https://userbase.kde.org/User:Gallaecio)
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Dbolton (https://userbase.kde.org/User:Dbolton)
             - Jack (https://userbase.kde.org/User:Jack)
             - Eugen Mohr

   :license: Creative Commons License SA 4.0

.. .. versionchanged::25.12 Change name of guide to timeline marker, Reorder menu structure to make it clearer

.. _guides:

Timeline Markers
================



Timeline markers in the picture below are the red flags. Not to be confused with :ref:`markers` on a clip (yellow in the picture below). Timeline markers can be either stationary or moved when clips are moved around. Markers are inside the clips and move with the clips.

.. figure:: /images/cutting_and_assembling/cutting_and_assembling-markers-2512.webp
   
Timeline markers can be used for certain points (Timeline Marker2) or ranges (Timeline Marker1).

Timeline markers can be used to define regions for rendering. See :ref:`rendering-guides`.

Timeline markers can also be used as chapters for DVD videos. See :ref:`rendering-guides`.


.. _add_guides:

3 Ways to add Timeline Markers
------------------------------

Following procedures add a timeline marker at the timeline playhead position:

* **Menu**

  * :menuselection:`Markers --> Add/Remove Timeline Marker`
  * Right click on :ref:`timeline ruler<timeline_ruler>` and choose in the menu :guilabel:`Add/Remove Timeline Marker`
  * Right click in the timeline and choose :guilabel:`Add/Remove TimeLine Marker`

.. .. versionadded:: 24.08 Insert guides in 10 different categories using NumPad 

* **Keyboard**

  * :kbd:`G` adds a timeline marker.
  * :kbd:`1` - :kbd:`0` (number 1 to 0 on the NumPad)

* **Mouse**

  .. figure:: /images/Kdenlive_add_guide_double-click.png

  * Double-click on top of the :ref:`timeline ruler<timeline_ruler>` and the timeline marker gets added were you have clicked


.. _timeline_ruler_right-click_menu:

Timeline ruler right click menu
-------------------------------

.. figure:: /images/cutting_and_assembling/timeline-markers_timeline-ruler-right-click-menu_2512.webp
   :align: left
   :scale: 77%
   
.. rst-class:: clear-both

:guilabel:`Add/Remove Timeline Marker`

:guilabel:`Edit Timeline Marker`: See :ref:`move_edit_guides`

.. .. versionadded:: 21.08
   
:guilabel:`Timeline Markers Locked`: See :ref:`move_edit_guides`  

:guilabel:`Export Markers`: Opens the Export Marker dialog.

:guilabel:`Go To Marker...`. Select a marker to which the playhead should jump.

.. .. versionadded:: 22.04

:guilabel:`Set Zone In/Out`: See also :doc:`/tips_and_tricks/tips_and_tricks/timeline_preview_rendering`.

:guilabel:`Adjust Timeline Zone to Selection`

:guilabel:`Create Marker from Zone`

:guilabel:`Create Marker from Zone Quickly`

:guilabel:`Add Project Note`: See :doc:`/project_and_asset_management/project_notes`

.. .. versionadded:: 20.12.

:guilabel:`Add Subtitle`: See :ref:`effects-subtitles`


.. .. versionchanged:: Extend Marker System with Range/Duration Support

.. _timeline_marker_with_range:

Timeline Marker With Range
--------------------------

.. figure:: /images/cutting_and_assembling/cutting_and_assembling-markers_with_range-2512.webp
   :align: left
   :scale: 77%

In the Edit Marker window you can enable :guilabel:`Range Marker` which allows you to determine a :guilabel:`Duration` of the marker. Default :guilabel:`Duration` is 1 second.

.. rst-class:: clear-both


.. _managing_guides:

Managing Categories and Markers
-------------------------------

.. .. versionadded:: 22.12


.. _categories:

Categories
~~~~~~~~~~

When starting a new project the categories for the project are pulled in from :guilabel:`Markers Categories` in setting :doc:`Configure Colors and Markers </getting_started/configure_kdenlive/configuration_colors+markers>`. These categories are for markers and timeline markers.

.. container:: clear-both

   .. figure:: /images/project-specific-categories_2512.webp
      :align: left
      :scale: 50%
   
   Project specific categories can be added, edited and deleted in :menuselection:`File --> Project Settings --> Markers`

.. rst-class:: clear-both

.. container:: clear-both

   .. figure:: /images/delete-category_2512.webp
      :align: left
      :scale: 77%
   
   :guilabel:`Delete category` When deleting a category were markers are assigned, Kdenlive asks if you really want to delete it or if you want to reassign the markers to another category. 

.. rst-class:: clear-both

.. _guide_view:

Markers View
~~~~~~~~~~~~

.. .. versionchanged:: 25.08 add a button to show all project clip markers in the list, add option to show thumbnails in markers list dialog 

.. figure:: /images/guides_view_2508.webp
   
:menuselection:`View --> Markers` opens the markers window were you can manage your markers.  


:1: Shows the selected object: Clip-Name, Sequence-Name 

:2: Search Timeline Marker / Clip Markers. If you enter `2` in this example, it shows only `guide2` / `marker2` in the list and in the timeline/on the clip monitor.

:3: Show only the chosen categories in the list and in the timeline/clip monitor.

:4: Show markers for all clips in the project

:5: Sort by categories, time, or comment, and change sort order (ascending/descending).

:6: Clicking on a marker or :kbd:`arrow-up arrow-down` will select it, and the playhead jumps to this marker in the timeline/clip monitor. Multi-selection: holding down :kbd:`Shift` to select a range of markers, or :kbd:`Control` to add individual markers to a selection. :kbd:`Control+A` selects all markers. Double-click or press :kbd:`F2` on a marker to open the :ref:`edit marker window <move_edit_guides>`/:ref:`edit marker window <move_edit_marker>`.

:7: Add a marker. Only here you have the possibility to add multiple markers with an interval.

:8: Edit a selected marker. The same as double-clicking a marker under point 4, or timeline markers in the :ref:`timeline ruler<timeline_ruler>`.

:9: Delete the selected marker(s).

:10: Set the default category for new markers.

:11: Timeline Markers only: :ref:`Locks Timeline Markers <move_edit_guides>`. Locked when the background is light gray (as shown on the screenshot).

:12: Refresh all thumbnails when thumbnails are enabled

:13: Enable/disable thumbnails. Import/:ref:`export markers/marker <export_guides>` or configure the :ref:`project categories <categories>`.


You can put a comment in the marker and make the comment display by choosing :ref:`editing` in the :menuselection:`Markers` menu or by clicking on the :ref:`editing` button.


.. _export_guides:

Export Timeline Markers as Chapters Description
-----------------------------------------------

.. .. versionadded:: 22.08

.. .. versionchanged:: 22.12

Timeline markers can mark chapters or different sections of a video while editing. Uploading edited videos to platforms like YouTube, the timeline markers can be exported as chapter marks that are supported by YouTube. This can be done by :guilabel:`Copy to Clipboard` and paste then into YouTube.

Right click in the :ref:`timeline ruler <timeline_ruler>` and choose :guilabel:`Export Markers` or :menuselection:`Markers --> Export Markers`. Then the window `Export markers as chapters description` appears.

.. figure:: /images/Kdenlive_export_guides_22-12.png
   
:guilabel:`Marker Type`: Choose one of the timeline marker types to mark chapters and use other types to do other things.

:guilabel:`Save As`: Text (for Youtube) or as JSON data file which can be re-imported.

:guilabel:`Offset`: This adds the ability to set a general offset (hh:mm:ss:ff) to each timeline marker.

:guilabel:`Format`: This defines how the chapter marks are exported. When using the 2 default format strings (as shown on the picture), Kdenlive check if the chapter marker matches YouTube's guideline, and display a notice if it doesn't match.

:guilabel:`i`: Shows all possible export strings. Select the string you want and Kdenlive adds it to the :guilabel:`Format` for export. Add spaces between the strings as needed. 

{{timecode}} adds timeline marker position at HH:MM.SS (default)

{{comment}} adds the timeline marker text (default)

{{frame}} adds the frame number of each timeline marker

{{index}} adds timeline marker number

{{nexttimecode}} adds next timeline marker position at HH:MM.SS

{{realtimecode}} adds timeline marker position at HH:MM:SS:FF

:guilabel:`Reset`: Resets the settings to the default: {{timecode}} {{comment}}

:guilabel:`Exported`: Shows what gets exported. To change the timeline marker text you have to edit the timeline marker in the timeline.

:guilabel:`Copy to Clipboard`: Copy the data viewed in :guilabel:`Exported` into the clipboard to use it in other applications (Youtube).

The warning in the blue box only show up if one of the 3 points are not fulfilled.


.. _move_edit_guides:

Move and Edit Timeline Markers
------------------------------

Timeline markers can be moved by clicking on a timeline marker text in the timeline and dragging it to the desired position.

Timeline markers can be moved by changing the :guilabel:`Position` in the edit window.

.. figure:: /images/cutting_and_assembling/timeline-markers_edit-marker_2512.webp
   :scale: 77%

Double-click on a timeline marker text in the timeline ruler opens the edit window (beside the possibility in :ref:`guide_view`).

:guilabel:`Comment` text and :guilabel:`Category` can be changed in the edit window.


Move Timeline Markers with Spacer Tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. .. versionadded:: 21.08.0

Easily moves timeline markers along with clips using the spacer tool by using the new :menuselection:`Timeline Marker Locked` option. When locked, the timeline markers stay in place. When unlocked, the timeline markers move with the clip.


.. figure:: /images/guidemove.gif
   