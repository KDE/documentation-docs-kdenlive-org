.. meta::
   :description: Kdenlive's User Interface - Monitor Menu
   :keywords: KDE, Kdenlive, clip, project, menu, monitor menu, modes, selection, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jack (https://userbase.kde.org/User:Jack)
             - Eugen Mohr

   :license: Creative Commons License SA 4.0

.. _monitor_menu:

Monitor Menu
============

.. .. versionchanged:: 25.12 Reorder menu structure and content 


.. figure:: /images/user_interface/menu_reference/menu_reference-monitor_menu-2512.webp
  :align: left
  :scale: 75%

  Kdenlive Monitor Menu

- :ref:`Switch Monitor <switch_monitor>`
- :ref:`Focus Timecode <focus_timecode>`
- :ref:`Play <play>`
- :ref:`Play Zone <play_zone>`
- :ref:`Play Zone From Cursor <play_zone_from_cursor>`
- :ref:`Loop Zone <loop_zone>`
- :ref:`Loop Selected Clip <loop_selected_clip>`
- :ref:`Go to <go_to>`
- :ref:`Seek <seek>`
- :ref:`Set Zone In <set_zone_in>`
- :ref:`Set Zone Out <set_zone_out>`
- :ref:`Insert Zone in Project Bin <insert_zone_in_project_bin>`
- :ref:`Switch Monitor Fullscreen <switch_monitor_fullscreen>`
- :ref:`Multitrack View <multitrack_view>`
- :ref:`Zoom In Monitor <zoom_in_monitor>`
- :ref:`Zoom Out Monitor <zoom_out_monitor>`
- :ref:`Current Monitor Overlay <current_monitor_overlay>`
- :ref:`Preview Resolution <preview_resolution>`
- :ref:`Monitor Config <monitor_config>`

.. rst-class:: clear-both



The monitor menu contains controls for viewing and navigating through the clips in your project for the purpose of making edits and seeing the effects of your changes.  Depending on which monitor window you have selected at the time, the controls will affect either the currently selected clip in the Project Bin (**Clip Monitor**) or the playhead in the Timeline (**Project Monitor**).


With the exception of the :menuselection:`Deinterlacer` and :menuselection:`Interpolation` items, it is much more practical to perform the actions on this menu using the associated keyboard shortcuts or the buttons at the bottom of the monitor windows.

----

.. _switch_monitor:

* **Switch Monitor**: Toggles between clip monitor and project monitor. when the project monitor is in focus the timeline is focus as well. Keyboard Shortcut :kbd:`T`

.. _focus_timecode:

* **Focus Timecode**: Focus to the timecode on the active monitor so you can change the timecode to the place you want to jump to. Keyboard shortcut :kbd:`=`

----

.. _play:

* **Play**: Start playing the monitor in focus with shortcut :kbd:`space`.

.. _play_zone:

* **Play Zone**: Plays from in-point to the out-point of a zone. Keyboard Shortcut :kbd:`Ctrl + space`

.. _play_zone_from_cursor:

* **Play Zone From Cursor**: Plays from the playhead to the out-point of a zone.

.. _loop_zone:

* **Loop Zone**: Plays from in-point to the out-point of a zone in a loop. Keyboard Shortcut :kbd:`Ctrl + shift + space`

.. _loop_selected_clip:

* **Loop Selected Clip**: This works in the timeline only. Plays from the first to the last selected clip in the timeline in a loop.

----

.. _go_to:

Go To
-----

This menu item opens a flyout with actions for jumping to dedicated points in the timeline:

.. figure:: /images/user_interface/menu_reference/menu_reference-go_to_menu-2512.webp
   :align: left
   :scale: 77%
   
   Go To Menu

.. rst-class:: clear-both

.. _seek:

Seek
----

This menu item opens a flyout with following seeking possibilities:

.. figure:: /images/user_interface/menu_reference/menu_reference-seek_menu-2512.webp
   :align: left
   :scale: 77%
   
   Seek Menu

.. rst-class:: clear-both

----

.. _set_zone_in:

* **Set Zone In**: This set the point where a zone starts. Shortcut :kbd:`I` 

.. _set_zone_out:

* **Set Zone Out**: This set the point where a zone ends. Shortcut :kbd:`O`

.. _insert_zone_in_project_bin:

* **Insert Zone in Project Bin**: When you have created a zone you can put the zone with this command into the project bin as a sub-clip of the original clip. This is useful when you have a long clip and you want only some parts of it. Shortcut :kbd:`Ctrl + I`. Another possibility is to use :ref:`markers_with_range`.

----

.. _switch_monitor_fullscreen:

* **Switch Monitor Fullscreen**: Switch the monitor to full screen when hit :kbd:`F11`.

.. _multitrack_view:

* **Multitrack View**: Multitrack view is described in detail :ref:`here <ui-multitrack_view>`.

.. _zoom_in_monitor:

* **Zoom In Monitor**: Zooms in.

.. _zoom_out_monitor:

* **Zoom Out Monitor**: Zooms out.

.. _current_monitor_overlay:

* **Current Monitor Overlay**: Opens a fly-out for the various available monitor overlays. More details see in :ref:`Clip Monitor <ui-monitors_cm_rightclick>` or :ref:`Project Monitor <ui-monitors_pm_right_click>`.

.. _preview_resolution:

* **Preview Resolution**: Preview resolution is described in detail :ref:`here <ui-monitors_preview_resolution>`.

.. _monitor_config:

* **Monitor Config**: Opens a fly-out for the various available monitor configurations. More details see in :ref:`Clip Monitor <ui-monitors_cm_rightclick>` or :ref:`Project Monitor <ui-monitors_pm_right_click>`.

