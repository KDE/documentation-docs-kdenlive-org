.. meta::
   :description: Kdenlive Documentation - Folder Structure
   :keywords: KDE, Kdenlive, project, working, file, management, folder structure, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Gallaecio (https://userbase.kde.org/User:Gallaecio)
             - Simon Eugster <simon.eu@gmail.com>
             - Jean-Baptiste Mardelle <jb@kdenlive.org>
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jack (https://userbase.kde.org/User:Jack)
             - Roger (https://userbase.kde.org/User:Roger)
             - Carl Schwan <carl@carlschwan.eu>
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0

  
.. |artgrid| raw:: html

   <a href="https://artgrid.io/insights/how-to-organize-your-video-files/" target="_blank">artgrid</a>

.. |owc| raw:: html

   <a href="https://www.owc.com/blog/how-to-organize-your-project-files-and-folders-for-faster-editing-in-premiere-pro" target="_blank">owc</a>

.. |awesomecontentcreator| raw:: html

   <a href="https://awesomecontentcreator.com/best-way-to-organize-video-files-for-editing/" target="_blank">awesomecontentcreator</a>


Folder Structure
================

The standard file structure for project related files for caching purposes is as follows:

* :file:`<project_folder>/proxy/` for the :doc:`clips</project_and_asset_management/project_bin/clips>` that have been generated

* :file:`<project_folder>/thumbs/` for thumbnails of all used clips

* :file:`<project_folder>/titles/` default location for the :doc:`title clips</titles_and_graphics/titles/titles>` saved outside the project file

* :file:`<project_folder>/.backup/` for your project's automatic :doc:`backups</project_and_asset_management/file_management/backup>`. These directories can be deleted if not required anymore (for example for saving space on the harddrive). **Kdenlive** will create backup files again when you load the project the next time but only from that point forward.


.. warning::
  The :file:`/titles/` directory is the default directory for saved :file:`.kdenlivetitle` title files. Make sure that you did not save any important files in there before deleting it.

.. hint::
  As already pointed out in the :ref:`quickstart`, it is recommended to use a different folder in your file system for each project.

You define the location of the project folder in the :doc:`Project Settings </project_and_asset_management/project_settings/general_settings>`.

Source clips can be located anywhere. Still, here are some thoughts about their location:

* Material (images, clips, audio) that is used for one project only can be put into a subdirectory of the project folder as well. This keeps all important files together, and searching for the files takes less time.

* Material that is used by multiple projects is convenient when kept together. Think about your video collection the same way as your photo collection.

You can find some examples on |artgrid|, |owc|, and |awesomecontentcreator|.

.. tip:: 
   You can check the file usage for your project via the :doc:`project files tab</project_and_asset_management/project_settings/tab_project_files>` and the :doc:`cached data tab</project_and_asset_management/project_settings/tab_cache_data>` in the :doc:`project settings</project_and_asset_management/project_settings>`.