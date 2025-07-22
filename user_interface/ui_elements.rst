.. meta::
   :description: Kdenlive Documentation - UI Elements, Icons and Buttons
   :keywords: KDE, Kdenlive, user interface, documentation, user manual, video editor, open source, free, learn, easy, user interface, ui elements, controls, icons, buttons

.. metadata-placeholders

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _ui_elements:

===========
UI Elements
===========

Controls
--------
.. figure:: /images/user_interface/kdenlive2304_ui-controls.webp
   :width: 700px
   :figwidth: 700px

   Kdenlive UI controls (example using the effect panel)

.. list-table::
   :width: 100%
   :widths: 30 70
   :header-rows: 1
   :class: table-wrap

   * - UI Element
     - Description
   * - 1 :guilabel:`collapse/expand`
     - Collapses or expands a section of the user interface
   * - 2 :guilabel:`check box`
     - Used to select an optional element or feature
   * - 3 :guilabel:`drop-down list box`
     - Allows to select from a list of possible values
   * - 4 :guilabel:`toolbar icons`
     - Various action icons specific to the panel. See :ref:`below <ui_elements-toolbar_icons>` for the icons.
   * - 5 :guilabel:`hamburger menu`
     - Opens a fly-out menu with more options
   * - 6 :guilabel:`spinner`
     - Used to increase or decrease a value one step at a time
   * - 7 :guilabel:`direct entry`
     - Used to enter a specific value. In most cases it is possible to use the :kbd:`Mouse wheel` to increase or decrease the value. Hold :kbd:`Shift` to increase by one (1), :kbd:`Ctrl` to increase by 10.
   * - 8 :guilabel:`button`
     - Used to enable a certain state while it is pushed in. Click again to make it come out.
   * - 9 :guilabel:`slider`
     - Allows for rapid changes of values. Drag the mouse left or right to move the slider. The value in an adjacent :guilabel:`direct entry` field is changed accordingly. Hold :kbd:`Shift` to increase by one (1), :kbd:`Ctrl` to increase by 10.
   * - 10 :guilabel:`action button`
     - Used to change a value in defined steps. Every click changes the value, wrapping at the end of the scale may occur.
   * - 11 :guilabel:`action icon`
     - Used to execute an action that is not repeatable (with exceptions)


.. _ui_elements-monitor_controls:

.. figure:: /images/user_interface/kdenlive2304_ui-monitor_controls.webp
   :width: 700px
   :figwidth: 700px

   Kdenlive UI controls (example using the monitor panel)

.. list-table::
   :width: 100%
   :widths: 30 70
   :header-rows: 1
   :class: table-wrap

   * - UI Element
     - Description
   * - 1 :guilabel:`edit frame`
     - [Project Monitor only] Identifies the object or area of the effect. :term:`Edit Mode<edit mode>` needs to be enabled for the frame to show.
   * - 2 :guilabel:`edit frame handles`
     - Used to change the size (square handles) and move the frame (circle in the middle)
   * - 3 :guilabel:`monitor overlay`
     - Hover over the defined hot spot (default: top right-hand side) to reveal the list of icons
   * - 4 :guilabel:`playhead`
     - Indicates the position in the :term:`timeline` or :term:`clip`
   * - 5 :guilabel:`timeline zone`
     - Indicates the timeline zone set with :kbd:`I` and :kbd:`O` or by clicking |zone-in| and |zone-out|, respectively
   * - 6 :guilabel:`zoom bar`
     - Used to zoom the timeline. Grab the white handles on either end and drag them left or right, or use :kbd:`Ctrl+MW` while hovering over the monitor timeline.
   * - 7 :guilabel:`audio level meter`
     - Displays the audio level of the project or clip when playback is running. The :ref:`audio mixer <audio_mixer>` settings will change the audio level appearance. 
   * - 8 :guilabel:`options drop-down`
     - Opens a list of options to select from
   * - 9 :guilabel:`timecode`
     - Shows the current position of the :term:`playhead` in the notation *hh:mm:ss:ff*, where *hh* is hours, *mm* is minutes, *ss* is seconds and *ff* is frame.
   * - 10 :guilabel:`tab (active)`
     - Currently active :term:`widget`
   * - 11 :guilabel:`tab (inactive)`
     - Available :term:`widgets<widget>` in that section of the work layout


Elements
--------
.. figure:: /images/user_interface/kdenlive2304_ui-elements.webp
   :width: 700px
   :figwidth: 700px

   UI areas and elements (example using the effect panel)

.. list-table::
   :width: 100%
   :widths: 30 70
   :header-rows: 1
   :class: table-wrap

   * - Element
     - Description
   * - [A] Effect panel header
     - Contains the name of the effect and the :guilabel:`collapse` icon and the effect panel toolbar
   * - [B] Effect parameters
     - Contains all the parameters for controlling the effect
   * - [C] Normal parameters
     - Contains all parameters that are not :term:`keyframable<keyframe>`
   * - [D] Keyframe panel
     - Contains the time ruler, the keyframes and the keyframe action icons
   * - [E] Keyframable parameters
     - Contains all parameters that can be keyframed\ [1]_
   * - [A1]
     - Name of the effect
   * - [A2]
     - Effect toolbar (for icons see :ref:`below <ui_elements-toolbar_icons>`)
   * - [D1]
     - Keyframes; red color is selected; a diamond shape denotes a linear keyframe, a square a discreet and a circle a smooth keyframe.
   * - [D2]
     - Keyframe action icons (for actions see :ref:`below <ui_elements-keyframe_action_icons>`)
   * - [E1]
     - Position and Size action icons (for actions see :ref:`below <ui_elements-pos-size_action_icons>`)


.. _ui_elements-monitor_elements:

.. figure:: /images/user_interface/kdenlive2304_ui-monitor_elements.webp
   :width: 700px
   :figwidth: 700px

   UI areas and elements (example using the monitor widget)

.. list-table::
   :width: 100%
   :widths: 30 70
   :header-rows: 1
   :class: table-wrap

   * - Element
     - Description
   * - [A] Monitor area
     - This is where the :term:`clip` playback is shown and where effects can be changed (only in the project monitor, if possible with the effect, and :term:`Edit Mode<edit mode>` is switched on)
   * - [B] Monitor time ruler
     - Shows the timeline for the project or clip where the current frame is indicated by the playhead or caret. A zoom bar and/or a timeline zone is displayed here if set.
   * - [C] Monitor toolbar
     - Contains controls/actions for the clip or project monitor widget
   * - [A1] Monitor overlay
     - Monitor overlay selection panel (for icons see :ref:`below <ui_elements-monitor_icons>`)
   * - [C1] Monitor controls/actions
     - For icons see :ref:`below <ui_elements-monitor_icons>`


.. _ui_elements-icons:

Icons and Buttons
-----------------

.. _ui_elements-toolbar_icons:

Effect Panel Toolbar Icons
~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :width: 80%
   :widths: 16 84
   :header-rows: 1
   :class: table-wrap

   * - Icon
     - Description
   * - |keyframe| |keyframe-disable|
     - Show :term:`keyframes<keyframe>` in timeline on/off
   * - |view-visible| |view-hidden|
     - Enable/disable :term:`effect`
   * - |adjustlevels|
     - Open the advanced effect menu
   * - |document-save|
     - Save current settings as new defaults for this effect
   * - |object-order-lower|
     - Move effect down one level. Changes the sequence effects are applied.
   * - |object-order-raise|
     - Move effect up one level. Changes the sequence effects are applied.
   * - |edit-delete|
     - Delete effect from effect stack


.. _ui_elements-keyframe_action_icons:

Keyframe Icons
~~~~~~~~~~~~~~
.. list-table::
   :width: 80%
   :widths: 16 84
   :header-rows: 1
   :class: table-wrap

   * - Icon
     - Description
   * - |keyframe-previous|
     - Jump to the previous :term:`keyframe`
   * - |keyframe-add|
     - Add a keyframe at the current position of the :term:`playhead/caret<playhead>`
   * - |keyframe-next|
     - Jump to the next keyframe
   * - |keyframe-remove|
     - Remove the keyframe at the current position of the playhead/caret. If multiple keyframes are selected, all selected keyframes are deleted.
   * - |align-horizontal-center|
     - Move selected keyframe to cursor/playhead/caret
   * - |edit-copy|
     - Copy selected keyframe(s)
   * - |edit-paste|
     - Paste keyframe(s)
   * - |linear|
     - Keyframe is of type 'linear' (interpolation towards this keyframe is linear)
   * - |discreet|
     - Keyframe is of type 'discreet' (no interpolation between the previous and this keyframe)
   * - |smooth|
     - Keyframe is of type 'smooth' (interpolation towards this keyframe is slightly dynamic with ease-in and ease-out with a little overshoot)
   * - |application-menu|
     - Opens the keyframe options window


.. _ui_elements-pos-size_action_icons:

Position and Size Icons
~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :width: 80%
   :widths: 16 84
   :header-rows: 1
   :class: table-wrap

   * - Icon
     - Description
   * - |align-horizontal-left|
     - Align the object frame to the left edge
   * - |align-horizontal-center|
     - Center the object frame horizontally
   * - |align-horizontal-right|
     - Align the object frame to the right edge
   * - |align-vertical-top|
     - Align the object frame to the top edge
   * - |align-vertical-center|
     - Center the object frame vertically
   * - |align-vertical-bottom|
     - Align the object frame to the bottom edge
   * - |zoom-original|
     - Zoom object frame to original size
   * - |zoom-fit-best|
     - Zoom object frame to best fit the project dimensions and center it
   * - |zoom-fit-width|
     - Zoom object frame to best fit the width of the project dimensions
   * - |zoom-fit-height|
     - Zoom object frame to best fit the height of the project dimensions


.. _ui_elements-monitor_icons:

Project / Clip Monitor Icons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :width: 80%
   :widths: 16 84
   :header-rows: 1
   :class: table-wrap

   * - Icon
     - Description
   * - |kdenlive-add-clip|
     - [Clip Monitor only] Insert the :term:`zone` into the :term:`project bin`
   * - 1:1 |go-down|
     - Set preview resolution
   * - |zone-in|
     - Set the :term:`Inpoint<In-point>` at the current position of the :term:`playhead`
   * - |zone-out|
     - Set the :term:`Outpoint<Out-point>` at the current position of the playhead
   * - |rewind|
     - Play backwards
   * - |play| |go-down|
     - Play; Play options
   * - |ffwd|
     - Fast forward
   * - |edit-mode|
     - [Project Monitor only] Toggle :term:`Edit Mode`
   * - |application-menu|
     - Monitor options menu
   * - |view-fullscreen|
     - Switch full screen
   * - |view-grid|
     - Change overlay. Click through the different available patterns.
   * - |zoom-in|
     - Zoom in
   * - |zoom-out|
     - Zoom out
   * - |list-add|
     - Add :term:`guide`
   * - |list-remove|
     - Remove guide
   * - |transform-move-horizontal|
     - Move toolbar. Click through to move the toolbar from the right (default) to the left and back.


.. _ui_elements-timeline_icons:

Timeline Icons
~~~~~~~~~~~~~~
.. list-table::
   :width: 80%
   :widths: 16 84
   :header-rows: 1
   :class: table-wrap

   * - Icon
     - Description
   * - |configure|
     - Timeline settings
   * - |timeline-use-zone-on| |timeline-use-zone-off|
     - Timeline :term:`zone` on/off
   * - |kdenlive-select|
     - Select tool
   * - |kdenlive-razor|
     - Razor tool
   * - |kdenlive-spacer|
     - Spacer tool
   * - |kdenlive-slip|
     - :term:`Slip tool`
   * - |kdenlive-ripple|
     - :term:`Ripple tool`
   * - |composite-track-preview|
     - :term:`Mix<Mixes>` clips (same track transition)
   * - |timeline-insert|
     - Insert clip :term:`zone` in timeline
   * - |timeline-overwrite|
     - Overwrite clip zone in timeline
   * - |timeline-extract|
     - Extract timeline zone
   * - |timeline-lift|
     - Lift timeline zone
   * - |favorite|
     - Favorite effects
   * - |preview-render-on|
     - Start preview render
   * - |go-down|
     - Preview render options
   * - |view-media-equalizer|
     - Audio mixer
   * - |add-subtitle|
     - Edit subtitle tool


.. _ui_elements-bin_icons:

Project Bin Icons
~~~~~~~~~~~~~~~~~
.. list-table::
   :width: 80%
   :widths: 16 84
   :header-rows: 1
   :class: table-wrap

   * - Icon
     - Description
   * - |kdenlive-add-clip| |go-down|
     - Add :term:`clip` or folder; open add source dialog
   * - |folder-new|
     - Create folder
   * - |edit-delete|
     - Delete (selected) clip(s)/folder(s)
   * - |tag|
     - Open Tags panel
   * - |view-filter| |go-down|
     - Filter; open filter selection


.. _ui_elements-status_bar_icons:

Status Bar Icons
~~~~~~~~~~~~~~~~
.. list-table::
   :width: 80%
   :widths: 16 84
   :header-rows: 1
   :class: table-wrap

   * - Icon
     - Description
   * - |tag|
     - Display color tags in the timeline
   * - |kdenlive-show-video|
     - Show video thumbnails
   * - |kdenlive-show-audio|
     - Show audio thumbnails
   * - |kdenlive-show-markers|
     - Show :term:`markers` comments
   * - |snap|
     - Snap
   * - |zoom-fit-best|
     - Zoom to fit project
   * - |zoom-in|
     - Zoom out
   * - |zoom-out|
     - Zoom in


----

.. [1] A keyframe is set for **all** keyframable parameters. If you want to change only a subset of the parameters you must create three keyframes: one at the frame where you want the parameters to change, one at the previous frame and one at the next frame. Then change the parameters at the middle keyframe and potentially at the next keyframe.


.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Icons used here (remove comment indent to enable them for this document)
   
   .. |add-subtitle| image:: /images/icons/add-subtitle.svg
   :width: 22px
   :class: no-scaled-link

   .. |adjustlevels| image:: /images/icons/adjustlevels.svg
   :width: 22px
   :class: no-scaled-link

   .. |align-horizontal-center| image:: /images/icons/align-horizontal-center.svg
   :width: 22px
   :class: no-scaled-link

   .. |align-horizontal-left| image:: /images/icons/align-horizontal-left.svg
   :width: 22px
   :class: no-scaled-link

   .. |align-horizontal-right| image:: /images/icons/align-horizontal-right.svg
   :width: 22px
   :class: no-scaled-link

   .. |align-vertical-top| image:: /images/icons/align-vertical-top.svg
   :width: 22px
   :class: no-scaled-link

   .. |align-vertical-center| image:: /images/icons/align-vertical-center.svg
   :width: 22px
   :class: no-scaled-link

   .. |align-vertical-bottom| image:: /images/icons/align-vertical-bottom.svg
   :width: 22px
   :class: no-scaled-link

   .. |application-menu| image:: /images/icons/application-menu.svg
   :width: 22px
   :class: no-scaled-link

   .. |bookmark| image:: /images/icons/bookmarks.svg
   :width: 22px
   :class: no-scaled-link

   .. |color-picker| image:: /images/icons/color-picker.svg
   :width: 22px
   :class: no-scaled-link

   .. |composite-track-preview| image:: /images/icons/composite-track-preview.svg
   :width: 22px
   :class: no-scaled-link

   .. |configure| image:: /images/icons/configure.svg
   :width: 22px
   :class: no-scaled-link

   .. |discreet| image:: /images/icons/discrete.svg
   :width: 22px
   :class: no-scaled-link

   .. |distribute-horizontal| image:: /images/icons/distribute-horizontal.svg
   :width: 22px
   :class: no-scaled-link

   .. |document-edit| image:: /images/icons/document-edit.svg
   :width: 22px
   :class: no-scaled-link

   .. |document-export| image:: /images/icons/document-export.svg
   :width: 22px
   :class: no-scaled-link

   .. |document-import| image:: /images/icons/document-import.svg
   :width: 22px
   :class: no-scaled-link

   .. |document-new| image:: /images/icons/document-new.svg
   :width: 22px
   :class: no-scaled-link

   .. |document-save| image:: /images/icons/document-save.svg
   :width: 22px
   :class: no-scaled-link

   .. |document-save-as| image:: /images/icons/document-save-as.svg
   :width: 22px
   :class: no-scaled-link

   .. |document-save-all| image:: /images/icons/document-save-all.svg
   :width: 22px
   :class: no-scaled-link

   .. |document-save-as-template| image:: /images/icons/document-save-as-template.svg
   :width: 22px
   :class: no-scaled-link

   .. |edit-clear-history| image:: /images/icons/edit-clear-history.svg
   :width: 22px
   :class: no-scaled-link
   
   .. |edit-copy| image:: /images/icons/edit-copy.svg
   :width: 22px
   :class: no-scaled-link

   .. |edit-delete| image:: /images/icons/edit-delete.svg
   :width: 22px
   :class: no-scaled-link

   .. |edit-download| image:: /images/icons/edit-download.svg
   :width: 22px
   :class: no-scaled-link

   .. |edit-mode| image:: /images/icons/kdenlive-edit-mode.svg
   :width: 22px
   :class: no-scaled-link

   .. |edit-paste| image:: /images/icons/edit-paste.svg
   :width: 22px
   :class: no-scaled-link

   .. |favorite| image:: /images/icons/favorite.svg
   :width: 22px
   :class: no-scaled-link

   .. |ffwd| image:: /images/icons/media-seek-forward.svg
   :width: 22px
   :class: no-scaled-link

   .. |folder-new| image:: /images/icons/folder-new.svg
   :width: 22px
   :class: no-scaled-link

   .. |go-down| image:: /images/icons/go-down.svg
   :width: 22px
   :class: no-scaled-link

   .. |go-next| image:: /images/icons/go-next.svg
   :width: 22px
   :class: no-scaled-link

   .. |go-up| image:: /images/icons/go-up.svg
   :width: 22px
   :class: no-scaled-link

   .. |hint| image:: /images/icons/hint.svg
   :width: 22px
   :class: no-scaled-link

   .. |kdenlive-add-clip| image:: /images/icons/kdenlive-add-clip.svg
   :width: 22px
   :class: no-scaled-link

   .. |kdenlive-audio| image:: /images/icons/kdenlive-audio.svg
   :width: 22px
   :class: no-scaled-link

   .. |kdenlive-hide-audio| image:: /images/icons/kdenlive-hide-audio.svg
   :width: 22px
   :class: no-scaled-link

   .. |kdenlive-hide-video| image:: /images/icons/kdenlive-hide-video.svg
   :width: 22px
   :class: no-scaled-link

   .. |kdenlive-lock| image:: /images/icons/track-locked.svg
   :width: 22px
   :class: no-scaled-link

   .. |kdenlive-razor| image:: /images/icons/edit-cut.svg
   :width: 22px
   :class: no-scaled-link

   .. |kdenlive-ripple| image:: /images/icons/kdenlive-ripple.svg
   :width: 22px
   :class: no-scaled-link

   .. |kdenlive-select| image:: /images/icons/kdenlive-select-tool.svg
   :width: 22px
   :class: no-scaled-link

   .. |kdenlive-show-video| image:: /images/icons/kdenlive-show-video.svg
   :width: 22px
   :class: no-scaled-link

   .. |kdenlive-show-audio| image:: /images/icons/view-media-visualization.svg
   :width: 22px
   :class: no-scaled-link

   .. |kdenlive-show-markers| image:: /images/icons/kdenlive-show-markers.svg
   :width: 22px
   :class: no-scaled-link

   .. |kdenlive-slip| image:: /images/icons/kdenlive-slip.svg
   :width: 22px
   :class: no-scaled-link

   .. |kdenlive-spacer| image:: /images/icons/distribute-horizontal.svg
   :width: 22px
   :class: no-scaled-link

   .. |keyframe| image:: /images/icons/keyframe.svg
   :width: 22px
   :class: no-scaled-link

   .. |keyframe-add| image:: /images/icons/keyframe-add.svg
   :width: 22px
   :class: no-scaled-link

   .. |keyframe-disable| image:: /images/icons/keyframe-disable.svg
   :width: 22px
   :class: no-scaled-link

   .. |keyframe-next| image:: /images/icons/keyframe-next.svg
   :width: 22px
   :class: no-scaled-link

   .. |keyframe-previous| image:: /images/icons/keyframe-previous.svg
   :width: 22px
   :class: no-scaled-link

   .. |keyframe-remove| image:: /images/icons/keyframe-remove.svg
   :width: 22px
   :class: no-scaled-link

   .. |linear| image:: /images/icons/linear.svg
   :width: 22px
   :class: no-scaled-link

   .. |list-add| image:: /images/icons/list-add.svg
   :width: 22px
   :class: no-scaled-link

   .. |list-remove| image:: /images/icons/list-remove.svg
   :width: 22px
   :class: no-scaled-link

   .. |media-record| image:: /images/icons/media-record.svg
   :width: 22px
   :class: no-scaled-link

   .. |network-server-database| image:: /images/icons/network-server-database.svg
   :width: 22px
   :class: no-scaled-link

   .. |object-order-lower| image:: /images/icons/object-order-lower.svg
   :width: 22px
   :class: no-scaled-link

   .. |object-order-raise| image:: /images/icons/object-order-raise.svg
   :width: 22px
   :class: no-scaled-link

   .. |play| image:: /images/icons/media-playback-start.svg
   :width: 22px
   :class: no-scaled-link

   .. |preview-add-zone| image:: /images/icons/preview-add-zone.svg
   :width: 22px
   :class: no-scaled-link

   .. |preview-remove-all| image:: /images/icons/preview-remove-all.svg
   :width: 22px
   :class: no-scaled-link

   .. |preview-remove-zone| image:: /images/icons/preview-remove-zone.svg
   :width: 22px
   :class: no-scaled-link

   .. |preview-render-off| image:: /images/icons/preview-render-off.svg
   :width: 22px
   :class: no-scaled-link

   .. |preview-render-on| image:: /images/icons/preview-render-on.svg
   :width: 22px
   :class: no-scaled-link

   .. |rewind| image:: /images/icons/media-seek-backward.svg
   :width: 22px
   :class: no-scaled-link

   .. |smooth| image:: /images/icons/smooth.svg
   :width: 22px
   :class: no-scaled-link

   .. |snap| image:: /images/icons/snap.svg
   :width: 22px
   :class: no-scaled-link

   .. |tag| image:: /images/icons/kdenlive-tag.svg
   :width: 22px
   :class: no-scaled-link

   .. |timeline-extract| image:: /images/icons/timeline-extract.svg
   :width: 22px
   :class: no-scaled-link

   .. |timeline-insert| image:: /images/icons/timeline-insert.svg
   :width: 22px
   :class: no-scaled-link

   .. |timeline-lift| image:: /images/icons/timeline-lift.svg
   :width: 22px
   :class: no-scaled-link

   .. |timeline-overwrite| image:: /images/icons/timeline-overwrite.svg
   :width: 22px
   :class: no-scaled-link

   .. |timeline-use-zone-off| image:: /images/icons/timeline-use-zone-off.svg
   :width: 22px
   :class: no-scaled-link

   .. |timeline-use-zone-on| image:: /images/icons/timeline-use-zone-on.svg
   :width: 22px
   :class: no-scaled-link

   .. |track-effect| image:: /images/icons/tools-wizard.svg
   :width: 22px
   :class: no-scaled-link

   .. |track-locked| image:: /images/icons/track-locked.svg
   :width: 22px
   :class: no-scaled-link

   .. |track-unlocked| image:: /images/icons/track-unlocked.svg
   :width: 22px
   :class: no-scaled-link

   .. |transform-move-horizontal| image:: /images/icons/transform-move-horizontal.svg
   :width: 22px
   :class: no-scaled-link

   .. |tools-wizard| image:: /images/icons/tools-wizard.svg
   :width: 22px
   :class: no-scaled-link

   .. |view-hidden| image:: /images/icons/view-hidden.svg
   :width: 22px
   :class: no-scaled-link

   .. |view-filter| image:: /images/icons/view-filter.svg
   :width: 22px
   :class: no-scaled-link

   .. |view-fullscreen| image:: /images/icons/view-fullscreen.svg
   :width: 22px
   :class: no-scaled-link

   .. |view-grid| image:: /images/icons/drag-surface.svg
   :width: 22px
   :class: no-scaled-link

   .. |view-media-equalizer| image:: /images/icons/view-media-equalizer.svg
   :width: 22px
   :class: no-scaled-link

   .. |view-preview| image:: /images/icons/view-preview.svg
   :width: 22px
   :class: no-scaled-link

   .. |view-refresh| image:: /images/icons/view-refresh.svg
   :width: 22px
   :class: no-scaled-link

   .. |view-right-close| image:: /images/icons/view-right-close.svg
   :width: 22px
   :class: no-scaled-link

   .. |view-split-left-right| image:: /images/icons/view-split-left-right.svg
   :width: 22px
   :class: no-scaled-link

   .. |view-visible| image:: /images/icons/view-visible.svg
   :width: 22px
   :class: no-scaled-link

   .. |visibility| image:: /images/icons/visibility.svg
   :width: 22px
   :class: no-scaled-link

   .. |zone-in| image:: /images/icons/zone-in.svg
   :width: 22px
   :class: no-scaled-link

   .. |zone-out| image:: /images/icons/zone-out.svg
   :width: 22px
   :class: no-scaled-link

   .. |zoom-fit-best| image:: /images/icons/zoom-fit-best.svg
   :width: 22px
   :class: no-scaled-link

   .. |zoom-fit-height| image:: /images/icons/zoom-fit-height.svg
   :width: 22px
   :class: no-scaled-link

   .. |zoom-fit-width| image:: /images/icons/zoom-fit-width.svg
   :width: 22px
   :class: no-scaled-link

   .. |zoom-in| image:: /images/icons/zoom-in.svg
   :width: 22px
   :class: no-scaled-link

   .. |zoom-out| image:: /images/icons/zoom-out.svg
   :width: 22px
   :class: no-scaled-link

   .. |zoom-original| image:: /images/icons/zoom-original.svg
   :width: 22px
   :class: no-scaled-link
