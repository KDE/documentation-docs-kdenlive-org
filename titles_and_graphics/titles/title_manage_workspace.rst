.. meta::
   :description: Kdenlive Documentation - Title Editor Workspace
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, titles, title clip, workspace, manage, coordinate, zoom, guides, background

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0



======================
Title Editor Workspace
======================

.. rubric:: Coordinate System
   
.. container:: clear-both

   .. figure:: /images/titles_and_graphics/title_toolbar-position.webp
      :width: 337px
      :figwidth: 337px
      :alt: title_toolbar-add_object
      :align: left

      Object position toolbar

   The default coordinate for the origin (0,0) is set to be the top left corner of the canvas and all objects.

.. rst-class:: clear-both

You can change this by clicking the :guilabel:`X` and :guilabel:`Y` buttons.

:guilabel:`+X` means the origin of the X-axis is on the left; :guilabel:`-X` means the origin of the X-axis is on the right.

:guilabel:`+Y` means the origin of the Y-axis is at the top; :guilabel:`-Y` means the origin of the Y-axis is at the bottom.

Therefore, :guilabel:`+X` and :guilabel:`-Y` sets the origin (0,0) of the coordinate system to the bottom left corner (something we ought to be familiar with from school).

.. note::
   This also sets the center for rotation.


.. rubric:: Guides, Zoom Level, and Background

.. figure:: /images/titles_and_graphics/titler_app_manage_workspace.webp
   :width: 360px
   :figwidth: 360px
   :align: left
   :alt: Title Editor Workspace Controls

   Title editor workspace controls

You can adjust some aspects of the workspace using the tools in this toolbar. By default, only :guilabel:`Show background` is selected.

If the title clip is in a track above another clip, the content of the clip below the title clip will be shown as the background.

:Use grid: Turns on a grid that objects snap to

:Show guides: Displays a set of guides and turns on the fields for number of vertical lines (default is 3), horizontal lines (default is 2), and the color button (default is red).

:Fit Zoom: Adjusts the zoom level to fit the standard viewport (or the canvas) to the width of the workspace

:Original Size (1:1): Adjusts the zoom level to display the title full size (depending on project settings)

:Zoom slider: Use the slider to adjust the zoom level. Alternatively, you can enter a zoom level percentage, or use :kbd:`Ctrl+MW` inside the workspace.

:Show background: When selected, the content of the clip in the timeline below the title clip is displayed. If not selected, the background can be set to :guilabel:`Checkered`, :guilabel:`Black`, or :guilabel:`White`.