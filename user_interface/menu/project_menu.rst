.. meta::
   :description: Project menu in Kdenlive video editor
   :keywords: KDE, Kdenlive, project, clip, folder, color, image, sequence, title, template, animation, subtitle, render, clean, generators, documentation, user manual, video editor, open source, free, learn, easy


.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jack (https://userbase.kde.org/User:Jack)
             - Carl Schwan <carl@carlschwan.eu>
             - Jack (https://userbase.kde.org/User:Jack)
             - Roger (https://userbase.kde.org/User:Roger)
             - Jack (https://userbase.kde.org/User:Jack
             - Yuri Chornoivan
             - Annew (https://userbase.kde.org/User:Annew)
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Eugen Mohr
             - Bernd Jordan


   :license: Creative Commons License SA 4.0

.. |glaxnimate| raw:: html

   <a href="https://glaxnimate.mattbas.org/" target="_blank">Glaxnimate</a>
   

.. _project_menu:

Project Menu
============

The Project Menu is for adding assets (audio, video, images, other clips) to and managing various aspects of your project.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_project_menu.webp
  :align: left
  :alt: kdenlive2304_project_menu
  
  Kdenlive Project Menu
  
Most of the function of the Project Menu are also available from within the Project Bin widget.

Use the navigation to the left to go to the various items.

.. rst-class:: clear-both


Add Clip or Folder
------------------

This function allows you to add video, audio and (single) image files from your file system. It is also available from the menu bar of the Project Bin or by right-click or double-click on empty space in the Project Bin.

.. Currently, the following formats are supported: <list of formats>

.. figure:: /images/user_interface/menu_reference/kdenlive2304_add_clip_window.webp
   :align:  left
   :height: 250px
   :alt: kdenlive2304_add_clip_window
   
   Adding a clip or entire folder
   
A more detailed explanation of this function is available in the :ref:`clips` section of this documentation.

.. rst-class:: clear-both


Add Color Clip
--------------

This function allows you to create a clip with a single color.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_add_color_clip_window.webp
   :align:  left
   :height: 250px
   :alt: kdenlive2304_add_color_clip_window
   
   Adding a Color Clip

It is also available from the menu bar of the Project Bin and by right-clicking on empty space in the Project Bin.

For more details refer to the :ref:`Color Clips <add_color_clip>` section of this documentation.

.. rst-class:: clear-both


Add Image Sequence
------------------

This function adds a series of still images as one clip to the Project Bin. 

.. figure:: /images/user_interface/menu_reference/kdenlive2304_add_image_sequence_window.webp
   :align:  left
   :height: 250px
   :alt: kdenlive2304_add_image_sequence_window
   
   Adding an Image Sequence

It is also available from the menu bar of the Project Bin and by right-click on empty space in the Project Bin.

For more details refer to the :ref:`Image Sequence <add_slideshow_clip>` section of this documentation.

.. rst-class:: clear-both


Add Title Clip
--------------

This function adds a Title Clip to the Project Bin. First, it opens the Titler app where you create the Title Clip. Once saved it shows up in the Project Bin.

A more detailed documentation of the Titler app is available in the :ref:`titles` section of the documentation.

This function is also available from the menu bar of the Project Bin and by right-click on empty space in the Project Bin.


Add Template Title
------------------

This function creates a Title Clip based on a Template Title.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_add_template_title_window.webp
   :align:  left
   :height: 250px
   :alt: kdenlive2304_add_template_title_window
   
   Adding a Template Title
   
You build the template in the Titler application like a normal Title Clip. The key is the placeholder '%s'. It will be replaced by the text you enter here.

This function is also available from the menu bar of the Project Bin and by right-click on empty space in the Project Bin.

Please refer to the :ref:`titles` section of this documentation for more details about Titles and Templates.

.. rst-class:: clear-both


Create Animation
----------------

This function creates an animation clip in the Project Bin and calls |glaxnimate|, the application to actually create the animation.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_create_animation_window.webp
   :align:  left
   :width: 430px
   :alt: kdenlive2304_create_animation_window
   
   Creating an animation

Glaxnimate has to be installed on your computer and the path to it must be set in :menuselection:`Settings --> Configure Kdenlive --> Environment --> Default Apps`.

This function is also available from the menu bar of the Project Bin and by right-click on empty space in the Project Bin.

.. rst-class:: clear-both


Add Sequence
------------

This function creates a new Sequence in the Project Bin.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_add_sequence_window.webp
   :align:  left
   :height: 250px
   :alt: kdenlive2304_add_sequence_window
   
   Add a new Sequence

Sequences were introduced with version 23.04 and are needed for nested timelines where you can edit clips separately and independently.

This function is also available from the menu bar of the Project Bin and by right-click on empty space in the Project Bin.

Please refer to the :ref:`sequence` section of this documentation for more details.

.. rst-class:: clear-both


.. _create_folder:

Create Folder
-------------

This function creates a new folder in the Project Bin.

The folder is a virtual folder and very useful to keep your assets organized. You can also create separate bins from each folder (see the :ref:`Create additional project bins <multibin>` section)

This function is also available from the menu bar of the Project Bin and by right-click on empty space in the Project Bin.

More details are available in the :ref:`Create Folder <project_tree>` section of this documentation.

.. tip:: A good way to keep your Project Bin neat and tidy is to have bin folders or separate bins for your footage (main video), B-roll, audio, still images, SFX and VFX, titles and so on.


.. _generators:

Generators
----------

This function allows to create generated clips in your Project Bin for

* Counter

* Color Bars (old TV test display)

* White Noise

This function is also available from the menu bar of the Project Bin and by right-click on empty space in the Project Bin. See the :ref:`clips` section in this documentation for more details.


Subtitles
---------

This function opens a flyout to switch the Subtitle Editor on or off and to offer additional options for dealing with subtitles.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_subtitles.webp
   :align:  left
   :height: 250px
   :alt: kdenlive2304_subtitles
   
   Adding subtitles

Please refer to the :ref:`subtitle` section of this documentation.

.. rst-class:: clear-both


View Mode
---------

This function allows to switch between the various views available for the Project Bin:

* Tree View - When enabled shows the Project Bin items as a hierarchy. Each item in the list can have several subitems (shown individually indented).

* Icon View - When enabled shows the Project Bin items in a flat grid of items shown by their thumbnails with captions


.. _clean_project:

Clean Project
-------------

This function can be used to remove any unused clips from the Project Bin.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_clean_project.webp
   :align:  left
   :width: 412px
   :alt: kdenlive2304_clean_project
   
   Clean up the project

You can undo this action with :menuselection:`Edit --> Undo`, through the :ref:`undo_history` or with the default keyboard shortcut :kbd:`Ctrl+Z`.

.. rst-class:: clear-both

.. note:: This is different from the :ref:`Project Settings <project_settings>` dialog button :guilabel:`Delete Files` in the Project Files tab which deletes files not used by the project from the hard drive.


Render
------

This function opens the Rendering Dialog with which you can create your video clip. Please refer to the :ref:`Rendering <render>` section of this documentation for more details.


Adjust Profile to Current Clip
------------------------------

This function offers up a suggested Project Profile that would be most suitable for the currently selected clip in the Project Bin.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_adjust_profile.webp
   :align:  left
   :width: 480px
   :alt: kdenlive2304_adjust_profile
   
   Adjusting the project profile to the clip properties
   
.. rst-class:: clear-both


Archive Project
---------------

This function allows you to copy all files required by the project to a specific folder of your choice.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_archive_project.webp
   :align:  left
   :height: 250px
   :alt: kdenlive2304_archive_project
   
   Archiving a project

Please refer to the :ref:`archiving` section of this documentation for more details.

.. rst-class:: clear-both


Open Backup File
----------------

This function opens the list of automatic backups of the project Kdenlive creates.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_open_backup_file.webp
   :align:  left
   :height: 250px
   :alt: kdenlive2304_open_backup_file
   
   Restore a backup file

From here you can select the restore point you want to go back to. More details are available in the :ref:`backup` section of this documentation.

.. rst-class:: clear-both


Project Settings
----------------

This function opens the Project Settings dialog where you can set all basic properties of the project.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_project_settings.webp
   :align:  left
   :width: 450px
   :alt: kdenlive2304_project_settings
   
   Project Settings window
   
More details about the various parameters and tabs are available in the :ref:`project_settings` section of the documentation.

.. attention:: Certain things cannot be changed once assets have been added to the project or put on the timeline. Changing certain properties of the project may lead to unwanted results. It is highly recommended to create a copy of the project file before changing project settings.

.. note:: Changing the project folder location does not work properly. In most cases the files are not moved.


.. .. toctree::
   :hidden:
   :glob:

   project_menu/*
