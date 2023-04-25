.. meta::
   :description: How to work with the project bin in Kdenlive video editor
   :keywords: KDE, Kdenlive, project bin, working, documentation, user manual, video editor, open source, free, learn, easy


.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jack (https://userbase.kde.org/User:Jack)
             - Roger (https://userbase.kde.org/User:Roger)
             - Carl Schwan <carl@carlschwan.eu>
             - Eugen Mohr
             - Smolyaninov (https://userbase.kde.org/User:Smolyaninov)
             - Tenzen (https://userbase.kde.org/User:Tenzen)

   :license: Creative Commons License SA 4.0

.. toctree::
   :maxdepth: 1
      

.. _project_tree:

The Project Bin
===============


The Project Bin is a view in Kdenlive which lists all the clips that are associated with the project. In earlier versions of Kdenlive this view was known as the Project Tree. The list following the example describes the options represented by the icons on the toolbar (identified by the numbers in the screenshots).


.. figure:: /images/Kdenlive_Project_bin_23_04.png
   :align: left
   :alt: Kdenlive_Project_bin_23_04
  
   23.04+

:ref:`1, 2, 3, 10 Load, Create <project_bin_load_create>`

:ref:`4 Delete <project_bin_delete>`

:ref:`5 Tagging <project_bin_tagging>`

:ref:`6 Option <project_bin_option>`

:ref:`7 Filter <project_bin_filter>`

:ref:`8 Search <project_bin_search>`

:ref:`9 Clip used <project_bin_clip_used>`

:ref:`11 Clip in Timeline <project_bin_in_timeline>`

:ref:`12 Sequence Folder <project_bin_sequence_folder>`


.. rst-class:: clear-both


.. _project_bin_load_create:

**1, 10**. Opens the Project Folder in a window for selecting video and audio clips to be added to the bin (1). Or double click on free space (10).  


**2, 10**. Displays a drop down list for adding other clip types to the Project Bin (2). Or right-click on free space (10). 


.. figure:: /images/Kdenlive_Add_other_clip_types_23-04.png
   :align: left
   :alt: Kdenlive_Add_other_clip_types
  
   Options from Menu under Icon 2


* :ref:`Add Clip or Folder <add_clip>`


* :ref:`Add Color Clip <add_color_clip>`


* :ref:`Add Image Clip <add_slideshow_clip>`


* :ref:`Add Title Clip <titles>`


* :ref:`Add Template Title Clip <titles>`


* :ref:`Create Animation... <add_animation>` (*new in version 22.08*)


* :ref:`Add Sequence... <menu_add_sequence>` (*new in version 23.04*)
   

* :ref:`online_resources`


* :ref:`generators`

.. rst-class:: clear-both

**3, 10**. Allows you to add folders to the Project Bin (3). Or right-click on free space (10) and select :guilabel:`Create Folder` to add folder. These are not actual file system folders but virtual folders to help you organize large Project Bins. See :ref:`create_folder`


.. _project_bin_delete:

**4**. Deletes the selected clip from the Project Bin (but not from the file system).


.. _project_bin_tagging:

**5** Color tagging.

.. versionadded:: 20.04.0

.. figure:: /images/tags.gif
   :width: 350px
   :alt: tags
   
   Menu under Icon 5

Edit tags: double click a tag for changing the description.

.. versionadded:: 22.08

.. figure:: /images/tags_change.png
   :width: 350px
   :alt: changing tags

You can: add, delete and reordering tags.

Reordering tags: grab a tag and drag it to the desired place in the list.


.. _project_bin_option:

**6**. Brings up additional options shown below for customizing the Project Bin view .


.. figure:: /images/kdenlive_project_bin2.png
   :width: 350px
   :alt: kdenlive_project_bin2
   
   Menu under Icon 6
 

.. _project_bin_filter: 

**7** Filter by categories

.. versionchanged:: 23.1


.. figure:: /images/filter.gif
   :width: 350px
   :alt: filter
   

.. figure:: /images/project_bin_filter_23-04.png
   :scale: 75%
   :alt: project bin filter
  
   Menu under Icon 7

The filter works in an OR way between objects of the same category, and in an AND way between different categories. 

Example: 

-	It shows clips which has red OR yellow tags.

-	It shows clips which has a red tag AND has 1 star AND is an unused clip AND is an A/V clip

**7a** Filter on/off

.. figure:: /images/project_bin_filter_toggle.png
   :scale: 100%
   :alt: project bin filter

   Menu under Icon 7a

Clicking on the filter button turns on or off the filter.


.. _project_bin_search:

**8**. A search box to display all the clips in the bin whose filenames or titles contain the entered text.


.. _project_bin_clip_used:

**9**.  Number of times this clip is used in the project timeline. It counts for video and audio, so an AV-Clip counts with 2 when it's one time in the timeline.


.. _project_bin_in_timeline:

**11**. The blue audio and video icon indicates that both, audio and video is in the timeline. You can drag&drop either the audio or the video part into the timeline by grab just the audio or the video icon.


.. _project_bin_sequence_folder:

.. versionadded:: 23.04

**12**. The folder Sequences is the default folder where sequences get added. More about sequences see :ref:`here <sequence>`.   


Clips can be dragged from the Project Bin to the :ref:`timeline`.

.. rst-class:: clear-both

.. _multibin:

Create additional project bins
------------------------------

.. versionadded:: 21.12

.. image:: /images/multibin.gif
   :alt: multibin 

You can create various bins from :ref:`folders <create_folder>` you have created. Right-click the folder name and choose :guilabel:`Open in new bin` 

Closing the extra bins either by pressing :kbd:`CTRL + w` or on the bin you want to close click on |application-menu| and choose :guilabel:`Close` .

.. _clip_right-click:

Clip - Right-Click Menu
-----------------------

The images below show the menu items available when you right-click a clip in the Project Bin.


.. image:: /images/Kdenlive_Project_bin_right_click_menu.png
   :width: 300px
   :alt: Kdenlive_Project_bin_right_click_menu


The menu items which appear when you right-click on an item in the Project Bin are also available from the :ref:`clip_menu`.

* :ref:`extract_audio`

* :ref:`transcode`

* :menuselection:`Clip Jobs`

   * :ref:`stabilize`

   * :ref:`automaticscenesplit`

   * :ref:`duplicate_clip_with_speed_change`

* :ref:`clip_in_timeline`

* :ref:`locate_clip`

* :ref:`reload_clip`

* :ref:`replace_clip`

* :ref:`duplicate_clip`

* :ref:`clips`

* :ref:`clips`

* :ref:`edit_clip`

* :ref:`rename_clip`

* :ref:`delete_clip`

If you want to reverse a clip you can do it via  :ref:`speed` or by :ref:`duplicate_clip_with_speed_change`
