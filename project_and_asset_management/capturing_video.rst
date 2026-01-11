.. meta::
   :description: Kdenlive Documentation - Capturing Video
   :keywords: KDE, Kdenlive, project bin, file, management, capturing, video, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jessej (https://userbase.kde.org/User:Jessej)
             - Jack (https://userbase.kde.org/User:Jack)
             - Roger (https://userbase.kde.org/User:Roger)
             - Julius Künzel <jk.kdedev@smartlab.uber.space
             - Eugen Mohr <to_be_documented>
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |dvgrab| raw:: html

   <a href="http://linux.die.net/man/1/dvgrab" target="_blank">dvgrab</a>

.. |blackmagic| raw:: html

   <a href="https://www.blackmagicdesign.com" target="_blank">Blackmagic</a>

.. |decklink| raw:: html

   <a href="https://www.blackmagicdesign.com/products/decklink" target="_blank">Decklink</a>


Capturing Video
===============

**Kdenlive** provides functionality for capturing video using |blackmagic|'s |decklink|, and via ScreenGrab.

For other devices, mostly connected via Firewire (also known as IEEE 1394 High Speed Serial Bus) card and cable, use |dvgrab| directly in a terminal.

You configure video capturing from :menuselection:`Menu --> Settings --> Configure Kdenlive -->` :doc:`Capture</getting_started/configure_kdenlive/configuration_capture>`.

You define the destination location for your captures by using :menuselection:`Menu --> Settings --> Configure Kdenlive --> Environment -->` :ref:`Default Folders<configure_environment_default_folders>`.


Screen Grab
-----------

This captures video off the PC screen. Enable the Screen Grab widget via :menuselection:`Menu --> View --> Screen Grab`.

.. hint:: 
  Any issues or errors with the screen grab are displayed in the Clip Monitor widget. It is recommended to move the Screen Grab widget to a position where the clip monitor is easily visible. For example, the Screen Grab widget can be added to the dock where the Project Bin or the Library is. Docking it to the Clip Monitor widget prevents a message from being visible.

.. figure:: /images/project_and_asset_management/capture_screen_grab.webp
   :width: 292px
   :figwidth: 292px
   :align: left
   
   The Screen Grab widget

:guilabel:`Monitor 0/1`:
  Select the monitor to record from

|media-record|\ :guilabel:`Screen Grab`:
  Start/Stop recording

|configure|\ :guilabel:`Configure Recording`:
  Opens the Kdenlive :menuselection:`Menu --> Settings --> Capture -->` :doc:`Screen Grab</getting_started/configure_kdenlive/configuration_capture>` window

.. rst-class:: clear-both

The recorded clip will be added to the project bin.

.. rubric:: Possible issues

Screen grab uses ffmpeg for recording and encoding. Most issues have to do with the version of ffmpeg installed or how ffmpeg was compiled.

Specifically, ffmpeg needs ``--enable-x11grab`` to work for screen grab. Check your Linux distro for this parameter for ffmpeg by typing ``ffmpeg -version`` in a terminal and look for that parameter in the information reported back by ffmpeg. [1]_ 

If you are capturing the screen and using the :guilabel:`x246 with audio` setting, the recording may crash. In this case create an Encoding Profile for Screen Capture where ``-acodec pcm_s16le``  is replaced by ``-acodec libvorbis -b 320k``.


Blackmagic
----------

This is for capturing from Blackmagic's |decklink| video capture cards.

.. note:: 
  There has been no major development or testing with this part of Kdenlive. It may work, it may have issues. No bug reports have been created, but there is not knowing how many users actually perform video capturing with this hardware.



----

.. [1] There are now two branches of *ffmpeg*: a *Libav* branch and an ffmpeg.org branch. The *ffmpeg* version from the latter branch reports the configuration when you run with ``ffmpeg -version``. The *Libav* version does not. So this method to check for the ``--enable-x11grab`` does not work if you have the *Libav* version of *ffmpeg*.
