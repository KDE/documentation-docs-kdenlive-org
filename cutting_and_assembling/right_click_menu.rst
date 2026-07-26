.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Gallaecio (https://userbase.kde.org/User:Gallaecio)
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jack (https://userbase.kde.org/User:Jack)
             - Tenzen (https://userbase.kde.org/User:Tenzen)
             - Eugen Mohr

   :license: Creative Commons License SA 4.0

.. _right_click_menu:

Right-Click Menus
=================


Clip in Timeline
----------------

This is the context menu that appears when you right-click on a clip in the timeline.  A different menu appears if you click in empty space in the timeline.

.. figure:: /images/cutting_and_assembling/cutting_and_assembling-right_click_menu-2608.webp

:guilabel:`Copy` will copy the clip and selected clips to the clipboard.

??? :guilabel:`Duplicate Clip` will create a copy of the clip and place it on the timeline after the selected clip.

:guilabel:`Paste Effects` will paste only the effects of the last copied clip to the selected clip.  See :ref:`edit_paste_effects`.

:guilabel:`Remove Effects` will remove all effects from the selected clip.

:guilabel:`Group Clips` - see :ref:`grouping`

:guilabel:`Ungroup Clips` - see :ref:`grouping`

.. figure:: /images/kdenlive_timeline_current_clip_duration02.png
   :align: right
   :scale: 70%

:guilabel:`Edit Duration` - will open the Duration Dialog and will allow you to adjust the position of the clip in the timeline, what time point of the source clip to start on the timeline, the duration of the clip, and what time point of the source clip to end on the timeline. Note that Kdenlive will automatically adjust co-related values. 

.. rst-class:: clear-both

.. figure:: /images/Kdenlive-restore-audio.gif
   :align: right
   :scale: 60%

:guilabel:`Restore audio` will add any audio track that is part of the original clip to the timeline

.. rst-class:: clear-both

:guilabel:`Disable clip` will disable the clip so it will not render in the project monitor or in a final video render. To disable the video or audio part of an A/V clip you have to un-group the A/V clip, disable the video or audio part and group the A/V clip again.

.. _delete_items:

:guilabel:`Delete Selected Item` will delete the item you have selected. Add to the selection: Holding down :kbd:`Shift` and click on additional items. :menuselection:`Timeline --> Current track --> Remove All Clips After Cursor` handles AV clips as 1 element, doesn't matter on which track they are. This function is only in the Timeline menu available this to avoid clutter.  

.. figure:: /images/Kdenlive-extract_clip.gif
   :align: right
   :scale: 50%

:guilabel:`Extract clip` will remove the clip from the timeline and the space it occupied. 

.. rst-class:: clear-both

.. .. versionchanged:: 26.08 renames Replace Timeline Clip to Replace with Project bin selection

:guilabel:`Replace with Bin Selection` will replace the selected clip with the clip that is selected in the project bin. A dialog box appear for confirming the replacement. If no clip is selected in the project bin it allows you to open the dialog for :guilabel:`Import New Clip`.

:guilabel:`Save Clip Part to Bin` save a specific cut section from the timeline back into your Project Bin as an organized sub-clip.

:guilabel:`Create Sequence from Selection` will create a new sequence from minimum two selected clips in the timeline. The selected clips will be replaced by the new created sequence. Details see :ref:`Create_nested_sequence`.

:guilabel:`Copy Selection to New Sequence` will copy in minimum two selected clips from the timeline to a new sequence.

.. figure:: /images/Kdenlive-timeline-righ-click-markersmenu.png
   :align: right
   :scale: 50%

The :guilabel:`Markers` sub-menu allows you to add, edit and remove markers from your clips that are displayed on the timeline.  These markers will move with the clips.  See :ref:`markers`.

.. rst-class:: clear-both

.. .. versionadded:: 25.08

.. figure:: /images/right-click-menu_align-to-reference_2508.webp
   :align: right
   :scale: 50%

The :guilabel:`Align to Reference` sub-menu allows you to set either audio or SMPTE-esque timecode to a reference. This is useful if two or more cameras recorded the same scene simultaneously.

:guilabel:`Set Audio Reference` and :guilabel:`Align Audio to Reference` are used to align clips on different tracks in the timeline based on the audio in the tracks. **Kdenlive** can use the almost identical audio track to align the two clips.

:guilabel:`Set Timecode Reference` and :guilabel:`Align Timecode to Reference` are used to align clips on different tracks in the timeline based on the SMPTE-esque timecode in the tracks.

   To use these features:

   * Select the clip that you would like to align *to*.

   * Right click, select :guilabel:`Set Audio Reference` or :guilabel:`Set Timecode Reference`.

   * Select all the clips that you would like to get aligned.

   * Right-click and select :guilabel:`Align Audio to Reference` or :guilabel:`Align Timecode to Reference`.

.. rst-class:: clear-both

.. _change_speed:

.. figure:: /images/Kdenlive-change_speed_dialog.png
   :align: right
   :scale: 50%

:guilabel:`Change speed` will open the change speed dialog that will allow you to increase or decrease the playback speed of a clip, allow you to play the clip in reverse, and will enable / disable pitch compensation for the audio on a speed-adjusted clip.

Doing speed change of a clip with the mouse see: :ref:`change_speed_of_a_clip` 

:guilabel:`Time Remap` will open the time remap dialog that will allow you to create a speed ramp for a clip.  See :ref:`effects-time_remapping`.

:guilabel:`Clip in project bin` will highlight the selected clip in the project bin.

:guilabel:`Cut Clip` Selecting this will cause the selected clip to be cut at the location of the :ref:`timeline`. See also  :ref:`editing`.

:guilabel:`Insert Effect` will open a sub-menu to allow you to quickly add the :doc:`/effects_and_filters/video_effects/transform_distort_perspective/transform` or the :doc:`/effects_and_filters/video_effects/color_image_correction/lift_gamma_gain` effects.

:guilabel:`Insert composition` will open a sub-menu to allow you to quickly add the :ref:`Composite and Transform <composite_with_transparency>` or the :doc:`Wipe </compositing/transitions/wipe>` composition.


.. _empty_space_in_timeline:

Empty Space in Timeline
-----------------------

A different menu appears if you click in empty space in the timeline.

.. figure:: /images/cutting_and_assembling/cutting-assembling_right-click-empty-space_2608.webp
   
:guilabel:`Paste` will paste a clip from the clipboard into the timeline

:guilabel:`Insert Space` will open the :ref:`Insert Space dialog <timeline_space-insert>` and will allow you to insert blank space in the timeline in a single track. 

:guilabel:`Remove Space` will :ref:`remove all space <timeline_space-remove>` between clips on the track.

:guilabel:`Remove Space in All Tracks` will :ref:`remove space between clips on all the tracks <timeline_space-remove>`.

:guilabel:`Add/Remove Timeline Marker` will add a timeline marker to the timeline or remove an existing one at the playhead's position.

:guilabel:`Edit Timeline Marker` will allow you to edit the timeline marker label.

.. .. versionadded:: 26.08 identify gaps in the timeline

:guilabel:`Identify Gaps` will open a sub-menu to either including :guilabel:`All Tracks` or on the :guilabel:`Selected Track` to create timeline range marker where a gap/space in the timeline exists.

:guilabel:`Go to Marker` will pop up a sub-menu with a list of your timeline markers and will move the timeline position marker to that guide.

:guilabel:`Insert composition` will open a sub-menu to allow you to quickly add the :ref:`Composite and Transform <composite_with_transparency>` or the :doc:`Wipe </compositing/transitions/wipe>` composition.

:guilabel:`Add Clip` (works in video tracks only) will open a sub-menu to allow you to quickly add :ref:`clips to the timeline <add_clips_directly_to_timeline>`.