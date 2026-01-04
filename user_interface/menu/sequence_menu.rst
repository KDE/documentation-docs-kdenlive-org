.. meta::
   :description: Editing in Kdenlive video editor - Sequence menu
   :keywords: KDE, Kdenlive, timeline, menu, editing, sequence, documentation, user manual, video editor, open source, free, learn, easy


.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jack (https://userbase.kde.org/User:Jack)
             - Eugen Mohr
             - Smolyaninov (https://userbase.kde.org/User:Smolyaninov)
             - Bernd Jordan

   :license: Creative Commons License SA 4.0



.. _sequence_menu:

Sequence Menu
=============

.. .. versionadded:: 22.12
.. .. versionadded:: 25.04 Zoom Audio Waveforms
.. .. versionchanged:: 25.12 Reorder menu structure and content. Removed Zoom Audio Waveforms
  

The Sequence Menu functions affect the clip or clips selected in the timeline, and perform actions with relation to the timeline.

.. figure:: /images/user_interface/menu_reference/menu_reference-sequence_menu-2512.webp
   :align: left
   :scale: 75%
   
   Kdenlive Sequence Menu

- :ref:`sequence_switch_to_next_sequence`
- :ref:`sequence_switch_to_previous_sequence`
- :ref:`Selection <selection>`
- :ref:`sequence_current_item`
- :ref:`Current clip <timeline-current_clip>`
- :ref:`Group Clips <timeline-group_clips>`
- :ref:`Ungroup Clips <timeline-ungroup_clips>`
- :ref:`Add Timeline Selection to Library <timeline-add_to_library>`
- :ref:`Create Sequence from Selection <timeline-create_sequence_from_selection>`
- :ref:`Insertion <insert_clip_zone>`
- :ref:`Removal <removal>`
- :ref:`Space <timeline-space>`
- :ref:`Current track <timeline-current_track>`
- :ref:`Tracks <sequence-menu_tracks>`
- :ref:`Subtitles <sequence-menu_subtitle>`
- :ref:`Timeline Preview <timeline-preview_rendering>`
- :ref:`Disable Timeline Effects <timeline-disable_timeline_effects>`
- :ref:`Show Video Thumbnails <timeline-show_video_thumbnails>`
- :ref:`Show Audio Thumbnails <timeline-show_audio_thumbnails>`
- :ref:`Show Markers Comments <timeline-show_markers_comments>`
- :ref:`Snap <timeline-toggle_snap>`
- :ref:`Zoom In <timeline-zoom_in>`
- :ref:`Zoom Out <timeline-zoom_out>`
- :ref:`Fit Zoom to Project <timeline-fit_zoom>`


.. rst-class:: clear-both


.. _sequence_switch_to_next_sequence:

Switch to next Sequence
-----------------------


.. _sequence_switch_to_previous_sequence:

Switch to previous Sequence
---------------------------



.. _selection:

Selection
---------

.. figure:: /images/user_interface/menu_reference/menu_reference-selection_menu-2512.webp
   :align: left
   :scale: 77%
   
   Sequence Selection Menu

- :ref:`sequence_select_clip`
- :ref:`sequence_add_clip_to_selection`
- :ref:`sequence_deselect_clip`
- :ref:`sequence_select_transition`
- :ref:`sequence_add_transition_to_selection`
- :ref:`sequence_deselect_transition`
- :ref:`sequence_adjust_timeline_zone_to_selection`

.. rst-class:: clear-both

The purpose of this sub-menu is to allow you to select multiple clips or transitions on the timeline for the purpose of performing operations on all of them simultaneously. However, it should be said up front that making selections this way is not very practical. That is because, in order to select a clip or transition using this menu, you must first position the playhead on it. A much quicker and easier way is to press :kbd:`Shift+RMB`\ [1]_ on each clip you want to add to the selection. The clips do not have to be adjacent to each other to be selected using this method. If the clips you want to select are all adjacent to each other, you can press :kbd:`Shift+LMB`\ [2]_ and hold and then drag your mouse across all the clips. A selection box ("lasso") will appear and every clip and/or composition it touches or encompasses will be selected once you let go of the mouse.


.. _sequence_select_clip:

Select Clip
~~~~~~~~~~~

This type of selection is useful if you work with the keyboard only. With :kbd:`alt + arrow left/right` you can jump from clip to clip.  

The following illustrations show how clips can be selected and a simple move to another track is be performed.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_timeline_selection_1.webp
   :width: 100%
   
   Figure 1: Three selected clips in track V1

In Figure 1, three of the five clips on the timeline have been selected using the :kbd:`Shift+LMB`\ [2]_ method. A selected clip has an orange outline and the highlight color of the filename text is red; not selected clips have a black outline and the filename highlight color is a semi-transparent grey.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_timeline_selection_2.webp
   :width: 100%
   
   Figure 2: Selected clip moved to track V2

Now that multiple clips have been selected, you can do things like moving (dragging), copying, pasting or deleting all of them at once. Or you can use the :ref:`grouping <timeline-group_clips>` function (:menuselection:`Menu --> Sequence --> Group Clips`; default keyboard shortcut is :kbd:`Ctrl+G`) to group the clips together. After clips have been grouped a click on one of the grouped clips selects the entire group. Any clip function (e.g. delete, copy, extract) applies to the entire group. Figure 2 shows that the selected clips from Figure 1 have been moved to another track. This was done by grabbing any of the selected clips with the mouse and dragging them to track V2. Clicking anywhere outside of the selected clips will deselect all of them. Note however, that if you had used the **Group Clips** function on the selection the clips will still be grouped even though they are no longer selected.


.. _sequence_add_clip_to_selection:

Add Clip to Selection
~~~~~~~~~~~~~~~~~~~~~

With :kbd:`Alt + +` you can add additional clips which are under the playhead. 


.. _sequence_deselect_clip:

Deselect Clip
~~~~~~~~~~~~~

With :kbd:`-` you can deselect clips which are under the playhead. 


.. _sequence_select_transition:

Select Transition
~~~~~~~~~~~~~~~~~

.. figure:: /images/user_interface/menu_reference/kdenlive2304_timeline_selection_3.webp
   :width: 100%
   
   Figure 3: Two selected transitions

Selecting multiple transitions works just like selecting clips. Click on the first one and then :kbd:`Shift+LMB`\ [2]_ on as many others as you'd like to add to the selection. Figure 3 shows two **Wipe** compositions selected. These compositions can now be copied, moved (dragged), deleted, etc. just as with clips. Selected compositions have an orange outline and a bright purple semi-transparent background color.


.. _sequence_add_transition_to_selection:

Add Transition To Selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~

With :kbd:`Alt + shift +` you can add additional transitions which are under the playhead. 


.. _sequence_deselect_transition:

Deselect Transition
~~~~~~~~~~~~~~~~~~~

With :kbd:`Shift + -` you can deselect transitions which are under the playhead. 


.. _sequence_adjust_timeline_zone_to_selection:

Adjust Timeline Zone to Selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With :kbd:`Shift + z` the :ref:`timeline zone <timeline_ruler>` get adjusted to the selection. It takes into account the first and the most right selection.


.. _sequence_current_item:

Current Item
------------

.. figure:: /images/user_interface/menu_reference/menu_reference-current_item_menu-2512.webp
   :align: left
   :scale: 77%
   
   Current Item Menu

.. rst-class:: clear-both


* **Edit Duration**: Opens a dialog window where the duration of the clip can be changed with frame-precision.
* **Resize Item Start**: This function (default keyboard shortcut: :kbd:`(`) trims the start of the clip in the current track to where the playhead is.
* **Resize Item End**: This function (default keyboard shortcut: :kbd:`)`) trims the end of the clip in the current track to where the playhead is.
* **Grab Current Item**: This function will make the currently selected item available for moving around with the keyboard arrow keys. The grabbed item will have a thick orange outline. Default shortcut: :kbd:`Shift+G`
* **Delete Selected Item**: Deletes the selected items (e.g. clip, composition). Default shortcut: :kbd:`Del`


.. _timeline-current_clip:

Current Clip
------------

.. figure:: /images/user_interface/menu_reference/menu_reference-current_clip_menu-2512.webp
   :align: left
   :scale: 77%
   
   Current Clip Menu

.. rst-class:: clear-both

This menu item opens a flyout with actions for the currently selected clip(s) in the Timeline:


* **Cut Clip**: Cuts the clip at the point where the playhead is in the Timeline. Default shortcut: :kbd:`Shift+R`
* **Mix Clips**: Creates a same-track-transition between the selected clips. Only works if they are adjacent to each other and on the same track. Default shortcut: :kbd:`U`
* **Change Speed**: Opens a dialog window where the speed change can be entered in %.
* **Restore Video**: If the clip had been added to the Timeline without the audio stream, or the audio stream was deleted, this function brings the audio stream back. It also groups the video stream and audio stream clips. You need a corresponding audio track for this function to work.
* **Disable clip**: Makes the clip invisible for playback or rendering purposes. The clip remains in the Timeline but will not be rendered. A disabled clip is greyed out in the Timeline.
* **Clip in Project Bin**: Opens the Project Bin and highlights the clip.
* **Extract Clip**: Removes the clip from the Timeline and removes the gap :kbd:`Shift+Del`. If the track is set to inactive the clips to the right of the extracted clip will not be moved to fill the gap.
* **Save Clip Part to Bin**: If the selected clip is part of a larger clip (e.g. a cut section) the selected clip part will be saved to the project bin as a new zone under the original clip.
* **Expand Clip**: If the selected clip is a library clip it will be expanded to show all of its components. Make sure you have enough video and audio tracks to hold all of its components.


.. _timeline-group_clips:

Group Clips
-----------

This groups the selected items (e.g. clips, compositions) in the Timeline. Default shortcut: :kbd:`Ctrl+G`. Once grouped together a click on one of the grouped clips selects the entire group.


.. _timeline-ungroup_clips:

Ungroup Clips
-------------

This ungroups a group of items.  Default shortcut: :kbd:`Ctrl+Shift+G`. The group items are still selected after that. Click anywhere outside of the group to deselect the items.


.. _timeline-add_to_library:

Add Timeline Selection to Library
---------------------------------

This function opens a dialog window to enter a name for the library item. Kdenlive will create a :file:`.mlt` clip in the Library from where it can be added to any project. This is useful for intros, outros, logos, watermarks or any other asset that will be used in many projects.

.. _timeline-create_sequence_from_selection:

Create Sequence from Selection
------------------------------

This creates a :ref:`new sequence <Create_nested_sequence>` with the selected clips.


.. _insert_clip_zone:

Insertion
---------

.. figure:: /images/user_interface/menu_reference/menu_reference-insertion_menu-2512.webp
   :align: left
   :scale: 77%
   
   Insertion Menu

- :ref:`insert_clip_zone_in_timeline`
- :ref:`overwrite_clip_zone_in_timeline`

.. rst-class:: clear-both


With this menu you can insert a clip or clip zone into the Timeline or overwrite what is in the Timeline with the clip or clip zone. The default keyboard shortcuts are :kbd:`V` for Insert, and :kbd:`B` for Overwrite.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_timeline_source_target.webp
   :align: left
   :width: 124px
   :figwidth: 124px
   
   ..

.. More info here: https://kdenlive.org/en/2019/08/kdenlive-19-08-released/

   3-point editing is explained in the documentation so this is obsolete


Since version 19.08 "3 point editing with keyboard shortcuts" is implemented. Source and target have to be activated for the clip to be inserted into the Timeline.

.. rst-class:: clear-both


.. _insert_clip_zone_in_timeline:

Insert Clip Zone in Timeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Say you have an eight second zone defined in a clip in the Clip Monitor. When you press :kbd:`V` or select :menuselection:`Menu --> Sequence --> Insertion --> Insert Clip Zone in Timeline`, it will insert the eight second segment of the clip from the Clip Monitor in the timeline.

.. note:: There is an important toggle switch in the Timeline toolbar that fundamentally changes the way the Insert Clip function works: :guilabel:`Use Timeline Zone for Insert`. If it is off (default) inserting a clip happens at the position of the playhead; if it is on inserting a clip happens at the Timeline Zone. See label "1" in the illustrations below.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_timeline_insert_clip_no_zone.webp
   :width: 100%
   
   Insert clip zone from Clip Monitor to Timeline (not using the Timeline Zone)

The clip selected in the Project Bin (in this example My_Video_7.mp4) is displayed in the Clip Monitor. An eight second zone has been defined (see the blue bar between the yellow brackets). The playhead in the Timeline has been positioned where the clip zone is to be inserted. Note the setting of the :guilabel:`Use Timeline Zone for Inserts` switch (1).

Press :kbd:`V` or select :menuselection:`Menu --> Sequence --> Insertion --> Insert Clip Zone in Timeline` and the section in the clip is inserted in the timeline. Any clip already in the Timeline in the target track will be cut, the clip zone inserted and the cut clip pushed to the right to make room for the inserted clip.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_timeline_insert_clip_no_zone_1.webp
   :width: 100%
   
   Insert clip zone from Clip Monitor to Timeline (insert mode)


.. _overwrite_clip_zone_in_timeline:

Overwrite Clip Zone in Timeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Press :kbd:`B` or select :menuselection:`Menu --> Sequence --> Insertion --> Overwrite Clip Zone in Timeline` and the section in the clip is inserted in the timeline overwriting portions of the clip currently in the target track.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_timeline_insert_clip_no_zone_2.webp
   :width: 100%
   
   Insert clip zone from Clip Monitor to Timeline (overwrite mode)

Please note that in the example for the overwrite mode the target track has been changed to V2 only. This is only to demonstrate how target track settings affect the clip operation (in this case no audio stream was inserted because the necessary audio track was set to inactive).

Using the Timeline Zone for inserting the clip:

.. figure:: /images/user_interface/menu_reference/kdenlive2304_timeline_insert_clip_zone.webp
   :width: 100%
   
   Insert clip zone from Clip Monitor to Timeline (using the Timeline Zone)

Press :kbd:`V` or select :menuselection:`Menu --> Sequence --> Insertion --> Insert Clip Zone in Timeline` and the section in the clip is inserted in the timeline starting where the Timeline Zone starts and only for the length of the Timeline Zone. Any clip already in the Timeline in the target track will be cut, the clip zone inserted and the cut clip pushed to the right to make room for the inserted clip.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_timeline_insert_clip_zone_1.webp
   :width: 100%
   
   Insert clip zone from Clip Monitor to Timeline (insert mode)

Press :kbd:`B` or select :menuselection:`Menu --> Sequence --> Insertion --> Overwrite Clip Zone in Timeline` and the section in the clip is inserted in the Timeline starting where the Timeline Zone starts and only for the length of Timeline Zone overwriting portions of the clip currently in the target track.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_timeline_insert_clip_zone_2.webp
   :width: 100%
   
   Insert clip zone from Clip Monitor to Timeline (overwrite mode)

Please note that in the example for the overwrite mode the target track has been changed to V2 only. This is only to demonstrate how target track settings affect the clip operation (in this case no audio stream was inserted because the necessary audio track was set to inactive).


.. _removal:

Removal
-------

.. figure:: /images/user_interface/menu_reference/menu_reference-removal_menu-2512.webp
   :align: left
   :scale: 77%
   
   Removal Menu

- :ref:`extract_timeline_zone`
- :ref:`lift_timeline_zone`

.. rst-class:: clear-both


This function extracts or lifts portions of the Timeline defined by the Timeline Zone. You set the Timeline Zone by defining the In-point and Out-point in the Timeline. Press :kbd:`I` for the In-point, :kbd:`O` for the Out-point. Alternatively, you can click on the :guilabel:`Set Zone In` and :guilabel:`Set Zone Out` icons in the Project Monitor toolbar.

.. hint:: You can also drag the Timeline Zone by grabbing the little square in the middle of the zone bar. This is useful if you want to use the zone with the same length in other places in your project.


.. _extract_timeline_zone:

Extract Timeline Zone
~~~~~~~~~~~~~~~~~~~~~

:guilabel:`Extract Timeline Zone` means to delete that section in the Timeline and moving to the left all clips that are to the right to fill the gap; :guilabel:`Lift Timeline Zone` means to delete that section in the Timeline but leave a gap where the lifted section was.

.. note:: This function takes into account all active tracks. Make sure to make active only those tracks where you want the Timeline Zone to be extracted or lifted from.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_timeline_removal.webp
   :width: 100%
   
   Timeline Removal: Timeline Zone and active tracks

Pressing :kbd:`Shift+X` or selecting :menuselection:`Menu --> Sequence --> Removal --> Extract Timeline Zone` will cut the clips where the Timeline Zone starts and ends, delete that portion and move all clips that are to the right in the Timeline left to close the gap.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_timeline_removal_extract_1.webp
   :width: 100%
   
   Timeline Zone extracted from the Timeline


.. _lift_timeline_zone:

Lift Timeline Zone
~~~~~~~~~~~~~~~~~~

Pressing :kbd:`Z` or selecting :menuselection:`Menu --> Sequence --> Removal --> Lift Timeline Zone` will cut the clips where the Timeline Zone starts and ends, delete that portion but leave all clips that are to the right in the Timeline thus creating a gap.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_timeline_removal_lift_1.webp
   :width: 100%
   
   Timeline Zone lifted from the Timeline

If you want only one track to be affected by this function switch all the other tracks to inactive.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_timeline_removal_extract_2.webp
   :width: 100%
   
   Timeline Zone extracted from the Timeline on only one track (V2)

.. figure:: /images/user_interface/menu_reference/kdenlive2304_timeline_removal_lift_2.webp
   :width: 100%
   
   Timeline Zone lifted from the Timeline on only one track (V2)


.. _timeline-space:

Space
-----

.. figure:: /images/user_interface/menu_reference/menu_reference-space_menu-2512.webp
   :align: left
   :scale: 77%
   
   Space Menu

- :ref:`timeline_space-insert`
- :ref:`timeline_space-remove`
- :ref:`timeline_space-remove`

.. rst-class:: clear-both

This menu item will open a flyout with actions for inserting or removing space in the Timeline.


.. _timeline_space-insert:

Insert Space
~~~~~~~~~~~~

This will open a dialog window where you can specify the duration of the space to be inserted and whether space is inserted in all tracks. 

This function can be used when you want to push all the existing clips on the timeline aside to make room for new clips but also want to preserve the relationships among all the clips that were shifted, including their transitions.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_timeline_insert_space_all_tracks.webp
   :align: left
   
   Figure 1: Insert space

In addition to invoking this menu from :menuselection:`Menu --> Sequence --> Space`, you can also bring it up by right-clicking on an empty spot on a track in the timeline.  There are a couple of important differences how :guilabel:`Insert Space` behaves, though, depending on which method you choose. Using :menuselection:`Menu --> Sequence --> Space --> Insert Space` brings up the **Add Space** dialog shown in Figure 1. Note that the default choice for :guilabel:`Insert space in all tracks` is un-checked.

.. rst-class:: clear-both

.. The section below refers to a version where the Insert (Add) Space dialog window was different and the behavior or defaults depended on whether the function was called via the Timeline menu or right-click in a Timeline track. Clarification is needed whether
   a) the section is deleted altogether
   b) the section is kept but a reference to the version that changed it is added

   .. figure:: /images/user_interface/menu_reference/kdenlive2304_timeline_insert_space.webp
   :align: left
   :alt: Figure 2.

   Figure 2

   When you access the menu by right-clicking on a track, the same dialog appears but the default is the track you clicked on.  In either case, you can obviously override the default by picking another option (Figure 2).  The other difference is that the insertion happens at the playhead when the operation originates from the Timeline menu; it takes place at the mouse cursor position when right-clicking.

   .. rst-class:: clear-both

In case you are wondering why the default :guilabel:`Duration` for the inserted space is 00:00:02:05 (hh:mm:ss:ff) which is not configurable in the :ref:`Kdenlive <settings_menu>` or :doc:`Project Settings</project_and_asset_management/project_settings/general_settings>`.  00:00:02:05 for a project with 30 fps means 65 frames. This default value of 65 frames for inserting space is hard-coded in Kdenlive and will equate to different amounts of time depending on the frame rate set in your project profile. For example, in a project with a rate of 25 frames per second this works out to be 00:00:02:10 - 2 seconds and 10 frames.

Let's look at an example, albeit an unrealistic one, of how inserting space from the playhead position will affect clips and compositions on different tracks. In general, inserting a space will shift any clips that the playhead is *touching* as well as all clips to the right of the playhead on the affected track(s).  Compositions are a little trickier because they span two tracks. They are assumed to “belong” to the higher track (regardless of the direction of the composition) and so if the playhead is touching them they will go only if the higher track is included in the shift.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_timeline_insert_space_1.webp
   :width: 90%
   
   Figure 3: Timeline before inserting space. Compare this with the illustrations below.

Figure 3 shows a scenario with clips on three video tracks before inserting a space. All of the following examples assume we are starting from this position.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_timeline_insert_space_2.webp
   :width: 90%
   
   Figure 4:

In Figure 4 we have chosen to :guilabel:`Insert a space on all tracks`. Since the playhead was touching both compositions and the clips on tracks V1 and V2, it shifted them along with all the clips to the right of the playhead. It did not shift the clip on track V3 because it was to the left of the playhead.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_timeline_insert_space_3.webp
   :width: 90%
   
   Figure 5

In Figure 5 we chose track V3. The composition went because it “belongs” to the clip on track V3, but the clip itself did not go because it was to the left of the playhead. The clip *My_Video_4.mp4* on track V3 also went because it was to the right of the playhead.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_timeline_insert_space_4.webp
   :width: 90%
   
   Figure 6

In Figure 6 we shifted the clips on track V2. Now the Wipe composition between tracks V3 and V2 does not shift, even though the playhead was touching it, because it belongs to track V3. The other transition does go because it belongs to the higher track V2.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_timeline_insert_space_5.webp
   :width: 90%
   
   Figure 7

Finally, in Figure 7, we chose track V1 and just the clips move.

If we had started this process by right-clicking on a spot on track V1 or V3 which corresponds to the playhead position in the example the results would have been the same.


.. _timeline_space-remove:

Remove Space / Remove Space in All Tracks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove Space is not the exact opposite of :ref:`Insert Space <timeline_space-insert>`.

The similarities are:

* If you access :guilabel:`Remove Space` from :menuselection:`Menu --> Sequence --> Space`, the playhead governs where the removal will happen. When using right-click in a track in the Timeline it happens at the mouse cursor.

* Transitions will move with clips on the higher track

There are the following differences:

* If you accessed :guilabel:`Remove Space` from :menuselection:`Menu --> Sequence --> Space`, the playhead must be on an empty space in the track where the space is to be removed.

* You cannot set the duration of the space to be removed – all the empty space between clips is removed. All the clips and transitions to the right of the playhead or mouse cursor will be shifted left until the first clip encounters another clip or the beginning of the track.


.. _timeline-current_track:

Current track
-------------

This menu item opens a flyout with the following functions for the current track:

.. figure:: /images/user_interface/menu_reference/menu_reference-current_track_menu-2512.webp
   :align: left
   :scale: 77%
   
   Current Track Menu

.. rst-class:: clear-both

* **Remove All Spaces After Cursor**: This function will close any gaps between the clips to the right of the cursor.

* **Remove All Clips After Cursor**: This function will remove all clips to the right of the cursor including the one the cursor is on.

.. note:: In this context 'Cursor' means the playhead in the Timeline.


.. _sequence-menu_tracks:

Tracks
------

This menu item opens a flyout with the following functions:

.. figure:: /images/user_interface/menu_reference/menu_reference-tracks_menu-2512.webp
   :align: left
   :scale: 77%
   
   Tracks Menu

.. rst-class:: clear-both

* **Sequence effects**: Lets you quickly apply audio or video effects to all tracks. This can be useful if you want one or more effects to be applied throughout the video. Click the :guilabel:`Master` button above track headers to see the Master Effect Stack. For more details see the :ref:`Master Effect <effects-master_effect>` section of the documentation.

* **Insert Track**: Displays a dialog which lets you choose which type of track to insert and where (before or after a specified existing track)

* **Delete Track**: Displays a dialog which lets you choose which track to delete

* **Switch Track Target Audio Stream**

* **Fit all Tracks in View**: When enabled, the :ref:`tracks fits to the height of the timeline <fit_tracks_to_view_height>`

----

* **Select All in Current Track**: Selects all items in the current track

* **Select All**: Selects all items in all tracks. Default shortcut: :kbd:`Ctrl+A`

* **Deselect**: Cancels the selection. Default shortcut: :kbd:`Ctrl+Shift+A`

----

* **Toggle Track Disabled**: Default shortcut: :kbd:`Shift+H`

* **Toggle All Track Disabled**: Default shortcut: :kbd:`Ctrl+Shift+H`

* **Toggle Track Lock**: Locks or unlocks the current track. A locked track cannot be edited and is marked with a red track number and the |kdenlive-lock| icon. Default shortcut: :kbd:`Shift+L`

* **Toggle All Track Lock**: Toggles the locked/unlocked status of all tracks. All locked tracks will be unlocked, all unlocked tracks will be locked. Default shortcut: :kbd:`Ctrl+Shift+L`

----

* **Toggle Track Active**: Makes the current track active or inactive. The track indicator is green when active, grey when inactive. Default shortcut: :kbd:`A`

* **Toggle All Tracks Active**: Toggles the active/inactive status of all tracks. All active tracks become inactive, all inactive tracks will become active. Default Shortcut: :kbd:`Shift+A`

* **Switch All Tracks Active**: Sets all track to active. Default shortcut: :kbd:`Alt+Shift+A`

----

* **Toggle Track Target**: Default shortcut: :kbd:`Shift+T`

* **Restore Current Clip Target Tracks**:

The sub-menu for inserting and deleting tracks can also be displayed by right-clicking anywhere in the track title.


.. _sequence-menu_subtitle:

Subtitles
---------

This function opens a flyout to switch the Subtitle Editor on or off and to offer additional options for dealing with subtitles.

.. figure:: /images/user_interface/menu_reference/menu_reference-subtitle_menu-2512.webp
   :align: left
   :scale: 77%
   
   Subtitle Menu

.. rst-class:: clear-both

Please refer to the :ref:`effects-subtitles` section of this documentation.


.. _timeline-preview_rendering:

Timeline Preview
----------------

This menu item opens a flyout with options for preview rendering:

.. figure:: /images/user_interface/menu_reference/menu_reference-timeline_preview_menu-2512.webp
   :align: left
   :scale: 77%
   
   Timeline Preview Menu

.. rst-class:: clear-both


* **Start Preview Render**: Starts the rendering process for all defined preview render zones where a change took place (e.g. cut, effect added, deleted or changed). Default shortcut :kbd:`Shift+Return`

* **Stop Preview Render**: Stops a running preview render process

* **Add Preview Zone**: Adds the currently defined Timeline Zone as a preview render zone

* **Remove Preview Zone**: Removes the currently defined Timeline Zone from the preview zones

* **Remove All Preview Zones**: Removes all preview render zones. A preview render can only be started if at least one preview zone is defined.


.. _timeline-disable_timeline_effects:

Disable Timeline Effects
------------------------

Switches Timeline Effects on or off. Click on the :guilabel:`Master` button in the Timeline toolbar to see the master effect stack.


.. _timeline-show_video_thumbnails:

Show Video Thumbnails
---------------------

Switches on or off the display of video thumbnails for the clips in the Timeline. Use the track right-click menu item :guilabel:`Thumbnails` to select which thumbnails will be displayed.


.. _timeline-show_audio_thumbnails:

Show Audio Thumbnails
---------------------

Switches on or off the display of the audio waveform in audio tracks.


.. _timeline-show_markers_comments:

Show Markers Comments
---------------------

Switches on or off the display of the comment of Markers and Timeline Markers.


.. _timeline-toggle_snap:

Snap
----

Switches on or off the snap function. With Snap turned on moving items along the Timeline will make them snap to other items including Markers and Timeline Markers even across different tracks. Default shortcut: :kbd:`Alt+M`


.. _timeline-zoom_in:

Zoom In
-------

Increases the zoom level of the Timeline. Default shortcut: :kbd:`Ctrl++`, or :kbd:`Ctrl+MW`\ [3]_ while the mouse is hovering anywhere over the Timeline.


.. _timeline-zoom_out:

Zoom Out
--------

Decreases the zoom level of the Timeline. Default shortcut: :kbd:`Ctrl+-`, or :kbd:`Ctrl+MW`\ [3]_ while the mouse is hovering anywhere over the Timeline.


.. _timeline-fit_zoom:

Fit Zoom to Project
-------------------

Adjusts the zoom level of the Timeline to fit the entire project into the visible Timeline window.


----

.. [1] RMB = Right mouse button
.. [2] LMB = Left mouse button
.. [3] MW = Mouse wheel