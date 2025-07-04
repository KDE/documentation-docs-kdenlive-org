.. meta::
   :description: Kdenlive Documentation - Title Clips
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, titles, title clip, text

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Vincent Pinon <vpinon@kde.org>
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jack (https://userbase.kde.org/User:Jack)
             - Roger (https://userbase.kde.org/User:Roger)
             - Carl Schwan <carl@carlschwan.eu>
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |kde_store| raw:: html

   <a href="https://store.kde.org/" target="_blank">KDE Store</a>


###########
Title Clips
###########

A **Title Clip** is, as the name suggests, a clip that contains a title usually mainly comprised of text. But it is more than that.

Besides text elements, **Title Clips** can contain rectangles, circles, and images. This is useful for creating complex titles, chevrons, lower thirds, call-outs, or other graphical elements to enhance your project. You can create :doc:`template titles</titles_and_graphics/titles/title_template_titles>` with limited wildcard/placeholder functionality to be used for other titles in the same project, and create patterns from selected texts and shapes that can be applied across different title clips.

A built-in :doc:`animation function</titles_and_graphics/graphics_and_animations/title_scrolling>` can be used to create scrolling text, for example for closing credits.

You can also save any title for use in other projects as a title template that is then available from the :guilabel:`Template` drop-down list in the title editor. Title templates are also available from the KDE Store and can be installed directly from within the `the title clip app`_.

Title clips behave like any other video or image clips in the timeline, and you can apply any effect to them. In particular keyframes, motion tracking, and transform allow for simple yet interesting animations.

Title clips by default have an alpha channel which makes compositing rather easy. Simply put a title clip on a track above a video or image, and texts and shapes of the title clip will overlay the clips on the tracks below. Of course, you can also use a :doc:`composition</compositing/compositions>` to create other effects.


The Title Clip App
==================

You create and edit title clips in the **Titler App**. When you select :guilabel:`Add Title Clip` or double-click an existing title clip in the :doc:`Project Bin</project_and_asset_management/project_bin>` or the :doc:`Timeline</user_interface/timeline>`, or right-click a title clip in the :doc:`Project Bin</project_and_asset_management/project_bin>` and select :guilabel:`Edit`, the **Titler App** is opened in a separate window.

You can size the window as usual but not maximize or minimize it. The focus stays on this window, and you cannot work, for example, on the timeline, or do other things with Kdenlive until you close that window.

.. _title-editor_layout:

The window's layout consists of several areas:

.. image:: /images/titles_and_graphics/titler_app_layout.webp

* The main workspace (1)
* Toolbars for `adding objects <title-add_objects_>`_ (2), `selecting objects <title-select_objects_>`_ (3), sizing and `aligning objects <title-move_objects_>`_ (4)/(5)/(6), :doc:`managing the workspace</titles_and_graphics/titles/title_manage_workspace>` (8)/(9), and :doc:`file operations</titles_and_graphics/titles/title_file_operations>` (10)
* Properties of the objects (7). You can adjust the width of the properties pane by dragging the line between the properties pane and the workspace left and right.

The workspace shows three boxes marked in red indicating safe zones\ [1]_. The outermost box (bright red) shows the project dimensions. Any object outside that area will be shown only partially or not at all.
The next smaller box (dark red) shows an area considered safe for action. The smallest box (dark red) shows an area considered the focus of the viewport and therefore safe for titles.


.. toctree:: 
   :hidden:

   title_manage_workspace
   title_file_operations
   title_template_titles


.. _title-create_clip:

Create a Title Clip
===================

You create a title clip using one of the following options:

* In the :doc:`Project Bin</project_and_asset_management/project_bin>`, click on |kdenlive-add-clip| |go-down| :guilabel:`Add Clip or Folder` and select :guilabel:`Add Title Clip`
* Right-click on empty space in the :doc:`Project Bin</project_and_asset_management/project_bin>` and select :guilabel:`Add Title Clip`
* Right-click an existing title clip, select :guilabel:`Duplicate clip`, and then double-click the newly created title clip (you may want to rename it first, though)

Kdenlive opens the title editor with a blank workspace (canvas). From here you can start `adding objects <title-add_objects_>`_, open a saved title, or use a title template.

Once you are done adding objects like texts, images, and shapes, click on :guilabel:`Create Title`. Kdenlive closes the window and adds a new title clip to the Project Bin. The name of the title clip is taken from the content of the text field that was created first. If needed, you can change the name of the title clip by double-clicking the name of the title clip in the Project Bin.

You can also save a title as a Title Template for use in other projects. A template is available from the :guilabel:`Template` drop-down list (see (10) in the `layout description <title-editor_layout_>`_). Click on |document-save-as|\ :guilabel:`Save as` or press :kbd:`Ctrl+S`, and specify the target folder and name for the title. Make sure that the title is saved in the :file:`.kdenlivetitle` format for Kdenlive to recognize it properly. For a title to be used as a template, it must be saved to this folder in your filesystem:

:Linux appimage: :file:`~/.local/share/kdenlive/titles`

:Linux Flatpak: :file:`~/.var/app/org.kde.kdenlive/data/kdenlive/titles`

:Windows: :file:`%AppData%/kdenlive/titles` (press :kbd:`Win+R` and copy **%AppData%/kdenlive/**)


Edit a Title Clip
=================

You edit a title clip using one of the following options:

* Double click the title clip in the :doc:`Project Bin</project_and_asset_management/project_bin>` or in the :doc:`Timeline</user_interface/timeline>`
* Right-click the title clip in the project bin and select Edit Clip

Once you are done editing the title clip, click on :guilabel:`Update Title`. Kdenlive closes the window and updates the title clip in the project bin and all occurrences of that title clip in the timeline. Your changes are available immediately.


.. _title-add_objects:

Add Objects to a Title Clip
===========================

.. toctree:: 
   :hidden:

   title_text
   title_shapes
   title_images
   title_patterns

.. container:: clear-both

   .. figure:: /images/titles_and_graphics/title_toolbar-add_object.webp
      :width: 109px
      :figwidth: 150px
      :alt: title_toolbar-add_object
      :align: left

      Add objects toolbar

   The toolbar for adding objects has icons for :doc:`text</titles_and_graphics/titles/title_text>` , :doc:`shapes</titles_and_graphics/titles/title_shapes>`, and :doc:`image</titles_and_graphics/titles/title_images>`.

.. rst-class:: clear-both

* Click on |insert-text|, or use the keyboard shortcut :kbd:`Alt+T`, then click in the main workspace to :doc:`create a new text field</titles_and_graphics/titles/title_text>`
* Click on |kdenlive-insert-rect|, or use the keyboard shortcut :kbd:`Alt+R`, then drag the mouse across the main workspace to create a :doc:`rectangle</titles_and_graphics/titles/title_shapes>`
* Click on |draw-ellipse|, or use the keyboard shortcut :kbd:`Alt+E`, then drag the mouse across the main workspace to create an :doc:`ellipse</titles_and_graphics/titles/title_shapes>`
* Click on |insert-image|, or use the keyboard shortcut :kbd:`Alt+I`, to bring up the Open File dialog window where you can :doc:`choose an image</titles_and_graphics/titles/title_images>` file to be inserted into the title clip

When the title editor window is opened the default item to be created is **Text**, so you can immediately start creating a text field.

A special way to add objects is to use :doc:`patterns</titles_and_graphics/titles/title_patterns>`.

The objects are placed on top of each other following the sequence in which they were created. If you need to bring an object/item forward that was created in the early stages, use the :guilabel:`Z-Index` field or click on the respective icon (|object-order-raise|, |object-order-lower|, |object-order-front|, |object-order-back|) in the stack toolbar. Likewise, you can also send an object/item backwards.


.. _title-select_objects:

Select Objects
==============

Click on |transform-move| :guilabel:`Select/Move` or use the keyboard shortcut :kbd:`Alt+S` to be able to select the different objects.

Click on |edit-select-all| :guilabel:`Select All` or press :kbd:`Ctrl+A`, drag a selection frame around objects, or hold Shift and select individual objects, for example to save them as a pattern.

If you want to select all Text objects, first select all objects, then click on |kdenlive-select-texts| :guilabel:`Keep only text items selected` or press :kbd:`Ctrl+T`.

The same logic can be applied for image objects (|kdenlive-select-images| :guilabel:`Keep only image items selected` or :kbd:`Ctrl+I`), and rectangle objects (|select-rectangular| :guilabel:`Keep only rectangle items selected` or :kbd:`Ctrl+R`).

Click on |edit-select-none| :guilabel:`Deselect` or press :kbd:`Ctrl+Shift+A` to deselect all objects.


.. _title-move_objects:

Adjust and Move Objects
=======================

Switch to **Select** mode first by clicking on the |transform-move| :guilabel:`Select/Move` icon or use :kbd:`Alt+S`.

For rectangles and ellipses, you can use the mouse to change the size of the shape by dragging the edges (you cannot drag the corners, though). Alternatively, you can use the :guilabel:`W` (width) and :guilabel:`H` (height) parameter values in the toolbar.

The size of a text field is determined by the font size and weight.

Move an item around by dragging it with the mouse, or by changing the :guilabel:`X` and :guilabel:`Y` coordinate values in the toolbar.

You can restrict movement horizontally and vertically by holding :kbd:`Shift` (only vertical movement is possible) or :kbd:`Shift+Alt` (only horizontal movement possible).

Rotation of an object can be done by entering the desired angle of rotation directly in the :guilabel:`Rotate X`, :guilabel:`Y`, and :guilabel:`Z` parameters. Note that the rotation will always be around the top left corner of the selected object. For certain rotation effects (see the Star Wars opening scrolling title) you need to apply effects to the title clip in the timeline (for example :doc:`/effects_and_filters/video_effects/transform_distort_perspective/corners`, :doc:`/effects_and_filters/video_effects/transform_distort_perspective/shear`, :doc:`Transform</effects_and_filters/video_effects/transform_distort_perspective/transform>`, or :doc:`/effects_and_filters/video_effects/transform_distort_perspective/rotate_3_way`).

The :guilabel:`Zoom` parameter is an easy way to change the size of an object without having to change the :guilabel:`W` and :guilabel:`H` parameters.

Alignment to the project dimensions is possible using the icons in the toolbar:

* |align-horizontal-left| :guilabel:`Align left` or |align-horizontal-right| :guilabel:`Align right` moves the selected object towards the left or right edge stopping at the edges of each of the safety boxes with each click on the icon.
* |align-vertical-top| :guilabel:`Align top` or |align-vertical-bottom| :guilabel:`Align bottom` moves the selected object towards the top or bottom edge stopping at the edges of each of the safety boxes with each click on the icon.
* |align-horizontal-center| :guilabel:`Align center horizontally` or |align-vertical-center| :guilabel:`Align center vertically` centers the selected object on the vertical or horizontal center axis of the outermost box.


----

.. [1] A safe zone refers to a specific area within the video frame where all the important action and titles are guaranteed to be visible. This concept is derived from the early days of television broadcasting when the edges of the TV screen could cut off portions of the video. To avoid this, broadcasters established 'safe' areas where they could be sure that everything would be visible on all television sets.

   There are two types of safe zones: the action safe zone and the title safe zone. The action safe zone is typically 90% of the total frame, ensuring that all the main action will be visible. The title safe zone is a smaller area, usually 80% of the total frame, where all text and graphics should be placed to ensure they are fully visible.

   For social media applications, vastly different safe zones exist and should be taken into account individually, as they are not available as overlays in Kdenlive.