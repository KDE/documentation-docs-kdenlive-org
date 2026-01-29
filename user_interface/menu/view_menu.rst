.. meta::
   :description: Kdenlive's User Interface - View Menu
   :keywords: KDE, Kdenlive, view, layout, dock, audio, mixer, sequence, title, timeline, animation, subtitle, render, documentation, user manual, video editor, open source, free, learn, easy, view menu

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jack (https://userbase.kde.org/User:Jack)
             - Carl Schwan <carl@carlschwan.eu>
             - Jack (https://userbase.kde.org/User:Jack)
             - Roger (https://userbase.kde.org/User:Roger)
             - Jack (https://userbase.kde.org/User:Jack
             - Yuri Chornoivan
             - Annew (https://userbase.kde.org/User:Annew)
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0

.. |KDE_store| raw:: html

   <a href="https://www.pling.com/browse?cat=333&amp;ord=latest" target="_blank">KDE Store</a>
   
   
.. _view_menu:

View Menu
=========

.. .. versionchanged:: 25.12 Reorder menu structure and content 

The View Menu controls the widgets that appear on screen, and is used for managing screen layouts.

   .. figure:: /images/user_interface/menu_reference/menu_reference-view_menu-2512.webp
     :align: left
     :scale: 77%
     
     Kdenlive View Menu

- :ref:`view_full_screen_mode`
- :ref:`view-load_layout`
- :ref:`view-save_layout`
- :ref:`view-manage_layout`
- :ref:`view_show_title_bars`
- :ref:`view-audio_mixer`
- :ref:`view-clip_monitor`
- :ref:`view-clip_properties`
- :ref:`view-compositions`
- :ref:`view-effects_stack`
- :ref:`view-effects`
- :ref:`view-library`
- :ref:`view-markers`
- :ref:`view-media_browser`
- :ref:`online_resources`
- :ref:`view-project_bin`
- :ref:`view-project_monitor`
- :ref:`view-project_notes`
- :ref:`view_scopes`
- :ref:`view-screen_grab`
- :ref:`view-speech_editor`
- :ref:`view-subtitles`
- :ref:`view-time_remapping`
- :ref:`view-timeline`
- :ref:`undo_history`

.. rst-class:: clear-both


.. _view_full_screen_mode:   

Full Screen Mode
----------------
	 
:guilabel:`Full Screen Mode` toggles the main window of Kdenlive in and out of full screen mode.
   
Please note: This is not to be confused with :kbd:`F11` which toggles the Project or Clip Monitor in and out of full screen mode.
   

.. _view-load_layout:

Load Layout
-----------

This function lets you switch to a previously saved custom workspace layout. More details are available in the :ref:`ui-workspace_layouts` section of this documentation.

.. figure:: /images/user_interface/menu_reference/kdenlive_load_layout01.webp
  :align: left
  
  Loading a workspace layout

Once you load a saved layout, that layout will remain the current one when starting Kdenlive until you switch to another saved layout or modify the current one. If you do make changes to a custom layout after loading it and then quit Kdenlive, you will not be prompted to save your changes to the named layout.  The changes will be remembered and applied the next time you launch Kdenlive, but be aware that you are now working with an unnamed layout. If you like the layout and want to preserve it, save it back to the original name or save it as a new name.

.. rst-class:: clear-both	 


.. _view-save_layout:

Save Layout
-----------

This function allows you to save the workspace layout.

.. save this for future use in a section for workspace layouting:
   Kdenlive allows a great deal of freedom to customize screen layout. You can choose which windows to display and where to position them.  You can resize them or undock them and move them to a second monitor.  Any changes you make to the layout will be automatically saved so that the next time you start Kdenlive, things will look as you left them.  This is fine if you have one layout that works for all your projects.  However, you may want to have different layouts for different types of projects and be able to switch between them as needed.  


.. figure:: /images/user_interface/menu_reference/kdenlive_save_layout01.webp
  :align: left
  :width: 290px
  
  Saving the current workspace layout

In the example shown, no custom layouts have been saved yet so they are just labeled 1 through 4. Click :menuselection:`Save Layout As` and then choose one of the four choices presented.

.. rst-class:: clear-both	 

.. container:: clear-both

   .. figure:: /images/user_interface/menu_reference/kdenlive_save_layout02.webp
      :align: left
      :width: 190px
      
      Naming the saved layout

   The Save Layout dialog appears and you can give your custom layout a name.

.. rst-class:: clear-both	 


.. _view-manage_layout:

Manage Layouts
--------------

This function allows you to manage the saved workspace layouts.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_manage_layouts.webp
   :align: left
   :width: 250px
   
   Kdenlive Manage Layouts function
   
You can delete, re-arrange, reset, import and export the saved layouts.

.. rst-class:: clear-both	 


.. _view_show_title_bars:

Show Title Bars
---------------

:guilabel:`Show Title Bars` toggles the display of the title bars of the various :term:`widgets<widget>` on and off. Turn it off if you need more real estate on your screen. For some widgets you need titlebars to move them around.
   
.. figure:: /images/user_interface/menu_reference/kdenlive_show_titles01.webp
   :align: left
   :width: 200px
	  
   Title Bar

.. figure:: /images/user_interface/menu_reference/kdenlive_show_titles02.webp
   :width: 200px
	  
   No Title Bar
   
.. rst-class:: clear-both	 


.. .. versionremoved:: 25.12
   With the introduction of the KDDockWidgets this function from QtWidget is not needed anymore as the window can now be freely arranged in any orientation.
   
   .. _view-dock_area_orientation:

   Dock Area Orientation
   ---------------------

   This function controls how Kdenlive arranges the workspace layout:

   * Arrange Dock Areas in Columns - Widgets can be stacked like washing machine and dryer at both ends of the screen and scaled vertically independent from the screen split between the Timeline and the area above

   * Arrange Dock Areas in Rows - Widgets can be put next to each other and scaling them horizontally does not affect the widgets in the row above them.

   See the :ref:`ui-customizing_interface` for more details and an illustration.


.. _view-audio_mixer:

Audio Mixer
-----------

Switches the Audio Mixer :term:`widget` on or off.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_audio_mixer.webp
   :align: left
   :height: 400px
   
   Kdenlive Audio Mixer widget
   
This is the main tool for audio handling. It shows all audio tracks and a master volume.

For more details please refer to the :ref:`audio_mixer` section of the documentation.

.. rst-class:: clear-both


.. _view-clip_monitor:

Clip Monitor
------------

Switches the Clip Monitor :term:`widget` on or off.


.. _view-clip_properties:

Clip Properties
---------------

Switches the Clip Properties :term:`widget` on or off.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_clip_properties.webp
   :align:  left
   :height: 250px
   
   Kdenlive Clip Properties widget
   
The Clip Properties :term:`widget` displays the properties of the selected clip. You can change some of the properties.

For more details see the chapter :doc:`Clip Properties</project_and_asset_management/project_bin/clip_properties>`.

.. rst-class:: clear-both


.. _view-compositions:

Compositions
------------

Switches the Compositions :term:`widget` on or off.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_compositions.webp
   :align:  left
   :height: 250px
   
   Kdenlive Compositions widget
   
The Compositions :term:`widget` lists all compositions available in Kdenlive. See the chapter about :doc:`Compositions</compositing/compositions>` for more details and a list of available Compositions.

You can drag a composition from the list and drop it on a clip in the Timeline.

.. rst-class:: clear-both


.. _view-effects_stack:

Effects/Composition Stack
-------------------------

Switches the Effects/Composition Stack on or off.

The Effects/Composition Stack shows all effects applied to a clip or a track. This is where you make changes to the effect settings. See the :ref:`Effects and Filters <effects_and_filters>` section of this documentation for more details.


.. _view-effects:

Effects
-------

Switches the Effects :term:`widget` on or off.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_effects.webp
   :align:  left
   :height: 250px
   
   Kdenlive Effects widget

The Effects :term:`widget` lists all the effects available in Kdenlive. It has groups for effect types (audio, video), custom effects, favorite effects and an option to download effects from |KDE_store|.

You can drag an effect from this list and drop it on a clip in the Timeline, the Project Bin or on the Effect Stack.

More details about effects are available in the :ref:`Effects and Filters <effects_and_filters>` section of this documentation.

.. rst-class:: clear-both


.. _view-library:

Library
-------

Switches the Library :term:`widget` on or off.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_library.webp
   :align:  left
   :height: 250px
   
   Kdenlive Library widget

The Library holds items for generic use in projects. For example watermarks, logos, lower-thirds, intros, and so on. Please refer to the :doc:`Library </project_and_asset_management/library>` section of this documentation for more details.

.. rst-class:: clear-both


.. _view-markers:

Markers
-------

Switches the Markers :term:`widget` on or off.

Markers (Timeline Markers former Guides) are a powerful tool to speed up your workflow. More details about them in the :ref:`guides` section of the documentation.


.. _view-media_browser:

Media Browser
-------------

Switches the Media Browser :term:`widget` on or off.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_media_browser.webp
   :align:  left
   :width: 450px
   
   Kdenlive Media Browser widget

The Media Browser allows you to easily navigate your file system and add clips to your project. For more details refer to the :doc:`Media Browser </project_and_asset_management/media_browser>` section of this documentation.

.. rst-class:: clear-both


.. _online_resources:

Online Resources
----------------

Switches the Online Resources :term:`widget` on or off.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_online_resources.webp
   :align:  left
   :height: 250px
   
   Kdenlive Online Resources widget

The Online Resources :term:`widget` allows you to include assets from various online media providers like Pixabay or Pexels in your project.

See also the :doc:`Online Resources</project_and_asset_management/project_bin/online_resources>` section of this documentation.

.. rst-class:: clear-both


.. _view-project_bin:

Project Bin
-----------

Switches the Project Bin :term:`widget` on or off.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_project_bin.webp
   :align:  left
   :height: 250px
   
   Kdenlive Project Bin widget

The Project Bin is the place where Kdenlive lists all the clips (video, audio, titles, images) or assets associated with the project. For more details refer to the :doc:`Project Bin </project_and_asset_management/project_bin>` section of this documentation.

New in 23.04: Sequences (needed for nested timelines). For more details please see the :ref:`Sequences <sequence>` section of the documentation.

.. rst-class:: clear-both


.. _view-project_monitor:

Project Monitor
---------------

Switches the Project Monitor on or off.

The Project Monitor is used to display your project's timeline, i.e. the edited version of your video. In Edit Mode you can directly manipulate certain effects from within the Project Monitor. Please refer to the :ref:`Project Monitor <ui-monitors_project_monitor>` section of this documentation for more details.


.. _view-project_notes:

Project Notes
-------------

Switches the Project Notes :term:`widget` on or off.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_project_notes.webp
   :align:  left
   :height: 250px
   
   Kdenlive Project Notes widget

Project Notes can be used to keep notes about your project, like ideas or things to do. Please refer to the :doc:`Project Notes </project_and_asset_management/project_notes>` section of this documentation for more details.

.. rst-class:: clear-both


.. _view_scopes:

Scopes
------

   .. figure:: /images/user_interface/menu_reference/menu_reference-view_scopes-2512.webp
     :align: left
     :scale: 87%
     
     Kdenlive View Scopes

- :ref:`view-audio_spectrum`
- :ref:`view-histogram`
- :ref:`view-rgb_parade`
- :ref:`view-vectorscope`
- :ref:`view-waveform`

.. rst-class:: clear-both



.. _view-audio_spectrum:

Scope - Audio Spectrum
~~~~~~~~~~~~~~~~~~~~~~

.. .. versionchanged:: 25.12

Switches the Audio Spectrum :term:`widget` on or off.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_audio_spectrum.webp
   :align:  left
   :height: 250px
   
   Kdenlive Audio Spectrum widget

This allows you to monitor the audio properties of your clip in detail. The graph only displays data while the clip is playing in the clip or project monitor.

It graphs the loudness of the audio in decibels (vertical axis) for each audio frequency (horizontal axis) in the current frame.

.. For more information read the Tips & Tricks chapter about :doc:`/more_information/earlier_versions/audio_spectrum_and_spectrogram`.

.. See also the :ref:`Spectrogram <audio_spectrum_and_spectrogram>` scope which displays a graphical representation of the spectrum over the entire clip.

.. rst-class:: clear-both


.. _view-histogram:

Scope - Histogram
~~~~~~~~~~~~~~~~~

.. .. versionchanged:: 25.12

Switches the Histogram :term:`widget` on or off.

.. figure:: /images/user_interface/menu_reference/view-scopes_histogram_2512.webp
   :align: left
   :height: 300px
   
   Kdenlive Histogram widget

This scope displays a frequency histogram of the luminance of the color components of the video. This information is useful when used in combination with color correction effects to perform color correction on the video. Color correction includes increasing the brightness or adjusting the white balance to ensure that white remains white and not blue.

The histograms have the luminance on the horizontal axis going from 0 on the left to 255 on the right. The vertical axis represents the count of the total number of pixels in the current video frame with a given luminance.

.. rst-class:: clear-both

For more information read the Tips & Tricks chapter about :doc:`/tips_and_tricks/scopes/histogram_working` in the section about :doc:`/tips_and_tricks/scopes/index`.

See also the :doc:`/effects_and_filters/video_effects/utility/histogram` video effect.

.. attention:: Versions before 21.12.2 had an issue in Windows where scopes did not show anything. For more details and a workaround please refer to the :ref:`Windows issues<issue-scopes>` section.


.. _view-rgb_parade:

Scope - RGB Parade
~~~~~~~~~~~~~~~~~~

.. .. versionchanged:: 25.12

Switches the RGB Parade :term:`widget` on or off.

.. figure:: /images/user_interface/menu_reference/view-scopes_rgb-parade_2512.webp
   :align:  left
   :height: 300
   
   Kdenlive RGB Parade widget

The RGB Parade :term:`widget` displays a histogram of the RGB components of the video data.

The horizontal axis represents the timeline in the video frame. The vertical axis is the pixel luminance from 0 to 255. The brightness of the point on the graph represents the count of the number of pixels with this luminance in this column of pixels in the video frame.

.. rst-class:: clear-both

More details including a more thorough explanation is available in the Tips & Tricks chapter about :doc:`/tips_and_tricks/scopes/waveform_and_rgb_parade` in the section about :doc:`/tips_and_tricks/scopes/index`.

See also the :doc:`/effects_and_filters/video_effects/utility/rgb_parade` video effect.


.. _view-vectorscope:

Scope - Vectorscope
~~~~~~~~~~~~~~~~~~~

.. .. versionchanged:: 25.12

Switches the Vectorscope :term:`widget` on or off.

.. figure:: /images/user_interface/menu_reference/view-scope_vectorscope_2512.webp
   :align:  left
   :height: 300
   
   Kdenlive Vectorscope widget

The Vectorscope :term:`widget` allows you to monitor the color properties of your clip in detail.

.. rst-class:: clear-both

More details are available in the Tip & Tricks chapter about the :doc:`Vectorscope </tips_and_tricks/scopes/vectorscope_working>` and :doc:`/tips_and_tricks/scopes/vectorscope_i_and_q_lines` in the section about :doc:`/tips_and_tricks/scopes/index`.

See also the :doc:`/effects_and_filters/video_effects/utility/vectorscope` and :doc:`/effects_and_filters/video_effects/utility/vectorscope_advanced` video effects.


.. _view-waveform:

Scope - Waveform
~~~~~~~~~~~~~~~~

.. .. versionchanged:: 25.12

Switches the Waveform :term:`widget` on or off.

.. figure:: /images/user_interface/menu_reference/view-scope_waveform_2512.webp
   :align:  left
   :height: 300px
   
   Kdenlive Waveform widget

Contrary to what its name might suggest the Waveform :term:`widget` is not for audio but represents the Luma component (whiteness) of the video. It is the same type of graph as for the :term:`RGB Parade`. The horizontal axis represents the horizontal axis in the video frame. The vertical axis is the pixel :term:`luma` from 0 to 255. The brightness of the point on the graph represents the count of the number of pixels with this :term:`luma` in this column of pixels in the video frame.

.. rst-class:: clear-both

More details are available in the :doc:`Tips & Tricks</tips_and_tricks/index>` chapter about the :doc:`Waveform </tips_and_tricks/scopes/waveform_and_rgb_parade>` in the section about :doc:`/tips_and_tricks/scopes/index`.

See also the :doc:`/effects_and_filters/video_effects/utility/video_waveform_monitor` video effect.


.. _view-screen_grab:

Screen Grab
-----------

Switches the Screen Grab :term:`widget` on or off.

.. note:: This function has issues and should not be used. It has not been maintained for a while. There are other tools and applications for screen recording or grabbing available, hence this function will most likely be deprecated.

You can configure the ScreenGrab function in :menuselection:`Menu --> Settings --> Configure Kdenlive -->`\ :doc:`/getting_started/configure_kdenlive/configuration_capture`.


.. _view-speech_editor:

Speech Editor
-------------

Switches the Speech Editor :term:`widget` on or off.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_speech_editor.webp
   :align:  left
   :width: 400px
   
   Kdenlive Speech Editor widget

The Speech Editor :term:`widget` allows you to use AI-based speech recognition to create subtitles for your video. You need to configure speech-to-text in Kdenlive in order to use this. More details about the configuration and potentially necessary installations as well as how to use speech recognition is available in the :ref:`Speech-to-Text <effects-speech_to_text>` section of this documentation.

.. rst-class:: clear-both


.. _view-subtitles:

Subtitles
---------

Switches the Subtitle :term:`widget` on or off.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_subtitles.webp
   :align:  left
   :height: 300px
   
   Kdenlive Subtitles widget

The Subtitle :term:`widget` is used to manage the subtitles for your project. For more details please refer to the :ref:`Subtitles <effects-subtitles>` section of this documentation.

.. rst-class:: clear-both


.. _view-time_remapping:

Time Remapping
--------------

The Time Remapping :term:`widget` allows you to create speed ramping.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_time_remapping.webp
   :align:  left
   :height: 300px
   
   Kdenlive Time Remapping widget

More details are available in the :ref:`Time Remapping <effects-time_remapping>` section of this documentation.

.. rst-class:: clear-both


.. _view-timeline:

Timeline
--------

Switches the Timeline on or off.

The Timeline is the central part of Kdenlive where you put together your video. A more detailed description is available in the :ref:`timeline` section of this documentation.


.. _undo_history:

Undo History
------------
.. .. versionchanged:: 25.08

Switches the Undo History :term:`widget` on or off.

The Undo History shows all the operations performed so far and allows to quickly restore your project to the state it was in several changes ago.

.. figure:: /images/user_interface/menu_reference/view-menu_undo-history_2508.webp
   :align:  left
   :height: 250px
   
   Kdenlive Undo History widget

There may be times when you want to quickly restore your project to the state it was in several changes ago. Instead of repeatedly executing single undo operations, it might be more efficient to jump right to the operation in question - if you could easily locate it.

Use :kbd:`RMB` anywhere in the window to open a context menu to clear all undo history. Clicking that button will issue a warning that the undo history will be deleted irretrievably. Clearing the undo history may be helpful to release memory in long edit sessions. The undo stack is cleared also when a timeline sequence gets deleted.

.. rst-class:: clear-both

.. container:: clear-both

   .. figure:: /images/undo_history_clean.png
      :align: left
      :width: 210px
      
      Figure 1

   That is where :menuselection:`Menu --> View --> Undo History` comes in. It opens a dockable window which lists all the changes made to your project in the order they were made. When a project file is first opened the window looks like Figure 1.


.. container:: clear-both

   .. figure:: /images/undo_history_pre-save.png
      :align: left
      :width: 210px
      
      Figure 2

   Each operation you perform from then on gets added to the list, as shown in Figure 2.  Notice that the most recent operation you have performed is highlighted. 


.. container:: clear-both

   .. figure:: /images/undo_history_back_three.png
      :align: left
      :width: 210px
      
      Figure 3

   In this example, if you wanted to undo the last three operations with one click all you have to do is click on the **Create color clip** entry and those three changes will be reversed in one fell swoop.  At this point if you are unhappy with undoing those changes you can easily redo them by clicking on any of the entries which are still in the list.


.. container:: clear-both

   .. figure:: /images/undo_history_commited.png
      :align: left
      :width: 210px
      
      Figure 4

   However, if you decided that reverting to that **Create color clip** entry looked good and you then made another change to the project the three remaining operations that were in the list in Figure 3 will be flushed from the buffer and be no longer available.  They will be replaced by the new operation you just performed.  See the result in Figure 4.


.. container:: clear-both

   .. figure:: /images/undo_history_post_save.png
      :align: left
      :width: 210px
      
      Figure 5

   Whenever you save your project the icon that looks like the backspace icon is repositioned next to the most recent operation in the list.  Figure 5 shows three additional operations which were performed after the file save shown by the square.  After saving the file you can still revert back to changes which were made before the save.
