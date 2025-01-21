.. meta::
   :description: Kdenlive Documentation - Project Settings
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



Project Settings
================

Project Settings define first and foremost the properties of the final video (a rescaling or output format change during the render process notwithstanding). That includes the dimensions (e.g. 1920x1080), aspect ratio (e.g. 16:9 or 4:3), frame rate (e.g. 30fps), color space, and interlaced or progressive rendering.

Besides that, you can define where Kdenlive stores all project assets, how many video and audio tracks there are initially (you can add or delete tracks later as needed), whether or not Kdenlive should create proxy files automatically and under what circumstances, and you can enter meta data like author's name and copyright information which will be embedded in the multimedia container during export/render.

Here you also define the categories and colors for the guides and markers you can use in the timeline to structure your project.

Once the project is underway, you can find here some statistics about your project, like number and size of the clips, used versus unused, and about the data cache. Kdenlive gives you full control over the use and utilization of your assets.

The project settings dialog is opened every time a new project is created (:menuselection:`Menu --> File --> New`), or via :menuselection:`Menu --> Project --> Project Settings`.

The Project Settings dialog window has six tabs:

.. toctree::
   :maxdepth: 1

   project_settings/general_settings
   project_settings/proxy_settings
   project_settings/guides_settings
   project_settings/tab_meta_data
   project_settings/tab_project_files
   project_settings/tab_cache_data