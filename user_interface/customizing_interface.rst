.. meta::
   :description: Kdenlive's User Interface - Customizing the Interface
   :keywords: KDE, Kdenlive, user interface, widget, layout, arrange, documentation, user manual, video editor, open source, free, learn, easy, customize

.. metadata-placeholder

   :authors: - Eugen Mohr
             - Maris Stalte (https://userbase.kde.org/User:limerick)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             
   :license: Creative Commons License SA 4.0


.. .. versionchanged:: 25.12 Switch to KDDockWidgets library for improved docking

.. _ui-customizing_interface:

Customizing the Interface
=========================

The user interface model allows you to freely adjust the different panels to support your workflow. You can add :term:`widgets<widget>` to and delete them from the different panels, rearrange them, change the size of the panels, and save the workspace layout so you can have different layouts with different widgets depending on the stage of your post-production work. For example, you can have different workspace layouts for video editing, color correction and sound editing. Kdenlive comes with four different workspace layouts already defined. See the :ref:`ui-workspace_layouts` chapter.

.. figure::  /images/user_interface/kdenlive2304_ui-workspaces.webp
   :align: left
   :width: 350px
   :figwidth: 350px
   
   Kdenlive’s default workspaces (example uses the Editing view; click to enlarge)

Here is a quick reminder of the different workspace panels (see :ref:`user_interface`). In this section we want to focus on the panels 1 thru 4 and panel #6. Panel #5 (timeline toolbar) is not really a panel by itself but is part of the timeline. Panels 7 and 8 are described in more detail in the :ref:`status_bar` (#8) and :ref:`toolbars` (#7) chapters.

.. rst-class:: clear-both



Kdenlive allows you to arrange the predefined five panels as you like by grabbing an empty part where there are no tabs.

Widgets can be rearrange the same way.

Here an example where the layout is arranged in column or rows:

.. |columns| image:: /images/user_interface/kdenlive2304_ui-screen_layout_columns.webp
   :width: 340px
   
.. |rows| image:: /images/user_interface/kdenlive2304_ui-screen_layout_rows.webp
   :width: 340px
   
.. list-table::

   * - |columns|
     - |rows|
   * - *Columns* (click to enlarge)
     - *Rows* (click to enlarge)

You can have widgets as tabs (see the yellow box in the screenshots above) regardless of the dock orientation setting.

Rearranged layouts are stored in the project file when saving.


.. _ui-adding_widgets:

Adding Widgets
--------------

You can add :term:`widgets<widget>` (e.g. :ref:`view-library`, :ref:`view-project_notes`) by enabling them in :menuselection:`Menu --> View`. Likewise, disable them by taking off the check mark right next to their entry in the menu.


.. _ui-moving_widgets:

Moving Widgets
--------------

You move a :term:`widget` by grabbing the tab or the :term:`title bar` and moving it to a new position. It is possible to move the widget to a different position within the same panel thereby simply changing the sequence of the tabs.

A widget can also be moved to a new panel, to its own (new) column or row, or undocked as a floating window. Put a floating window on a second screen on which you can dock other widgets to create a new panel. 

.. note:: In order to move widgets without a tab they must have :term:`title bars<title bar>`. You can switch them on and off in :menuselection:`Menu --> View --> Show Title Bars`.

.. figure::  /images/user_interface/menu-view_Show-title-bar_2512.webp
   :align: left
   :scale: 77%
   
   Make sure Show Title Bars is enabled

.. rst-class:: clear-both

This shows you the title bar of each widgets when un-docked

.. figure::  /images/user_interface/view_title-bar_2512.webp
   :align: left
   :scale: 77%
   
   Title bar of the timeline view

.. rst-class:: clear-both

On the title bar are 3 icons

.. figure::  /images/user_interface/view-title_bar_icons-2512.webp
   :align: left
   :scale: 77%
   
.. rst-class:: clear-both

* :ref:`Auto-hide <ui-auto_hide>`. Let's you save space by hiding window until needed. 

* Undock window. The window get undocked and ready for moving.

* Close. The window get closed and can be re-opened in :menuselection:`Menu --> view`

In the example below the :ref:`Clip <ui-monitors_clip_monitor>` and :ref:`Project Monitor <ui-monitors_project_monitor>` widgets are being undocked and turned into floating windows:

.. figure:: /images/user_interface/kdenlive2308_ui-monitors_separate_windows.gif
   :width: 100%
   :figwidth: 100%
   
   Moving Clip and Project Monitor to their own independent windows (undocking)

The Kdenlive layout reacts to your dragging of the widget and you need to pay close attention which docking indicator change color when you move over them.

.. figure:: /images/user_interface/ui-manage_layouts_2512.webp
   :width: 100%
   :figwidth: 100%
   
   Docking indicators when a widget is undocked and hovered over a panel

:1: Panel docking indicator. Docking inside the panel: top, right, bottom, left or center. In this example it would be placed to the left side showed by the blue indicator. 

:2: Edge docking indicator. Docking outside of a panel: top, right, bottom, left. Here a window can be :ref:`auto-hided <ui-auto_hide>`

:3: Blue indicator where the widget would land if you release it

.. tip:: When trying to move a floating window to a new position Kdenlive may think you want to move it to a panel or create a new row or column. It is recommended to use the standard size handles of the window manager to adjust the top left and bottom right corners accordingly.


.. _ui-auto_hide:

Auto-hide
~~~~~~~~~

.. figure:: /images/user_interface/ui-auto_hide-2512.gif

   Space Saving: Displays more content by hiding panels until needed.

Click the pin icon (first icon in the title bar) to enable the auto-hide feature which lets you pin dockable window (widgets) to the edges (top, right, bottom, left; See point 2 above) of the main window, making them disappear into a sidebar and reappear as overlays when clicked. 

Restoring: Click the pin icon again (now on the overlay) to restore it to its original docked position. 
   

.. _ui-resizing_widgets:

Resizing Widgets
----------------

You can only resize the column or row the :term:`widget` is docked in. Hover over the widget's edge on either side and the mouse pointer will change into the re-size pointer. Now drag the edge until the desired size is reached. You can only drag horizontally or vertically individually.


.. _ui-saving_layout:

Saving the Layout
-----------------

Once you have arranged the :term:`widgets<widget>` to your liking you can save the layout via :menuselection:`Menu --> View --> Save Layout`. A dialog windows opens where you can name the new layout. If you enter the name of an existing layout a warning will appear but you can overwrite the layout.

The current layout is saved within the Kdenlive project file. 

It is good practice and very helpful to have different layouts for the different tasks of post-production. See the :ref:`ui-workspace_layouts` chapter for more details.


.. _ui-loading_layout:

Loading a Layout
----------------

You can load a layout either by selecting it from :menuselection:`Menu --> View --> Load Layout`, or by clicking on the desired one listed in the :ref:`menu bar <menubar>` (top-right hand corner of the screen).


.. _ui-manage_layouts:

Managing Layouts
----------------

Kdenlive displays only eight saved layouts when selecting :menuselection:`Menu --> View --> Load Layout`, and in the :ref:`menu bar <menubar>` only four are displayed. But you can have many more.

.. figure::  /images/user_interface/kdenlive2304_ui-manage_layouts.webp
   :align: left
   :width: 250px
   :figwidth: 250px
   
   List of available layouts

Selecting :menuselection:`Menu --> View --> Manage Layouts` opens this window where you can manage the workspace layouts available.

Use |go-up| and |go-down| to move the highlighted layout up and down in the list. The first eight from this list will be available through the menu.

Click on |view-refresh| to refresh the list. Use |edit-delete| to delete the highlighted entry.

You can export |document-export| and import |document-import| saved layouts.
