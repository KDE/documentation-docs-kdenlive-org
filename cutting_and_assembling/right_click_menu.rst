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


.. figure:: /images/kdenlive_right-click_on_clip.png
   

* :menuselection:`Copy` will copy the clip and selected clips to the clipboard.


* :menuselection:`Paste Effects` will paste only the effects of the last copied clip to the selected clip.  See :ref:`edit_paste_effects`.


* :menuselection:`Delete Effects` will remove all effects from the selected clip.


* :menuselection:`Group Clips` - see :ref:`grouping`


* :menuselection:`Ungroup Clips` - see :ref:`grouping`


* :menuselection:`Edit Duration` - will open the Duration Dialog and will allow you to adjust the position of the clip in the timeline, what time point of the source clip to start on the timeline, the duration of the clip, and what time point of the source clip to end on the timeline. Note that Kdenlive will automatically adjust co-related values. 


.. figure:: /images/kdenlive_timeline_current_clip_duration02.png
   

* :menuselection:`Restore audio` will add any audio track that is part of the original clip to the timeline


.. figure:: /images/Kdenlive-restore-audio.gif
   

* :menuselection:`Disable clip` will disable the clip so it will not render in the project monitor or in a final video render. To disable the video or audio part of an A/V clip you have to un-group the A/V clip, disable the video or audio part and group the A/V clip again.

.. _delete_items:

* :menuselection:`Delete Selected Item` will delete the item you have selected. Add to the selection: Holding down :kbd:`Shift` and click on additional items. :menuselection:`Timeline --> Current track --> Remove All Clips After Cursor` handles AV clips as 1 element, doesn't matter on which track they are. This function is only in the Timeline menu available this to avoid clutter.  

* :menuselection:`Extract clip` will remove the clip from the timeline and the space it occupied. 


.. figure:: /images/Kdenlive-extract_clip.gif
   

* :menuselection:`Save timeline zone to bin` will take the selected timeline zone and add markers to your clips in the project bin.


.. figure:: /images/Kdenlive-timeline-righ-click-markersmenu.png
   
* The markers sub-menu allows you to add, edit and remove markers from your clips that are displayed on the timeline.  These markers will move with the clips.  See :ref:`markers`.


.. .. versionadded:: 25.08

.. figure:: /images/right-click-menu_align-to-reference_2508.webp

The :menuselection:`Align to Reference` sub-menu allows you to set either audio or SMPTE-esque timecode to a reference. This is useful if two or more cameras recorded the same scene simultaneously.

* :menuselection:`Set Audio Reference` and :menuselection:`Align Audio to Reference` are used to align clips on different tracks in the timeline based on the audio in the tracks. **Kdenlive** can use the almost identical audio track to align the two clips.

* :menuselection:`Set Timecode Reference` and :menuselection:`Align Timecode to Reference` are used to align clips on different tracks in the timeline based on the SMPTE-esque timecode in the tracks.


   To use these features:


   * Select the clip that you would like to align *to*.


   * Right click, select :menuselection:`Set Audio Reference` or :menuselection:`Set Timecode Reference`.


   * Select all the clips that you would like to get aligned.


   * Right-click and select :menuselection:`Align Audio to Reference` or :menuselection:`Align Timecode to Reference`.




.. _change_speed:

Change speed
^^^^^^^^^^^^

*  :menuselection:`Change speed` will open the change speed dialog that will allow you to increase or decrease the playback speed of a clip, allow you to play the clip in reverse, and will enable / disable pitch compensation for the audio on a speed-adjusted clip.


   .. figure:: /images/Kdenlive-change_speed_dialog.png
      
   Doing speed change of a clip with the mouse see: :ref:`change_speed_of_a_clip` 


* :menuselection:`Clip in project bin` will highlight the selected clip in the project bin.


* :menuselection:`Cut Clip` Selecting this will cause the selected clip to be cut at the location of the :ref:`timeline`. See also  :ref:`editing`.


* :menuselection:`Insert Effect` will open a sub-menu to allow you to quickly add the :doc:`/effects_and_filters/video_effects/transform_distort_perspective/transform` or the :doc:`/effects_and_filters/video_effects/color_image_correction/lift_gamma_gain` effects.


* :menuselection:`Insert composition` will open a sub-menu to allow you to quickly add the :ref:`Composite and Transform <composite_with_transparency>` or the :doc:`Wipe </compositing/transitions/wipe>` composition.


Empty Space in Timeline
-----------------------



A different menu appears if you click in empty space in the timeline.


.. figure:: /images/kdenlive_right-click_in_timeline_space.png
   

* :menuselection:`Paste` will paste a clip from the clipboard into the timeline


* :menuselection:`Insert Space` will open the Insert Space dialog and will allow you to insert blank space in the timeline in a single track. 


* :menuselection:`Remove Space` will remove all space between clips on the track.


* :menuselection:`Remove Space in All Tracks` will remove space between clips on all the tracks.


* :menuselection:`Add/Remove Timeline Marker` will add a timeline marker to the timeline.


* :menuselection:`Edit Guide` will allow you to edit the timeline marker label.


* :menuselection:`Go to TimeLine Marker` will pop-up a sub-menu with a list of your timeline markers and will move the timeline position marker to that guide.


* :menuselection:`Insert composition` will open a sub-menu to allow you to quickly add the :ref:`Composite and Transform <composite_with_transparency>` or the :doc:`Wipe </compositing/transitions/wipe>` composition.
