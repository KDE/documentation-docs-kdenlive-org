.. meta::
   :description: Kdenlive Documentation - Configuration Timeline
   :keywords: KDE, Kdenlive, documentation, user manual, configuration, preferences, timeline, video editor, open source, free, learn, easy


.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Timeline
--------

This section controls certain aspects of the Timeline.

.. figure:: /images/getting_started/configure_timeline_2412.webp
   :width: 700px
   :figwidth: 700px
   
   The Timeline section

:1: :guilabel:`Thumbnails` - :guilabel:`Enable for Video/Audio`. By default, thumbnails for video and audio clips will be generated. They will be stored in the :file:`videothumbs` and :file:`audiothumbs` folders, respectively, of the project. See the :doc:`Project Defaults</getting_started/configure_kdenlive/configuration_project_defaults>` section.

:2: :guilabel:`Separate audio channels`. If checked, you will get a separate waveform in the audio thumbnail for each audio channel in the audio track. If unchecked, you will get a single, combined waveform as the audio thumbnail.

:3: :guilabel:`Pause playback when seeking`. If checked, playback in the clip or project monitor will be paused when the playhead is moved manually or you click on a new position in the timeline. Once the seek position is reached, you must click :guilabel:`Play` again to continue playback. If not checked, playback will continue once the playhead is released, and playback is ongoing while you click on a new position in the timeline. This allows looping playback (see :ref:`loop_playback`)

:4: :guilabel:`Jump to timeline start if playback is started on last frame in timeline`

:5: :guilabel:`Seek to clip when adding effect`. If checked, this will position the playhead to the clip in the timeline to which you are adding effects.

:6: :guilabel:`Autoscroll while playing`. If checked, the timeline will scroll during playback to keep the playhead visible in the timeline. If unchecked, the timeline stays put, and the playhead may leave the timeline.

:7: :guilabel:`Scroll vertically with mouse wheel (MW), horizontally with Shift+MW`. Changes the default behavior of the mouse wheel (MW) in the timeline.

:8: :guilabel:`Display clip markers comments`. If checked, comments added to markers are displayed.

:9: :guilabel:`Default track height`. Determines the default height of the tracks in the timeline in pixels. The height can be adjusted anytime by dragging the line between tracks. See the chapter about :ref:`resizing_tracks` for more details.

:10: :guilabel:`Raise Properties Pane when Selecting in Timeline`. Determine for :guilabel:`Clips`, :guilabel:`Transitions`, and :guilabel:`Tracks` whether selecting any of these raises the corresponding properties pane (provided their respective view has been enabled. See the chapter about :doc:`Views</user_interface/menu/view_menu>` for more details).

:11: :guilabel:`On import enable` determines what Kdenlive shall do when an audio clip has multiple audio streams.

:12: :guilabel:`Check if project contains enough tracks`. By default, Kdenlive checks whether the project an audio clip with multiple streams is added to has enough audio tracks to divide the clip into, and if needed asks if it should generate the additionally required audio tracks automatically.