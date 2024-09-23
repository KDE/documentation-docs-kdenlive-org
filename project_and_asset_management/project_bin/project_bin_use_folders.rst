.. meta::
   :description: Kdenlive Documentation - Using the Project Bin - Folders
   :keywords: KDE, Kdenlive, project bin, folder, using, documentation, user manual, video editor, open source, free, learn, easy

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
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |rename| replace:: |document-edit|\ :guilabel:`Rename`

.. |open_new_bin| replace:: |document-open|\ :guilabel:`Open Current Folder in New Bin`

.. |target_seq| replace:: |favorite|\ :guilabel:`Default Target Folder for Sequences`

.. |target_audio| replace:: |favorite|\ :guilabel:`Default Target Folder for Audio Captures`

.. |create_folder| replace:: |folder-new|\ :guilabel:`Create Folder`

.. |delete_folder| replace:: |edit-delete|\ :guilabel:`Delete Folder`


.. ====================================================================================================
   This file is being .. include(d):: in project_bin_use.rst and the chapter title designation follows the structure of the parent file. Hence the use of --- and ~~~ as chapter designation
   ====================================================================================================

.. _project_bin_use_folders:

Folders
-------

Folders help keeping the Project Bin organized, structured, and easy to navigate. Folders can be nested and turned into :doc:`individual bins <project_bin_use_multiple_bins>`.

.. container:: clear-both

   .. figure:: /images/project_and_asset_management/project_bin_folder_create.webp
      :width: 334px
      :figwidth: 334px
      :align: left
      :alt: project_bin_folder_create

      Creating folders in the project bin
      
   You create a folder by clicking the |folder-new|\ :guilabel:`Create Folder` icon in the project bin toolbar.

   Alternatively, right-click on empty space in the project bin and select |folder-new|\ :guilabel:`Create Folder`.

   If you want to create a folder below an existing one, select that folder first.

   You can delete a folder by selecting the folder and clicking on the |edit-delete|\ :guilabel:`Delete Folder` icon, or by right-click on the folder and selecting |edit-delete|\ :guilabel:`Delete Folder`.

.. rst-class:: clear-both

.. rubric:: Folder Right-Click Menu

Right-click on a folder opens this context menu:

.. image:: /images/project_and_asset_management/project_bin_folder_options.webp
   :width: 351px

|rename|:
   Renames the folder. Keyboard shortcut is :kbd:`F2`. You can also just double-click the folder name in the bin

|open_new_bin|:
   Creates a new bin from the folder

|target_seq|:
   Check this if you want this folder to be target for new sequences

|target_audio|:
   Select this if you want this folder to receive all audio captures

|create_folder|:
   Creates a new folder. If nothing has been selected in the bin, a new folder is created at the bin level. If a folder has been selected, a new folder underneath the selected one is created.

|delete_folder|:
   Deletes the selected folder.

.. Note:: 
   Deleting an empty folder happens immediately without any are-you-sure? dialog. Only if there is content will there be a warning dialog window that you need to confirm or cancel.