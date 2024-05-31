.. meta::
   :description: Kdenlive Tips & Tricks - Using Camcorder Proxy Clips
   :keywords: KDE, Kdenlive, useful information, import external proxy clips, camcorder, camera, editing, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             
   :license: Creative Commons License SA 4.0

.. moved from https://community.kde.org/Kdenlive/Development/externalProxy


.. _using_camcorder_proxy_clips:

Using Camera Proxy Clips
========================

.. .. versionadded:: 19.04
   .. versionchanged:: 23.08
   .. versionchanged:: 24.05

Kdenlive supports using external proxy clips. Some cameras, like Sony PXW-X70 and others allow you to record proxy clips during the normal recording operation.

For Sony camcorders, the file layout is the following:

- On your :abbr:`SD (Secure Digital - a proprietary, non-volatile, flash memory card format developed by the SD Association)` card, you will have a folder with original full resolution clips (called "Clips") and a folder with low res proxy clips (called "Sub").
- The proxy clips will end with "S03.MP4" instead of ".MXF".

For example: 

**Original clip:**
   Clips/Clip0001.MXF
**Proxy:**
   Sub/Clip0001S03.MP4

You can create your own external camcorder proxy links directly in the :ref:`proxy clip setup <configure_proxy_clips>`.

Or you can do it manually: In Kdenlive we have a file called :file:`externalproxies.rc` that will be installed in :code:`$INSTALL_PREFIX/share/kdenlive/externalproxies.rc` (Windows: :code:`KDENLIVE_INSTALL_FOLDER/bin/data/kdenlive/externalproxies.rc`). This is a text file that lists supported camera profiles giving indication about the path and name of proxy clips. This is currently in the form:

.. code-block:: cfg

   profile name=<proxy_folder> (relative to original clip); <proxy clip prefix>; <proxy clip suffix>; <original_folder> (relative to proxy file); <original_clip_prefix>; <original_clip_suffix>

Following camera proxies are supported: 

.. code-block:: cfg

   Sony PXW=../Sub;;S03.MP4;../Clip;;.MXF
   GoPro LRV=./;GL;.LRV;./;GX;.MP4;./;GP;.LRV;./;GP;.MP4;./;GOPR;.LRV;./;GOPR;.MP4
   Akaso LRV=./;;.LRV;./;;.MP4
   DJI LRF=./;;.LRF;./;;.MP4
   Insta360 AcePro LRV=./;LRV;.lrv;./;VID;.mp4;./;PRO_LRV;.lrv;./;PRO_VID;.mp4


In order to use the already available proxy files go to the project settings, and in the tab :ref:`configure_proxy_clips` check :guilabel:`Enable proxy clips` if not enabled already, and then check :guilabel:`External proxy clips` and select your camera profile. Now when you add a clip to your project, Kdenlive will automatically use the camera generated proxy instead of creating a new one. You can also directly add the proxy clip in the project and it will be recognized as a proxy.

.. |send_us| raw:: html

   <a href="mailto:contact@kdenlive.org">send us</a>

This greatly improves workflow if you have such a camera. Other camera brands also enable the creation of proxy clips, so if you have one, please |send_us| information about the path and naming schemes so we can include it in Kdenlive. 
