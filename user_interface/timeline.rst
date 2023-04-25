.. meta::
   :description: Timeline, central part of Kdenlive video editor
   :keywords: KDE, Kdenlive, timeline, track, configure, navigation, working, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Jean-Baptiste Mardelle <jb@kdenlive.org>
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jack (https://userbase.kde.org/User:Jack)
             - Roger (https://userbase.kde.org/User:Roger)
             - Carl Schwan <carl@carlschwan.eu>
             - Eugen Mohr
             - Tenzen (https://userbase.kde.org/User:Tenzen)

   :license: Creative Commons License SA 4.0

.. _timeline:

Timeline
========

.. contents::

The timeline is the central part of **Kdenlive**. It is made of four different areas:

.. figure:: /images/kdenlive_timeline.webp
  :width: 900px
  :align: left
  :alt: Timeline pane


.. rst-class:: clear-both

.. _timeline_areas:

Timeline Areas
--------------

1 -  **Timeline**. This is the area where you drop your clips to the various tracks. It shows the clips with or without thumbnails, with or without the audio frequency curve, transitions and compositions, as well as the markers, guides and keyframes (if any).

2 - **Timeline ruler**. This area shows the time in hh:mm:ss:ff notation. It also shows the current zone (if defined) and the preview render zones and their respective render status. A more detailed description can be found :ref:`further down here <timeline_ruler>`. Left-clicking in the timeline ruler will move the :ref:`timeline` and seek to that position. For the right-click menu see the :ref:`detailed description <timeline_ruler_right-click_menu>`.

3 - **Timeline Toolbar** - This is an important area where the tools for working with the clips in the timeline are easily accessible. Feel free to adjust the timeline toolbar to accommodate your workflow. For details how to do that refer to the section about toolbar configuration.

4 - **Track Header**. This area displays track header data like track type (V for video, A for audio), track number, with your without track effects, hidden or muted, locked or unlocked, and an optional track name. Each track can be adjusted in height individually as well as expanded or collapsed. A more detailed description can be found :ref:`further down here <track_header>`. For the right-click menu see the detailed section.


Timeline
--------

.. _zoombars:

Zoombars
~~~~~~~~

.. versionadded:: 21.04.0

.. container:: clear-both

   .. image:: /images/Zoom-bar.gif
      :align: left 
      :alt: Zoom-bar

   Besides the availability of zoombars in the monitor and keyframe scroll bars, zoombars are now available in the timeline as well. You can easily zoom in/out in the timeline by dragging the edges of the timeline scrollbar. (Vertical zoombars coming soon.) Recommend playing this video in full-screen mode.

.. _keybinding_info:

Key binding information
~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 21.04.0

.. container:: clear-both

   .. image:: /images/Context-and-keybinds.gif
      :align: left 
      :alt: context-and-keybinds

   Key binding info has been added on the left while context item information has been moved to the right of the :ref:`status_bar`. Recommend playing this video in full-screen mode.

.. _timeline_visuals:

Timeline visuals
~~~~~~~~~~~~~~~~

.. versionadded:: 21.04.0

The timeline got a visual overhaul with more and better looking guides/marker colors, the guides have been moved above the timeline ruler while preview and zone bars have been moved below.

.. image:: /images/timeline-overhaul.png
   :alt: timeline_overhaul
  
Before (above) and after (below)

.. rst-class:: clear-both

.. _splitAV:

Split Audio/Video
~~~~~~~~~~~~~~~~~

.. versionadded:: 19.04.0

.. image:: /images/splitAV.gif
   :alt: splitAV
 
The way timeline tracks work has changed. Each track is now either audio or video, and will only accept audio and video clips respectively. When dragging an AV clip from the project bin to the timeline the clip will be automatically split with the video part going on a video track, and the audio part on an audio track.

The separation of audio/video is important for implementing :ref:`same-track-transitions <same_track_transition>`.

.. _timeline_cursor:

Timeline Cursor/Position Caret/Playhead
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: clear-both

   .. image:: /images/kdenlive_timeline_playhead.png
      :width: 450px
      :align: left
      :alt: timeline playhead

   This indicates the position we are displaying in the :ref:`monitors`. You can scroll the position by dragging the Timeline cursor (a.k.a Position Caret or Playhead). 

   Beginning with version 0.9.4, dragging the timeline cursor will play the audio of the clip (a.k.a. Audio Scrubbing).  This feature only works if you have checked :menuselection:`Use Open GL for video display` in :ref:`configure_kdenlive`.

.. rst-class:: clear-both

.. _keyboard_navigation:

Keyboard Navigation
~~~~~~~~~~~~~~~~~~~

.. versionadded:: 19.04.0

You now have the possibility to move clips and compositions with your keyboard. To do it, select a clip in the timeline and use the :guilabel:`Grab Current Item` function from the :menuselection:`Menu --> Timeline` menu or use the default shortcut of :kbd:`Shift + G`.

.. image:: /images/shift-g.gif
   :alt: Moving clips and compositions with Shift+G

You can then move the item with the arrow keys.

Keyframes can also be moved individually. Just click on a keyframe in the timeline, then move it :kbd:`Left` or :kbd:`Right`, change its value with :kbd:`+` and :kbd:`-`. Use :kbd:`Alt + arrow` to go to another keyframe.

.. image:: /images/moving-keyframes.gif
   :alt: Moving clip keyframes in the timeline

.. _keyframe_handling:

Keyframe handling
~~~~~~~~~~~~~~~~~

.. versionadded:: 19.04.0

.. image:: /images/keyframe-improvements.gif
   :alt: Improved keyframe handling
   
* Add a new keyframe by double clicking in timeline.
* You can move a keyframe without altering its value by using the vertical line that appears when you are above or below a keyframe.
* Remove a keyframe by dragging it far above or below the clip limits.

.. _disable_clips:

Disabling individual clips
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 19.04.0

.. container:: clear-both

   .. image:: /images/Disabling_individual_clips.png
      :align: left
      :alt: Disabling_individual_clips
  
   Individual clips can be disabled while still in the timeline but with no audio and no video – (works for all clip types). Right-click on the clip and choose :guilabel:`Disable clip` or :guilabel:`Enable clip`.

.. rst-class:: clear-both


.. _timeline_ruler:

Timeline Ruler
--------------

The timeline ruler shows the timecode information in the notation of hh:mm:ss:ff (default) or in frames. It displays the currently defined timeline zone (1) and the preview render zone (2) and its respective rendering status (red: not yet rendered; yellow: being rendered; green: finished).

.. image:: /images/kdenlive_timeline_ruler.webp
   :alt: Timeline Ruler

The timeline zone can be moved by dragging the square in the middle, and sized by either dragging the left or right edge or by positioning the playhead in the timeline and pressing :kbd:`I` or :kbd:`O` to set in-point and out-point, respectively.
For more detailed information on preview render please refer to this section of the documentation.

.. image:: /images/Kdenlive_timeline_ruler_context-menu.png
   :width: 450px
   :alt: Timeline ruler context menu

Right click into the timeline ruler opens the context menu and allows you to:

  * :ref:`Manipulate guides <guides>`
  * :ref:`Set Zone In/Out <timeline-preview-rendering>`
  * :ref:`Add Project Notes <notes>`
  * :ref:`Add Subtitle <subtitle>`


.. _timeline_toolbar:

Timeline Toolbar
----------------

The timeline toolbar controls various aspects of the editor. It can be configured to accommodate your workflow (see :ref:`Configuring the Toolbars <configuring_the_toolbars>` for more details).

.. image:: /images/kdenlive_timeline_toolbar.webp
   :width: 900px

This is a quick overview of the main sections of the toolbar. A more detailed description can be found in the :ref:`timeline_toolbar3` section of this documentation.

1 - Enable track compositing and switching split view of audio and video (see :ref:`layout_modes`)

2 - Selects the editing mode: Normal, Overwrite, Insert (see :ref:`timeline_edit_modes`)

3 - Edit Tools: Selection Tool, Razor Tool, Spacer Tool, Slip Tool, Ripple Tool (see :ref:`timeline_edit_tools`)

4 - Clip and Zone Tools: Mix Clips, Insert Clip Zone in Timeline, Overwrite Clip Zone in Timeline, Extract Timeline Zone, Lift Timeline Zone, Expand Clip (see also :ref:`3-point editing <three_point_editing>`)

5 - Preview Render Tools - Start/Stop Render, Open Preview Render Options Dialog, Add Preview Render Zone, Delete All Preview Render Zones

6 - Toggle Audio Mixer Widget

7 - Status Bar icons (in lieu of the status bar which can be switched off in the View menu)*

\* Please note this is a customized version of the timeline toolbar and the section #7 is not part of the default toolbar

.. _tracks:

Tracks
------

The timeline is made of tracks. There are two kinds of tracks: audio and video. The number of tracks is defined when creating a new project in the :ref:`project_settings`. Adding a clip to the timeline can be achieved by dragging it from  :ref:`project_tree` or the :ref:`monitors`.

.. _track_header:

Track Header
~~~~~~~~~~~~

This area shows some options for a track:

.. container:: clear-both

   .. image:: /images/kdenlive_timeline4.webp
      :align: left
      :alt: Track header information
   
   
   1 Track collapse and expand icon. Click on it to collapse or expand the track: hold Shift and click to expand or collapse all tracks of the same type.
   
   2 Track name. Click on it to enter or change the name of the track.
   
   3 Track type and track number
   
   4 Track control icons. Use them to:
   
     + Lock the track |kdenlive-lock| which will prevent adding clips, removing clips, or moving of clips on the timeline;  
     + Mute the track |kdenlive-hide-audio| (audio tracks only)  
     + Hide video |kdenlive-hide-video| from this track; and,  
     + Enable/Disable track effects |tools-wizard| allows you to enable or disable the effects applied to the track.

.. rst-class:: clear-both

.. _adding_tracks:

Adding Tracks
~~~~~~~~~~~~~

In order to add a track right-click anywhere in the track header area. In the Add Track dialog window specify what type of track, where and how many you want to insert.

.. image:: /images/kdenlive_timeline_add_track.webp
   :alt: Add track(s)

.. _deleting_tracks:

Deleting Tracks
~~~~~~~~~~~~~~~

In order to delete a track right-click anywhere in the track header area. In the Delete Track dialog window select the tracks you want to delete.

.. image:: /images/kdenlive_timeline_delete_track.webp
   :alt: Delete track(s)

.. _resizing_tracks:

Resizing Tracks
~~~~~~~~~~~~~~~

.. versionadded:: 19.04.0

Tracks can be individually resized. Holding down :kbd:`Shift` makes all video or audio tracks change in height simultaneously.

.. image:: /images/resize-tracks.gif
   :alt: resize-tracks

.. _layout_modes:

Switching between mixed or split audio
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Switch live between two different layout modes (Mixed or Split).

.. image:: /images/layout-modes.gif
   :alt: layout-modes

.. _configurable_tracks:

Configurable Tracks
~~~~~~~~~~~~~~~~~~~

.. versionadded:: 19.04.0

.. container:: clear-both

   .. image:: /images/Configurable_thumbnails.png
      :align: left
      :alt: Configurable_thumbnails
  
   **Video track** - You can choose to display either
   
   - :guilabel:`In Frame`
   
   - :guilabel:`In/Out Frames`
   
   - :guilabel:`All Frames` or 
   
   - :guilabel:`No Thumbnails`

.. container:: clear-both

   .. image:: /images/audio-track_right-click.png
      :align: left
      :alt: audio-track_right-click

   **Audio track** - You can enable:
   
   - :guilabel:`Show Record Controls` to record audio direct into the track. More details see :ref:`audio-recording`.
   
   - :guilabel:`Separate Channels` to see each channel of an audio track (i.e stereo, 5.1)
   
   - :guilabel:`Normalize Audio Thumbnails` maximize the audio level peak to -3dB.   

.. rst-class:: clear-both



.. _loop_playback:

Continuously loop playback
--------------------------

- Disable :guilabel:`Pause playback when seeking` in :ref:`configure_timeline` settings (:menuselection:`Settings --> Configure Kdenlive --> Timeline`). 
- Make a timeline zone the length you like to loop.
- Loop Zone (:kbd:`Ctrl + Shift + Space`)


.. toctree::
   :maxdepth: 4


  
