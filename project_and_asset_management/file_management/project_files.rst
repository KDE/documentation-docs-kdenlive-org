.. meta::
   :description: Kdenlive Documentation - Project File Details
   :keywords: KDE, Kdenlive, project, working, file, management, details, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Gallaecio (https://userbase.kde.org/User:Gallaecio)
             - Vincent Pinon <vpinon@kde.org>
             - Jack (https://userbase.kde.org/User:Jack)
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |mlt-xml-doc| raw:: html

   <a href="https://www.mltframework.org/docs/mltxml/" target="_blank">MLT's XML documentation</a>

.. |mlt-dtd-doc| raw:: html

   <a href="https://github.com/mltframework/mlt/blob/master/src/modules/xml/mlt-xml.dtd" target="_blank">MLT's DTD</a>

.. |mlt| raw:: html

   <a href="https://www.mltframework.org/" target="_blank">MLT</a>

.. |github-repo| raw:: html
   
   <a href="https://invent.kde.org/multimedia/kdenlive/-/blob/master/dev-docs/fileformat.md" target="_blank">github repository</a>

Project File Details
====================

Kdenlive's :file:`.kdenlive` project files use an :abbr:`XML(Extensible Markup Language)` format based on MLT's format to describe the source media used in a project, as well as the use of that media in the timeline. For more details see |mlt-xml-doc| and |mlt-dtd-doc| (document type definition).

For most media, such as video, audio, and images, Kdenlive stores only a reference in a project, not the media itself. Only some media gets stored directly inside Kdenlive's project files, most notably Kdenlive :doc:`title</project_and_asset_management/project_bin/title_clip>` and :doc:`color clips</project_and_asset_management/project_bin/color_clip>`.

The advantages of using this file format are:

* |mlt| is able to directly render Kdenlive project files. MLT simply ignores all the additional Kdenlive-specific project data and just sticks to its rendering information. The Kdenlive-specific data is the additional icing on top that makes working with projects much easier than editing at the (lower) rendering level.
* Kdenlive can directly include and work with MLT rendering files, just the same way it works with other media. In fact, Kdenlive's :doc:`library clips</project_and_asset_management/library>` are simply MLT rendering files, nothing more.

The project file holds all relevant information about

* target video and audio properties (selected in the :doc:`project profile</project_and_asset_management/project_settings/general_settings>`)
* references to all the source materials (and to their :term:`proxies<proxy>`)
* position, duration and edits of the clips in the timeline, with applied effects and their respective parameters including keyframes, and everything to get the final result

Project files are associated with a :doc:`working directory</project_and_asset_management/file_management/folder_structure>`, in which **Kdenlive** will generate *proxies* and *thumbnails*, so that an overview of your media always shows up quickly.

.. note::
   If you move your project file, you should declare the directory change in the project properties.

The development of Kdenlive introduces changes to the :file:`.kdenlive` document format from time to time. For example, the introduction of sequences (also known as nested timelines) in version 23.04 required new objects to be stored in the :file:`.kdenlive` file. The document version changed from 1.04 to 1.1. You can find the document version in the :file:`.kdenlive` file in the line containing this:

.. code::
   
   <property name="kdenlive:docproperties.version">1.1</property>
   
When Kdenlive opens a project file that was created with a lower (previous) version of Kdenlive, it upgrades the document version, and automatically creates a backup copy of the original project file. Kdenlive tells you that a backup was created and the project file was updated to the new document version. In the project folder you will find a file called :file:`myproject_backup.kdenlive` (where *myproject* is the name of your project file). In case something does not work with the new version of Kdenlive, you can downgrade Kdenlive and open the backup of your project.

This is important because document versions are not necessarily backwards compatible. In other words: higher (newer) versions of the :file:`.kdenlive` file format cannot be opened with lower (previous) versions of Kdenlive . For example, projects created with Kdenlive 23.04 or higher (newer) cannot be opened by a Kdenlive version lower than (prior to) 23.04 (e.g. 22.12.8) because the 23.04 release of Kdenlive introduced the document change from 1.04 to 1.1 for the nested timelines.


.. .. versionadded:: 20.08.0
   A major refactoring of the project file fixes a long standing issue with the decimal separator (comma/point) conflict causing many crashes.

.. warning::
   Projects created with 20.08 forward are not backwards compatible, that is, you won't be able to open your :file:`.kdenlive` project files with older versions.

.. .. versionadded:: 23.04.0
   With introducing sequences the project file version is 1.1 (from 1.04 -> 1.1) and is not backward compatible. Once opened in 23.04 you cannot open the project file in older versions.

.. warning::
   Projects created with 23.04 forward are not backwards compatible, that is, you won't be able to open your :file:`.kdenlive` project files with older versions.

For the more technically inclined user a more detailed description of the file format and how the various objects are described is available in the |github-repo| of Kdenlive.