.. meta::
   :description: Kdenlive Documentation - File Management - Archiving
   :keywords: KDE, Kdenlive, project bin, working, file, management, archive, archiving, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Neverendingo (https://userbase.kde.org/User:Neverendingo)
             - Claus Christensen
             - Yuri Chornoivan
             - Jean-Baptiste Mardelle <jb@kdenlive.org>
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Tenzen (https://userbase.kde.org/User:Tenzen)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0



Archiving
=========

The Archiving feature (:menuselection:`Menu --> File --> Archive Project`, see :ref:`file_archive_project`) in **Kdenlive** allows you to copy all files required by the project (images, video clips, project files,...) to a folder, and alternatively to compress the whole into a :file:`tar.gz` or a :file:`zip` file.

.. figure:: /images/project_and_asset_management/archive_project.webp
   :width: 360px
   :figwidth: 360px
   :align: left

   Archiving the project

Archiving changes the project file to update the path of video clips to the archived versions.

This can be useful if you finished working on a project and want to keep a copy of it, or if you want to move a project from one computer to another.

.. container:: clear-both

   .. figure:: /images/project_and_asset_management/open_archived_project.webp
      :width: 360px
      :figwidth: 360px
      :align: left
   
   The resulting tar.gz or zip file can be opened directly in **Kdenlive** with :menuselection:`Menu --> File --> Open`, then switch file ending to :guilabel:`Archived Project`.

.. container:: clear-both

   .. figure:: /images/project_and_asset_management/open_archived_project_target.webp
      :width: 360px
      :figwidth: 360px
      :align: left
   
   Kdenlive will extract the archive to a location you specify before opening it.

.. container:: clear-both

   .. figure:: /images/project_and_asset_management/open_project_missing_files.webp
      :width: 360px
      :figwidth: 360px
      :align: left
   
   If you have archived the project with the option :guilabel:`Archive only timeline clips`, **Kdenlive** will ask what it should do with the not archived clips.
