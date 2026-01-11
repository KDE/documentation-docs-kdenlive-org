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
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0

.. attention:: This page is not maintained anymore and contains information referring to features or functions from earlier versions of Kdenlive that are deprecated or have been superseded by something else.


Capturing Video
===============


Firewire
--------


This captures video from sources connected via a firewire (also known as -  IEEE 1394 High Speed Serial Bus) card and cable. This functionality uses the `dvgrab <http://linux.die.net/man/1/dvgrab>`_ program and the settings for this can be customized by clicking the spanner icon or choosing  :menuselection:`Settings --> Configure Kdenlive`.  See :doc:`Configure Kdenlive</getting_started/configuration>`.


To perform a capture:


* Plug in your device to the firewire card and turn it on to play mode


* Click the *Connect Button* 

.. figure:: /images/Kdenlive_Connect_firewire_button.png
  :align: left
 
* Click the Record Button – note it toggles to grey while you are recording


* Click the Record button again to stop capture. Or click the stop button.


* Once capturing is finished, click the disconnect button 

.. figure:: /images/Kdenlive_Disconnect_capture.png
  :align: left
 

* In the *Captured Files* dialog, click the import button to have the captured files automatically imported into the project bin.


.. figure:: /images/Kdenlive_Captured_files_dialog.png
  :align: left
 

.. note::

  If your device does not start playing the source device when you click the record button, you may have to start playback on your device manually and then click record.


FFmpeg
------

I believe this captures video from an installed Web Cam using *Video4Linux2*.

