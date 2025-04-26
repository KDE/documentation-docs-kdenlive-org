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

The File Menu contains the normal file operations as well as the option to import and export project files using the OpenTimelineIO format.

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
     :alt: kdenlive2402_clip-problems
  
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

Open Recent
-----------

Displays a picklist of recently saved files (up to 10) to choose from. Click the :menuselection:`Clear List` choice when you want to start over with a fresh list.

Save
----

Saves the current state of the project. Prompts for a file name if this is the first time the file is being saved. The default keyboard shortcut is :kbd:`Ctrl+S`.

Save As
-------

Saves the current state of the project in a :file:`.kdenlive` file. Prompts for a file name. Kdenlive then continues with the new project. The default keyboard shortcut is :kbd:`Ctrl+Shift+S`.

Save Copy
---------

Saves the current state of the project in a :file:`.kdenlive` file as a copy. Prompts for a file name. Kdenlive returns to the current project.

Revert
------

This abandons any changes to the project you have made since last saving and reverts back to the last saved version of the project.


Transcode Clips
---------------

.. container:: clear-both

   .. figure:: /images/user_interface/menu_reference/kdenlive2304_transcode_2.webp
     :align: left
     :width: 300px
     :alt: kdenlive2304_transcode_2
  
     Transcode clips


   Use this to convert a video or audio clip from one codec/format to another.

   Choose one source file or multiple source files and a profile that represents the desired destination codec/format. Optionally change the destination path and file name and hit :guilabel:`Start`. Otherwise, hit :guilabel:`Abort` to close the windows.

   Transcoding a clip should be faster than loading the clip into the timeline and re-encoding it into a different format.

   * :guilabel:`Add clip to project` controls if after the conversion, the new clip is added to the :doc:`Project Bin </project_and_asset_management/project_bin>`.

   * :guilabel:`Close after encode` Uncheck this checkbox if there is the need to convert to another format after the conversion.

.. rst-class:: clear-both


.. _file_opentimeline-export:
.. .. versionadded:: 25.04, as C++ interface

OpenTimelineIO Export
---------------------

•	Export a timeline with multiple tracks and clips
•	Support for markers and guides

.. Note::

   Guides are converted to OTIO markers on the timeline stack.

   Clip markers are converted to OTIO markers. Note that clip markers work differently between Kdenlive and OTIO; in Kdenlive they are shared between each instance of the clip, in OTIO the they are unique to each instance of the clip.

   The Kdenlive marker types are stored as OTIO metadata for round-tripping files. This allows the guides and clip markers to be properly recreated when importing an OTIO file that was created with Kdenlive. The metadata is stored under the key "kdenlive" to keep it separate from metadata of other applications.


.. _file_opentimeline-import:
.. .. versionadded:: 25.04, as C++ interface

OpenTimelineIO import
---------------------

•	Import a timeline with multiple tracks and clips
•	Support for markers and guides

.. note:: 

   OTIO files do not contain information about rendering, so we get the render resolution from the first video clip.

   OTIO markers on the timeline stack are converted to Kdenlive guides.
   
   OTIO markers on clips are converted to Kdenlive clip markers. Note that clip markers work differently between Kdenlive and OTIO; in Kdenlive they are shared between each instance of the clip, in OTIO the they are unique to each instance of the clip.
   
   If the OTIO marker metadata does not contain the Kdenlive marker type, we pick the Kdenlive guide/marker with the closest color to the OTIO marker.


Quit
----

Exits **Kdenlive**.

Prompts you to save any unsaved changes. The default keyboard shortcut is :kbd:`Ctrl+Q`.