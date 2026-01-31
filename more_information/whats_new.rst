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

.. _25.12: https://kdenlive.org/news/releases/25.12.0/

.. _25.08: https://kdenlive.org/news/releases/25.08.0/

.. _25.04: https://kdenlive.org/news/releases/25.04.0/

.. _24.12: https://kdenlive.org/news/releases/24.12.0/

.. _24.08: https://kdenlive.org/news/releases/24.08.0/

.. _24.05: https://kdenlive.org/news/releases/24.05.0/

.. _24.02: https://kdenlive.org/news/releases/24.02.0/

.. _23.08: https://kdenlive.org/news/releases/23.08.0/

.. _23.04: https://kdenlive.org/news/releases/23.04.0/

.. _22.12: https://kdenlive.org/news/releases/22.12.0/

.. _22.08: https://kdenlive.org/news/releases/22.08.0/

.. _22.04: https://kdenlive.org/news/releases/22.04.0/

.. _21.12: https://kdenlive.org/news/releases/21.12.0/

.. _21.08: https://kdenlive.org/news/releases/21.08.0/

.. _21.04: https://kdenlive.org/news/releases/21.04.0/

.. _20.12: https://kdenlive.org/news/releases/20.12.0/

.. _20.08: https://kdenlive.org/news/releases/20.08.0/

.. _20.04: https://kdenlive.org/news/releases/20.04.0/

.. _19.12: https://kdenlive.org/news/releases/19.12.0/

.. _19.08: https://kdenlive.org/news/releases/19.08.0/

.. _19.04: https://kdenlive.org/news/releases/19.04.0/


.. _whats_new:

==========
What's New
==========

.. versionadded:: 25.12 (see 25.12_ release notes)

   * Added 1080p preview scaling in :ref:`monitor <ui-monitors_preview_resolution>`
   * Added 10-bit pipeline support for :ref:`effects <effects-effects_tab>` and :ref:`composition <compositions-effects_tab>` and :ref:`rendering <rendering_preset_categories>`
   * Moved controls and settings to hamburger menus in :ref:`color scopes <view-audio_spectrum>`
   * Added clipping indicator in :ref:`audio mixer <audio_mixer>`
   * Moved timeline audio waveform zoom control from audio track header to :ref:`status bar <status_bar>`
   * Added button to hide clip overlays (clip name, effect names, ...) in the :ref:`timeline <status_bar>`
   * Added placeholder explaining how to import media in :doc:`project bin </project_and_asset_management/project_bin>`
   * Replaced "Guide" with "Marker" and/or :ref:`"timeline marker" <guides>`
   * Added range/duration support in :ref:`marker system <markers_with_range>`
   * Reordered menu structure to make it :ref:`clearer <menu>`
   * Revamped audio view in :ref:`clip monitor <ui-monitors_clip_monitor>`
   * Introduced KDDockWidgets library for :ref:`improved window docking <ui-moving_widgets>`
   * Added safe-area button, vertical safe-area layout, and zoom-reset in :ref:`monitor toolbar <ui_elements-monitor_elements>`
   * Added a :ref:`welcome screen <welcome_and_splash_screen>`


.. versionadded:: 25.08 (see 25.08_ release notes)

   * Added checkerboard option in :ref:`clip monitor<ui-monitors_clip_monitor_hamburger>`
   * Added possibility to :ref:`hide all tracks at once<sequence-menu_tracks>`
   * Added possibility to :doc:`make autosave configurable</getting_started/configure_kdenlive/configuration_misc>`
   * Revamp and updated the :doc:`titler</titles_and_graphics/titles/title_images>`
   * Revamp and updated the :doc:`notes widget</project_and_asset_management/project_notes>`
   * Added possibility for :ref:`timecode offset per sequence<sequence_timecode_offset>`
   * Added possibility to :ref:`show thumbnails/all project clip markers in markers list<guide_view>`
   * Removed link to app :ref:`MediaInfo<configure_environment_mlt>`
   * Added possibility to :ref:`manually clear all undo history<undo_history>`
   * Added possibility to :ref:`align clip based on SMPTE-esque timecode<delete_items>`
   * Added possibility to :ref:`expand/collapse items (effects, folders) and navigate effects with arrows<track_header>`
   * Added in the timeline :ref:`ctrl+x for cut<edit_menu>`
   * Added possibility to :doc:`disable power management while rendering or when playback</getting_started/configure_kdenlive/configuration_environment>`
   * Revamp :ref:`audio mixer and levels<audio_mixer>`
   * Added possibility to :ref:`create a new subtitle layer by Shift+drag a subtitle down<subtitle-multi-layer_subtitling>`


.. versionadded:: 25.04 (see 25.04_ release notes)

   * Introduced :doc:`object segmentation</effects_and_filters/video_effects/alpha_mask_keying/object_mask>`
   * Introduced support for :ref:`OpenTimeLineIO import and export <file_opentimelineio_export>`
   * Added possibility to :ref:`zoom waveform in the audio track <status_bar>`
   * Added possibility to :ref:`collapse and expand all effects in the effect stack<effect_functions>`
   * Added in the :ref:`duration dialog a checkbox for ripple delete<resizing_multiple_timeline_items>`
   * Added :doc:`shortcuts for find next/previous text phrase in the project notes</project_and_asset_management/project_notes>`


.. versionadded:: 24.12 (see 24.12_ release notes)

   * Introduced :ref:`multiple Subtitle Tracks <effects-subtitles>`
   * Introduced :ref:`built-in effects <builtin-effects>`
   * Introduced :ref:`resizing multiple timeline items <resizing_multiple_timeline_items>`
   * Added on :ref:`effects and compositions a direct link to the documentation <effect_functions>`
   * Added a :ref:`shortcut to extract clip from timeline <timeline-current_clip>`
   * Added new :doc:`MLT HSL color correction effect </effects_and_filters/video_effects/color_image_correction/hsl_primaries>`


.. versionadded:: 24.08 (see 24.08_ release notes)

   * Introduced :ref:`effect direct control in monitors <ui-monitors_effect_direct_control>`
   * Introduced :ref:`keyframe curve editor <effects-curve-editor>`
   * Added ability to :ref:`add guides/marker in 10 categories using the NumPad <add_guides>`
   * Introduced :doc:`easing method to fades </effects_and_filters/video_effects/motion/fade_in>`


.. versionadded:: 24.05 (see 24.05_ release notes)

   * Added ability in :ref:`audio recording to set default bin <capturing_audio_target>`
   * Changed that new :ref:`recorded audio don't get highlighted in the project bin <audio-recording>`
   * Revamped :ref:`audio recording short keys <audio-recording>`
   * Added ability :doc:`to use custom project subfolder on disk </getting_started/configure_kdenlive/configuration_environment>`
   * Added ability :ref:`in monitor to play zone from cursor position <ui-monitors_pm_right_click>`
   * Added ability :doc:`to configure play/pause playback when clicking into monitor </getting_started/configure_kdenlive/configuration_playback>`
   * Introduced :ref:`subtitles translation using SeamlessM4T engine <Translate_with_SeamlessM4T>`
   * Added ability :ref:`to set maximum character per subtitle <Translate_with_SeamlessM4T>`
   * Added an :ref:`output log when subtitles are generated <Translate_with_SeamlessM4T>`
   * Added :doc:`the possibility to customizing camcorder proxy files </getting_started/configure_kdenlive/configuration_proxy_clips>`
   * Introduced :ref:`configurable behavior to change all effects in a group <grouped_clips_effect>`
   * Added ability :ref:`for multi-format rendering <rendering-more_options>`
   * Revamped and :doc:`improved multiple project bin </project_and_asset_management/project_bin/project_bin_use_multiple_bins>`
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
   * Changes to the :ref:`Media jobs <media_jobs>` menu
   * Changes to the :ref:`Configure clip jobs <configure_clip_jobs>` dialog window
   * Added :kbd:`Shift+z` to :ref:`adjust timeline zone <adjust_timeline_zone>` to selected clips


.. versionadded:: 23.04 (see 23.04_ release notes)

   * Introduced :ref:`Nested timelines / Sequences <sequence>`
   * Changed the :ref:`Media jobs <media_jobs>` menu
   * Added a feature to :ref:`configure clip jobs <configure_clip_jobs>`
   * Ability to :ref:`split subtitle after first line <split_subtitle_after_first_line>`
   * Added :ref:`character count and zoom <subtitle-char_count_and_zoom>` to subtitles
   * Added ability to filter the project bin :doc:`using categories </project_and_asset_management/project_bin/project_bin_use_filters>`
   * Added ability to :ref:`upload to YouTube and NextCloud <rendering-sharing_video>` directly from Kdenlive


.. versionadded:: 22.12 (see 22.12_ release notes)

   * Added ability to :ref:`switch between a menubar and a hamburger menu <menubar>`
   * New timeline menu entry :ref:`Current Track <sequence_menu>`
   * Removed the marker tab from :doc:`clip properties</project_and_asset_management/project_bin/clip_properties>`
   * Added ability to :ref:`double-click on animation to edit <edit_an-animation>`
   * Added new function to :ref:`remove all spaces <remove_spaces>` in the current track
   * Added the ability to :ref:`manage categories and guides <managing_guides>`
   * Added the ability to :ref:`manage categories and markers <managing_markers>`
   * Changes to :ref:`export guides as chapter descriptions <export_guides>`
   * Changes to :ref:`export markers as chapter descriptions <export_guides>`
   * Revamped the :ref:`rendering dialog <render>` window


.. versionadded:: 22.08 (see 22.08_ release notes)

   * :doc:`Add animation </project_and_asset_management/project_bin/animation>` (Glaxnimate integration and support of Lottie animation files)
   * :doc:`Edit Project Bin tags <project_bin_use_tags>`
   * Deprecated Track compositing fly-out menu (1a/b/c in :ref:`timeline_toolbar2`)
   * Switched to :guilabel:`Enable Track Compositing` being a toggle (see :ref:`timeline_toolbar2`)
   * :ref:`Export guides as chapter descriptions <export_guides>`
   * Added ability to add a :ref:`style <subtitle-style-editor>` to subtitles
   * Added ability to :ref:`import and export <subtitle-import_export>` subtitles


.. versionadded:: 22.04 (see 22.04_ release notes)

   * :ref:`Find action <help-find_action>`
   * Proxy Clips can now be used in preview
   * Added Set Zone In/Out to :ref:`Timeline Ruler right-click menu <timeline_ruler_right-click_menu>`
   * Changed the :guilabel:`Audio` checkbox to a simple checkbox in the Rendering dialog window (see :ref:`More Options <rendering-more_options>`)
   * Added ability to use :ref:`guides for multi export <rendering-multi_export>`
   * Added ability to :ref:`share your videos <rendering-sharing_video>`


.. versionadded:: 21.12 (see 21.12_ release notes)

   * Added the ability to :doc:`create additional project bins </project_and_asset_management/project_bin/project_bin_use_multiple_bins>`
   * Added a checkbox to :doc:`ignore subfolder structure </project_and_asset_management/project_bin/clips>` when importing media
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
   * New :doc:`Media Browser </project_and_asset_management/media_browser>`
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
   * :doc:`Colored tags in the Project Bin </project_and_asset_management/project_bin/project_bin_use_tags>`
   * :ref:`Change clip speed <change_speed_of_a_clip>`
   * :ref:`ui-multitrack_view`


.. versionadded:: 19.12 (see 19.12_ release notes)

   * New :ref:`effects-master_effect` to apply effects to the entire timeline


.. versionadded:: 19.08 (see 19.08_ release notes)

   * Introduced :ref:`3-Point Editing <three_point_editing>` with the keyboard
   * Added ability to have :doc:`colored tags </project_and_asset_management/project_bin/project_bin_use_tags>` in the Project Bin


.. versionadded:: 19.04 (see 19.04_ release notes)

   * :ref:`Support for external monitor display using Blackmagicdesign DeckLink cards <ui-monitors>`
   * :ref:`ui-monitors_display_toolbar`
   * :ref:`Split audio/video <splitAV>`
   * :ref:`Keyboard navigation <keyboard_navigation>`
   * :ref:`Keyframe handling <keyframe_handling>` directly in the clip in the timeline
   * Ability to :ref:`disable individual clips <disable_clips>` in the timeline
   * :ref:`Resizing tracks <resizing_tracks>`
   * :ref:`Configurable tracks <configurable_tracks>`
   * :doc:`Audio record controls in the track header </project_and_asset_management/capturing_audio>`
