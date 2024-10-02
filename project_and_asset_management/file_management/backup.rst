.. meta::
   :description: Kdenlive Documentation - File Management - Backups
   :keywords: KDE, Kdenlive, project bin, working, file, management, backup, restore, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Gallaecio (https://userbase.kde.org/User:Gallaecio)
             - Jean-Baptiste Mardelle <jb@kdenlive.org>
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0



Backup
======

A backup file is automatically created each time you save your project. To restore a backup file, go to :menuselection:`Menu > Project > Open Backup File`. The **Restore Backup File** dialog window will show you a list of all the backup files for your current project.

.. container:: clear-both

   .. figure:: /images/project_and_asset_management/restore_backup_file.webp
      :width: 360px
      :figwidth: 360px
      :align: left
      :alt: restore_backup_file

      Restoring a backup file

  In case something went wrong (corrupted project file, unwanted change, ...), you can now restore a previous version of the file using this feature. Just select the version you want and click |document-open|\ :guilabel:`Open`.

.. rst-class:: clear-both

**Kdenlive** keeps up to 20 versions of your project file in the last hour, 20 versions from the current day, 20 versions in the last 7 days and 20 older versions, which should be sufficient to recover from any problem.

.. seealso:: 
  :doc:`/project_and_asset_management/file_management/project_files`
