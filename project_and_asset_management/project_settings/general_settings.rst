.. meta::
   :description: Kdenlive Documentation - General Project Settings
   :keywords: KDE, Kdenlive, project, setup, settings, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Jean-Baptiste Mardelle <jb@kdenlive.org>
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Vincent Pinon <vpinon@kde.org>
             - Jack (https://userbase.kde.org/User:Jack)
             - Tenzen (https://userbase.kde.org/User:Tenzen)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0



General Settings
================

The first tab in the Project Settings dialog is for general project settings. It contains the important information about the project.

.. rubric:: Layout and Controls

.. container:: clear-both

   .. figure:: /images/project_and_asset_management/project_settings_settings.webp
      :align: left
      :alt: project_settings

      The Project Settings dialog window

.. rst-class:: clear-both

:1: The available tabs for the different settings: Settings, :doc:`Proxy</project_and_asset_management/project_settings/proxy_settings>`, :doc:`Markers</project_and_asset_management/project_settings/guides_settings>`, :doc:`Metadata</project_and_asset_management/project_settings/tab_meta_data>`, :doc:`Project Files</project_and_asset_management/project_settings/tab_project_files>`, and :doc:`Cache Data</project_and_asset_management/project_settings/tab_cache_data>`. The two latter ones are only available via :menuselection:`Menu --> File --> Project Settings`.
      
:2: Defines how to set up the `project folder`_

:3: Filters the list of available project profiles by :abbr:`fps(frames per second)` or scanning method

:4: Opens the dialog for :ref:`creating new <project_profile_create>` project profiles

:5: List of all available `project profiles <project_profile>`_ (left) and their details (right)

:6: Defines how many initial `video and audio tracks <tracks>`_ the project will have. You can add and delete tracks later from within the timeline.

:7: Defines the number of `audio channels`_

:8: Defines whether or not you want `thumbnails`_ of the clips in the timeline

:9: Select which `profile <timeline preview>`_ you want to use for the preview render feature


.. _project_folder:

Project Folder
--------------

As recommended in the :ref:`quickstart` section, you should create a new folder for your project. This folder will hold all temporary files that are used during the editing of your project (thumbnails, proxy clips, etc).

.. seealso:: 
   :doc:`/project_and_asset_management/file_management/folder_structure`

.. list-table::
   :width: 100%
   :widths: 35 65
   :class: table-wrap

   * - :guilabel:`Default`
     - Lets Kdenlive determine the best location for the project folder
   * - :guilabel:`Parent folder of the project file`
     - Uses the parent folder of the folder the :file:`.kdenlive` project file is located in
   * - :guilabel:`Custom`
     - Enter the path to the folder, or click on the |document-open|\ :guilabel:`Open file dialog` icon to navigate to the folder


.. _project_profile:

Project Profile / Preset
------------------------

The project profile (or preset) will define the format of your project, like the dimensions (or frame size) and the aspect ratio, the frame rate (or fps), the color space, and whether or not the frames are interlaced.

You can use the pull-down menus to filter the list of profiles by :guilabel:`Fps` (frames per second) or :guilabel:`Scanning` (Interlaced or Progressive).

You should carefully choose your project profile and select the one which best fits your desired output. All video operations on the project (like compositing, transformations, use of keyframes, etc.) will then use this profile and the inherent properties.

For example, if your desired output is a 4K video, select one of the 4K profiles; if you want to create a video suitable for social media on smartphones or YouTube Shorts, select a profile for vertical output (found in the **Custom** category).

.. _project_profile_create:

.. container:: clear-both

   .. figure:: /images/project_and_asset_management/project_settings_preview_profile_create.webp
      :width: 360px
      :figwidth: 360px
      :align: left
      :alt: project_settings_preview_profile_create

      Creating a new project profile

You can manage the list of project profiles from here. Click on the |configure|\ :guilabel:`Manage project profiles` icon. By default, the profile currently highlighted in the list will be opened for editing. In case this is the profile used in the current project, an error message will be displayed saying that it cannot be edited while the project is open.

Further details can be found in the :doc:`Configure Project Defaults</getting_started/configure_kdenlive/configuration_project_defaults>` section of this documentation.

.. rst-class:: clear-both

.. warning:: 
   Make sure you click on the |document-save|\ :guilabel:`Save profile` icon before you :guilabel:`Close` this window. Kdenlive does not issue a warning if the changed or newly created project profile was not saved.


Tracks
------

You can select the default number of audio and video tracks that your project will have. You can always add or remove tracks later in the timeline of an existing project.


Audio Channels
--------------

You can select the number of audio channels per audio track. The following settings are supported:

.. list-table:: 
   :class: table-wrap

   * - :guilabel:`2 Channels (Stereo)`
     - The default and most common setup
   * - :guilabel:`4 Channels`
     - 
   * - :guilabel:`6 Channels`
     - 


Thumbnails
----------

If ticked, audio and video thumbnails are shown in the :ref:`timeline`. They can also be enabled/disabled through buttons in the :ref:`status_bar`.


Timeline Preview
----------------

This setting determines what codec to use for the :doc:`preview render feature</tips_and_tricks/tips_and_tricks/timeline_preview_rendering>`. Select the codec that works best for your HW environment and the sources you are using in the project.

.. container:: clear-both

   .. figure:: /images/project_and_asset_management/project_settings_preview_profile.webp
      :width: 360px
      :figwidth: 360px
      :align: left
      :alt: project_settings_preview_profile

      The list of available preview profiles

You can also change the settings for the various preview profiles or create new ones. Click on the |configure|\ :guilabel:`Display Profile Parameters` icon to open this dialog window.

.. rst-class:: clear-both

If you are just interested in the parameters used in the selected preview profile click on the |help-about|\ :guilabel:`Information` icon.