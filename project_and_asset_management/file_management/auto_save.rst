.. meta::
   :description: Kdenlive Documentation - File Management - Auto Saves
   :keywords: KDE, Kdenlive, project bin, working, file, management, auto save, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Julius Künzel <jk.kdedev@smartlab.uber.space 
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0



Auto Save
=========

.. .. versionchanged::25.08


.. figure:: /images/project_and_asset_management/file-management_auto-save_2508.webp
   :width: 100px
   :figwidth: 500px
   
   Green square top right: Auto save is ongoing

Backup files (auto saves) are generated according to the settings in :menuselection:`Menu --> Settings --> Configure Kdenlive -->` :doc:`Misc</getting_started/configure_kdenlive/configuration_misc>` (default is every 60 seconds and/or 25 operations). This is where you can switch it on or off. 

Autosaves are offered the first time after you open the project again in case the autosave is newer than the last saved project version.

Autosaves are stored in stale files, not in normal :file:`.kdenlive` files.
