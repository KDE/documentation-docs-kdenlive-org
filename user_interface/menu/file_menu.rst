.. meta::
   :description: Kdenlive Documentation - File Menu
   :keywords: KDE, Kdenlive, file, menu, new, open, save, revert, transcode, clips, quit, documentation, user manual, video editor, open source, free, learn, easy


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
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)


   :license: Creative Commons License SA 4.0


.. _file_menu:

File Menu
=========

.. .. versionchanged:: 25.12 Reorder menu structure and content 

The File Menu contains the normal file operations as well as the option to import and export project files using the OpenTimelineIO format.

.. figure:: /images/user_interface/menu_reference/menu_reference-file_menu-2512.webp
   :align: left
   :scale: 74%
      
   Kdenlive File Menu

- :ref:`file_new`
- :ref:`file_open`
- :ref:`file_open_recent`
- :ref:`file_revert`
- :ref:`file_save`
- :ref:`file_save_as`
- :ref:`file_save_copy`
- :ref:`file_archive_project`
- :ref:`file_render`
- :ref:`file_opentimelineio_import`
- :ref:`file_opentimelineio_export`
- :ref:`file_open_backup_file`
- :ref:`file_project_settings`
- :ref:`file_quit`

.. rst-class:: clear-both


.. _file_new:

New
---

Creates a new Kdenlive project. The default keyboard shortcut is :kbd:`Ctrl+N`.

See :ref:`quickstart`.

The default settings that appear on this feature are defined in :menuselection:`Menu --> Settings --> Configure Kdenlive`. See the chapter :doc:`Configure Kdenlive</getting_started/configuration>` for more details.


.. _file_open:

Open
----

Opens a :file:`.kdenlive` project file. The default keyboard shortcut is :kbd:`Ctrl+O`.

.. container:: clear-both

   .. figure:: /images/user_interface/menu_reference/kdenlive2402_clip-problems.webp
     :align: left
     :width: 300px
  
     Clip Problems


   When opening a project and the needed clips are moved to another place, Kdenlive gives you the possibility to search for the clips needed in the project.

   In the dialog, sort the column as you need it when click on :guilabel:`Type`, :guilabel:`Status`, :guilabel:`Original Path`, :guilabel:`New Path`.

   * :guilabel:`Recreate missing proxies` if the proxies were deleted
   
   **Selected Items**

   * :guilabel:`Search Manually` search manually for the new path

   * :guilabel:`Remove` removes selected clips from re-assigning to a new path (useful when source clips are not available anymore)

   **All Missing Items**

   * :guilabel:`Search Recursively` point to the new path where all project clips are stored and Kdenlive re-assign the clips automatically

   * :guilabel:`Use Placeholders` instead of the original clips  

.. rst-class:: clear-both


.. _file_open_recent:

Open Recent
-----------

Displays a picklist of recently saved files (up to 10) to choose from. Click the :menuselection:`Clear List` choice when you want to start over with a fresh list.


.. _file_revert:

Revert
------

This abandons any changes to the project you have made since last saving and reverts back to the last saved version of the project.


.. _file_save:

Save
----

Saves the current state of the project including the actual layouts. Prompts for a file name if this is the first time the file is being saved. The default keyboard shortcut is :kbd:`Ctrl+S`.


.. _file_save_as:

Save As
-------

Saves the current state of the project in a :file:`.kdenlive` file. Prompts for a file name. Kdenlive then continues with the new project. The default keyboard shortcut is :kbd:`Ctrl+Shift+S`.


.. _file_save_copy:

Save Copy
---------

Saves the current state of the project in a :file:`.kdenlive` file as a copy. Prompts for a file name. Kdenlive returns to the current project.


.. _file_archive_project:

Archive Project
---------------

This function allows you to copy all files required by the project to a specific folder of your choice.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_archive_project.webp
   :align:  left
   :width: 360px
   :figwidth: 360px
   
   Archiving a project

Please refer to the :doc:`archiving</project_and_asset_management/file_management/archiving>` section of this documentation for more details.

.. rst-class:: clear-both


.. _file_render:

Render
------

This function opens the Rendering Dialog with which you can create your video clip. Please refer to the :ref:`Rendering <render>` section of this documentation for more details. The default keyboard shortcut is :kbd:`Ctrl+Return`


.. _file_opentimelineio_import:

OpenTimelineIO import
---------------------

.. .. versionadded:: 25.04, as C++ interface

•	Import a timeline with multiple tracks and clips
•	Support for markers and guides

.. note:: 

   OTIO files do not contain information about rendering, so we get the render resolution from the first video clip.

   OTIO markers on the timeline stack are converted to Kdenlive guides.
   
   OTIO markers on clips are converted to Kdenlive clip markers. Note that clip markers work differently between Kdenlive and OTIO; in Kdenlive they are shared between each instance of the clip, in OTIO the they are unique to each instance of the clip.
   
   If the OTIO marker metadata does not contain the Kdenlive marker type, we pick the Kdenlive guide/marker with the closest color to the OTIO marker.


.. _file_opentimelineio_export:

OpenTimelineIO Export
---------------------

.. .. versionadded:: 25.04, as C++ interface

•	Export a timeline with multiple tracks and clips
•	Support for markers and guides

.. Note::

   Guides are converted to OTIO markers on the timeline stack.

   Clip markers are converted to OTIO markers. Note that clip markers work differently between Kdenlive and OTIO; in Kdenlive they are shared between each instance of the clip, in OTIO they are unique to each instance of the clip.

   The Kdenlive marker types are stored as OTIO metadata for round-tripping files. This allows the guides and clip markers to be properly recreated when importing an OTIO file that was created with Kdenlive. The metadata is stored under the key "kdenlive" to keep it separate from metadata of other applications.


.. _file_open_backup_file:

Open Backup File
----------------

This function opens the list of automatic backups of the project Kdenlive creates.

.. figure:: /images/project_and_asset_management/restore_backup_file.webp
   :align:  left
   :width: 360px
   :figwidth: 360px
   
   Restore a backup file

From here you can select the restore point you want to go back to. More details are available in the :doc:`backup</project_and_asset_management/file_management/backup>` section of this documentation.

.. rst-class:: clear-both


.. _file_project_settings:

Project Settings
----------------

This function opens the Project Settings dialog where you can set all basic properties of the project.

.. figure:: /images/user_interface/menu_reference/project_settings.webp
   :align:  left
   :width: 360px
   
   Project Settings window
   
More details about the various parameters and tabs are available in the :doc:`Project Settings</project_and_asset_management/project_settings/general_settings>` section of the documentation.

.. attention:: Certain things cannot be changed once assets have been added to the project or put on the timeline. Changing certain properties of the project may lead to unwanted results. It is highly recommended to create a copy of the project file before changing project settings.

.. note:: Changing the project folder location does not work properly. In most cases the files are not moved.


.. _file_quit:

Quit
----

Exits **Kdenlive**.

Prompts you to save any unsaved changes. The default keyboard shortcut is :kbd:`Ctrl+Q`.