.. meta::
   :description: Kdenlive's User Interface - Project Monitor
   :keywords: KDE, Kdenlive, clip, project, monitor, project monitor, overlay, resizing, zoombar, preview, toolbar, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Julius Künzel <jk.kdedev@smartlab.uber.space
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _ui-monitors_project_monitor:

Project Monitor
---------------

.. figure:: /images/user_interface/kdenlive_ui-monitors_pm_elements.webp
   :width: 350px
   :figwidth: 350px
   :align: left
   :alt: kdenlive_ui-monitors_pm_elements

   Project Monitor elements

The Project Monitor displays your project's :term:`timeline` - i.e. the edited version of your video. It has the same functions and options as the :ref:`ui-monitors_clip_monitor` except for the |edit-mode| icon which switches :term:`Edit Mode` on or off.

For more details about the icons in the monitor toolbar refer to :ref:`this section <ui_elements-monitor_icons>` of the manual.

.. rst-class:: clear-both


Project Monitor Controls
~~~~~~~~~~~~~~~~~~~~~~~~

1) The position caret. Shows the current location in the project relative to the whole project. You can click and drag this to move the position in the project.

2) The timecode control. You can type a timecode here and press :kbd:`Enter` to bring the playhead to an exact location.

3) Timecode control arrows. You can move the Project Monitor one frame at a time with these. Alternatively, you can use :kbd:`left` and :kbd:`right` (keyboard arrow keys).


.. _project_monitor_hamburger:

Hamburger Menu
~~~~~~~~~~~~~~

.. figure:: /images/user_interface/kdenlive2304_ui-monitors_pm_options.webp
   :width: 350px
   :figwidth: 350px
   :align: left
   :alt: kdenlive2304_ui-monitor_pm_options

   Project Monitor options

* **Volume** - Set the Project Monitor playback volume. This does not affect the master volume setting.

* **Go to Guide** - If :term:`guides<guide>` are defined the list of guides is displayed and selecting one positions the :term:`playhead` at the guide's timecode.

* **Force Monitor Size** - You can force the Project Monitor to display the video at 100% (original size), 50% or adjust it to the Project Monitor widget's size.

* **Set current image as thumbnail** - Takes the a snapshot of the current frame and uses that as the thumbnail for the clip.

* **Audio Scrubbing** - If enabled plays the audio track while scrubbing through the timeline. You may want to turn this off to improve scrubbing performance or if the noise is distracting.

* **Show Audio Levels** - If enabled shows the frequency curve of the master audio in the Project Monitor.

.. rst-class:: clear-both


.. _ui-monitors_pm_zones:

Creating Zones
~~~~~~~~~~~~~~

.. figure:: /images/user_interface/kdenlive_ui-monitors_pm_zone.webp
   :width: 350px
   :figwidth: 350px
   :align: left
   :alt: kdenlive_ui-monitors_pm_zone

   Project Monitor zone

You can use the :kbd:`I` and :kbd:`O` keys or the |zone-in| and |zone-out| icons to create a zone in the Project Monitor the same way you make zones in the Clip Monitor with the notable exception that the zone defined in the Project Monitor also sets the zone in the :term:`Timeline`. The zone will be indicated by a colored bar both on the :term:`timeline` and underneath the Project Monitor.

.. rst-class:: clear-both

You can have Kdenlive only render the selected zone - see :ref:`rendering-selected_zone`.


.. _ui-monitors_pm_right_click:

Right-click Menu
~~~~~~~~~~~~~~~~

.. figure:: /images/user_interface/kdenlive2304_ui-monitor_pm_right-click.webp
   :width: 350px
   :figwidth: 350px
   :align: left
   :alt: kdenlive2304_ui-monitor_pm_right-click

   Project Monitor right-click menu options

These are the menu items that are available when you right-click in the Project Monitor. These actions affect the clip that is currently selected in the :ref:`timeline`. Similar menu items are available from a right-click menu in the :ref:`ui-monitors_clip_monitor`. However, the clip monitor menu items affect the currently selected clip in the :ref:`project bin <project_tree>`.

.. rst-class:: clear-both

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
     -
     - Plays the :term:`clip` currently selected in the :term:`project bin`
   * - Play Zone
     - :kbd:`Ctrl+Space`
     - Plays the current :term:`zone` and stops
   * - Loop Zone
     - :kbd:`Ctrl+Shift+Space`
     - Plays the current :term:`zone` in a continuous loop
   * - Loop Selected Clip
     -
     - Plays the currently selected :term:`clip` in a continuous loop
   * - Go to Project Start
     - :kbd:`Ctrl+Home`
     - Goes to the beginning of the clip
   * - Go to Previous Guide
     - :kbd:`Ctrl+Left`
     - Goes to the previous :term:`guide`
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
     - Goes to the next :term:`guide`
   * - Go to Project End
     - :kbd:`Ctrl+End`
     - Goes the end of the clip
   * - Go to Guide...
     -
     - The menu item pops out a list of existing :term:`guides<guide>` to select from. When one is selected the playhead moves to that guide.
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
     - Opens the :ref:`Project Notes <notes>` widget and adds a hyperlink to the current frame in the clip. You can enter more text to describe the scene.
   * - Set Zone In
     - :kbd:`I`
     - Sets the :term:`in-point` for the :term:`zone`
   * - Set Zone Out
     - :kbd:`O`
     - Sets the :term:`out-point` for the :term:`zone`
   * - Set current image as thumbnail
     -
     - Uses the current frame as the thumbnail for the clip in the project bin
   * - Multitrack View
     - :kbd:`F12`
     - Switches the project monitor area to the :ref:`ui-monitors_pm_multitrack_view`. All active tracks will be displayed. For more details about how to use this in Editing refer to the :ref:`multicam_tool` chapter.
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


.. _ui-monitors_pm_multitrack_view:

Multitrack View
~~~~~~~~~~~~~~~

.. figure:: /images/user_interface/kdenlive_ui-monitors_pm_multitrack.webp
   :width: 350px
   :figwidth: 350px
   :align: left
   :alt: kdenlive_ui-monitors_pm_multitrack

Selecting this allows you to view all the video tracks at once in a split screen in the project monitor. Kdenlive starts with video track #1 in the top left corner and displays the other tracks sequentially. Hidden tracks are not displayed.

For more details about how to use this in Editing refer to the :ref:`multicam_tool` chapter.


.. ##########################################################################################################################################
   Not sure what to do with this section of the original documentation: This is not part of the right-click menu anymore but is not yet explained in the Monitor Menu

   Real Time (Drop Frames)
   ~~~~~~~~~~~~~~~~~~~~~~~

   This right-click menu item has been moved to the main menu :menuselection:`Monitor --> Monitor Config --> Real Time (drop frames)`

   Setting this to the Checked state means the clip monitor will drop frames during playback to ensure the clip plays in real time. This does not affect the final rendered file - it just affects how the clip appears when being previewed in the clip monitor.

   ##########################################################################################################################################
