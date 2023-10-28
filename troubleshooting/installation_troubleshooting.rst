.. meta::
   :description: Troubleshooting Kdenlive - Installation Troubleshooting
   :keywords: KDE, Kdenlive, troubleshooting, documentation, installation, user manual, video editor, open source, free, learn, easy, help

.. metadata-placeholder

   :authors: - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |media_info| raw:: html

   <a href="https://mediaarea.net/MediaInfo/Download" target="_blank">here</a>

.. |packman_repository| raw:: html

   <a href="https://www.opensuse-community.org/" target="_blank">packman repository</a>

.. |replace_vendor_package| raw:: html

   <a href="https://en.opensuse.org/SDB:Vendor_change_update#Full_repository_Vendor_change" target="_blank">replace vendor package</a>


.. _troubleshooting-installation:

Installation Troubleshooting
============================

I am missing a package and cannot install Kdenlive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A dependency is missing and it is recommended to install it.

.. list-table::
   :widths: 30 70
   :class: table-wrap

   * - Frei0r
     - This package provides many effects and transitions. Without it, Kdenlive's features will be reduced. You can simply install frei0r-plugins from your package manager.
   * - Breeze icons
     - Many icons used by Kdenlive come from the Breeze Icons package. Without it, many parts of the UI will not appear correctly. You can simply install breeze-icon-theme or breeze-icons from your package manager.
   * - MediaInfo
     - Download and install MediaInfo from |media_info|


My MLT installation cannot be found, or Kdenlive cannot start MLT backend
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is obviously something wrong with your MLT installation. Either it is not installed or not in a standard location. You can test your MLT installation from a terminal by typing ``melt color:red``. This should bring up a red window (press :kbd:`q` to close it).

- If you see an error message try reinstalling MLT or check that you don't have several versions installed on the system
- If you see the red window, check where your MLT is installed: ``which melt``. Then delete Kdenlive's config file (:file:`$HOME/.config/kdenliverc`) and restart Kdenlive.


Kdenlive says a MLT module is missing. What do I do?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An MLT dependency is missing and it is required to install it.

.. list-table::
   :widths: 30 70
   :class: table-wrap

   * - SDL
     - Is used to output audio. Install `libsdl 1.x` from your package manager.
   * - Avformat
     - Is the FFmpeg module. Make sure you have ffmpeg installed on your system.
   * - XML
     - Make sure libxml2 is installed. On Windows, ensure that no conflicting libxml2.dll is placed in `C:\\Windows\\System32` or comparable folders. If you find a `libxml2.dll` there, try to rename it to `libxml2.old.dll` and then to restart kdenlive. Note that renaming `libxml2.dll` in folder `System32` may break whichever other app has put libxml2.dll there.


It says that the following codecs were not found in my system...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some audio / video codecs are not installed by default. Installing a package called ``libavcodec-extra`` might solve the problem.

On openSuse, you need to add the |packman_repository|, then enable |replace_vendor_package| on the packman repository.