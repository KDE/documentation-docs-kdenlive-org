.. meta::
   :description: Kdenlive's User Interface - Customizing the Interface
   :keywords: KDE, Kdenlive, user interface, documentation, user manual, video editor, open source, free, learn, easy, customize

.. metadata-placeholder

   :authors: - Eugen Mohr
             - Maris Stalte (https://userbase.kde.org/User:limerick)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             
   :license: Creative Commons License SA 4.0


.. _ui-customizing_interface:

Customizing the Interface
=========================

The user interface model allows you to freely adjust the different panels to support your workflow. You can add :term:`widgets<widget>` to and delete them from the different panels, rearrange them, change the size of the panels, and save the workspace layout so you can have different layouts with different widgets depending on the stage of your post-production work. For example, you can have different workspace layouts for video editing, color correction and sound editing. Kdenlive comes with four different workspace layouts already defined. See the :ref:`ui-workspace_layouts` chapter.

.. figure::  /images/user_interface/kdenlive2304_ui-workspaces.webp
   :align: left
   :width: 350px
   :figwidth: 350px
   :alt: kdenlive2304_ui-workspaces

   Kdenlive’s default workspaces (example uses the Editing view; click to enlarge)

Here is a quick reminder of the different workspace panels (see :ref:`user_interface`). In this section we want to focus on the panels 1 thru 4 and panel #6. Panel #5 (timeline toolbar) is not really a panel by itself but is part of the timeline. Panels 7 and 8 are described in more detail in the :ref:`status_bar` (#8) and :ref:`toolbars` (#7) chapters.

.. rst-class:: clear-both

Kdenlive allows you to arrange these five panels in columns or in rows. You define this in :menuselection:`Menu --> View --> Dock Area Orientation`. In both cases the timeline panel (#4) determines what is a row and what is a column.
The difference is that if you select :guilabel:`Arrange dock areas in columns` you can add columns to the right of the timeline that extend from top to bottom. You can still add widgets above or below other widgets but the right edge of the timeline will be. If you select :guilabel:`Arrange dock areas in rows` you have two rows to start with. You can drag widgets below the timeline to create a new row but not above the first and between the first and second row. You can move widgets with a row to create new columns.

.. |columns| image:: /images/user_interface/kdenlive2304_ui-screen_layout_columns.webp
   :width: 340px
   :alt: kdenlive2304_ui-screen_layout_columns

.. |rows| image:: /images/user_interface/kdenlive2304_ui-screen_layout_rows.webp
   :width: 340px
   :alt: kdenlive2304_ui-screen_layout_rows

.. list-table::

   * - |columns|
     - |rows|
   * - *Columns* (click to enlarge)
     - *Rows* (click to enlarge)

Note that you can still have widgets in rows within one column, and in columns within one row. See the dashed lines in the images above. Similarly, you can have widgets as tabs (see the yellow box in the screenshots above) regardless of the dock orientation setting.


.. _ui-adding_widgets:

Adding Widgets
--------------

You can add :term:`widgets<widget>` (e.g. :ref:`view-library`, :ref:`view-project_notes`) by enabling them in the :menuselection:`Menu --> View Menu`. Likewise, disable them by taking off the check mark right next to their entry in the menu.


.. _ui-moving_widgets:

Moving Widgets
--------------

You move a :term:`widget` by grabbing the tab or the :term:`title bar` and moving it to a new position. It is possible to move the widget to a different position within the same panel thereby simply changing the sequence of the tabs.

A widget can also be moved to a new panel, to its own (new) column or row, or undocked as a floating window. In the example below the :ref:`Clip <ui-monitors_clip_monitor>` and :ref:`Project Monitor <ui-monitors_project_monitor>` widgets are being undocked and turned into floating windows:

.. figure:: /images/user_interface/kdenlive2308_ui-monitors_separate_windows.gif
   :width: 100%
   :figwidth: 100%
   :alt: kdenlive2308_ui-monitors_separater_windows

   Moving Clip and Project Monitor to their own independent windows (undocking)

The Kdenlive layout reacts to your dragging of the widget and you need to pay close attention which layout elements change color when you move over them.

.. list-table::
   :header-rows: 1

   * - Reaction
     - Result when let go
   * - Widget underneath changes color
     - Widget is added as a tab to the panel
   * - Empty highlighted area appears
     - Widget is dropped in to a new column or row
   * - No color change
     - [Only when hovering over the timeline panel or the menu bar] Widget becomes a floating window

.. tip:: When trying to move a floating window to a new position Kdenlive may think you want to move it to a panel or create a new row or column. It is recommended to use the standard size handles of the window manager to adjust the top left and bottom right corners accordingly.

.. note:: In order to move widgets without a tab they must have :term:`title bars<title bar>`. You can switch them on and off in :menuselection:`Menu --> View --> Show Title Bars`.


.. _ui-resizing_widgets:

Resizing Widgets
----------------

You can only resize the column or row the :term:`widget` is docked in. Hover over the widget's edge on either side and the mouse pointer will change into the re-size pointer. Now drag the edge until the desired size is reached. You can only drag horizontally or vertically individually.


.. _ui-saving_layout:

Saving the Layout
-----------------

Once you have arranged the :term:`widgets<widget>` to your liking you can save the layout via :menuselection:`Menu --> View --> Save Layout`. A dialog windows opens where you can name the new layout. If you enter the name of an existing layout a warning will appear but you can overwrite the layout.

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
   :alt: kdenlive2304_ui-manage_layouts

   List of available layouts

Selecting :menuselection:`Menu --> View --> Manage Layouts` opens this window where you can manage the workspace layouts available.

Use |go-up| and |go-down| to move the highlighted layout up and down in the list. The first eight from this list will be available through the menu.

Click on |view-refresh| to refresh the list. Use |edit-delete| to delete the highlighted entry.

You can export |document-export| and import |document-import| saved layouts.
