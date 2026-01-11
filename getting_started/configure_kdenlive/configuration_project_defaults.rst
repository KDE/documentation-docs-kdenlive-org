.. meta::
   :description: Kdenlive Documentation - Configuration Project Defaults
   :keywords: KDE, Kdenlive, documentation, user manual, configuration, preferences, project, defaults, video editor, open source, free, learn, easy


.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Project Defaults
----------------

Kdenlive uses these settings for creating a new project (see Menu > File > New, or when Kdenlive starts and the option for opening the last project is not checked). To change the parameters for a currently open project, use the :doc:`Project Settings</project_and_asset_management/project_settings>`. Please note that while changing parameter for the open project is possible, it is not recommended as it may break things like keyframes and cuts.

.. figure:: /images/getting_started/configure_project_defaults_2412.webp
   :width: 700px
   :figwidth: 700px
   
   The Project Defaults section

:1: :guilabel:`Project Folder`. This is an important setting for keeping your projects organized and your file system shipshape. Kdenlive creates the following folders for each project: :file:`audiothumbs`, :file:`sequences`, :file:`videothumbs`, and :file:`workfiles`. See also :doc:`/getting_started/configure_kdenlive/configuration_info`.

:1a: If set to :guilabel:`Default`, Kdenlive will create these folders in a special folder in the installation path. For Linux this is :file:`/home/<username>/.var/app/org.kde.kdenlive/cache/kdenlive/<projectID>/`. For Windows this is :file:`%APPDATA\\Local\\kdenlive\\cache`.

:1b: :guilabel:`Parent folder of project file`. If this is selected, Kdenlive will create the folders for the project in the parent folder of the project file. For example, if your project file is in :file:`/home/my/projects/project_1/`, Kdenlive will create project related files in :file:`../project_1/`: :file:`/home/my/projects/project_1/audiothumbs/`, :file:`/home/my/projects/project_1/sequences/`, etc.

:1c: :guilabel:`Custom project folder`: You can specify a folder to use for these project folders.

:2: :guilabel:`Select the Default Profile (preset)`. In this section you define which of the profiles to be used when creating a new project. Use the filters for :guilabel:`Fps` and :guilabel:`Scanning` (the old fashioned reference to :term:`interlaced` or :term:`progressive`). You can create a new profile from here by clicking on |configure|\ :guilabel:`Manage project profiles` icon. For details about how to do that, please see :ref:`Project Profiles / Preset <project_profile>`.

:3: :guilabel:`Video/Audio Tracks`. Determines the number of video and tracks a new project has. You can add and delete tracks later at any time.

:4: :guilabel:`Audio channels`. Determines how many channels each audio track supports. Options are **2 channels (stereo)** (default), **4 channels**, and **6 channels**.

:5: :guilabel:`Timeline Preview profile`. Select which encoding profile to use for the :doc:`Preview Render</tips_and_tricks/tips_and_tricks/timeline_preview_rendering>` function. The available options depend on your HW and installed codecs. You can manage the profiles by clicking on the |configure|\ :guilabel:`Show profile parameters` icon. To see the profile parameters in the text window below the profile selection field, click on the |help-about| icon.


.. rubric:: Encoding Profiles
   
.. figure:: /images/getting_started/configure_project_defaults_preview_profiles_2412.webp
   :width: 500px
   :figwidth: 500px
   
   Timeline Preview profiles

:1: List of available profiles

:2: The parameters used in the selected profile

:3: Click on |list-add| to create a new profile based on the selected one, |document-edit| to edit the selected profile, |edit-delete| to delete the selected profile. |edit-download| does not have a function yet.