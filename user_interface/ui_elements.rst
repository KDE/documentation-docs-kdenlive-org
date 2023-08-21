.. meta::
   :description: Kdenlive's User Interface - UI Elements, Icons and Buttons
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
   :align: left

   Kdenlive UI controls (example using the effect panel)
..

.. list-table::
   :width: 100%
   :widths: 30 70
   :header-rows: 1

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
     - Used to enter a specific value. In most cases it is possible to use the :kbd:`Mouse wheel` to increase or decrease the value.
   * - 8 :guilabel:`button`
     - Used to enable a certain state while it is pushed in. Click again to make it come out.
   * - 9 :guilabel:`slider`
     - Allows for rapid changes of values. Drag the mouse left or right to move the slider. The value in an adjacent :guilabel:`direct entry` field is changed accordingly.
   * - 10 :guilabel:`action button`
     - Used to change a value in defined steps. Every click changes the value, wrapping at the end of the scale may occur.
   * - 11 :guilabel:`action icon`
     - Used to execute an action that is not repeatable (with exceptions)


.. _ui_elements-monitor_controls:

.. figure:: /images/user_interface/kdenlive2304_ui-monitor_controls.webp
   :width: 700px
   :figwidth: 700px
   :align: left

   Kdenlive UI controls (example using the monitor panel)
..

.. list-table::
   :width: 100%
   :widths: 30 70
   :header-rows: 1

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
     - Used to zoom the timeline. Grab the white handles on either end and drag them left or right, or use :kbd:`Ctrl+Mouse wheel` while hovering over the monitor timeline.
   * - 7 :guilabel:`audio level meter`
     - Displays the audio level of the project or clip when playback is running
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
   :align: left

   UI areas and elements (example using the effect panel)
..

.. list-table::
   :width: 100%
   :widths: 30 70
   :header-rows: 1

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
   :align: left

   UI areas and elements (example using the monitor widget)
..

.. list-table::
   :width: 100%
   :widths: 30 70
   :header-rows: 1

   * - Element
     - Description
   * - [A] Monitor area
     - This is where the :term:`clip` playback is shown and where effects can be changed (only in the project monitor, if possible with the effect, and :term:`Edit Mode<edit mode>` is switched on)
   * - [B] Monitor time ruler
     - Shows the timeline for the project or clip where the current frame is indicated by the playhead or caret. A zoom bar and/or a timeline zone is displayed her if set.
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
   * - |toggle-edit-mode|
     - Toggle :term:`Edit Mode`
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


**Notes**

.. [1] A keyframe is set for **all** keyframable parameters. If you want to change only a subset of the parameters you must create three keyframes: one at the frame where you want the parameters to change, one at the previous frame and one at the next frame. Then change the parameters at the middle keyframe and potentially at the next keyframe.
