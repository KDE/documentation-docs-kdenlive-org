.. meta::
   :description: How to install Kdenlive video editor
   :keywords: KDE, Kdenlive, install, Installation, documentation, user manual, video editor, open source, free, learn, easy


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
             - Eugen Mohr

   :license: Creative Commons License SA 4.0

.. _installation:

Installation
============

.. contents::

Visit the `download <https://kdenlive.org/download/>`_ page of the Kdenlive Web site for up to date information on installing **Kdenlive**.

Non-KDE Desktops and Windows
----------------------------

**Kdenlive** can be installed on non-KDE Desktops and on Windows without any issues.

Kdenlive on macOS
-----------------

**Kdenlive** run under macOS 11 and 12 on Intel CPU only (available on the `download <https://kdenlive.org/download/>`_ page). Kdenlive isn't running on MacOS 10 and on M1.

Configuration Information
-------------------------

Kdenlive's application-wide persistent settings are stored in the following locations, depending on your platform. 


.. list-table::
   :header-rows: 1

   * - Linux  
     - Windows
     - macOS  
     - Description
   * - :file:`~/.config/kdenliverc`
     - :file:`%LocalAppData%\\kdenliverc`
     -
     - General settings of the application. Delete this and restart Kdenlive to reset the application to "factory" settings
   * - :file:`~/.config/kdenlive-appimagerc`
     - 
     - 
     - Linux AppImage only: contains the general settings of the application
   * - :file:`~/.config/session/kdenlive_*`
     -
     -
     - temporary session info
   * - :file:`~/.cache/kdenlive`
     - :file:`%LocalAppData%\\kdenlive`
     -
     - cache location storing audio and video thumbnails, and proxy clips, user defined titles, LUTS, lumas
   * - :file:`~/.local/share/kdenlive`
     - :file:`%AppData%\\kdenlive`
     -
     - contains downloaded: effects, export, library, opencvmodels, profiles, speech models, and titles
   * - :file:`~/.local/share/kdenlive/lumas`
     - :file:`%LocalAppData%\\kdenlive\\lumas`
     -
     - lumas folder inside here contains the files used for :ref:`wipe`
   * - :file:`~/.local/share/kdenlive/.backup`
     - :file:`%AppData%\\kdenlive\\.backup`
     -
     - Auto Save Recovery files
   * - :file:`~/.config/kdenlive-layoutsrc`
     - :file:`%LocalAppData%\\kdenlive-layoutsrc` 
     -
     - contains the layout settings
   * - :file:`~/.local/share/kxmlgui5/kdenlive/kdenliveui.rc`
     - :file:`%LocalAppData%\\kxmlgui5\kdenlive\\kdenliveui.rc` 
     -
     - contains UI configuration, if your UI is broken, delete this file
   * - :file:`~/.local/share/knewstuff3`
     - :file:`%LocalAppData%\\knewstuff3` 
     - 
     - contains LUT definition
   
**Windows**

To reach above folders: :kbd:`windows + r` then copy above path into the window.

Kdenlive in a Windows domain
----------------------------

If you want to use Kdenlive with domain users with using Windows Active Directory and/or Group Policies (GPOs) make sure all users have read/write rights to the following folders:

.. epigraph::

   %AppData%\\kdenlive

   %LocalAppData%\\kdenlive   

   %LocalAppData%\\kdenliverc   

   %LocalAppData%\\kdenlive-layoutsrc   

   %LocalAppData%\\kxmlgui5\\kdenlive\kdenliveui.rc   

   %AppData%\\kdenlive\\.backup   

   %LocalAppData%\\knewstuff3

Do also make sure no GPO is blocking the access to these folders.