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

.. figure:: /images/Kdenlive_timeline.png
  :width: 450px
  :align: left
  :alt: Timeline pane

The timeline is the central part of **Kdenlive**. It is made of 4 different areas (see screenshot).


1 - **Track resizing icon**. This icon allows you to adjust the track height in the timeline from normal to small.  This does not affect the video or the render in any way.  The default height of tracks can be configured in **Kdenlive's** :ref:`configure_kdenlive` dialog.


2 - **Timeline ruler**. This shows the time in frames or in hh:mm:ss notation. The area highlighted in green is called the selection zone, and is useful if you want to render only a part of your project. Left-clicking in the timeline ruler will move the :ref:`timeline` and seek to that position. The Timeline ruler context menu allows you to manage :ref:`guides`.


3 -  **Track header**. This box shows some options for a track. First is the track name (Main Video Track in the screenshot). That name can be changed by simply clicking in it. Below are icons to

   * :menuselection:`Lock the track` |kdenlive-lock| which will prevent adding clips, removing clips, or moving of clips on the timeline;
   * :menuselection:`Mute the track` |kdenlive-hide-audio|
   * :menuselection:`Hide video` |kdenlive-hide-video| from this track; and,
   * :menuselection:`Enable/Disable track effects` |tools-wizard| allows you to enable or disable the effects applied to the track.
   * Right clicking in the track header will give you a context menu allowing to manage (add / delete) tracks.


4 - The track itself, this is where you can drop your clips.


.. versionadded:: 21.04.0
  
**Zoombars**


Besides the availability of zoombars in the monitor and keyframe scroll bars, zoombars are now available in the timeline as well. You can easily zoom in/out in the timeline by dragging the edges of the timeline scrollbar. (Vertical zoombars coming soon.) Recommend playing this video in full-screen mode.

.. image:: /images/Zoom-bar.gif
   :align: left 
   :alt: Zoom-bar
 
  

**Key binding information**


Key binding info has been added on the left while context item information has been moved to the right of the :ref:`status_bar`. Recommend playing this video in full-screen mode.


.. image:: /images/Context-and-keybinds.gif
   :align: left 
   :alt: context-and-keybinds
  


**Improved timeline visuals**


The timeline got a visual overhaul with more and better looking guides/marker colors, the guides have been moved above the timeline ruler while preview and zone bars have been moved below.


.. image:: /images/timeline-overhaul.png
   :align: left 
   :alt: timeline_overhaul
  
Before (above) and after (below)


Split Audio/Video
-----------------



.. versionadded:: 19.04.0


.. image:: /images/splitAV.gif
   :align: left 
   :alt: splitAV


.. versionadded:: 19.04.0 
   
The way timeline tracks work has changed. Each track is now either audio or video, and will only accept audio and video clips respectively. When dragging an AV clip from the project bin in the timeline, the clip will be automatically split, the video part going on a video track, and the audio part on an audio track.   


The separation of audio/video is important for implementing same-track-transitions.


Timeline Cursor/Position Caret/Playhead
---------------------------------------

.. image:: /images/kdenlive_timeline_playhead.png
   :width: 450px
   :align: left
   :alt: timeline playhead

This indicates the position we are displaying in the :ref:`monitors`. You can scroll the position by dragging the Timeline cursor (a.k.a Position Caret or Playhead). 


Beginning with version 0.9.4, dragging the timeline cursor will play the audio of the clip (a.k.a. Audio Scrubbing).  This feature only works if you have checked :menuselection:`Use Open GL for video display` in :ref:`configure_kdenlive`.


Tracks
------

The timeline is made of tracks. There are two kinds of tracks: audio and video. The number of tracks is defined when creating a new project in the :ref:`project_settings`. Adding a clip in timeline can be achieved by dragging it from the :ref:`project_tree` or the :ref:`monitors`. More about tracks see :ref:`tracks`


Resizing tracks
~~~~~~~~~~~~~~~

.. versionadded:: 19.04.0


.. image:: /images/resize-tracks.gif
   :align: left
   :alt: resize-tracks
  


Tracks can be individually resized. (Holding down :kbd:`Shift` makes all video or audio tracks change in height simultaneously.) 


.. image:: /images/layout-modes.gif
   :align: left
   :alt: layout-modes
  


Switch live between two different layout modes (Mixed or Split).


Configurable thumbnails for each track
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 19.04.0


.. image:: /images/Configurable_thumbnails.png
   :align: left
   :alt: Configurable_thumbnails
  


You can choose to display between :menuselection:`In frame`, :menuselection:`In/Out frames`, :menuselection:`All frames` or :menuselection:`No thumbnails`.


Disabling individual clips
--------------------------

.. versionadded:: 19.04.0


.. image:: /images/Disabling_individual_clips.png
   :align: left
   :alt: Disabling_individual_clips
  


Individual clips can be disabled while still in the timeline but with no audio and no video – (works for all clip types). Right-click on the clip and choose :menuselection:`Disable clip` or :menuselection:`Enable clip`.


.. toctree::
   :maxdepth: 1
   :caption: See also:

   menu/timeline_menu
