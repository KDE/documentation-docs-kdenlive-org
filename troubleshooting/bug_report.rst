.. meta::
   :description: Troubleshooting Kdenlive - Filing a Bug Report
   :keywords: KDE, Kdenlive, troubleshooting, documentation, user manual, video editor, open source, free, learn, easy, bug report

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |bug_tracker| raw:: html

   <a href="https://bugs.kde.org/" target="_blank">bug tracker</a>

.. |bug_tracker_URI| raw:: html

   <a href="https://bugs.kde.org/" target="_blank">bugs.kde.org</a>

.. |bug_tracker_search| raw:: html

   <a href="https://bugs.kde.org/buglist.cgi?bug_status=__open__&amp;product=kdenlive" target="_blank">Search the bug tracker</a>

.. |r_kdenlive| raw:: html

   <a href="https://www.reddit.com/r/kdenlive/" target="_blank">r/kdenlive</a>

.. |official_forum| raw:: html

   <a href="https://discuss.kde.org/tag/kdenlive" target="_blank">official forum on Discuss</a>

.. |discord_1| raw:: html

   <a href="https://discord.gg/Sk5kk3Pjnn" target="_blank">Discord</a>

.. |discord_2| raw:: html

   <a href="https://discord.gg/" target="_blank">Arkengheist's Discord</a>
   
.. |flatpak_debugging| raw:: html

   <a href="https://docs.flatpak.org/en/latest/debugging.html" target="_blank">https://docs.flatpak.org/en/latest/debugging.html</a>
   


.. _troubleshooting-bug_report:

Filing a Bug Report
===================

Bugs happen. That is a fact. But they can be fixed. And the better a bug report is the easier it is for the development team to replicate, investigate, and eventually fix it.

All bug reports need to be logged in the official |bug_tracker|. And feature requests are tracked there as well using the severity item wishlist.

First Things First
------------------

But before you do, please do the following:

.. rubric:: Step 1: Upgrade to the latest release

Please upgrade to the latest released versions of Kdenlive. We do not answer bug reports for old Kdenlive versions (unless they are still reproducible in the latest version).

.. rubric:: Step 2: Search the official Kdenlive documentation

RTFM - *Read The Fine Manual* is a phrase often used to mock users asking questions that could be answered by reading the documentation. In the days and age of YouTube tutorial this may not be as important or relevant anymore, but you are encouraged to consult the official Kdenlive documentation. It can be searched and contains a wealth of good and valuable information.

.. rubric:: Step 3: Search the forums

Kdenlive has a large community that is active in forums and chat rooms. Check the |official_forum| whether other users encountered the same issue. Perhaps a fix or workaround exists. Other channels to check are

- |r_kdenlive| subreddit
- |discord_1|\ [1]_
- Telegram
- Mastodon

.. rubric:: Step 4: Query open issues

|bug_tracker_search|. Perhaps the issue you are experiencing has already been reported or is even being worked on. The bug's status is a good indicator for what is currently happening:

- :guilabel:`REPORTED` is a bug that has been reported but nothing has happened so far. There may be a discussion about it, so it is worth checking if it may apply to your issue.
- :guilabel:`NEEDSINFO` is a reported bug, which needs more feedback. This means, a dev team member looked at it but needs more details.
- :guilabel:`CONFIRMED` means that the bug can be reproduced (either by other users or the dev team)
- :guilabel:`ASSIGNED` means that a developer is handling the bug
- :guilabel:`RESOLVED` means that the bug was fixed in the development version

.. rubric:: Step 5: Report the bug

If you have a crash at Kdenlive startup or when trying to play a video file, please follow these steps:

- If you compiled Kdenlive and/or MLT yourself, make sure you followed all steps described in our instructions.
- Check that you don't have several versions of MLT installed
- Try playing your video file with FFmpeg's player. From a terminal: :code:`ffplay myvideo.mpg`
- Try playing your video file with MLT's player. From a terminal: :code:`melt myvideo.mpg`

Include the results in your :ref:`bug report<troubleshooting-bug_enter>` as **attachments**.

.. _troubleshooting_good_bug_report:

For a good bug report please include the following information:

- Your Kdenlive and MLT version. You can copy that information from Kdenlive :menuselection:`Menu --> Help --> About`.
- Your operating system (OS), like Windows, Linux distro, or MacOS including the respective version
- The installation method for Kdenlive, like Windows installer or standalone, or Linux flatpak or appimage
- Detailed steps to reproduce the bug. Screenshots and screen recordings are very useful for replicating the issue.
- Any error messages or log files you can provide. Please do not copy & paste log content into the bug report but add it as an **attachment**.
- If the bug crashes Kdenlive, provide a backtrace.

.. _troubleshooting_bug_backtrace:

:How to get useful crash information (backtrace):

A backtrace contains valuable information for the dev team. It needs a bit of OS specific setup and command line wizardy and may therefore be not everyone's cup of tea.

:Linux appimage:
   Please install the following packages: gdb, kdenlive-dbg, libmlt-dbg (package names may be slightly different depending on your distro)

   When Kdenlive crashes, if the KDE crash handler dialog pops up, you can copy the data it provides. Otherwise, start Kdenlive from a terminal like this:

   Type :code:`gdb kdenlive`

   After gdb read debug symbols, type :code:`run`

:Linux Flatpak:
   First of all make sure the Flatpak debug symbols are installed by typing :code:`flatpak install org.kde.kdenlive.Debug` to a command line.

   Now you can start the Flatpak from a command line like this:

   - Start a shell inside the Kdenlive Flatpak sandbox: :code:`flatpak run --command=sh --devel org.kde.kdenlive`
   - Type :code:`gdb /app/bin/kdenlive`
   - After gdb read debug symbols, type :code:`run`

   For more details on Flatpak debugging see here: https://docs.flatpak.org/en/latest/debugging.html

:Windows:
   Build Kdenlive with KDE Craft locally as described here:
   
   - Type to the command line :code:`cd C:/CraftRoot/mingw64/bin`
   - Start gdb with :code:`gdb`
   - Start Kdenlive -> get the PID number
   - :code:`attach 3288` (replace 3288 by the PID number)
   - Wait on the (gdb) prompt
   - Type :code:`c`

   Once you followed the platform specific instructions above to start Kdenlive, you can trigger the bug. When Kdenlive crashes, go to your terminal window and type:

   :code:`thread apply all bt full`

   Then press enter until you see the full data. Copy the log to a file and attach it to the bug report as an **attachment**.


.. _troubleshooting-bug_enter:

Creating the Bug Report
-----------------------

Now that you have all the relevant and important information, it is time to file the bug report in the official KDE Bug Tracker, Bugzilla.

Open a browser and enter |bug_tracker_URI| in the URI field.

.. figure:: /images/troubleshooting/kde_bugtracking_system.webp
   :width: 450px
   :figwidth: 450px
   :align: left

   KDE Bug Tracking System welcome screen

You may need to log on first or even create a user account. Please follow the onscreen instructions for that.

Click on :guilabel:`File a Bug`.

.. container:: clear-both
   
   .. figure:: /images/troubleshooting/kde_bug_classification.webp
      :width: 450px
      :figwidth: 450px
      :align: left
   
      KDE Bug Tracking System classification selection

   Click on :guilabel:`Application` to get to the list of all applications using Bugzilla.

.. container:: clear-both
   
   .. figure:: /images/troubleshooting/kde_bug_application.webp
      :width: 450px
      :figwidth: 450px
      :align: left
   
      KDE Bug Tracking System application selection

   The list is sorted alphabetically. Scroll down to where Kdenlive is listed, or use :kbd:`Ctrl+F` to open a search field and enter `kdenlive`. This should work in most browsers but may be different in yours.

.. rst-class:: clear-both

Bugzilla will open the detailed bug report screen where you can enter the bug report. Some fields are mandatory (indicated by the red \*) and some will be populated with data collected from your system.

.. figure:: /images/troubleshooting/kde_bug_enter.webp
   :width: 650px
   :figwidth: 650px

   KDE Bug Tracking System entering bug details

:1: The bug report will be filed under your user name's email address
:2: Select a component that best fits the type of problem you encountered
:3: Select the version of Kdenlive you are using
:4: Specify the severity of the problem. If you want to create a feature request, select :guilabel:`wishlist`.
:5: Select the platform you are using. This helps when troubleshooting.
:6: Select the operating system (OS) you are using
:7: Enter a short but descriptive summary if the bug or problem you are reporting
:8: This is where you describe the problem in more detail. The text between **\*\*\*** is for informational purpose only trying to prevent unnecessary bug reports. If you want to continue filing a bug report, please select this text and delete it. Then start entering your problem description.

    Please be as detailed as possible describing what you did when the bug was triggered or Kdenlive did not work as expected.

    There are a few sections prescribed already, like :guilabel:`Step to Reproduce`, :guilabel:`Observed Results`, and :guilabel:`Expected Results` that guide you through the bug report. It just helps structuring the report for easy reference and replication by the developer team.

    In the section :guilabel:`Software/OS Version` you can paste the relevant data from Kdenlive :menuselection:`Menu --> Help --> About Kdenlive --> Components --> Copy to Clipboard`.

    .. figure:: /images/troubleshooting/kde_bug_kdenlive_components.webp
      :width: 400px
      :figwidth: 400px
   
      Copy information from Kdenlive

:9: You can add attachments like screen recordings, screenshots, and text files with debugging and terminal output information.
:10: Click :guilabel:`Submit Bug` to file your bug report


----

.. [1] This is a privately maintained server and not affiliated in any way, shape, or form with Kdenlive