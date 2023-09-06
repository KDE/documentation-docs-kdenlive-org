.. meta::
   :description: Kdenlive's User Interface - Clip Monitor
   :keywords: KDE, Kdenlive, clip, project, monitor, clip monitor, overlay, resizing, zoombar, preview, toolbar, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Julius Künzel <jk.kdedev@smartlab.uber.space
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. #########################################################################################################################################
   Not needed but keeping it here just in case

   .. |save_clip_zone| image:: /images/Kdenlive_Save_clip_zone.png
                       :alt: Kdenlive_Save_clip_zone

   .. |extract_clip_zone| image:: /images/Kdenlive_Extract_zone.png
                         :alt: Kdenlive_Extract_zone

   #########################################################################################################################################


.. _ui-monitors_clip_monitor:

Clip Monitor
------------

.. figure:: /images/user_interface/kdenlive2304_ui-monitors_cm_elements.webp
   :width: 350px
   :figwidth: 350px
   :align: left
   :alt: kdenlive2304_ui-monitors_cm_elements

   Clip Monitor elements

The Clip Monitor displays the unedited\ [#f1]_ clip that is currently selected in the :ref:`Project Bin <project_tree>`. It has the same functions and options as the :ref:`ui-monitors_project_monitor` except for the |kdenlive-add-clip| icon which adds the clip zone to the Project Bin where it will appear as child clip underneath the clip. See :ref:`ui-monitors_cm_clip_zone` for more details.

For more details about the icons in the monitor toolbar refer to :ref:`this section <ui_elements-monitor_icons>` of the manual.

.. rst-class:: clear-both


.. _ui-monitors_clip_monitor_hamburger:

Hamburger Menu
~~~~~~~~~~~~~~

.. figure:: /images/user_interface/kdenlive2304_ui-monitor_cm_options.webp
   :width: 350px
   :figwidth: 350px
   :align: left
   :alt: kdenlive2304_ui-monitor_cm_options

   Clip Monitor options

* **Volume** - Set the Clip Monitor playback volume. This does not affect the master volume setting.

* **Go to Marker** - If :term:`markers` are defined for the clip the list of markers is displayed and selecting one positions the :term:`playhead` at the marker's timecode.

* **Force Monitor Size** - You can force the Clip Monitor to display the video at 100% (original size), 50% or adjust it to the Clip Monitor widget's size (Free Resize).

* **Background Color** - Set the background color for the Clip Monitor

* **Extract Zone** - Saves the current :term:`zone` as a :file:`.mlt` file and adds it to the :term:`project bin` if :guilabel:`Add clip to project` is selected. See also *Extract Zone* in the :ref:`ui-monitors_cm_rightclick` section below.

* **Set Current Image as Thumbnail** - Takes the a snapshot of the current frame and uses that as the thumbnail for the clip.

* **Always show audio thumbnails** -

* **Audio Scrubbing** - If enabled plays the audio track while scrubbing through the timeline. You may want to turn this off to improve scrubbing performance or if the noise is distracting.

* **Show Audio Levels** - If enabled shows the frequency curve of the master audio in the Project Monitor.

* **Show Source Timecode** -

.. rst-class:: clear-both


.. _ui-monitors_cm_clip_zone:

Creating Zones
~~~~~~~~~~~~~~

Zones are defined regions of clips that are indicated by a colored section in the clip monitor's timeline - see item 3 above. The beginning of a zone is set by clicking |zone-in| or pressing :kbd:`I`. The end of a zone is set by clicking |zone-out| or pressing :kbd:`O`.


.. _ui-monitors_cm_rightclick:

Right-Click Menu
~~~~~~~~~~~~~~~~


.. figure:: /images/user_interface/kdenlive2304_ui-monitor_cm_right-click.webp
   :width: 350px
   :figwidth: 350px
   :align: left
   :alt: kdenlive2304_ui-monitor_cm_right-click

   Clip Monitor right-click menu options

These are the menu items that are available when you right-click in the Clip Monitor. These actions affect the clip that is currently selected in the :ref:`project_tree`. Similar menu items are available from a right-click menu in the :ref:`ui-monitors_project_monitor`. However, the project monitor menu items affect the currently selected clip on the :ref:`timeline`.

.. rst-class:: clear-both


.. list-table::
   :width: 100%
   :widths: 20 25 60
   :class: table-wrap
   :header-rows: 1

   * - Item
     - Shortcut
     - Description
   * - Play
     -
     - Plays the :term:`clip` currently selected in the :term:`project bin`
   * - Play Zone
     - :kbd:`Ctrl+Space`
     - Plays the current :term:`zone` and stops
   * - Loop Zone
     - :kbd:`Ctrl+Shift+Space`
     - Plays the current :term:`zone` in a continuous loop
   * - Go to Project Start
     - :kbd:`Ctrl+Home`
     - Goes to the beginning of the clip
   * - Go to Previous Guide
     - :kbd:`Ctrl+Left`
     - Goes to the previous :term:`marker<markers>` or :term:`guide`
   * - Go to Previous Snap Point
     - :kbd:`Alt+Left`
     - Moves the :term:`playhead` to the previous :term:`snap point`
   * - Go to Zone Start
     - :kbd:`Shift+I`
     - Goes to the start of the :term:`zone`
   * - Go to Clip Start
     - :kbd:`Home`
     - Moves the clip playhead to the beginning of the clip
   * - Go to Clip End
     - :kbd:`End`
     - Moves the clip playhead to the end of the clip
   * - Go to Zone End
     - :kbd:`Shift+O`
     - Goes to the end of the :term:`zone`
   * - Go to Next Snap Point
     - :kbd:`Alt+Right`
     - Moves the :term:`playhead` to the next :term:`snap point`
   * - Go to Next Guide
     - :kbd:`Ctrl+Right`
     - Goes to the next :term:`marker<markers>` or :term:`guide`
   * - Go to Project End
     - :kbd:`Ctrl+End`
     - Goes the end of the clip
   * - Add Marker
     -
     - Opens the Edit Marker dialog window for adding a new :term:`marker<markers>` into the clip at the current time point.

.. figure:: /images/user_interface/kdenlive2308_ui-monitors_edit_marker.webp
   :width: 350px
   :figwidth: 350px
   :align: left
   :alt: kdenlive2308_ui-monitors_edit_marker

   Edit Marker dialog window to add or edit a marker

.. list-table::
   :width: 100%
   :widths: 20 25 60
   :class: table-wrap

   * - Add Marker/Guide quickly
     - :kbd:`Num+*`
     - Adds a new marker at the current time point
   * - Edit Marker
     -
     - Brings up a dialog where you can edit the :term:`marker<markers>` that is at the current time point. Use *Go to marker* to put the monitor at the marker you want to edit.
   * - Delete Marker
     -
     - Deletes the :term:`marker<markers>` that is at the current time point. Use *Go to marker* to put the monitor at the marker you want to delete.
   * - Delete All Markers
     -
     - Deletes all the :term:`markers` from the current clip.
   * - Go to Marker...
     -
     - The menu item pops out a list of existing :term:`marker<markers>` to select from. When one is selected the playhead moves to that marker.
   * - Extract Zone
     -
     - This brings up the **Cut Clip** dialog.

.. figure:: /images/user_interface/kdenlive2308_ui-monitors_cut_clip.webp
   :width: 350px
   :figwidth: 350px
   :align: left
   :alt: kdenlive2308_ui-monitors_cut_clip

   Cut Clip dialog to extract zone

The current :term:`zone` can be saved as a :file:`.mov` file in your file system. If the :guilabel:`Add clip to project` is checked the zone will be added as a separate clip to the project bin.

.. list-table::
   :width: 100%
   :widths: 20 25 60
   :class: table-wrap

   * - Insert Zone in Project bin
     - :kbd:`Ctrl+I`
     - Inserts the current :term:`zone` into the project bin as a sub-clip of the original clip
   * - Extract Frame
     -
     - Opens the **Save Image** dialog window to save the current frame as an image file (default is :file:`.png`) to your file system
   * - Extract Frame to Project
     -
     - Same as :guilabel:`Extract Frame` but in addition the image file is brought into the project bin

.. figure:: /images/user_interface/kdenlive2308_ui-monitors_save_image.webp
   :width: 350px
   :figwidth: 350px
   :align: left
   :alt: kdenlive2308_ui-monitors_save_image

   Save Image dialog for extracting frames

.. #########################################################################################################################################
   Not sure what to do with this section of the documentation: Suggest to delete it as it refers to a very old version

   On the authors 0.9.2  and 0.9.5 version of **Kdenlive** this feature is broken for .dv format clips at least.  It does work for .mp4 type clips. However, the accuracy of the cuts on the clip is way out.

   .. code-block:: text

   ffmpeg version 0.8.3-4:0.8.3-0ubuntu0.12.04.1, Copyright (c) 2000-2012 the Libav developers
    built on Jun 12 2012 16:37:58 with gcc 4.6.3
   [dv @ 0x9d71480] Can't initialize DV format!
   Make sure that you supply exactly two streams:
       video: 25fps or 29.97fps, audio: 2ch/48kHz/PCM
       (50Mbps allows an optional second audio stream)
   Output #0, dv, to '/home/ttguy/Videos/Tape3_006_0.dv':
    Metadata:
      encoder         : Lavf53.21.0
      Stream #0.0: Video: dvvideo, yuv420p, 720x576 [PAR 64:45 DAR 16:9], q=2-31, 28800 kb/s, 90k tbn, 25 tbc
      Stream #0.1: Audio: pcm_s16le, 32000 Hz, 2 channels, 1024 kb/s
   Stream mapping:
    Stream #0.0 -> #0.0
    Stream #0.1 -> #0.1
   Could not write header for output file #0 (incorrect codec parameters ?)

   #########################################################################################################################################


.. list-table::
   :width: 100%
   :widths: 20 25 60
   :class: table-wrap

   * - Add Project Note
     -
     - Opens the :ref:`notes` widget and adds a hyperlink to the current frame in the clip. You can enter more text to describe the scene.
   * - Set Zone In
     - :kbd:`I`
     - Sets the :term:`in-point` for the :term:`zone`
   * - Set Zone Out
     - :kbd:`O`
     - Sets the :term:`out-point` for the :term:`zone`
   * - Set current image as thumbnail
     -
     - Uses the current frame as the thumbnail for the clip in the project bin
   * - Always show audio thumbnails
     -
     - Switches the permanent display of the audio waveform on or off. If unchecked (i.e. off) the audio graph is only displayed when the mouse is near the bottom of the monitor area and the Monitor Overlay Audio Waveform option is selected.
   * - Current Monitor Overlay
     -
     - Opens a fly-out for the various available monitor overlays
   * - Monitor Info Overlay
     -
     - Switches all monitor overlays on or off
   * - Monitor Overlay Timecode
     -
     - Switches the display of the timecode on or off
   * - Monitor Overlay Playback FPS
     -
     - Switches the display of the frame-per-seconds (:term:`fps`) on or off
   * - Monitor Overlay Markers
     -
     - Switches the display of the marker lines and thumbnails on or off
   * - Monitor Overlay Audio Waveform
     -
     - Switches the display of the audio waveform on or off
   * - Monitor Overlay Clip Jobs
     -
     - Switches the display of running clip jobs on or off


.. ##########################################################################################################################################
   Not sure what to do with this section of the original documentation: This is not part of the right-click menu anymore but is not yet explained in the Monitor Menu

   Real time (drop frames)
   '''''''''''''''''''''''

   Setting this to the Checked state means the clip monitor will drop frames during playback to ensure the clip plays in real time. This does not effect the final rendered file - it just effect how the clip appears when being previewed in the clip monitor

   ##########################################################################################################################################


.. _ui-monitors_cm_seeking:

Seeking
~~~~~~~

.. versionadded:: 20.08.0 Inside the clip monitor: hold down :kbd:`Shift` and move the mouse left/right.


.. _ui-monitors_cm_drag_av_into_timeline:

Drag Audio or Video Only to Timeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. versionadded:: 19.04.0 Possibility to drag only the video or audio stream of a clip from the project bin or clip monitor to the timeline

.. figure:: /images/user_interface/kdenlive2304_ui-monitors_cm_av_only.webp
   :width: 250px
   :figwidth: 250px
   :align: left
   :alt: kdenlive2304_ui-monitors_cm_av_only

..

Move with the mouse to the lower left-hand corner of the clip monitor to access the video and audio icons. Left click on the respective icon to drag either the video or audio stream into the timeline.

.. rst-class:: clear-both

This is very useful if you only need one of the streams as it avoids the un-grouping and subsequent deletion of one of the streams of the clip in the timeline.



**Notes**

.. [#f1] "Unedited" means without any cuts. Please note that clips in the Project Bin can have effects and hence people may consider them "edited".
