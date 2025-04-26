.. meta::
   :description: Kdenlive Documentation - Configuration Settings and Preferences
   :keywords: KDE, Kdenlive, documentation, user manual, install, installation, configuration, preferences, video editor, open source, free, learn, easy


.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Configuration
=============

Kdenlive offers a wide variety of settings to adapt the application to your individual preferences and workflow.

General configuration settings for Kdenlive are available through :menuselection:`Menu --> Settings --> Configure Kdenlive`.

The Configure Kdenlive window has a search function making it easy for you to find the setting(s) you are searching for.

.. figure:: /images/getting_started/configure_search_2412.gif
   :width: 450px
   :figwidth: 450px
   :align: left
   :alt: configure_search_2412

   Search function in the Configure Kdenlive window

While typing, Kdenlive highlights any phrase or section the search term matches.

Sections that do not contain the search term are hidden from view.

.. rst-class:: clear-both


The configuration settings are divided into the following sections:

.. list-table:: 
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - :doc:`Misc</getting_started/configure_kdenlive/configuration_misc>`
     - This section contains settings for the general behavior of Kdenlive, how to handle clip import and effects, and the default duration for the various clip types.
   * - :doc:`Project Defaults</getting_started/configure_kdenlive/configuration_project_defaults>`
     - Kdenlive uses these settings for creating a new project (see :menuselection:`Menu --> File --> New`, or when Kdenlive starts and the option for opening the last project is not checked). To change the parameters for a currently open project, use the Project Settings. Please note that while changing parameter for the open project is possible, it is not recommended as it may break things like keyframes and cuts.
   * - :doc:`Proxy Clips</getting_started/configure_kdenlive/configuration_proxy_clips>`
     - This section contains settings pertaining to enabling and managing proxy clip generation.
   * - :doc:`Timeline</getting_started/configure_kdenlive/configuration_timeline>`
     - This section controls certain aspects of the timeline
   * - :doc:`Tools</getting_started/configure_kdenlive/configuration_tools>`
     - Currently, this section contains only the setting for cutting subtitles.
   * - :doc:`Environment</getting_started/configure_kdenlive/configuration_environment>`
     - This section contains settings pertaining to proxy and transcoding jobs, cache data, third party application and tools, and default folders and apps
   * - :doc:`Colors and Guides</getting_started/configure_kdenlive/configuration_colors+guides>`
     - This section defines which colors to use for thumbnails, guides and markers, and monitor overlays, as well as grid spacing. Here you can also manage the categories for guides and markers.
   * - :doc:`Speech to Text</getting_started/configure_kdenlive/configuration_plugins>`
     - This section is used to manage the various models used for Speech To Text (VOSK and Whisper) and Object Detection
   * - :doc:`Playback</getting_started/configure_kdenlive/configuration_playback>`
     - This section contains settings for playback during editing and external displays
   * - :doc:`Capture</getting_started/configure_kdenlive/configuration_capture>`
     - This section contains settings for screen captures, the Blackmagic DeckLink system, and audio recording
   * - :doc:`JogShuttle</getting_started/configure_kdenlive/configuration_jogshuttle>`
     - This section contains the settings for certain attached jog shuttle devices
   * - :doc:`Transcode</getting_started/configure_kdenlive/configuration_transcode>`
     - This section contains all the available profiles for transcoding video sources that are not in an edit-friendly format, for example have been recorded with a variable frame rate


.. warning:: Clicking :guilabel:`Restore Defaults` will reset every setting in every section to the default value! It is **not** restricted to the current, selected section.
   
   One exception: A deleted category for Guides and Markers cannot be restored! 


.. toctree::
   :hidden:

   configure_kdenlive/configuration_misc
   configure_kdenlive/configuration_project_defaults
   configure_kdenlive/configuration_proxy_clips
   configure_kdenlive/configuration_timeline
   configure_kdenlive/configuration_tools
   configure_kdenlive/configuration_environment
   configure_kdenlive/configuration_colors+guides
   configure_kdenlive/configuration_plugins
   configure_kdenlive/configuration_playback
   configure_kdenlive/configuration_capture
   configure_kdenlive/configuration_jogshuttle
   configure_kdenlive/configuration_transcode
   configure_kdenlive/configuration_info
