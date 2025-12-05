.. meta::
   :description: Kdenlive Documentation - Clip Monitor
   :keywords: KDE, Kdenlive, clip, project, monitor, clip monitor, overlay, resizing, zoombar, preview, toolbar, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Julius Künzel <jk.kdedev@smartlab.uber.space
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0



.. _ui-monitors_clip_monitor:

Clip Monitor
------------

.. figure:: /images/user_interface/kdenlive2402_ui-monitors_cm_elements.webp
   :width: 350px
   :figwidth: 350px
   :align: left
   :alt: kdenlive2402_ui-monitors_cm_elements

   Clip Monitor elements

The Clip Monitor displays the unedited\ [#f1]_ clip that is currently selected in the :doc:`Project Bin </project_and_asset_management/project_bin>`. It has the same functions and options as the :ref:`ui-monitors_project_monitor` except for the |kdenlive-add-clip| icon which adds the clip zone to the Project Bin where it will appear as child clip underneath the clip. See :ref:`ui-monitors_cm_clip_zone` for more details.

|  **1** Video Stream indicator
|  **2** Audio Stream indicator
|  **3** Clip Zone indicator
|  **4** List of last opened clips 

.. .. .. versionadded:: 24.02
  Item 4 added

.. rst-class:: clear-both

Number **4**: Hover with the mouse to the top and a list of last opened clips appears. You can select a clip which then show up in the clip monitor.

For more details about the icons in the monitor toolbar refer to :ref:`this section <ui_elements-monitor_icons>` of the manual.


.. _ui-monitors_clip_monitor_hamburger:

Hamburger Menu
~~~~~~~~~~~~~~

.. figure:: /images/user_interface/kdenlive2508_ui-monitor_cm_options.webp
   :width: 350px
   :figwidth: 350px
   :align: left
   :alt:

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

.. .. versionchanged:: 24.05

.. figure:: /images/user_interface/kdenlive2405_ui-monitor_cm_right-click.webp
   :width: 350px
   :figwidth: 350px
   :align: left
   :alt: kdenlive2304_ui-monitor_cm_right-click

   Clip Monitor right-click menu options

These are the menu items that are available when you right-click in the Clip Monitor. These actions affect the clip that is currently selected in the :doc:`project bin</project_and_asset_management/project_bin>`. Similar menu items are available from a right-click menu in the :ref:`ui-monitors_project_monitor`. However, the project monitor menu items affect the currently selected clip on the :ref:`timeline`.

.. rst-class:: clear-bothMouse whee

|

.. list-table::
   :width: 100%
   :widths: 20 25 60
   :class: table-wrap
   :header-rows: 1

   * - Item
     - Shortcut
     - Description
   * - Play
     - :kbd:`Space` or click into the monitor
     - Plays the :term:`clip` currently selected in the :term:`project bin`. (:doc:`Disable play on click in the settings</getting_started/configure_kdenlive/configuration_playback>`)
   * - Play Zone
     - :kbd:`Ctrl+Space`
     - Plays the current :term:`zone` and stops
   * - Play Zone From Cursor
     - 
     - Plays the current :term:`zone` from cursor to the end of the :term:`zone`
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
   :alt: kdenlive2308_ui-monitors_edit_marker

   Edit Marker dialog window to add or edit a marker

.. list-table::
   :width: 100%
   :widths: 20 25 60
   :class: table-wrap

   * - Add Marker quickly
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
   :alt: kdenlive2308_ui-monitors_save_image

   Save Image dialog for extracting frames


.. list-table::
   :width: 100%
   :widths: 20 25 60
   :class: table-wrap

   * - Add Project Note
     -
     - Opens the :doc:`Project Notes</project_and_asset_management/project_notes>` widget and adds a hyperlink to the current frame in the clip. You can enter more text to describe the scene.
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



.. _ui-monitors_cm_seeking:

Seeking
~~~~~~~

.. .. versionadded:: 20.08.0

Inside the clip monitor: hold down :kbd:`Shift` and move the mouse left/right.


.. _ui-monitors_cm_drag_av_into_timeline:

Drag Audio or Video Only to Timeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. .. versionadded:: 19.04.0

It is possible to drag only the video or audio stream of a clip from the project bin or clip monitor to the timeline

.. figure:: /images/user_interface/kdenlive2304_ui-monitors_cm_av_only.webp
   :width: 250px
   :figwidth: 250px
   :align: left
   :alt: kdenlive2304_ui-monitors_cm_av_only

..

Move with the mouse to the lower left-hand corner of the clip monitor to access the video (1) and audio (2) icons. Left click on the respective icon to drag either the video or audio stream into the timeline.

.. rst-class:: clear-both

This is very useful if you only need one of the streams as it avoids the un-grouping and subsequent deletion of one of the streams of the clip in the timeline.


----

.. [#f1] "Unedited" means without any cuts. Please note that clips in the Project Bin can have effects and hence people may consider them "edited".
