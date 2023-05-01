.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Gallaecio (https://userbase.kde.org/User:Gallaecio)
             - Vincent Pinon <vpinon@kde.org>
             - Jack (https://userbase.kde.org/User:Jack)
             - Eugen Mohr

   :license: Creative Commons License SA 4.0



.. _project:

Project File Details
====================


**Kdenlive** projects consist in a singe :file:`.kdenlive` file (in XML format), gathering :


* target video and audio properties

* references to all the source materials (and to their lighter *proxies* work copies)

* clips arrangement on the timeline, with effects applied, and everything to get the final result


Project files are associated with a working directory, in which **Kdenlive** will generate *proxies* and *thumbs*, so that an overview of your media always shows up quickly (if you move your project file, you should declare the directory change in the project properties).

When Kdenlive opens a project file that upgrades the document version, like with 20.08.0 or 23.04.0, it automatically creates a backup copy of the original project file. When a project was created with an older document version, like Kdenlive < 20.08.0 or < 23.04.0 and you opened it, look into the project folder. You should have a file called `myproject_backup.kdenlive`. This is a copy of the original project file before the upgrade and you should be able to open it correctly either with Kdenlive 20.04.x or 22.12.x or the newly release 23.04.0 version.

Otherwise, Kdenlive also keeps a copy of all saved versions of your project files. Go to :menuselection:`Project --> Open Backup File` and you should see a list of the archived versions. More details see :ref:`backup`.



.. versionadded:: 20.08.0

   A major refactoring of the project file fixes a long standing issue with the decimal separator (comma/point) conflict causing many crashes.

.. warning::

   Projects created with 20.08 forward are not backwards compatible, that is, you won’t be able to open your :file:`.kdenlive` project files with older versions.

.. versionadded:: 23.04.0

   With introducing sequences the project file version is 1.1 (from 1.04 -> 1.1) and is not backward compatible. Once opened in 23.04 you cannot open the project file in older versions.

.. warning::

   Projects created with 23.04 forward are not backwards compatible, that is, you won’t be able to open your :file:`.kdenlive` project files with older versions.

