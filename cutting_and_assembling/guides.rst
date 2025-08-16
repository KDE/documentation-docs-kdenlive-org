.. meta::
   :description: Set guides in Kdenlive video editor
   :keywords: KDE, Kdenlive, set guides, DVD, youtube, editing, timeline, documentation, user manual, video editor, open source, free, learn, easy


.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Gallaecio (https://userbase.kde.org/User:Gallaecio)
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Dbolton (https://userbase.kde.org/User:Dbolton)
             - Jack (https://userbase.kde.org/User:Jack)
             - Eugen Mohr

   :license: Creative Commons License SA 4.0



.. _guides:

Guides
======



Guides in the picture below are the purple flags. Not to be confused with :ref:`markers` (green in the picture below). Guides are static on the timeline and can be either stationary or moved when clips are moved around. Markers are inside the clips and move with the clips.


.. figure:: /images/Kdenlive_Markers_and_guides_crop.png
   :align: left
   

Guides can be used to define regions for rendering. See :ref:`rendering-guides`.


Guides can also be used as chapters for DVD videos. See :ref:`rendering-guides`.


.. _add_guides:

3 ways to add guides
--------------------

Following procedures add a guide at the timeline playhead position:

* **Menu**

  * :menuselection:`Timeline --> Guides --> Add/Remove Guide`
  * Right click on :ref:`timeline ruler<timeline_ruler>` and choose in the menu :guilabel:`Add/Remove Guide`
  * Right click in the timeline and choose :guilabel:`Add/Remove Guide`

.. .. versionadded:: 24.08
..    Insert guides in 10 different categories using NumPad 

* **Keyboard**

  * :kbd:`G` adds a guide.
  * :kbd:`1` - :kbd:`0` (number 1 to 0 on the NumPad)

* **Mouse**

  .. figure:: /images/Kdenlive_add_guide_double-click.png

  * Double-click on top of the :ref:`timeline ruler<timeline_ruler>` and the guide gets added were you have clicked


.. _timeline_ruler_right-click_menu:

Timeline ruler right click menu
-------------------------------

.. figure:: /images/Kdenlive_Add_guide.png
   :align: left
   

.. rst-class:: clear-both

:guilabel:`Add/Remove Guide`

:guilabel:`Edit Guide`: See :ref:`move_edit_guides`

.. .. versionadded:: 21.08
   
:guilabel:`Guides Locked`: See :ref:`move_edit_guides`  


:guilabel:`Go To Guide...`. Select a guide to which the playhead should jump.

.. .. versionadded:: 22.04

:guilabel:`Set Zone In/Out`: See also :doc:`/tips_and_tricks/tips_and_tricks/timeline_preview_rendering`.

:guilabel:`Add Project Notes`: See :doc:`/project_and_asset_management/project_notes`

.. .. versionadded:: 20.12.

:guilabel:`Add Subtitle`: See Subtitle


.. _managing_guides:

Managing categories and guides
------------------------------

.. .. versionadded:: 22.12


.. _categories:

Categories
~~~~~~~~~~

When starting a new project the categories for the project are pulled in from :guilabel:`Guides and Markers Categories` in setting :doc:`Configure Colors and Guides</getting_started/configure_kdenlive/configuration_colors+guides>`. 

.. figure:: /images/Kdenlive_project_specific_categories.png
   :width: 350px
   
Project specific categories can be added, edited and deleted in :menuselection:`Project --> Project Settings --> Guides`

.. figure:: /images/Kdenlive_delete_category.png
   :width: 250px
   
Deleting a category were guides are assigned, Kdenlive ask if you really want to delete it or if you want to reassign the guide to another category. 


.. _guide_view:

Guides View
~~~~~~~~~~~

.. .. versionchanged:: 25.08
   add a button to show all project clip markers in the list
   Add option to show thumbnails in markers list dialog 

.. figure:: /images/guides_view_2508.webp
   
:menuselection:`View --> Guides` opens the guides window were you can managing your guides.  


:1: Shows the selected object: Clip-Name, Sequence-Name 

:2: Search guides/markers. If you enter `2` in this example it shows only `guide2` / `marker2` in the list and in the timeline/on the clip monitor.

:3: Show only the chosen categories in the list and in the timeline/clip monitor.

:4: Show markers for all clips in the project

:5: Sort by categories, time, or comment, and change sort order (ascending/descending).

:6: Click on a guide/marker or :kbd:`arrow-up arrow-down` will select it and the playhead jumps to this guide/marker in the timeline/clip monitor. Multi-selection: holding down :kbd:`Shift` or :kbd:`Control` to select single guides. :kbd:`Control + A` select all guides/markers. Double-click or :kbd:`F2` on a guide/marker opens the :ref:`edit guide window <move_edit_guides>`/:ref:`edit marker window <move_edit_marker>`.

:7: Add a guide/marker. Only here you have the possibility to add multiple guides/markers with an interval.

:8: Edit a selected guide/marker. The same as double-clicking a guide/marker under point 4, or guides in the :ref:`timeline ruler<timeline_ruler>`.

:9: Delete the selected guide(s)/marker(s).

:10: Set the default category for new guides/markers.

:11: Guides only: :ref:`Locks guide <move_edit_guides>`. Locked when the background is light gray (as shown on the screenshot).

:12: Refresh all thumbnails when thumbnails are enabled

:13: Enable/disable thumbnails. Import/:ref:`export guides/marker <export_guides>` or configure the :ref:`project categories <categories>`.


You can put a comment in the guide/marker and make the comment display by choosing :ref:`editing` in the :menuselection:`Timeline` menu or by clicking on the :ref:`editing` button.


.. _export_guides:

Export guides as chapters description
-------------------------------------

.. .. versionadded:: 22.08

.. .. versionchanged:: 22.12

Guides can mark chapters or different sections of a video while editing. Uploading edited videos to platforms like YouTube, the guides can be exported as chapter marks that are supported by YouTube. This can be done by :guilabel:`Copy to Clipboard` and paste then into YouTube.

Right click in the :ref:`timeline ruler <timeline_ruler>` and choose :guilabel:`Export Guides` or :menuselection:`Timeline -> Guides -> Export Guides` or :menuselection:`View --> Guides --> Export`. Then the window `Export guides as chapters description` appears.

.. figure:: /images/Kdenlive_export_guides_22-12.png
   
:guilabel:`Marker Type`: Choose one of the guide types to mark chapters and use other types to do other things.

:guilabel:`Save As`: Text (for Youtube) or as JSON data file which can be re-imported.

:guilabel:`Offset`: This adds the ability to set a general offset (hh:mm:ss:ff) to each guide.

:guilabel:`Format`: This defines how the chapter marks are exported. When using the 2 default format strings (as shown on the picture), Kdenlive check if the chapter marker matches YouTube's guideline, and display a notice if it doesn't match.

:guilabel:`i`: Shows all possible export strings. Select the string you want and Kdenlive adds it to the :guilabel:`Format` for export. Add spaces between the strings as needed. 

{{timecode}} adds guide position in HH:MM.SS (default)

{{comment}} adds the guide text (default)

{{frame}} adds the frame number of each guide

{{index}} adds guide number

{{nexttimecode}} adds next guide position in HH:MM.SS

{{realtimecode}} adds guide position in HH:MM:SS:FF

:guilabel:`Reset`: Resets the settings to the default: {{timecode}} {{comment}}

:guilabel:`Exported`: Shows what get exported. To change the guide text you have to edit the guide in the timeline.

:guilabel:`Copy to Clipboard`: Copy the data viewed in :guilabel:`Exported` into the clipboard to use it in other applications (Youtube).

The warning in the blue box only show up if one of the 3 points are not fulfilled.


.. _move_edit_guides:

Move and edit guides
--------------------

Guides can be moved by click on a guides text in the timeline and drag it to the desired position.

.. figure:: /images/Kdenlive_edit_guide.png
   
Guides can be moved by changing the :guilabel:`Position` in the edit window.

Double-click on a guide text in the timeline ruler opens the edit window (beside the possibility in :ref:`guide_view`).

:guilabel:`Comment` text and :guilabel:`Category` can be changed in the edit window.


Move Guides with Spacer Tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

.. .. versionadded:: 21.08.0

Easily moves guides along with clips using the spacer tool by using the new :menuselection:`Guides Locked` option. When locked the guides stay in place. When unlocked the guides move with the clip.


.. figure:: /images/guidemove.gif
   :align: left
   