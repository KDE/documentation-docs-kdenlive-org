.. meta::
   :description: Kdenlive Documentation - Configuration Environment
   :keywords: KDE, Kdenlive, documentation, user manual, configuration, preferences, environment, default folders, default apps, mlt, mime types, python, video editor, open source, free, learn, easy


.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Dirkolus (https://userbase.kde.org/User:Dirkolus)
             - Jessej (https://userbase.kde.org/User:Jessej)
             - Jack (https://userbase.kde.org/User:Jack)
             - Roger (https://userbase.kde.org/User:Roger)
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0

.. |mediainfo| raw:: html

   <a href="https://mediaarea.net/en/MediaInfo" target="_blank">MediaInfo</a>

.. |krita| raw:: html

   <a href="https://krita.org/en/" target="_blank">Krita</a>

.. |audacity| raw:: html

   <a href="https://www.audacityteam.org/" target="_blank">Audacity</a>

.. |glaxnimate| raw:: html

   <a href="https://glaxnimate.mattbas.org/" target="_blank">Glaxnimate</a>


Environment
-----------

.. .. versionadded:: 22.08
   Use lower CPU priority for proxy and transcode tasks

.. .. versionadded:: 22.12
   Warn if cache data exceeds

.. .. versionadded:: 24.02
   Check for Updates

.. .. versionremoved:: 25.04
   Python tab

.. .. versionadded:: 25.08
   Prevent sleep when playing and rendering


This section defines some of the most important settings for Kdenlive.

.. figure:: /images/getting_started/configure_environment_2508.webp
   :width: 700px
   :figwidth: 700px
   
   The Environment section

:1: :guilabel:`Concurrent threads`. Defines the number of threads to use for proxy clip generation and transcode jobs. Those jobs will run in the background. The value entered is passed to ffmpeg as the :code:`-threads` parameter. Increasing this parameter may not have an effect if you have changed the proxy encoding settings using :doc:`project settings</project_and_asset_management/project_settings/proxy_settings>` to a codec that ffmpeg does not do multi-threading on. Multi-threading is supported for MPEG-2, MPEG-4, H.264, and VP8.

:2: :guilabel:`Use lower CPU priority`. This instructs Kdenlive to lower the priority of the proxy clip generation and transcode jobs. It helps keeping the main UI responsive when proxies are created or clips are being transcoded.

:3: :guilabel:`Warn if cached data exceeds`. Add a maximal cache size that Kdenlive checks every two weeks. Kdenlive issues a warning message if the total cached data size exceeds this limit. If you need to purge the cache, use the :doc:`/tips_and_tricks/useful_info/manage_cached_data` feature.

:4: :guilabel:`Check for updates`. If checked, Kdenlive will show a pop-up window with a reminder if your version is older than six (6) months.

:5: :guilabel:`Prevent sleep when playing and rendering`. If checked, Kdenlive disables the system's power management to avoid sleep mode and screen locking while playback and rendering.

:6: Tabs for the different environment settings.


.. _configure_environment_mlt:

MLT Environment
~~~~~~~~~~~~~~~

.. .. versionchanged:: 25.08

These settings tell Kdenlive where to find the MLT executables and profile files. Only advanced users would really need to change these settings. Kdenlive is basically a frontend to the MLT program. Since Kdenlive version 25.08 |mediainfo| is not needed anymore as Kdenlive can read the timecode directly from MLT and shows these details in the clip properties. The values differ depending on your OS.

.. figure:: /images/getting_started/configure_environment_MLT_Windows_2508.webp
   :width: 500px
   
   Environment variables in Kdenlive installed on Windows

.. figure:: /images/getting_started/configure_environment_MLT_Linux_2508.webp
   :width: 500px
   
   Environment variables in Kdenlive installed on Linux

.. figure:: /images/getting_started/configure_environment_MLT_appimage_2508.webp
   :width: 500px
   
   Environment variables in Kdenlive appimage on Linux

.. figure:: /images/getting_started/configure_environment_MLT_MacOS_2508.webp
   :width: 500px
   
   Environment variables in Kdenlive on MacOS


.. _configure_environment_default_folders:

Default Folders
~~~~~~~~~~~~~~~

These settings tell Kdenlive where project files are to be stored. It also controls what folder Kdenlive will use as a temporary file storage location and where files captured from an external source will be saved.

.. .. versionchanged:: 22.08
   .. versionchanged:: 24.05

.. figure:: /images/getting_started/kdenlive2405_configure_environment_default_folders.webp
   :width: 500px
   
   Default folders on Windows.

.. figure:: /images/getting_started/configure_environment_default_folders_appimage_2412.webp
   :width: 500px
   
   Default folders on Linux (appimage).

.. figure:: /images/getting_started/configure_environment_default_folders_linux_2412.webp
   :width: 500px
   
   Default folders on Linux (flatpak).

.. figure:: /images/getting_started/kdenlive2405_configure_environment_default_folders_MacOS.webp
   :width: 500px
   
   Default folders on MacOS.


.. .. _configure_environment_python:

.. .. versionadded:: 24.02
      Python tab

.. .. versionremoved:: 25.04
      Python tab

.. Set on remark, we may need it again
   Python
   ~~~~~~

   *Python* is used for the speech-to-text feature. These settings tell Kdenlive where *Python* can be found on your system or whether a virtual environemnt (venv) should be set up and used.

   .. figure:: /images/getting_started/configure_environment_python_appimage_2_2412.webp
      :width: 500px
      :alt: configure_environment_python_appimage_2_2412

      Python tab on Linux (appimage) using venv

   :guilabel:`Use python virtual environment (recommended)`. When enabled, Kdenlive creates a :file:`venv` folder and copies/symlinks *Python* into this folder.

   Using the virtual environment (venv) stores *Python* as you have installed it on your system in the :file:`venv` folder.  If you install speech to text, the VOSK and Whisper libraries will be installed in the :file:`venv` folder as well.

   This has many benefits including easier dependency management and reduced risk of package conflicts and errors caused by software deprecation.

   Path for :file:`venv`:

   - Linux: :file:`~/.local/share/kdenlive/venv`
   - Windows: :file:`%LocalAppData%\\kdenlive\\venv`

   To remove the installed :file:`venv` packages click on :guilabel:`Delete`. This will completely remove the :file:`venv` folder with all installed packages. Note that this does not remove the downloaded models (VOSK/Whisper) that can still occupy significant disk space.

   .. figure:: /images/getting_started/kdenlive2402_configure_environment_python.webp
      :width: 500px
      :alt: Kdenlive_Configure_environment_python

      Python tab on Windows

   .. figure:: /images/getting_started/configure_environment_python_appimage_1_2412.webp
      :width: 500px
      :alt: configure_environment_python_appimage_1_2412

      Python tab on Linux (appimage) not using venv

   .. figure:: /images/getting_started/configure_environment_python_flatpak_1_2412.webp
      :width: 500px
      :alt: configure_environment_python_flatpak_1_2412

      Python tab on Linux (flatpak) not using venv

   .. figure:: /images/getting_started/configure_environment_python_flatpak_2_2412.webp
      :width: 500px
      :alt: configure_environment_python_flatpak_2_2412

      Python tab on Linux (flatpak) using venv


.. _configure_environment_default_apps:

Default Apps
~~~~~~~~~~~~

These settings control which external application opens when you choose :ref:`edit_clip` for a clip in the Project Bin. 

.. figure:: /images/getting_started/configure_environment_default_apps_1_2412.webp
   :width: 500px
   :figwidth: 500px
   
   Settings for default apps

:guilabel:`Image editing`: A free software would be |krita|.

:guilabel:`Audio editing`: A free software would be |audacity|.

:guilabel:`Animation editing`: Kdenlive integrates nicely with and updates files automatically which are saved in |glaxnimate| which is available from its homepage for Linux, Windows, and MacOS.

.. note:: **Mac user:** See these :ref:`instructions <kdenlive_macos>` how to install and run :file:`dmg` files.

.. note:: **Windows user:** Make sure all the paths point to an :file:`.exe` file. :file:`glaxnimate.exe` is in folder :file:`%PROGRAMFILES%\\glaxnimate\\bin\\`.

.. rubric:: Example

.. figure:: /images/getting_started/configure_environment_default_apps_2_2412.webp
   :width: 500px
   
   Examples of properly configured default apps on Linux (appimage)


Mime types
~~~~~~~~~~

Specifies the Media Types (formerly known as MIME types) which Kdenlive can work with.

.. figure:: /images/getting_started/configure_environment_mime_types_2412.webp
   :width: 500px
   :figwidth: 500px
   
   Supported MIME Types

.. .. versionadded:: 22.08
   Added file type: `AVIF`, `HEIF` and `JPEG XL`
   Added animation file type: `Json` (Lottie animations) and `rawr` (Glaxnimate animation)

