.. meta::
   :description: Kdenlive Documentation - The Media Browser
   :keywords: KDE, Kdenlive, media browser, add clips, project bin, asset, management, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0



Media Browser
=============

.. .. versionadded:: 21.04.0
  
The Media Browser allows you to easily navigate through your file system. You can enable it from the :doc:`View</user_interface/menu/view_menu>` menu.

The main advantage of using the Media Browser is the ability to drag clips not only to the project bin but also directly into the timeline. Make sure that when you drop a clip to the timeline there is enough space and a valid video/audio track combination available.

.. rubric:: Layout and Controls

.. container:: 

   .. figure:: /images/project_and_asset_management/project_bin_clips_add.webp
   
      The Media Browser layout and controls

.. rst-class:: clear-both


.. list-table::
   :class: table-wrap

   * - **1**
     - |go-previous|\ :guilabel:`Go back` goes back in your navigation or browsing history
   * - 
     - |go-next|\ :guilabel:`Go forward` goes forward in your navigation or browsing history
   * -
     - |go-up|\ :guilabel:`Go up` goes up one level in the file system folder hierarchy
   * - 
     - |folder-new|\ :guilabel:`Add folder` creates a :doc:`new folder</project_and_asset_management/project_bin/project_bin_use_folders>` in the current project bin. These are virtual folders that help you organize large bins. Folders can be turned into their own bins.
   * - **2**
     - |view-refresh|\ :guilabel:`Refresh document` refreshes the current view (default keyboard shortcut :kbd:`F5`)
   * - **3**
     - |view-list-icons|\ :guilabel:`Icons View` switches to icon view
   * - 
     - |view-list-details|\ :guilabel:`Compact View` switches to compact view
   * -
     - |view-list-tree|\ :guilabel:`Details View` switches to details view
   * - **4**
     - |view-preview|\ :guilabel:`Show Preview` opens the preview pane to display a preview of the  file where the mouse pointer is hovering over (default keyboard shortcut :kbd:`F12`)
   * - **5**
     - |view-sort|\ :guilabel:`Sorting` opens a context list menu to specify sort field, sort order, and position of folders and hidden files
   * - **6**
     - Use the slider or the :guilabel:`Zoom In` and :guilabel:`Zoom Out` buttons to increase or decrease the icon size 
   * - **7**
     - |folder-new|\ :guilabel:`New folder` opens the new folder dialog window (default keyboard shortcut :kbd:`Ctrl+shift+N`)
   * - **8**
     - |configure|\ :guilabel:`Options` opens a context list menu to specify what to show
   * - **9**
     - :guilabel:`Import image sequence` enables the import of a series of images that can be used to make a stop motion animation (see also :doc:`/project_and_asset_management/project_bin/image_sequence`)
   * - **10**
     - :guilabel:`Ignore subfolder structure` enables importing video footage or audio recording folders while automatically ignoring any sub-folder structures created by some devices, such as the Sony XDCam, Panasonic P2, Canon camcorders, or Zoom audio recorders.


.. rubric:: The Media Browser in Action

.. figure:: /images/Media-browser.gif
   :align: left

.. note:: 
  Depending on the version of Kdenlive, the Media Browser may look slightly differently.

.. container:: 

   .. figure:: /images/project_and_asset_management/media_browser_2.webp
   
      Alternative Media Browser layout and controls

.. rst-class:: clear-both


.. list-table::
   :class: table-wrap

   * - **1**
     - |go-up|\ :guilabel:`Go up` goes up one level in the file system folder hierarchy
   * - 
     - |go-previous|\ :guilabel:`Go back` goes back in your navigation or browsing history
   * -
     - |go-next|\ :guilabel:`Go forward` goes forward in your navigation or browsing history
   * - **2**
     - Zoom out and zoom in (increases or decreases the size of the icons in the file list)
   * - **3**
     - |view-preview|\ :guilabel:`Show Preview` opens the preview pane to display a preview of the  file where the mouse pointer is hovering over (default keyboard shortcut :kbd:`F11`)
   * - **4**
     - |document-open|\ :guilabel:`Import Selection` imports the selected files to the project bin 
   * - **5**
     - |application-menu|\ :guilabel:`Options` opens a context list menu to specify sort field, sort order, and position of folders and hidden files
   * -
     - .. figure:: /images/project_and_asset_management/media_browser_2_options.webp
   * - **6**
     - |kdenlive-show-video| opens a context list menu with additional navigation elements
   * -
     - .. figure:: /images/project_and_asset_management/media_browser_2_nav_list.webp
   * - **7**
     - :guilabel:`Import image sequence` When checked, Kdenlive will look for files with a filename pattern similar to the selected file and open the :doc:`Add Image Sequence</project_and_asset_management/project_bin/image_sequence>` dialog window.
   * - **8**
     - :guilabel:`Ignore subfolder structure` When checked, Kdenlive will import the clips in the selected folders and sub-folders without recreating the folder structure in the project bin
