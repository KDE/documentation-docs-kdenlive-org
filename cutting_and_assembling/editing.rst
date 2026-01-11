.. meta::
   :description: Editing in Kdenlive video editor
   :keywords: KDE, Kdenlive, edit, animation, editing, timeline, documentation, user manual, video editor, open source, free, learn, easy


.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Jean-Baptiste Mardelle <jb@kdenlive.org>
             - TheDiveO
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Vincent Pinon <vpinon@kde.org>
             - Jessej (https://userbase.kde.org/User:Jessej)
             - Jack (https://userbase.kde.org/User:Jack)
             - Roger (https://userbase.kde.org/User:Roger)
             - TheMickyRosen-Left (https://userbase.kde.org/User:TheMickyRosen-Left)
             - Eugen Mohr
             - Smolyaninov (https://userbase.kde.org/User:Smolyaninov)
             - Tenzen (https://userbase.kde.org/User:Tenzen)
             - Anders Lund

   :license: Creative Commons License SA 4.0





.. _editing:

Editing
=======


Editing is done in the :ref:`timeline`. Add a clip by dragging it from the :doc:`project bin</project_and_asset_management/project_bin>` or the :ref:`ui-monitors`. Once a clip is dropped on a track, it can be moved (drag and drop it) to another place on the same track or onto another track.


.. figure:: /images/Kdenlive-addcliptotimeline.gif


.. .. versionadded:: 19.08.0
   Editing with keyboard shortcuts was introduced

Editing with keyboard shortcuts can speed up the editing work, and you can do editing steps that are not possible or not as quick and easy with the mouse. Working with keyboard shortcuts from version 19.08 onwards is different as in previous Kdenlive versions. Mouse operations have not changed and work as before. See `3 Point Editing`_


Seeking through your project
----------------------------

The timeline cursor shows your current position in the project. The positions of the cursors on the timeline ruler and Project Monitor are always in sync. Position can be moved in the following ways:


* Keyboard shortcut: right / left arrows for one frame, Shift+ right / left for 1 second


* Clicking/dragging in the :ref:`timeline` or in an empty area of the timeline. 


* Clicking/dragging in the :ref:`ui-monitors` ruler.


* Rotating the mouse wheel while the pointer is over the :ref:`timeline` or over the :ref:`ui-monitors`


* Editing the timecode in the :ref:`ui-monitors`  timecode widget


* Clicking the up or down arrows on the :ref:`ui-monitors` timecode widget


Cutting a Clip
--------------

To cut a clip, the easiest way is to place the timeline cursor where you want to cut the clip, then select the clip (left click in it) and use the menu :menuselection:`Timeline --> Current Clip --> Cut Clip` (default shortcut: :kbd:`Shift + R`).


Or  :menuselection:`Right Click --> Cut Clip`


Alternatively - use the `Spacer Tool`_.


Resizing a Clip
---------------

A clip can be resized from its start or end by dragging its left or right edge. If you want a more precise resize, you can place the timeline cursor wherever you want the resize to end and use the menu :menuselection:`Timeline --> Resize Item Start` (default shortcut: :kbd:`(` or :menuselection:`Timeline --> Resize Item End` (default shortcut: :kbd:`)`)


To even more precisely control the length of a clip, double click it in the timeline and adjust its duration using the **Clip duration** dialog. You can have frame-level accuracy with this method.


.. figure:: /images/kdenlive_timeline_current_clip_duration02.png


You can also resize a clip by cutting it with the  `Razor Tool`_ and then deleting the bit you do not want.

.. .. versionadded:: 19.08

Adjust AV clips independently with :kbd:`Shift + resize` to resize only audio or video part of a clip. 

:kbd:`alt + Move` in timeline allows to move the audio or video part to another track independently.

.. figure:: /images/av-metamove.gif

.. .. versionadded:: 23.08

.. figure:: /images/resize_clip_yellow_indicator.gif

Select a clip in the project bin. When resizing this clip in the timeline the clip monitor shows a yellow indicator relative to the original clip length. 


.. _resizing_multiple_timeline_items:

Resizing multiple timeline items
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. .. versionadded:: 24.12

Select several clips in the timeline. Double click on one of the clips. The Duration dialog window pops up. Enable :guilabel:`Apply duration to all items`, otherwise nothing happens.

The duration/resize is linked to the start position of each clip. Meaning if you select three clips and reduce the duration you get gaps between each clip as the start position of each clip is fixed.

:guilabel:`Position` show the start position of the most left selected clip

.. .. versionadded:: 25.04

:guilabel:`Duration` shows the length of the first selected clip done by :kbd:`Shift + LMB`. When selected by :kbd:`Shift + drag` it show the length of the most left clip.

.. figure:: /images/kdenlive2504_resizing-multiple-clip.webp
   :width: 50%
   :figwidth: 50%

   Selection with :kbd:`Shift + drag` shows the length of the most left clip 

-	Shorten and lengthen duration: The clips get shortened/lengthened but keep their starting position

-	Clips attached to each other: You cannot lengthen the clips

.. .. versionadded:: 25.04

Change duration with :guilabel:`Ripple resize` enabled

.. figure:: /images/kdenlive2504_resizing-multiple-clip-ripple.webp
   :width: 50%
   :figwidth: 50%

   Selection with :kbd:`Shift + click` shows the length of the first selected clip

-	Shorten and lengthen duration: The starting position of the left most selected clip on each track is fixed. Any gaps between clips are kept.

-	Clips attached to each other: All clips attached to the right will lengthen or shorten according to the left most clip, keeping their attachment.


.. _edit_an-animation: 

Edit an Animation
-----------------

.. .. versionadded:: 22.12

.. note::
   This requires Glaxnimate version >= 0.5.1

Double click on an animation clip in the timeline and this will open Glaxnimate. 

.. figure:: /images/animation_with__background.png


The background of the animation in Kdenlive will also be shown in Glaxnimate.

.. figure:: /images/glaxnimate_with_background.png


It is possible to have several Glaxnimate instances open, but the background will only be send to the one opened first in Glaxnimate. If you like to see the Kdenlive background of another animation clip, save the animation and close Glaxnimate before you double click another animation clip.


.. _change_speed_of_a_clip: 

Change Speed of a Clip
----------------------

.. .. versionadded:: 19.08

.. figure:: /images/adjustspeed.gif


Adjust the speed of a clip by pressing :kbd:`CTRL + dragging` a clip in the timeline.

Doing with right click on the clip see :ref:`change_speed`. 


.. _remove_spaces:

Removing Space Between Clips
----------------------------

Right click in the space between the clips and choose :menuselection:`Remove Space`. Be aware however that if you have clips on multiple tracks in the timeline and they are not grouped, then removing space may disturb the alignment of the clips between the different tracks – the space is only removed from the timeline where you clicked.  Under this situation it may be safer to use the `Spacer Tool`_.


.. figure:: /images/Kdenlive-removespace.gif

.. .. versionadded:: 22.12

:menuselection:`Timeline --> Current track --> Remove All Spaces After Cursor`

It handles AV clips as 1 element, doesn't matter on which track they are. This function is only in the Timeline menu available this to avoid clutter. 

More details see :ref:`timeline_space-remove`.


.. _adjust_timeline_zone:

Adjust timeline zone
--------------------

.. .. versionadded:: 23.08

:kbd:`Shift+z` adjusts timeline zone to selected clips

.. figure:: /images/adjust_timeline_zone_to_selection.gif


.. _timeline_toolbar2:

Timeline Toolbar
----------------

There is a toolbar between monitors and the timeline that controls various aspects of the editor. 


.. figure:: /images/Kdenlive-middle-toolbar.png


1.  `Track Compositing`_ drop down.

.. .. versionchanged:: 22.08

.. figure:: /images/Kdenlive-enable-track-composition.png

Track compositing is now a simple checkbox instead of the deprecated none/high resolution choice.

When enabled Kdenlive is set to :ref:`track_compositing_hq`

When disabled Kdenlive is set to :ref:`track_compositing_none`

.. deprecated:: 22.08

1a, 1b and 1c cannot be selected anymore.   

   1a. :ref:`track_compositing_none`

   1b. :ref:`track_compositing_preview`

   1c. :ref:`track_compositing_hq`

1d. **Mixed Audio tracks** changes the order in which tracks are displayed to mixed audio and video tracks.  For example, from the bottom of the timeline to the top of the timeline: A1, V1, A2, V2, A3, V3

1e. **Split Audio tracks** changes the order in which tracks are displayed to separate audio and video tracks.  For example, from the bottom of the timeline to the top of the timeline: A1, A2, A1, V1, V2, V3

1f. **Split Audio tracks (reverse)** changes the order in which tracks are displayed to separate audio and video tracks with the audio tracks in reverse order.  For example, from the bottom of the timeline to the top of the timeline: A1, A2, A3, V1, V2, V3

2. **Timeline Edit Mode**  Drop Down. These same settings can be found under the :menuselection:`Tool` menu.

2a. **Timeline Normal Mode**

2b. **Timeline Overwrite Mode**

2c. **Timeline Insert Mode**

3. Use timeline zone |timeline-use-zone-on| / Do not use timeline zone |timeline-use-zone-off| for insert (toggles). See :doc:`/tips_and_tricks/useful_info/insert_overwrite_advanced_timeline_editing` for more details.


**Tool Group** (one of these 3 can be active)

Active buttons are grey.


4. `Selection Tool`_ - Also selected with the 'S' hotkey.  Allows the selection and manipulation of clips on the timeline

5. `Razor Tool`_ - Also selected with the 'X' hotkey, or to cut at the point of the play head use "Shift-R". This allows a clip to be cut into two clips.

6. `Spacer Tool`_ - Also selected with the 'M' hotkey.  This tool will select all clips at one point in the timeline and allow them to be shifted at once.

7. Position indicator - displays the time point or frame number of the location of the hovering mouse on the left side, and the total length of the project on the right side.

7a. **hh:mm:ss:ff;** Sets the position indicator to display time units

7b. **Frames** Sets the position indicator to display frames

8. **Mix Clips** - allows same-track transitions to be applied between two clips. See :ref:`same_track_transition` for a detailed explanation.

9. Insert Clip Zone in Timeline. See :doc:`/tips_and_tricks/useful_info/insert_overwrite_advanced_timeline_editing` for more details.

10. Overwrite Clip Zone in Timeline. See :doc:`/tips_and_tricks/useful_info/insert_overwrite_advanced_timeline_editing` for more details.

11. Extract Timeline Zone

12. Lift Timeline Zone

13. Favourite Effects

14. Start Preview Render

14a. Stop Preview Render

14b. Add Preview Zone

14c. Remove Preview Zone

14d. Remove All Preview Zones

14e. Automatic Preview

14f. Disable Timeline Preview

14g. Manage Cached Data

.. .. versionadded:: 22.04

   .. figure:: /images/preview_using_proxy_clips.png


   14h. Preview Using Proxy Clips. Option to render preview using original clips, not proxies (disabled by default). 


Items 14, 14a-14g are covered in detail by the Tips & Tricks chapter about :doc:`/tips_and_tricks/tips_and_tricks/timeline_preview_rendering`.

1.   Show/Hide the :ref:`audio_mixer` tool.  The audio mixer tool allows audio to be managed in the project.

2.   Show/Hide the :ref:`effects-subtitles` Tool.  This will show or hide the subtitle track where subtitles can be created or edited in the project.


.. _timeline_edit_modes:

Track Compositing
-----------------

.. partly moved from https://kdenlive.org/en/project/timeline-track-compositing/

The track compositing applies uniformly to all tracks in your timeline.

.. tip::

  Under certain compositing conditions, if you see the outcome of a transition not to be what you would expect, try to switch track compositing off for a quick check. If the oddity is gone, then this is an interference between the automatic timeline track compositing and your user transitions.

.. .. versionchanged:: 22.08

Track compositing is now a simple checkbox instead of the none/high resolution choice.


.. _track_compositing_hq:

High Quality
~~~~~~~~~~~~

.. deprecated:: 22.08

When track compositing is set to High-Quality tracks with alpha channel information will be automatically composited with the other tracks using an algorithm that is somewhat slower than the algorithm used with :ref:`track_compositing_preview` but which retains higher fidelity color information.


.. _track_compositing_none:

None
~~~~

.. deprecated:: 22.08

When Track Compositing is set to None you will not get tracks with alpha channel information to composite with the other tracks unless an explicit composite or affine transition is added between the clips. This is basically kind of an expert mode when you need full control over any compositing in your timeline.


.. _track_compositing_preview:

Preview
~~~~~~~

.. deprecated:: 21.08

.. note::

    Final rendering always uses either **High Quality** or **None**. So Preview quality is, well, for preview only.

When track compositing is set to Preview tracks with alpha channel information will be automatically composited with the other tracks using an algorithm that is somewhat faster than the algorithm used with :ref:`track_compositing_hq` but which slightly degrades the colors.


.. _editing_active_tracks:

Active track
------------

.. .. versionchanged:: 24.05

.. figure:: /images/kdenlive2405_editing_active-track.webp
   :align: left
   :width: 350px 
   :figwidth: 350px


   An :term:`active track`

.. rst-class:: clear-both
      
**1** Target track (3-point editing). The highlighted target strip indicates that in the project bin an A/V clip is selected (the selected clip has an audio and video part).

**2** Active track (3-point editing)

**3** Track header

**4** Empty part of the track

Only active tracks can accept clips or react to an edit function. An :term:`active track` is indicated by a:

-	highlighted track number (**2**) (for 3-point editing)

-	blueish or brownish track (**3 4**) (depends on the color scheme), working with the mouse or insert clip by paste

When you work with the mouse Kdenlive make a track active as you drop a clip to the timeline or you select a clip.

Make a track active by:

-	click into the track header (**3**)

-	double click into an empty part of the track (**4**) (the playhead moves to this point too). This is useful when you copy & paste clips.

-	:kbd:`1-9` select a video track 

-	:kbd:`alt+1-9` select an audio track 

-	arrow key up/down

For 3-point editing

-	:kbd:`Alt+Shift+A` Switch all tracks active

-	:kbd:`Shift+A` Toggle all tracks active/inactive

-	:kbd:`A` Toggle track active

-	:kbd:`Shift+T` Toggle track target

:ref:`Here you find more timeline shortcuts <ui-shortcuts_timeline>`.


Timeline Edit Modes
-------------------

.. _timeline_normal_mode:

Normal Mode
~~~~~~~~~~~

In this edit mode, you can not drag clips on top of other clips in the same track in the timeline. You can drag them to another track in the timeline but not into the same track at the same time point as an existing clip. Contrast this to overwrite mode.

.. _timeline_overwrite_mode:

Overwrite Mode
~~~~~~~~~~~~~~

In this edit mode, you can drag a clip onto a track where there is an existing clip and the incoming clip will overwrite that portion of the existing clip (or clips) covered by the incoming clip.


.. figure:: /images/kdenlive_overwrite_mode_before01.png

   
   Before


.. figure:: /images/kdenlive_overwrite_mode_after01.png

   
   After


In the "After" screenshot above, you can see that the clip which was dragged from the upper track has replaced a portion of the clip on the lower track.


**Rearrange clips in the timeline**


Performing a rearrange edit. This technique lets you quickly change the order of clips in the timeline.

.. figure:: /images/Overwrite-mode.gif

 

Drag a clip, as you drop it to a new location performs an overwrite edit that overwrites the existing clip.

.. _timeline_insert_mode:

Insert Mode
~~~~~~~~~~~

With this mode selected and you drop a selection into the timeline the selection will be inserted into the timeline at the point where the mouse is released. The clip that the selection is dropped on is cut and clips are moved to the right to accommodate the incoming clip.


.. figure:: /images/Kdenlive_Insert_mode0before.png

   
   Before


.. figure:: /images/Kdenlive_Insert_mode1before.png

   
   During


.. figure:: /images/Kdenlive_Insert_mode1after.png

   
   After. Incoming Clip inserted. Clips after the insert point are shifted Right


**Rearrange edit in the timeline**

Performing a rearrange edit. Only clips in the destination track are shifted; clips in other tracks are not affected. This technique lets you quickly change the order of clips in the timeline. 

It always closes all space in the track.

.. figure:: /images/Insert-mode.gif

   
Drag a clip, as you drop it to a new location. Releasing the clip performs an insert edit that shifts clips in the destination track only.


.. _timeline_edit_tools:

Timeline Edit Tools
-------------------

Selection Tool
~~~~~~~~~~~~~~

Use this to select clips in the timeline. The cursor becomes a hand when this tool is active. 


Razor Tool
~~~~~~~~~~
 
Use this to cut clips in the timeline. The cursor becomes a pair of scissors when this tool is active.

:kbd:`ESC`: Return from any tools back to Selection tool.

Spacer Tool
~~~~~~~~~~~

Use this tool (|distribute-horizontal|) to temporarily group separate clips and then drag them around the timeline to create or remove space between clips. Very useful. Experiment with this tool to see how it works.


.. figure:: /images/Kdenlive_Spacer_tool_crop.png
   :width: 300px

   


In the above example, these clips are not grouped. However, the spacer tool groups them temporarily for you so you can move them all as a group.

:kbd:`ESC`: Return from any tools back to Selection tool.


.. _slip_tool:

Slip Tool
~~~~~~~~~

.. .. versionadded:: 21.12

.. figure:: /images/slip_trim02.jpg


Slip keeps the original duration of the clip. Like working with old film material: beneath the given "window" of the clip length it slips the film strip back and forth.

.. figure:: /images/slip.gif


Use Slip (|kdenlive-slip|) to trim, in a single operation, the IN and OUT points of a clip forward or backward by the same number of frames, while keeping the original duration and without affecting adjacent clips.

You can slip multiple clips at once now: select all clips you want to slip with the selection tool using :kbd:`Shift` then enable the slip tool and go ahead…

Slip can be done with the mouse, with the :kbd:`arrow` keys and with the buttons on the monitor toolbar.

:kbd:`ESC`: Return from any tools back to Selection tool. 


.. _ripple_tool:

Ripple Tool
~~~~~~~~~~~

.. figure:: /images/ripple-trim.png


Ripple changes the original duration of the clip. Like working with old film material: You lengthen or shorten the film strip and move the adjacent clips back and forth as you do that.

Use Ripple (|kdenlive-ripple|) to trim a clip and shift following clips in the track by the number of frames you trim. When you shorten a clip by this action all clips that follow the cut shift back in time, contrariwise, when you extend a clip the clips after the cut shift forward in time. If an empty space is on the track it behaves as a clip and it shifts in time as a standard clip would be.

You can Ripple only a single clip at once.

Ripple can be done with the mouse only.

:kbd:`ESC`: Return from any tools back to Selection tool.


.. _ripple_trim_to_playhead:

Ripple Trim to Playhead
~~~~~~~~~~~~~~~~~~~~~~~

To cut a clip on an active track at the playhead position without getting a gap in the timeline do the following.

- enable ripple

- place the playhead at the desired place

- hit :kbd:`(`: This cuts and removes the clip and space to the left side of the playhead. :kbd:`)` does the same but to the right side of the playhead.


.. _multicam_tool:

Multicam Tool
~~~~~~~~~~~~~

.. figure:: /images/multicam.gif

   
The multicam tool allows to cut between several cameras while playback is running. Add your clips in different tracks, but at the same position in the timeline and activate the multicam tool by going to menu :menuselection:`Tool -> Multicam tool`. You may trim the clips in the desired track while the timeline is playing by pressing their corresponding numbers (for track V1, press key :kbd:`1`; for track V2 press key :kbd:`2`, etc…) or simply select the desired track in the project monitor by clicking on it with the mouse.

Select multicam tool will switch on the :ref:`ui-multitrack_view` in the project monitor and set a marker at the current timeline position. You can then seek/play to the wanted position, click on a track view in the project monitor and it will lift all tracks except for the previously active track. You can then repeat seek and click in another track to continue lifting tracks.

It doesn't stop playing when you perform the operation to avoid to lose the rhythm and to work as you are working during a live broadcasting. If you need to correct the editing you can manually stop and trim the cut as you do when you video editing as normal.

The audio tracks is not involved in the process as you generally use only one audio track (the one which come from the main mixer to which the other ones are synced to)

:kbd:`ESC`: Return from any tools back to Selection tool.


.. _status_bar:

Status Bar
----------

.. .. versionadded:: 25.12 Audio track: add Zoom Audio Waveforms. Add button to hide clip overlays (clip name, effect names, ...) 

.. figure:: /images/cutting-assembling_statusbar_2512.webp
   :width: 500px
   :figwidth: 500px


:1: Hints what you can do when you hover over items.

:2: Names of the clip you hover over in the timeline

:3: Mode you are in (default is :guilabel:`Select` = :guilabel:`Normal Mode`)

:4: Switch for :guilabel:`Color Tags`

:5: Switch for :guilabel:`Video Thumbnails`

:6: Switch for :guilabel:`Audio Thumbnails`. Toggles zooming audio waveforms from 1 (default) 2, 4, 8. It affects all displayed waveforms and all audio tracks. See `Show Audio Thumbnails`_

:7: Switch for :guilabel:`markers`. See `Show marker comments`_

:8: Switch for :guilabel:`Clip Names`, effect names and info in the timeline
   
:9: Switch for :guilabel:`Snap`. See `Snap`_

:10: :guilabel:`Fit Zoom to Project`. See `Fit Zoom to Project`_

:11: Zoom Out

:12: Zoom slider `Zoom Project`_

:13: Zoom In


Split Audio and Video Automatically
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When this is on and you drag a clip to the timeline, the audio in the clip will end up on an audio track and the video on a video track. You can achieve the same result if you select the clip, :ref:`right_click_menu`, :menuselection:`Split Audio`.  When this is off and you drag a clip onto the timeline, both the audio and video tracks are combined into one video track.


.. ==================================================================================================
   Is this not deprecated?

   Automatic Transitions
   ~~~~~~~~~~~~~~~~~~~~~

   When active, any transitions added to the timeline will have the automatic transition option checked by default.
   See :ref:`transitions_compositions`


Show Video Thumbnails
~~~~~~~~~~~~~~~~~~~~~

When on, the video clips in the timeline will contain thumbnails as well as a filename. Otherwise, they just have the clip filename.

When the timeline is zoomed in to the maximum, the video track will show a thumbnail for every frame in the clip. When the timeline is not on maximum zoom, the video track will show a thumbnail for the first and last frame in the clip.


Show Audio Thumbnails
~~~~~~~~~~~~~~~~~~~~~

When on, the audio clip will have a wave representation of the audio data as well as a filename.  Otherwise, they just have the clip filename.


Show marker comments
~~~~~~~~~~~~~~~~~~~~

This toggles on and off the display of :ref:`markers` saved within :doc:`clips</project_and_asset_management/project_bin/clips>` (the text with the gold background in the example below) and within :doc:`guides` (the text with the purple background).

.. figure:: /images/Kdenlive_Markers_and_guides_crop.png



Snap
~~~~

When this feature is on, dragging the beginning of one clip near to the end of another will result at the end of the first clip snapping into place to be perfectly aligned with the beginning of the second clip. As you move the two ends near to each other, as soon as they get within a certain small distance, they snap together so there is no space and no overlap. Note that this occurs even if the clips are on different tracks in the timeline.


Clips will also snap to the cursor position, markers and :doc:`guides`.


Fit Zoom to Project
~~~~~~~~~~~~~~~~~~~

This will zoom the project out so that it all fits in the timeline window. This is the same function that is triggered by :ref:`sequence_menu` Menu item, :menuselection:`Fit Zoom to Project`.


Zoom project
~~~~~~~~~~~~

The magnifying glasses zoom in or out on the timeline. The slider adjusts the zoom by large increments. These same settings are controlled by the :menuselection:`Timeline` menu items, :menuselection:`Zoom In` and :menuselection:`Zoom Out`.


Cutting Footage from multiple aligned tracks - Ripple Delete
------------------------------------------------------------

.. This is available on the :menuselection:`Timeline` menu under :menuselection:`All clips --> Ripple Delete`  [1]_ .

.. **Seems missing in Kdenlive 17.04 & 18.04**

There are 4 possibilities for ripple delete (point 1 and 2 are the classical `Ripple Delete`):

1. On the active track: Cut out the piece on the clip which you do not want with :kbd:`Shift+R`. Right click on that piece and choose :menuselection:`Extract Clip` or press :kbd:`Shift+Del`. This removes the clip and slides everything else to the left to fill the gap. The playhead stays where you made the last cut.

2. On the active track: Empty spaces between clips can only be removed by right click on empty space and choose :menuselection:`Remove Space`. 

3. On all tracks together: Mark `In` and `Out` points in the Project Monitor or on the Timeline, then choose :menuselection:`Timeline --> Removal --> Extract Timeline Zone` (or :kbd:`Shift+X`). Kdenlive deletes all footage between the `In` and `Out` points in unlocked tracks, slides everything else back to fill the gap, and puts the playhead on the In point.

4. On the active track with `Insert Mode`: Cut out the piece on the clip which you don't want with :kbd:`Shift+R`. Hit `Delete`. This removes the clip and slides everything else to the left to fill the gap. The playhead stays where you made the last cut.

You can do a ripple trim to the playhead using :ref:`ripple_trim_to_playhead`.


.. _three_point_editing:

3 point editing
---------------

.. .. versionadded:: 19.08.0

3 important points to understand the 3 point editing concept (with keyboard shortcuts): 


Source
~~~~~~

.. figure:: /images/3p-Source-1.gif
   :align: right
   :width: 200px

On the left of the track head the green vertical lines (V1 or A2). The green line is connected to the source clip in the project bin. Only when a clip is selected in the project bin, the green line shows up depending on the type of the clip (A/V clip, picture/title/color clip, audio clip).

.. rst-class:: clear-both

Target
~~~~~~

.. figure:: /images/3p-Target-active-1.gif
   :align: right
   :width: 200px

In the track head the target V1 or A1 is active when it’s yellow. An active target track reacts to edit operations like insert a clip even if the source is not active.


**The concept is like thinking of connectors**

Connect the source (the clip in the project bin) to a target (a track in the timeline). Only when both connectors on the **same** track are switched on the clip “flow” from the project bin to the timeline.


.. important::

    Active target tracks without connected source react on edit operations.

Examples of advanced edit
~~~~~~~~~~~~~~~~~~~~~~~~~

Here is a brief introduction to the 3 point editing system.

.. figure:: /images/3p-Insert-clip-1.gif
   :align: right
   :width: 200px
  
1. Select a clip in the project bin with an up/down arrow

2. Navigate the clip by the :kbd:`JKL` keys or by the :kbd:`left/right` arrows and set the IN and the OUT point by the :kbd:`I` and :kbd:`O` keys.

3. Hit :kbd:`T` to change to the timeline

4. Select a video or audio track in the timeline (up/down arrow key) and set it as source with :kbd:`Shift + T`.

5. Activate the track as a target with shortcut :kbd:`A` (this connects the track to the source)

6. Hit :kbd:`V` (insert) or :kbd:`B` (overwrite) to add the clip at the play-head position or to fill the selected area in the timeline if it is active. If you need to activate it use the :kbd:`G` key.

.. container:: clear-both

   .. figure:: /images/3p-Advanced-edit-1.gif
      :align: right
      :width: 200px

   In the following example, we want only to insert the audio part of a clip in A2 and we want to create a gap in all the other video and audio tracks:

   1. Activate all the target tracks which contain clips (yellow buttons).

   2. Activate just the audio source on A2

   3. Press :kbd:`V` (insert).

.. rst-class:: clear-both

For more information about 3 point editing check :ref:`Advanced Timeline Editing <advanced_timeline_editing>` 

..   .. [1] available on bleeding edge version > 0.9.10 (Jan2015)
