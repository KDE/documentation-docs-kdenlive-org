.. meta::
   :description: Kdenlive Manual - What's New
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, what's new, new

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             - Eugen Mohr

   :license: Creative Commons License SA 4.0


   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   This page lists the major releases and what features where introduced, changed or deprecated

   Unless a maintenance release (e.g. 23.08.1) introduces a lot or significantly new functionality
   any new features of the .x release should be listed under the respective main release
   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. _24.08: https://kdenlive.org/2024/09/kdenlive-24-08-0-released/

.. _24.05: https://kdenlive.org/2024/05/kdenlive-24-05-0-released/

.. _24.02: https://kdenlive.org/2024/03/kdenlive-24-02-0-released/

.. _23.08: https://kdenlive.org/2023/08/kdenlive-23-08-0-released/

.. _23.04: https://kdenlive.org/2023/04/kdenlive-23-04-0-released/

.. _22.12: https://kdenlive.org/2022/12/kdenlive-22-12-released/

.. _22.08: https://kdenlive.org/2022/08/kdenlive-22-08-released/

.. _22.04: https://kdenlive.org/2022/05/kdenlive-22-04-released/

.. _21.12: https://kdenlive.org/2021/12/kdenlive-21-12-is-out/

.. _21.08: https://kdenlive.org/2021/08/kdenlive-21-08-is-out/

.. _21.04: https://kdenlive.org/2021/04/kdenlive-21-04-released/

.. _20.12: https://kdenlive.org/2020/12/kdenlive-20-12-is-out/

.. _20.08: https://kdenlive.org/2020/08/kdenlive-20-08-is-out/

.. _20.04: https://kdenlive.org/2020/04/kdenlive-20-04-is-out/

.. _19.12: https://kdenlive.org/2019/12/kdenlive-19-12-0-is-out/

.. _19.08: https://kdenlive.org/2019/08/kdenlive-19-08-released/

.. _19.04: https://kdenlive.org/2019/04/kdenlive-19-04-released/


.. _whats_new:

==========
What's New
==========

.. versionadded:: 24.08 (see 24.08_ release notes)

   * Introduced :ref:`effect direct control in monitors <ui-monitors_effect_direct_control>`
   * Introduced :ref:`keyframe curve editor <effects-curve-editor>`
   * Added ability to :ref:`add guides/marker in 10 categories using the NumPad <add_guides>`
   * Introduced :doc:`easing method to fades <effects_and_filters/video_effects/motion/fade_in>`


.. versionadded:: 24.05 (see 24.05_ release notes)

   * Added ability in :ref:`audio recording to set default bin <capturingaudio>`
   * Changed that new :ref:`recorded audio don't get highlighted in the project bin <audio-recording>`
   * Revamped :ref:`audio recording short keys <audio-recording>`
   * Added ability :ref:`to use custom project subfolder on disk <configure_environment>`
   * Added ability :ref:`in monitor to play zone from cursor position <ui-monitors_pm_right_click>`
   * Added ability :ref:`to configure play/pause playback when clicking into monitor <configure_playback>`
   * Introduced :ref:`subtitles translation using SeamlessM4T engine <Translate_with_SeamlessM4T>`
   * Added ability :ref:`to set maximum character per subtitle <Translate_with_SeamlessM4T>`
   * Added an :ref:`output log when subtitles are generated <Translate_with_SeamlessM4T>`
   * Added :ref:`the possibility to customizing camcorder proxy files <configure_proxy_clips>`
   * Introduced :ref:`configurable behavior to change all effects in a group <grouped_clips_effect>`
   * Added ability :ref:`for multi-format rendering <rendering-more_options>`
   * Revamped and :ref:`improved multiple project bin <multibin>`
   * Introduced :ref:`double click to select a track <editing_active_tracks>`


.. versionadded:: 24.02 (see 24.02_ release notes)

   * Revamped :ref:`document checker dialog when open a project <file_open>`
   * Added ability for :ref:`multiple subtitles <effects-subtitles>`
   * Added ability to :ref:`change either the audio or video part of an AV-clip <replace_clip>`
   * Added :ref:`automatically check for updates <automatically_check_for_updates>`
   * Added :ref:`easing modes for keyframes <effects-keyframe-types-interpolation>`
   * Added ability to :ref:`enable/disable effect stack of a clip <disable-enable_clip_stack>`
   * Added ability to :ref:`edit grouped clips <group_clips_edit>`
   * Changed the :ref:`place where Python is stored for speech to text <effects-speech_to_text>`
   * Added ability to :ref:`create sequences from text selection <creating_clips_by_speech_recognition>`


.. versionadded:: 23.08 (see 23.08_ release notes)

   * Changed the way the default sequence is displayed when you :ref:`delete all sequence tabs <Delete_all_sequence_tabs>`
   * Added :kbd:`Shift+double-click` to :ref:`reset track to default height <reset_track_to_default_height>`
   * Added ability to :ref:`fit tracks to view height <fit_tracks_to_view_height>`
   * Changes to the :ref:`Clip jobs <clip_jobs>` menu
   * Changes to the :ref:`Configure clip jobs <configure_clip_jobs>` dialog window
   * Added :kbd:`Shift+z` to :ref:`adjust timeline zone <adjust_timeline_zone>` to selected clips


.. versionadded:: 23.04 (see 23.04_ release notes)

   * Introduced :ref:`Nested timelines / Sequences <sequence>`
   * Changed the :ref:`Clip jobs <clip_jobs>` menu
   * Added a feature to :ref:`configure clip jobs <configure_clip_jobs>`
   * Ability to :ref:`split subtitle after first line <split_subtitle_after_first_line>`
   * Added :ref:`character count and zoom <subtitle-char_count_and_zoom>` to subtitles
   * Added ability to filter the project bin :ref:`using categories <project_bin_filter>`
   * Added ability to :ref:`upload to YouTube and NextCloud <rendering-sharing_video>` directly from Kdenlive


.. versionadded:: 22.12 (see 22.12_ release notes)

   * Added ability to :ref:`switch between a menubar and a hamburger menu <menubar>`
   * New timeline menu entry :ref:`Current Track <timeline_menu>`
   * Removed the :ref:`marker tab <audio_properties>` from audio properties
   * Added ability to :ref:`double-click on animation to edit <edit_an-animation>`
   * Added new function to :ref:`remove all spaces <remove_spaces>` in the current track
   * Added the ability to :ref:`manage categories and guides <managing_guides>`
   * Added the ability to :ref:`manage categories and markers <managing_markers>`
   * Changes to :ref:`export guides as chapter descriptions <export_guides>`
   * Changes to :ref:`export markers as chapter descriptions <export_markers>`
   * Revamped the :ref:`rendering dialog <render>` window


.. versionadded:: 22.08 (see 22.08_ release notes)

   * :ref:`Add animation <add_animation>` (Glaxnimate integration and support of Lottie animation files)
   * :ref:`Edit Project Bin tags <project_bin_tagging>`
   * Deprecated Track compositing fly-out menu (1a/b/c in :ref:`timeline_toolbar2`)
   * Switched to :guilabel:`Enable Track Compositing` being a toggle (see :ref:`timeline_toolbar2`)
   * :ref:`Export guides as chapter descriptions <export_guides>`
   * Added ability to add a :ref:`style <subtitle-style>` to subtitles
   * Added ability to :ref:`import and export <subtitle-import_export>` subtitles


.. versionadded:: 22.04 (see 22.04_ release notes)

   * :ref:`Find action <view-find_action>`
   * Proxy Clips can now be used in preview
   * Added Set Zone In/Out to :ref:`Timeline Ruler right-click menu <timeline_ruler_right-click_menu>`
   * Changed the :guilabel:`Audio` checkbox to a simple checkbox in the Rendering dialog window (see :ref:`More Options <rendering-more_options>`)
   * Added ability to use :ref:`guides for multi export <rendering-multi_export>`
   * Added ability to :ref:`share your videos <rendering-sharing_video>`


.. versionadded:: 21.12 (see 21.12_ release notes)

   * Added the ability to :ref:`create additional project bins <multibin>`
   * Added a checkbox to :ref:`ignore subfolder structure <add_clip>` when importing media
   * New :ref:`slip_tool` for editing


.. versionadded:: 21.08 (see 21.08_ release notes)

   * Enable locking of Guides (see :ref:`timeline Ruler right-click menu <timeline_ruler_right-click_menu>`)
   * :ref:`Guides are moving <move_edit_guides>` with the Spacer tool
   * Introducing :ref:`effects-masking_effects` (see :doc:`/effects_and_filters/video_effects/alpha_mask_keying/mask_apply`)
   * New :ref:`effects-time_remapping` feature


.. versionadded:: 21.04 (see 21.04_ release notes)

   * Added :ref:`zoombars <zoombars>` to the timeline
   * Added :ref:`Key binding information <keybinding_info>` to the status bar
   * Timeline visual overhaul (see :ref:`Timeline visuals <timeline_visuals>`)
   * New :ref:`Media Browser <media_browser>`
   * New icons in the keyframe panel (see :ref:`effects-working_with_keyframes`)
   * Ability to import and export keyframes from/to the clipboard (see :ref:`effects-exchange_keyframes`)
   * Introducing :ref:`effects-effect_zones`
   * Added :ref:`spell checking <subtitle-spell_check>` to subtitles
   * Added a :ref:`typewriter <title-text_typewriter>` effect to the Titler app


.. versionadded:: 20.12 (see 20.12_ release notes)

   * Introducing :ref:`effects-subtitles`
   * Added Subtitles to :ref:`Timeline Ruler right-click menu <timeline_ruler_right-click_menu>`
   * Ability to copy and paste keyframes between effects and across clips (see :ref:`effects-keyframes`)


.. versionadded:: 20.08 (see 20.08_ release notes)

   * :ref:`ui-monitors_zoombar`
   * :ref:`Workspace layouts <ui-workspace_layouts>`
   * Keyframe ruler with zoombars (:ref:`effects-keyframes`)


.. versionadded:: 20.04 (see 20.04_ release notes)

   * :ref:`ui-monitors_preview_resolution`
   * :ref:`Colored tags in the Project Bin <project_bin_tagging>`
   * :ref:`Change clip speed <change_speed_of_a_clip>`
   * :ref:`ui-multitrack_view`


.. versionadded:: 19.12 (see 19.12_ release notes)

   * New :ref:`effects-master_effect` to apply effects to the entire timeline


.. versionadded:: 19.08 (see 19.08_ release notes)

   * Introduced :ref:`3-Point Editing <three_point_editing>` with the keyboard
   * Added ability to have :ref:`colored tags <project_bin_tagging>` in the Project Bin


.. versionadded:: 19.04 (see 19.04_ release notes)

   * :ref:`Support for external monitor display using Blackmagicdesign DeckLink cards <ui-monitors>`
   * :ref:`ui-monitors_display_toolbar`
   * :ref:`Split audio/video <splitAV>`
   * :ref:`Keyboard navigation <keyboard_navigation>`
   * :ref:`Keyframe handling <keyframe_handling>` directly in the clip in the timeline
   * Ability to :ref:`disable individual clips <disable_clips>` in the timeline
   * :ref:`Resizing tracks <resizing_tracks>`
   * :ref:`Configurable tracks <configurable_tracks>`
   * :ref:`Audio record controls in the track header <capturingaudio>`
