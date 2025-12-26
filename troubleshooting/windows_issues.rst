.. meta::
   :description: Troubleshooting Kdenlive - Windows Issues
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, help, learn, Windows issue, Windows workaround, problem solving, Windows scopes, solution

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - TheMickyRosen-Left (https://userbase.kde.org/User:TheMickyRosen-Left)
             - Carl Schwan <carl@carlschwan.eu>
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |download_page| raw:: html

   <a href="https://kdenlive.org/en/download" target="_blank">download page</a>

.. |intel_updater| raw:: html

   <a href="https://www.intel.com/content/www/us/en/download/18002/intel-driver-support-assistant.html?wapkw=Intel-Driver-Support-Assistant" target="_blank">Intel Updater</a>



.. _troubleshooting-windows_issues:

Windows Issues
==============

Version 21.12.3 has a few issues that have workarounds. The purpose of this section is to document these issues and their workarounds.

.. _issue-directx:

Title tool, display real background not working in "DirectX" backend
--------------------------------------------------------------------

Something with the settings went wrong. Go to: :menuselection:`Menu --> Settings --> Reset Configuration` and try again.


Render problems
---------------

After rendering you get de-synced audio or wrong effects or black frames at end of the last clip: Download version 20.08.1 or higher from the |download_page|.

Disable :ref:`render-more_options_parallel_processing` in the render dialog window (check :guilabel:`More Options`).


.. _issue-scopes:

Windows issue with scopes, scopes don't show anything
-----------------------------------------------------

.. note::

    .. versionadded:: 21.12.2
        All video scopes are working with DirectX.


Workaround: Change the back-end to OpenGL via :menuselection:`Menu --> Settings --> OpenGL Backend --> OpenGL`

If it is still not working go to: :menuselection:`Menu --> Markers --> Timeline Markers Locked` and try again.



Audio crackling while playback
------------------------------

Change the audio driver in :menuselection:`Menu --> Settings --> Configure Kdenlive` (or :kbd:`Ctrl+Shift+,`), select :menuselection:`Playback --> Audio Backend` and play around with :menuselection:`WinMM` (Win7), :menuselection:`Wasapi` (Win10), or :menuselection:`DirectSound` to see what gives the best result.

You have to restart Kdenlive after each change.


Message *This application failed to start because no Qt platform plugin could be initialized*
---------------------------------------------------------------------------------------------

Open :menuselection:`Menu --> Settings --> Configure Kdenlive` (or press :kbd:`Ctrl+Shift+,`). Then go to the :menuselection:`Environment --> MLT Environment` section and make sure the paths point to the same path as "MLT profiles folder".

Download: :download:`qt.conf </files/qt.conf>`. Put the file :file:`qt.conf` into the :file:`bin` folder (the folder where :file:`kdenlive.exe` is).


First time use of Kdenlive
--------------------------

This issue should be solved with version 19.04.2-6. In order to make sure :file:`kdenliverc` is correctly set up start Kdenlive twice (start -> close -> start). Then start your work.


Intel graphics card driver
--------------------------

Updated Intel graphics driver version leads to a corrupted Kdenlive :abbr:`GUI (Graphical User Interface)`.

**Solution 1:** Open Kdenlive. Move the mouse to the top. The menus are showing up. Try to reach :menuselection:`Menu --> Settings --> OpenGL Backend` and select OpenGLES. Restart Kdenlive. This should solve your Intel graphic driver issue.

.. text moved from forum: https://forum.kde.org/viewtopic.php%3Ff=265&t=161309.html#p425882

   Maybe this statement helps (forum user "Windows User"): I would like to confirm that this issue seems to be mostly fixed. When I use the latest daily build of Kdenlive on Windows 10 with the latest Intel graphics drivers, I still get a corrupted GUI after opening Kdenlive. The only way to resolve this is to choose Settings > OpenGL Backend > OpenGLES from the menu. I can't see the menu when the GUI is corrupt but I can click where the menu should be. A quick test of Kdenlive after doing this seems fixed.


**Solution 2:** Press :kbd:`Win+R` and type **appdata**. Go to :file:`Local` and within it open :file:`kdenliverc` with an editor. Search for ``[misc]`` and delete ``[misc]`` and the following entry. Then restart Kdenlive.


.. _issue-style:

Timeline right-click menu closes immediately after releasing mouse button
-------------------------------------------------------------------------

Don't use the application style :guilabel:`Fusion`.

Go to: :menuselection:`Menu --> Settings --> Application Style` and choose :guilabel:`Default` or :guilabel:`Windows`.


.. _issue-force_breeze_icon_theme:

Icons are missing
-----------------

Go to: :menuselection:`Menu --> Settings` and click on :guilabel:`Reset Configuration`. Kdenlive restarts, and you should see the icons.


Cannot open projects made with previous version, timeline snaps back, cannot import clip
----------------------------------------------------------------------------------------

Go to: :menuselection:`Menu --> Settings --> Reset configuration`.

If this is not solving the problem: Press :kbd:`Win+R` and type **appdata**. Go to :file:`Local` and within it rename :file:`kdenliverc` to :file:`kdenliverc.old`. Start Kdenlive, close it and then start Kdenlive again.

If you have still problems, delete proxy clips and other cached data by going to :menuselection:`Menu --> File --> Project Setting --> Cache Data` where you can delete cached data.


Windows 10: timeline stuttering or Kdenlive hangs
--------------------------------------------------

Most probably you got a major Win10 update (i.e 1809). If so, you have to update all drivers for audio and video.
   
Intel drivers can be updated with this |intel_updater|.


Message *Clip is invalid, will be removed*
------------------------------------------

This message can appear if you do a clean reinstall of Kdenlive (see above). Simply close and open Kdenlive once, and it should be fixed.

Additionally this can be a problem either with the :file:`kdenliverc` file or you have some mismatch in the :file:`%APPDATA%\\local` folder.


Message *Failed to filter source* in :doc:`Motion Tracker</effects_and_filters/video_effects/alpha_mask_keying/motion_tracker>` effect
------------------------------------------------------------------------------------------------------------------------------------------

You may get an error of ``mlt_repository_init: failed to dlopen C:\Program Files\kdenlive\lib\mlt/libmltjack.dll`` or ``animation initialized FAILED`` followed by many lines of ``Current Frame: <f>, percentage: <p>``.

In this case, delete all :file:`kdenlive` folders in :file:`C:\\Program Files\\`, :file:`%AppData%\\Roaming\\`, and :file:`%AppData%\\Local\\`, and then do a new install of Kdenlive.   


Any critical bug
----------------

This describes the process of doing a clean install on Windows®.

Firstly, delete your normal Kdenlive folder (containing the application).

Access the **Appdata** folder (:kbd:`Win+R` and then type **APPDATA** in full caps). Go to :file:`Local` and search for folder :file:`kdenlive`.

.. note:: If you have any saved effects, or clips stored in your library, make a backup of the :file:`library` and the :file:`effect-templates` folders.

Then delete the :file:`kdenlive` folder.

Reinstall the latest version of Kdenlive from the |download_page|.


JPG files appear as white picture after rendering
-------------------------------------------------

This issue should be solved with version 19.04.0. If not, convert the JPG to PNG and it renders correctly.


Play/Pause issue
----------------

This issue is solved with version 18.08.2 (30. Oct 2018). Get the current version from the |download_page|.


Qt rendering crash
------------------

Hit :kbd:`Ctrl+Shift+,` or go to :menuselection:`Menu --> Settings --> Configure Kdenlive`, and then to :menuselection:`Environment` and make sure the paths point to the same path as "MLT profiles folder".

When switching from version 17.12 to 18.04/18.08, a Qt rendering crash appears. To make sure this doesn't happen, you need to edit the :file:`kdenliverc` file in the :file:`AppData\\local` folder. To access your appdata, press :kbd:`Win+R` (:kbd:`Windows` key and :kbd:`R` key simultaneously) and type **appdata**. Go to :file:`local` and within it rename :file:`kdenliverc` to :file:`kdenliverc.old`.


Kdenlive cannot be deleted, running process on exit
---------------------------------------------------

This issue is solved with Windows version 18.12.1. Get the current version from the |download_page|.

If you want to reinstall Kdenlive or re-run Kdenlive, it may tell you "The file or folder is open in another program". Windows® then won't let you delete or re-run Kdenlive.

To fix this you have to kill the running process: press and hold :kbd:`Ctrl+Shift+Esc` and expand the task manager by clicking :menuselection:`All details`. Then find :file:`kdenlive.exe` and :file:`dbus-daemon.exe`, and click :menuselection:`End task` for both of them.

Or download :download:`Kdenlive-kill.zip </files/Kdenlive-kill.zip>`. Unpack it and just double-click the batch file which kills all running Kdenlive processes.


Kdenlive crashes at start up, Kdenlive cannot be uninstalled
------------------------------------------------------------

If Kdenlive crashes at startup or if the uninstaller doesn't work delete the entire folder: :file:`C:\\Program Files\\kdenlive`.

Re-install Kdenlive.

You may have to manually delete the Kdenlive folder in the Start menu.


Kdenlive crash or green monitor
---------------------------------

Get all newest Windows® updates. Afterwards, update your graphics card driver, your sound card driver and your printer driver.
Some crashes could occur of incompatibility of the graphics card and sound card with the newest Windows®10 updates (18.09 update).
After you have updated the drivers re-start the computer and try again by starting :file:`kdenlive.exe`.

If this is not solving the problem switch your standard printer to “Microsoft XPS Document Writer” and try again to start Kdenlive.

Delete the :file:`kdenliverc` file.

Make sure you set concurrent threads to ``1``: Go to :menuselection:`Menu --> Settings --> Configure Kdenlive` (or :kbd:`Ctrl+Shift+,`) and then in :menuselection:`Environment --> Proxy and Transcode Jobs` set :guilabel:`Concurrent threads` to ``1``.


Audio pops and ticks in render
------------------------------

The current Kdenlive version (November 2018, version 18.08.3) has audio issues that have workarounds. If this problem appears make sure the audio file uses 16-bit PCM WAV format.
