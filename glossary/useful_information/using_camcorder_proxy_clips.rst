.. meta::
   :description: Editing in Kdenlive video editor
   :keywords: KDE, Kdenlive, useful information, import external proxy clips, editing, documentation, user manual, video editor, open source, free, learn, easy


.. metadata-placeholder

   :authors: - Eugen Mohr
             
   :license: Creative Commons License SA 4.0

.. moved from https://community.kde.org/Kdenlive/Development/externalProxy

..
  Copy/paste from EXCEL sheet direct into the online converter.
  Grid tables online converter: https://www.tablesgenerator.com/text_tables 
  On top of the converter click on tab "text"
  On the bottom set "to reStructuredText syntax". Now the table header line is bold.
   

.. _using_camcorder_proxy_clips:

Using camera proxy clips
========================

.. versionadded:: 19.04

.. versionchanged:: 23.08

Kdenlive's refactoring version, due in April 2019 now supports using external proxy clips. Some cameras, like Sony PXW-X70 and others allow you to record proxy clips during the normal recording operation.

For Sony camcorders, the file layout is the following:

   - On your SD card, you will have a folder with original full resolution clips (called "Clips") and a folder with low res proxy clips (called "Sub").
   - The proxy clips will end with "S03.MP4" instead of ".MXF".

For example: 

**Original clip:**
   Clips/Clip0001.MXF
**Proxy:**
   Sub/Clip0001S03.MP4

In Kdenlive we now have a file called externalproxies.rc that will be installed in $INSTALL_PREFIX/share/kdenlive/externalproxies.rc / Windows: KDENLIVE_INSTALL_FOLDER/bin/data/kdenlive/externalproxies.rc. This is a text file that lists supported camera profiles, giving indication about the path and name of proxy clips. This is currently in the form: profile name = Proxy folder (relative to original clip) ; Proxy clip prefix; Proxy clip suffix; Original folder (relative to proxy file); original clip prefix; original clip suffix.

Following camera proxies are supported: 

.. code-block::

   Sony PXW=../Sub;;S03.MP4;../Clip;;.MXF
   GoPro LRV=./;GL;.LRV;./;GX;.MP4;./;GP;.LRV;./;GP;.MP4;./;GOPR;.LRV;./;GOPR;.MP4
   Akaso LRV=./;;.LRV;./;;.MP4
   DJI LRF=./;;.LRF;./;;.MP4


Then, in the project settings under :ref:`configure_proxy_clips` you can check the "External proxy" feature and select your camera profile. Then, you can add a clip to your project, and it will automatically use the camera generated proxy instead of creating a new one. You can also directly add the proxy clip in the project and it will be recognized as a proxy.

This greatly improves workflow if you have such camera. Other camera brands also enable the creation of proxy clips, so if you have one, please send us information about the path and naming schemes so we can include it in Kdenlive 