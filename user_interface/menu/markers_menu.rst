.. meta::
   :description: Kdenlive's User Interface - Markers Menu
   :keywords: KDE, Kdenlive, markers, project, menu, markers menu, jobs, marker, automatic transition, transcode, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             - Eugen Mohr

             

   :license: Creative Commons License SA 4.0


.. _markers_menu:

Markers Menu
============

.. .. versionchanged:: 25.12 Reorder menu structure and content 

The functions in this menu affect markers that are selected in the Timeline **or** in the Project Bin. Menu functions are available depending on whether a clip is selected in the Project Bin or in the Timeline.

.. figure:: /images/user_interface/menu_reference/menu_reference-markers_menu-2512.webp
   :align: left
   :scale: 77%
      
   Markers Menu

- :ref:`add_marker`
- :ref:`add_marker_quickly`
- :ref:`edit_marker`
- :ref:`delete_marker`
- :ref:`add_remove_timeline_marker`
- :ref:`edit_timeline_marker`
- :ref:`delete_timeline_marker`
- :ref:`delete_all_markers`
- :ref:`timeline_markers_locked`
- :ref:`search_marker`
- :ref:`marker_menu_export_markers`
- :ref:`add_markers_by_category`

.. rst-class:: clear-both

.. _markers_menu-markers:

The menu allows you to Add, Edit or Delete Markers or Timeline Markers (Guides). For more details see the section about :ref:`Markers` in this documentation.

.. note:: The Add Marker function behaves differently depending on whether a clip is selected in the Project Bin or in the Timeline **and** where the playhead is currently **and** whether the focus is on the Timeline or the Clip Monitor.


.. _add_marker:

Add Marker
----------

Adds a Marker to the clip at the current timepoint. Markers are properties of the clips in the Project Bin. So this action puts a marker in the clip in the Project Bin.

.. note:: In order for the Add Marker to work a clip must be selected in the Timeline. You can create multiple Markers in the markers widget for the clip selected in the Project Bin independent of the Timeline.


.. _add_marker_quickly:

Add Marker Quickly
------------------

Adds a new marker at the current time point. Shortcut :kbd:`Num+*` (On Numlock pad: :kbd:`*`)


.. _edit_marker:

Edit Marker
-----------

For this to work the playhead needs to be right on top of a Marker. If it is not you get an error on the bottom left "No Marker found at Cursor time". Use the :kbd:`Left` and :kbd:`Right` keys to move the playhead one frame at a time, or use them with :kbd:`ALT` to jump to the next or previous edit point (for example cuts, clip edges, Markers and Timeline Markers).

As Markers are properties of the clips in the Project Bin, this action changes the Marker from the clip in the Project Bin and thus in any other instance of this clip in the Timeline.


.. _delete_marker:

Delete Marker
-------------

For this to work the playhead needs to be right on top of a Marker. If it is not you get an error on the bottom left "No Marker found at Cursor time". Use the :kbd:`Left` and :kbd:`Right` keys to move the playhead one frame at a time, or use them with :kbd:`ALT` to jump to the next or previous edit point (for example cuts, clip edges, Markers and Timeline Markers).

As Markers are properties of the clips in the Project Bin, this action removes the Marker from the clip in the Project Bin and thus from any other instance of this clip in the Timeline.


.. _add_remove_timeline_marker:

Add/Remove Timeline Marker
--------------------------

This will add or remove a Timeline Marker (Guide) in the Timeline at the current position of the playhead. Default shortcut: :kbd:`G`


.. _edit_timeline_marker:

Edit Timeline Marker
--------------------

This will open a dialog window for the current Timeline Marker (Guide) where you can change the position in the Timeline, the name and the category.


.. _delete_timeline_marker:

Delete Timeline Marker
----------------------

This will delete the Timeline Marker (Guide) at the current playhead position.


.. _delete_all_markers:

Delete All Markers
------------------

Deletes all Markers from the current clip.

As Markers are properties of the clips in the Project Bin, this action removes the Marker from the clip in the Project Bin and thus from any other instance of this clip in the Timeline.

This will delete all Timeline Markers from the timeline without any further warning. Use :guilabel:`Undo` or :menuselection:`Menu --> Edit --> Undo` or :kbd:`Ctrl+Z` to undo this action.


.. _timeline_markers_locked:

Timeline Markers Locked
-----------------------

This will lock the Timeline Markers (Guides) in the Timeline so that specific actions do not move the Timeline Markers.


.. _search_marker:

Search Marker
-------------

This will bring the focus to the Search field in the Marker widget.


.. _marker_menu_export_markers:

Export Markers
--------------

This will open a dialog window in which you can specify the export options for Markers. Use this function to create chapters for YouTube uploads.


.. _add_markers_by_category:

Add Markers by Category
-----------------------

Opens a flyout to add a marker by category:

.. figure:: /images/user_interface/menu_reference/menu_reference-add_marker_by_category_menu-2512.webp
   :align: left
   :scale: 77%
      
   Add Markers by Category Menu

