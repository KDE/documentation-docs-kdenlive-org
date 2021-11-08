.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Simon Eugster <simon.eu@gmail.com>
             - Jean-Baptiste Mardelle <jb@kdenlive.org>
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Vincent Pinon <vpinon@kde.org>
             - Sunab (https://userbase.kde.org/User:Sunab)
             - Jack (https://userbase.kde.org/User:Jack)
             - Roger (https://userbase.kde.org/User:Roger)
             - Xyquadrat (https://userbase.kde.org/User:Xyquadrat)
             - TheMickyRosen-Left (https://userbase.kde.org/User:TheMickyRosen-Left)
             - Carl Schwan <carl@carlschwan.eu>
             - Geolgar (https://userbase.kde.org/User:Geolgar)
             - Tenzen (https://userbase.kde.org/User:Tenzen)

   :license: Creative Commons License SA 4.0

.. _installation:

Installation
============

.. contents::

Visit the `download <https://kdenlive.org/download/>`_ page of the Kdenlive Web site for up to date information on installing **Kdenlive**.

Non-KDE Desktops
----------------

**Kdenlive** can be installed on non-KDE Desktops without any issues.

Kdenlive on macOS
-----------------

**Kdenlive** and **MLT** can compile and run under macOS. There is no stable macOS version yet, but you can help to have one soon by testing our daily macOS version (available on the `download <https://kdenlive.org/download/>`_ page). If you have experience with building software for macOS, please help us!

Configuration Information
-------------------------

Kdenlive's application-wide persistent settings are stored in the following locations, depending on your platform. 


.. list-table::
   :header-rows: 1

   * - Description
     - Linux
     - Windows
     - macOS
   * - General settings of the application. Delete this and restart Kdenlive to reset the application to "factory" settings
     - :file:`~/.config/kdenliverc`
     -
     -
   * - temporary session info
     - :file:`~/.config/session/kdenlive_*`
     -
     -
   * - cache location storing audio and video thumbnails, and proxy clips
     - :file:`~/.cache/kdenlive`
     - :file:`%LOCALAPPDATA%\kdenlive\cache`
     -
   * - contains user library clips, speech models, profiles and titles
     - :file:`~/.local/share/kdenlive`
     - :file:`%APPDATA%\kdenlive`
     -
   * - lumas folder inside here contains the files used for :ref:`wipe`
     - :file:`~/.local/share/kdenlive/HD`
     - :file:`%PROGRAMFILES%\kdenlive\bin\data\kdenlive\lumas`
     -
   * - Auto Save Recovery files
     - :file:`~/.local/share/stalefiles/kdenlive`
     -
     -


