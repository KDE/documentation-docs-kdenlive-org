.. meta::
   :description: Kdenlive's User Interface - Clip and Project Monitor
   :keywords: KDE, Kdenlive, clip, project, monitor, overlay, resizing, zoombar, preview, toolbar, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Julius Künzel <jk.kdedev@smartlab.uber.space
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |bmd_decklink| raw:: html

   <a href="https://www.blackmagicdesign.com/ca/products/decklink" target="_blank">Blackmagicdesign DeckLink</a>


.. _ui-monitors:

Monitors
========

Kdenlive uses two monitor :term:`widgets<widget>` to display and play back your videos, images, titles, animations or audio files:

.. toctree::
   :maxdepth: 1
   :glob:

   monitors/*

The monitor widgets can be switched on or off by checking :menuselection:`Menu --> View --> Clip Monitor` and :menuselection:`Project Monitor`, repectively. Once activated, they can be selected by clicking the corresponding tab which appears at the bottom of the monitor window.

.. .. versionadded:: 19.04

Kdenlive supports an external monitor display using |bmd_decklink| cards.

The :ref:`ui-monitors_clip_monitor` plays the :term:`clip` selected in the :doc:`Project Bin </project_and_asset_management/project_bin>`. The :ref:`ui-monitors_project_monitor` plays the timeline of the project starting at the position of the :term:`playhead`.


.. _ui-monitors_controls_and_elements:

Controls and Elements
---------------------

.. figure:: /images/user_interface/kdenlive2304_ui-monitor_controls.webp
   :width: 700px
   :figwidth: 700px
   :align: left

   Monitor controls (see :ref:`this table <ui_elements-monitor_controls>` for more details)
..

.. figure:: /images/user_interface/kdenlive2304_ui-monitor_elements.webp
   :width: 700px
   :figwidth: 700px
   :align: right

   Monitor areas and elements (see :ref:`this table <ui_elements-monitor_elements>` for more details)
..


.. _ui-monitors_display_toolbar:

Monitor Display Toolbar
-----------------------

.. .. versionadded:: 19.04

.. figure:: /images/user_interface/kdenlive2308_ui-monitor_overlay.gif
   :width: 350px
   :figwidth: 350px
   :align: left
   :alt: kdenlive2308_ui-monitor_overlay

   Monitor Display Toolbar and overlay options

The monitor display toolbar appears when you hover over the defined hotspot. By default this is the top right-hand side of the monitor area. Click on |transform-move-horizontal| to move the monitor display toolbar to the left-hand side or back. You can switch it off altogether by right-click in the monitor area, and selecting :menuselection:`Current Monitor Overlay --> Monitor Info Overlay`.

.. rst-class:: clear-both

The toolbar has the following options:

.. list-table::
   :width: 80%
   :widths: 10 90
   :class: table-wrap
   :header-rows: 1

   * - Icon
     - Description
   * - |view-fullscreen|
     - Switch full screen
   * - |view-grid|
     - Change overlay. Click through the different available patterns.
   * - |zoom-in|
     - Zoom in It’s always for the entire clip. Cut it if needed and apply motion tracking only to the resulting pieces where needed.
   * - |zoom-out|
     - Zoom Out
   * - |list-add|
     - Add guide
   * - |list-remove|
     - Remove guide
   * - |transform-move-horizontal|
     - Move Toolbar. Click through to move the toolbar from the right (default) to the left and back.


.. _ui-monitors_effect_direct_control:

Monitor and Effect Direct Control
---------------------------------

.. .. versionadded:: 24.08


.. figure:: /images/user_interface/kdenlive2408_ui-monitor_effect_direct_control.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2408_ui-monitor_effect_direct_control

   Changing clips position and size, enabling grid

Effects which can use direct control in the monitor are effects which have the following parameters: X, Y, Width, Height, Opacity (Alpha, optional) and Rotation. 

.. rst-class:: clear-both

Once such an effect is applied (either to a clip in the project bin, a clip in the timeline, a track or on master) you can:

.. list-table::
   :width: 80%
   :widths: 10 90
   :class: table-wrap
   :header-rows: 1

   * - Icon
     - Description
   * - |snap|
     - Enable a grid to which the clip will snap. :ref:`Changing grid size <ui-monitors_change_overlay_color>`
   * - |keyframe-next|
     - Go to the next keyframe.
   * - |keyframe-previous|
     - Go to the previous keyframe.
   * - |keyframe-add|
     - Add a keyframe
   * - |keyframe-record|
     - Add automatic keyframe

-	Move and resize. While resizing, holding:

   -	:kbd:`Shift` keep the aspect ratio

   -	:kbd:`Ctrl` keeps the center position untouched

-	Project monitor: cycling trough resized clips with :kbd:`Alt+click`

Once such an effect is applied, the monitor overlay selection panel does not have the |list-add| |list-remove| icon anymore (add/remove guide). To show the |list-add| |list-remove| icon again disable the effects |view-hidden| in the :ref:`effect/composition stack header <effect_stack_functions>`.

.. _ui-effect_direct_control:

Following effects can be used for direct control:

.. list-table::
   :width: 80%
   :widths: 100
   :class: table-wrap
   :header-rows: 1

   * - Effect name
   * - :doc:`Audio Level Visualization Filter </effects_and_filters/video_effects/on_master/audio_level_visualization_filter>`
   * - :doc:`Audio Spectrum Filter </effects_and_filters/video_effects/on_master/audio_spectrum_filter>`
   * - :doc:`Audio Waveform Filter </effects_and_filters/video_effects/on_master/audio_waveform_filter>`
   * - :doc:`Dynamic Text </effects_and_filters/video_effects/generate/dynamic_text>`
   * - :doc:`Position and Zoom </effects_and_filters/video_effects/transform_distort_perspective/position_and_zoom>`
   * - :doc:`Pillar Echo </effects_and_filters/video_effects/transform_distort_perspective/pillar_echo>` 
   * - :doc:`Transform </effects_and_filters/video_effects/transform_distort_perspective/transform>`
   * - :doc:`Crop by padding </effects_and_filters/video_effects/transform_distort_perspective/crop_padding>`


.. _ui-monitors_change_overlay_color:

Monitor Change Overlay Color and Grid Size
------------------------------------------

.. .. versionchanged:: 24.08


.. figure:: /images/user_interface/kdenlive2408_ui-monitor_overlay_color.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_ui-monitor_overlay_color

   Changing the color of the monitor overlay and grid size

The color of the guide and grid overlay as well as the grid size can be changed in :menuselection:`Menu --> Settings --> Configure Kdenlive --> Colors and Guides`.

.. rst-class:: clear-both


.. _ui-monitors_resizing:

Resizing the Monitor
--------------------

.. figure:: /images/user_interface/kdenlive2304_ui-monitor_resize.gif
   :width: 350px
   :figwidth: 350px
   :align: left
   :alt: kdenlive2304_ui-monitor_resize

   Resizing the monitor widget

You can resize the monitors by dragging the widget's edges. Make sure the mouse pointer changes to the sizing shape.

.. rst-class:: clear-both


.. _ui-monitors_zoombar:

Monitor Zoom Bar
----------------

.. .. versionadded:: 20.08.0

.. figure:: /images/user_interface/kdenlive_ui-monitor_zoombar.gif
   :width: 350px
   :figwidth: 350px
   :align: left
   :alt: kdenlive-ui-monitor_zoombar

   Monitor zoom bar (audio file example)

The timeline rulers of the monitors have zoom bars. To activate, hover over the timeline ruler and use :kbd:`Ctrl+Mouse wheel`. A zoom bar will appear with a scrollbar that has handles on the left and the right. At the same time, the timeline ruler scaling marks will change according to the zoom factor. This is helpful when trying to make frame-accurate cuts or setting :term:`zones<zone>`.

.. rst-class:: clear-both


.. _ui-monitors_preview_resolution:

Preview Resolution
------------------

.. .. versionadded:: 20.04.0

.. figure:: /images/user_interface/kdenlive2304_ui-monitor_preview_res.webp
   :width: 73px
   :figwidth: 73px
   :align: left
   :class: no-scaled-link
   :alt: kdenlive2304_ui-monitor_preview_res

   Preview resolutions

Changing the Preview Resolution speeds up the editing experience by scaling the video resolution of the monitors. It can be used instead of :term:`proxies<proxy>` or with proxies. Speed improvement depends on your source files.

Playback speed depends on several factors: source material, use of proxies, type and number of effects, and the CPU capabilities. There is limited to no GPU support for video playback. :doc:`Preview Rendering </tips_and_tricks/tips_and_tricks/timeline_preview_rendering>` is highly recommended if playback speed is lacking.

.. rst-class:: clear-both


.. _ui-multitrack_view:

Multitrack View
---------------

.. .. versionadded:: 20.04.0

You enable the multitrack view via :menuselection:`Menu --> Monitor --> Multitrack view` or via right-click in the Project Monitor area and selecting :guilabel:`Multitrack View` or by pressing :kbd:`F12`.

.. image:: /images/Multicam0.gif
   :alt: Multicam

The multitrack view interface allows you to select a track in the timeline by clicking on the project monitor. See the section about :ref:`multicam editing <multicam_tool>` for using it during Editing.


.. _ui-separate_monitors:

Clip and Project Monitor in Separate Windows
--------------------------------------------

If you want to have the :ref:`Clip <ui-monitors_clip_monitor>` and/or the :ref:`Project Monitor <ui-monitors_project_monitor>` in their own individual windows click on the respective tab and drag the monitor :term:`widget` out into its own window. This undocks the widgets from their space. From there you can move them even to other monitors you may have connected.

.. figure:: /images/user_interface/kdenlive2308_ui-monitors_separate_windows.gif
   :width: 100%
   :figwidth: 100%
   :alt: kdenlive2308_ui-monitors_separater_windows

   Moving Clip and Project Monitor to their own independent windows (undocking)

To put the monitors back into the tabbed view click on the monitor's title bar (enable it via :menuselection:`Menu --> View --> Show Titlebars`) and drag the window on top of another widget. See the :ref:`ui-customizing_interface` chapter for more details.

.. note:: There is low risk that the monitor widget has no title bar (intermittent defect). In this case you will need to reset the Kdenlive settings by deleting :file:`~/.config/kdenliverc` (Linux) or :file:`C:\\Users\\<user_name>\\AppData\\Roaming\\kdenlive\\kdenlivestaterc` (Windows).
