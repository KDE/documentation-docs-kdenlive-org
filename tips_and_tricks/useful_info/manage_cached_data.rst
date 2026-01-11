.. meta::
   :description: Kdenlive Tips & Tricks - Manage Cached Data
   :keywords: KDE, Kdenlive, tips, tricks, tips & tricks, useful information, project, manage, cache, data, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - TheDiveO
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             
   :license: Creative Commons License SA 4.0


Manage Cached Data
==================

.. .. versionadded:: 16.04.1

Kdenlive 16.04.1 rather quietly introduced a useful new feature to be found in the timeline toolbar: :guilabel:`Manage Cached Data`. It allows you to see how much disk space your projects each eat up. You can then also selectively clean up project-cached data when you do not need it anymore after finishing a project. See also the :doc:`archiving</project_and_asset_management/file_management/archiving>` feature.

.. figure:: /images/tips_and_tricks/manage_cached_data.webp
   :align: left
   :width: 250px

   Manage Cached Data

You reach this new dialog via the timeline toolbar :guilabel:`Preview Render` |preview-render-on| button, then :guilabel:`Manage Cached Data`.

This opens a dialog window with two tabs: Cached data for the :guilabel:`Current Project`, and an overall view on :guilabel:`All Projects`.

.. rst-class:: clear-both

Current Project Tab
-------------------

.. figure:: /images/tips_and_tricks/manage_cached_data_current.webp
   :align: left
   :width: 350px

   Manage cached data for the current project

The :guilabel:`Current Project` tab gives a detail view on your currently loaded project with a nice pie chart. It shows you at a glance how much space individual elements of your project need for caching, such as the timeline preview rendering cache, proxy clips, or audio and video thumbnails.

Here, you can selectively delete cached data by simply clicking on the corresponding :guilabel:`Delete` |edit-delete| buttons.

To remove all cache data for the currently loaded project, clip on the bottom :guilabel:`Delete` |edit-delete| icon.

Finally, when you click on the link at the bottom the folder containing the project cache will open in your file manager.

.. rst-class:: clear-both

All Projects Tab
----------------

.. figure:: /images/tips_and_tricks/manage_cached_data_all.webp
   :align: left
   :width: 350px

   Manage cached data for all projects

The :guilabel:`All Project` tab gives a view on the space used for all your projects, backups and proxy clip data. This helps identifying the "space hoggers" in your file system.

.. rst-class:: clear-both

Select a project in the file manager-like window. The pie chart will show its part of the total data cache. Click on the :guilabel:`Delete Selected Cache` |edit-delete| button to clean the cache for the selected project. The |edit-clear-history| button cleans up unused cache.

The **Backup data** section shows how much space is used by your backups and a link to the backup folder. Clicking the link opens the folder in your default file manager. Clicking on |edit-clear-history| deletes old backups (defined by the time setting below), clicking on |edit-delete| deletes **all** backups.

The **Proxy clip data** section shows how much space is used by proxy clips and a link to the proxy clip folder. Clicking the link opens the folder in your default file manager. Clicking on |edit-clear-history| deletes old proxy files (defined by the time setting below), clicking on |edit-delete| deletes **all** proxy files.

You can specify the number of months you want Kdenlive to retain when executing any of the |edit-clear-history| actions with the :guilabel:`Cleanup will delete data older than` parameter.


.. rubric:: Notes

.. |kdenlive_org| raw:: html

   <a href="https://kdenlive.org/en/project/manage-cached-data/" target="_blank">kdenlive.org</a>

**Sources**
  The original text was submitted by user *TheDiveO* to the now defunct kdenlive.org blog. For this documentation it has been lifted from |kdenlive_org|, updated and adapted to match the overall style.