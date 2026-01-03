.. meta::
   :description: Kdenlive Documentation - Project and Asset Management
   :keywords: KDE, Kdenlive, file loading, start video editing, first steps, documentation, user manual, video editor, open source, free, learn, easy, project, asset, management, assets

.. metadata-placeholder

   :authors: - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             
   :license: Creative Commons License SA 4.0



############################
Project and Asset Management
############################


.. toctree::
   :hidden:

   /project_and_asset_management/project_settings
   /project_and_asset_management/project_bin
   /project_and_asset_management/media_browser
   /project_and_asset_management/library
   /project_and_asset_management/capturing_video
   /project_and_asset_management/capturing_audio
   /project_and_asset_management/project_notes
   /project_and_asset_management/file_management


Kdenlive works with projects. A project contains all the :term:`assets<Asset>` (sources), the :term:`timeline` with your :term:`clips<Clip>` in different :term:`tracks<Track>`, the cuts and trims, :term:`compositions<Composition>` and :term:`transitions<Transition>`, :doc:`annotations</project_and_asset_management/project_notes>`, :term:`markers`, :term:`timeline marker <Timeline Marker (former Guide)>` - in short, everything you and Kdenlive need to produce a video file as the result of your work.

.. hint:: 
   When creating a project, select a project profile with the final video in mind. The :doc:`project settings</project_and_asset_management/project_settings>` determine the resolution (e.g. 1920x1080), the frame rate (e.g. 25 fps), other :doc:`meta data</project_and_asset_management/project_settings/tab_meta_data>`, and how to deal with the project's assets.

.. note::
   You can change the project profile later but it is not recommended as it may lead to undesirable results, in particular when you use keyframes.

The :doc:`Project Bin</project_and_asset_management/project_bin>` holds all your assets. You can load (or import) video and audio files, single images or entire :doc:`image sequences</project_and_asset_management/project_bin/image_sequence>`, create :doc:`color</project_and_asset_management/project_bin/color_clip>` and :doc:`title clips</titles_and_graphics/titles/titles>`, :doc:`animations</titles_and_graphics/graphics_and_animations/glaxnimate>`, and download assets from various :doc:`online sources</project_and_asset_management/project_bin/online_resources>` directly into your project.

While the project bin is for a specific project, you can use the :doc:`library</project_and_asset_management/library>` feature to store assets for use in other projects. That is also the only way to share or copy assets between projects.

Kdenlive offers limited :doc:`video</project_and_asset_management/capturing_video>` and :doc:`audio</project_and_asset_management/capturing_audio>` capturing functionality, for example to create voice overs, or use screenshots.

You can :doc:`take notes</project_and_asset_management/project_notes>` for your project that capture timestamps for easy reference during the editing process. This is very useful for big and complex projects or productions.

Kdenlive has an :doc:`auto-save feature</project_and_asset_management/file_management/auto_save>`, creates :doc:`backups</project_and_asset_management/file_management/backup>` in the background, and allows to :doc:`archive a project</project_and_asset_management/file_management/archiving>` with all the assets included.