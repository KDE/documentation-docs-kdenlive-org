.. meta::
   :description: Kdenlive Documentation - Configuration Capture Firewire
   :keywords: KDE, Kdenlive, documentation, user manual, configuration, preferences, capture, firewire, video capture, video editor, open source, free, learn, easy


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


.. attention:: This page is not maintained anymore and contains information referring to features or functions from earlier versions of Kdenlive that are deprecated or have been superseded by something else.


Configure Firewire Capture
~~~~~~~~~~~~~~~~~~~~~~~~~~

The image shows the Configure Firewire capture tab which can be accessed from the :menuselection:`Settings --> Configure Kdenlive` menu or from the spanner icon in the capturing.


.. image:: /images/Kdenlive_Configure_Capture.png
   :width: 500px
   :alt: Kdenlive_Configure_Capture



The firewire capture functionality uses the `dvgrab <http://linux.die.net/man/1/dvgrab>`_ program.
The settings applied here to define how dvgrab will be used to capture the video. 

**Capture Format options** are

* DV RAW
* DV AVI Type 1
* DV AVI Type 2
* HDV

The first three are quality-wise the same (exactly the same DV 25Mb/s standard definition codec), just packed differently into the file. Type 2 seems to be the most widely supported by other applications.

The raw format contains just the plain video frames (with audio interleaved) without any additional information. Raw is useful for some Linux software. Files in this format can also be played with Windows QuickTime when renamed to :file:`file.dv`.

AVI files may contain multiple streams. Typically, they include one video and one audio stream. The native DV stream format already includes the audio interleaved into its video stream. A type 1 DV AVI file only includes one DV video stream where the audio must be extracted from the DV video stream. A type 2 DV AVI file includes a separate audio stream in addition to the audio data already interleaved in the DV video stream. Therefore, the type 2 DV AVI file is redundant and consumes more space.

HDV is a high-definition format used on tape-based HD camcorders.

**Add recording time to captured file name** option: If this is unchecked then each captured file will get a sequential number post-pended to the file names listed in the Capture file name setting. With this checked, date and timestamp (derived from when the footage was captured) is post-pended to the capture file name, e.g. **capture2012.07.15_11-38-37.dv**

**Automatically start a new file on scene cut** option:  With this checked it tries to detect whenever a new recording starts, and store it into a separate file. This is the -autosplit parameter in  `dvgrab <http://linux.die.net/man/1/dvgrab>`_  and it works by detecting timecode discontinuities from the source footage.  Where a timecode discontinuity is anything backward or greater than one second it will start a new capture file.

The **dvgrab additional parameters** edit box allows you to add extra dvgrab switches to the capture process that will run. See  `dvgrab manual <http://linux.die.net/man/1/dvgrab>`_ for more info.