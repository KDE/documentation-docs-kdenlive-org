.. meta::
   :description: Kdenlive Documentation - Using the Project Bin
   :keywords: KDE, Kdenlive, project bin, working, using, documentation, user manual, video editor, open source, free, learn, easy

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



Using the Project Bin
=====================

The Project Bin\ [1]_ is where all your :term:`assets<Asset>` are. Depending on the size of your project, that list can quickly become confusing and difficult to work with. Kdenlive has several features to manage the bin's content.


User Interface
--------------

.. container:: clear-both

   .. figure:: /images/project_and_asset_management/project_bin_layout.webp
      :align: center
   
      The Project Bin in Kdenlive

.. rst-class:: clear-both

.. list-table::
   :class: table-wrap

   * - **1**
     - |kdenlive-add-clip|\ :guilabel:`Add clip or folder` opens a window similar to the file manager of your OS allowing you to navigate around your file system and select :doc:`files to be added</project_and_asset_management/project_bin/clips>` to the project bin.
   * - 
     - |go-down| opens a pop-up window from where you can select what kind of clip you want to add 
   * - 
     - |folder-new|\ :guilabel:`Add folder` creates a :doc:`new folder </project_and_asset_management/project_bin/project_bin_use_folders>` in the current project bin. These are virtual folders that help you organize large bins. Folders can be turned into their own bins.
   * - **2**
     - |edit-delete|\ :guilabel:`Delete clip or folder` deletes the currently selected clip or folder from the bin
   * - **3**
     - |tag|\ :guilabel:`Tags Panel` toggles the :doc:`tags <project_bin_use_tags>` panel
   * - **4**
     - |application-menu|\ :guilabel:`Options` opens a pop-window with more `options` including the option to :ref:`scale <scaling_the_view>` the view
   * - **5**
     - |view-filter|\ :guilabel:`Filter` switches a :doc:`filter <project_bin_use_filters>` on or off
   * - 
     - |go-down|\ :guilabel:`Filter` opens a pop-up window to :doc:`set filter <project_bin_use_filters>` parameters
   * - **6**
     - Search field to :doc:`search for assets <project_bin_use_searching>` in the bin
   * - **7**
     - |go-up|\ :guilabel:`Sort` Toggles between sorting ascending and descending
   * - **8**
     - The folder with all the sequences. It is there even if you did not :doc:`create a sequence </project_and_asset_management/project_bin/sequence>`.
   * - **9**
     - Folders created by the user (for illustration purposes only). You can turn folders into :doc:`individual bins <project_bin_use_multiple_bins>` that can be added to your workspace and docked.
   * - **10**
     - |kdenlive-audio| indicates a file with an audio stream
   * - 
     - |kdenlive-show-video| indicates a file with a video stream
   * - **11**
     - Indicators for duration of the clip in the format :abbr:`hh:mm:ss:ff(hours:minutes:seconds:frames)`, and the number of instances in sequences (first number) and the timeline (second number).


.. _scaling_the_view:

Scaling the View
~~~~~~~~~~~~~~~~

You can zoom the project bin view in and out.

.. container:: clear-both

   .. figure:: /images/project_and_asset_management/project_bin_scale_view.gif
      :width: 360px
      :figwidth: 360px
      :align: left
   
      Scaling the project bin view

   Click on the |application-menu|\ :guilabel:`Options` icon and use the slider or the buttons to the left or right of it to increase or decrease the zoom level.

.. rst-class:: clear-both


Changing the View
~~~~~~~~~~~~~~~~~

You can switch the project bin view from Tree View to Icon View, change the sort criterion, show additional columns for Date, Description, Rating, and have a preview in the thumbnails for video files.

.. container:: clear-both

   .. figure:: /images/project_and_asset_management/project_bin_options.webp
      :width: 360px
      :figwidth: 360px
      :align: left
   
      Scaling the project bin view

   Click on the |application-menu|\ :guilabel:`Options` icon and select the :guilabel:`View Mode`, :guilabel:`Sort By` criteria, and tick the boxes for additional columns.

   Select |favorite|\ :guilabel:`Disable Bin Effects` to (temporarily) disable any effect applied to a clip in the Project Bin. See also the chapter about :doc:`/effects_and_filters` and  :ref:`effects_everywhere-bin_clips`.

.. rst-class:: clear-both


Thumbnail Video Preview
~~~~~~~~~~~~~~~~~~~~~~~

A neat feature is to have a preview in the thumbnails for video files. This allows scrubbing in the thumbnail to quickly check whether that particular clip has the scene or footage you are looking for. 

.. container:: clear-both

   .. figure:: /images/project_and_asset_management/project_bin_options_video_preview.webp
      :width: 301px
      :figwidth: 301px
      :align: left
   
      Scaling the project bin view

   Check the :guilabel:`Show Video Preview in Thumbnails` to enable the feature.

.. rst-class:: clear-both


.. attention:: 
  This will trigger several clip jobs to generate the video previews. Depending on the size of your project bin and video assets this may take a while. You can continue working with Kdenlive but expect some performance degradation.


.. include:: project_bin_use_tags.rst

.. include:: project_bin_use_filters.rst

.. include:: project_bin_use_sorting.rst

.. include:: project_bin_use_searching.rst

.. include:: project_bin_use_multiple_bins.rst

.. include:: project_bin_use_folders.rst

.. include:: project_bin_use_context_menu.rst



----

.. [1] In earlier versions of Kdenlive this view was known as the Project Tree.
