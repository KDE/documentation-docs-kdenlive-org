.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Vincent Pinon <vpinon@kde.org>
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jessej (https://userbase.kde.org/User:Jessej)
             - Dbolton (https://userbase.kde.org/User:Dbolton)
             - Jack (https://userbase.kde.org/User:Jack)
             - Roger (https://userbase.kde.org/User:Roger)
             - KGHN (https://userbase.kde.org/User:KGHN)

   :license: Creative Commons License SA 4.0

.. _render:

Rendering
=========

..
  TODO:
  * How to choose the correct output format and bit rate?   * What to do for rendering lossless, for an iPhone, or whatever? (Dropdown containing targets like lossless/HQ/player)   


.. contents::


Rendering is the process where the edited clips are saved into a single complete video clip. During the rendering process the video can be compressed and converted to a number of different video formats (aka codecs).


The rendering dialog is brought up from the render button |media-record| from selecting :menuselection:`Render` in the :ref:`project_menu`  or by the :kbd:`Ctrl + Enter` shortcut.


Rendering Dialog Ver 17.04
--------------------------

.. image:: /images/Kdenlive_Render_dialog_17_04.png
   :alt: File rendering dialog - ver 17.04


Rendering Profile Categories
----------------------------

.. image:: /images/Kdenlive_Render_dialog_17_04_categories_expanded.png
   :alt: File rendering categories- ver 17.04


**Kdenlive** offers many different preset rendering profiles to choose from. The rendering profiles are grouped into categories. See picture Above.


.. image:: /images/Kdenlive_Rendering_options2.png
   :alt: Kdenlive_Rendering_options2


File Rendering - earlier Versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following figures show the render dialog when the :menuselection:`Destination` category is **File Rendering**. The first two figures show the layout of the dialog under ver 0.9.10 of **Kdenlive** and the third figure shows how the dialog appears in ver 0.9.8 of **Kdenlive**. 


Version 0.9.10 of **Kdenlive** changes the render dialog significantly because it implements a method where you can choose to render the project with either a variable video bitrate (VBR) or a constant video bitrate (CBR)


Variable Bit Rate - earlier Versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /images/Kdenlive_Render_dialog_vbr_0.9.10.png
   :alt: File rendering dialog Variable Bit Rate - ver 0.9.10


When a variable bitrate profile is selected, the :menuselection:`File Size` section displays a drop down for choosing the **Video quality** you want. This quality figure is a codec-dependent number representing the quality of the video that will be rendered. Generally, lower numbers mean higher quality video and larger file sizes (e.g. x264, MPEG2, VPx), but some codecs use opposite order (e.g. Theora). Profiles provided with **Kdenlive** offer these numbers ordered from best quality (almost lossless) to lower quality (still not degrading too much).  The exact file size that is produced can not be predicted when using the VBR method.  The idea behind this is that you specify a certain quality of video that you want through the entire video and the encoding optimizes bitrate to give you that constant quality, lowering data size for low action scenes and using more bits for high action scenes.


Example: 1min 55 seconds of 720 x 576 H.264 iPhone footage rendered at quality 15 with the H.264/AAC High Profile would produce a file size of 186 Mb. Whereas rendering the same footage at quality quality 20 produced an 83Mb file.


Constant Bit Rate - earlier Versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /images/Kdenlive_Render_dialog_cbr_0.9.10.png
   :alt: File rendering dialog Constant Bit Rate - ver 0.9.10


When a constant bitrate (CBR) profile is selected, the :menuselection:`File Size` section displays a drop down for choosing the **Video bitrate** you want. This is similar to the version <=0.9.8 behaviour of **Kdenlive**. You select the video bitrate you want and the video is encoded at that video bitrate across its entire length.

.. image:: /images/Kdenlive_Render_dialog_0.9.8.png
   :alt: File rendering dialog - ver 0.9.8


DVD Rendering - earlier Versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DVD Rendering produces files that are compatible with DVD authoring software.  MPEG2 files created from :ref:`render` profiles are less likely to be compatible with DVD software.  For quality settings see :ref:`render` and :ref:`render`. For DVD VBR lower :menuselection:`Video quality` setting number means better quality.

Note that this rendering does not create a DVD file system. It merely creates DVD-compatible MPEG2 files that can be used by DVD authoring software.  If you check the :menuselection:`Open DVD Wizard after Rendering` check box, then the :ref:`dvd_wizard` will open and you can use it to create a DVD file system (in .ISO format).  The DVD Wizard is also available from the :ref:`file_menu`.  

:menuselection:`Create chapter file based on guides` enables chapter markings on your DVD. Chapters work with the "next" and "previous" buttons on the DVD player and can populate scene selection menus. In order to create chapters this way you need to have marked chapters with  :ref:`guides` on timeline. DVD wizard enables marking of chapters also during DVD creation step.


.. image:: /images/Kdenlive_DVD_rendering.png
   :alt: Kdenlive_DVD_rendering


Websites  - earlier Versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /images/Kdenlive_WebSites_rendering.png
   :alt: Kdenlive_WebSites_rendering


Mobile Devices  - earlier Versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /images/Kdenlive_Mobile_devices.png
   :alt: Kdenlive_Mobile_devices


Create Custom Render Profiles
-----------------------------

You can create your own custom render profiles by clicking the button highlighted in the screenshot below.


.. image:: /images/Custom_render_profiles.png
   :width: 350px
   :alt: Custom_render_profiles

|document-new|

This will open the **Save Profile** dialog (also shown in the above screenshot) and the :menuselection:`Parameters` section will be filled in with the render parameters of the profile that you had selected when you clicked the |document-new| button. You can edit values in the parameters and save your own custom render profile.


The parameters in the rendering profile are *melt* parameters. For an explanation of their meaning, check the *melt* `documentation <http://www.mltframework.org/bin/view/MLT/Documentation>`_ or type ``melt -help`` in a command prompt.


The above screenshot shows the **Save Profile** dialog as it appears in version <=0.9.4 of **Kdenlive**.


In version >=0.9.5 there is an improved version of the **Save Profile** dialog (see below) which allows you to customize the bitrates that are offered in the render profile.


.. image:: /images/Kdenlive_Custom_render_profile_0.9.5.png
   :width: 350px
   :alt: Kdenlive_Custom_render_profile_0.9.5


See also :ref:`render_profile_parameters`


Rendering In Batch mode
-----------------------

If you have a lot of rendering jobs to do, you can use **Kdenlive** to create rendering scripts which you can accumulate and then execute in batch mode overnight. See :ref:`rendering`.


Alternatively, once you have submitted a rendering job on a project and it is up and running in the **Job Queue**, you can drag the render window out of the way and edit the project some more or load a new project and render that one too. The second render job submitted will go into the **Job Queue**. Editing the project after a render job is submitted will not change the settings on that job.


.. image:: /images/Kdenlive_Rendering_job_queue.png
   :width: 400px
   :alt: Kdenlive_Rendering_job_queue


Rendering Using the Guide Zone Option
-------------------------------------

This makes use of :ref:`guides` to define a region of the project that is to be rendered. See :ref:`rendering`.


Rendering Using the Selected Zone Option
----------------------------------------

If you select the :menuselection:`Selected Zone` radio button from the bottom of the render dialog, **Kdenlive** will only render that portion of the project which has a selected zone created for it. See :ref:`monitors`


Render Overlay
--------------

.. image:: /images/Kdenlive_Render_overlay.png
   :align: left
   :alt: Kdenlive_Render_overlay


This option overlays a time code or frame count over the rendered video.  This will put the overlay over the entire rendered project.  Alternatively you can use the :ref:`dynamic_text` effect to overlay selected regions of the video.


.. image:: /images/Kdenlive_Render_overlay_result_eg.png
   :width: 150px
   :alt: render overlay result


Export Metadata
---------------

Check this to have the metadata which has been entered under :menuselection:`Project Settings- >` :ref:`project_settings`  placed into the metadata of the rendered file.


In version 0.9.6 for Linux, you have to double-click the data area of a metadata field line to make the field available for input.


This image shows metadata settings for a project:


.. image:: /images/Kdenlive_project_settings_metadata.png
   :alt: Kdenlive_project_settings_metadata


And this is the metadata on the resulting clip (rendered with :menuselection:`Export Metadata` checked).


.. image:: /images/Kdenlive_Clip_properties_metadata_res.png
   :alt: Kdenlive_Clip_properties_metadata_res


.. code-block:: bash

  $ ffprobe dog_rotated_meta_data.mp4


.. code-block:: bash

  
      Metadata:
      major_brand     : isom
      minor_version   : 512
      compatible_brands: isomiso2avc1mp41
      title           : Bailey
      encoder         : Lavf53.21.1
      copyright       : VSF
  


This reveals a bug in ver 0.9.4 of **Kdenlive** - the full title is not placed in the metadata - it is truncated at the first space. This has been fixed in 0.9.5 of **Kdenlive** as mentioned in legacy Mantis bug tracker ID 2996.


Export Audio Checkbox
---------------------
 
This is an unusual one. Instead of a normal on/off checkbox toggle, the :menuselection:`Export Audio` checkbox cycles among three choices.

As if that weren't confusing enough, the *Export audio (automatic)* option may appear different depending on your combination of distribution, desktop environment and theme.  See three examples below:

Regardless of how the checkbox on the *Export audio (automatic)* option may appear on your installation, rest assured that when that option is showing, it is enabled.


So what do the three options mean?


.. image:: /images/Kdenlive_Export_audio_check_box_crop.png
   :alt: Kdenlive_Export_audio_check_box_crop

*Export audio (automatic)* means detect if an audio track is present and write the audio track if found


.. image:: /images/kdenlive_export_audio_checked_ubuntu.png
   :alt: kdenlive_export_audio_checked_ubuntu

*Export audio*, when checked, means write an audio track in the rendered file even if there is no audio track to write.


.. image:: /images/kdenlive_export_audio_unchecked_ubuntu.png
   :alt: kdenlive_export_audio_unchecked_ubuntu

*Export audio*, when unchecked, means do not write an audio track in the rendered file.


The difference in behavior between enabling *Export audio* versus *Export audio (automatic)* can be seen in the situation where you have a video on the timeline but there is no audio track on the timeline and the video in the video track also does not have an audio track. An example of such a situation is shown in the screenshot below.


.. image:: /images/Kdenlive_Video_with_no_audio.png
   :alt: Kdenlive_Video_with_no_audio


In this situation, if you render with *Export audio (automatic)*, the rendered file will not have an audio track (Result 1 on screenshot below). But if you render with *Export Audio* checked, then the rendered file will contain an audio track – the track will however be empty  (Result 2 on screenshot below).


.. image:: /images/Kdenlive_Render_export_audio_auto_vs_just_checked2.png
   :alt: Kdenlive_Render_export_audio_auto_vs_just_checked2


FFprobe on file generated from an audio-less track using *Export audio (automatic)*. Note only one stream – Stream #0.0 – a video stream. **Kdenlive** automatically detected there was not an audio track and so it did not write one.


.. code-block:: bash

  $ ffprobe dog_rotated_exp_audio_auto.mp4


.. code-block:: bash

    Metadata:
      major_brand     : isom
      minor_version   : 512
      compatible_brands: isomiso2avc1mp41
      encoder         : Lavf53.21.1
  Duration: 00:00:03.62, start: 0.000000, bitrate: 12592 kb/s
  Stream #0.0(und): Video: h264 (High), yuv420p, 1280x720 [PAR 1:1 DAR 16:9], 12587 kb/s, 27.83 fps, 27.83 tbr, 30k tbn, 55.66 tbc
  


FFprobe on file generated from an audio-less track using *Export audio* checked. Note two streams – Stream #0.0 and Stream #0.1 – the latter being an aac audio track.  We forced **Kdenlive** to write an audio track even though there was not any source audio to write.

.. code-block:: bash

  $ ffprobe dog_rotated_exp_audio.mp4


.. code-block:: bash

  
    Metadata:
      major_brand     : isom
      minor_version   : 512
      compatible_brands: isomiso2avc1mp41
      encoder         : Lavf53.21.1
    Duration: 00:00:03.62, start: 0.000000, bitrate: 12598 kb/s
  
  
  Stream #0.0(und): Video: h264 (High), yuv420p, 1280x720 [PAR 1:1 DAR 16:9], 12587 kb/s, 27.83 fps, 27.83 tbr, 30k tbn, 55.66 tbc
  Stream #0.1(und): Audio: aac, 48000 Hz, stereo, s16, 2 kb/s
  


In cases where there is an audio track ...


.. image:: /images/Kdenlive_Video_plus_Audio_in_seperate_tracks.png
   :align: left
   :alt: Kdenlive_Video_plus_Audio_in_seperate_tracks


Rendering with :menuselection:`Export audio` unchecked will produce a file with no audio track – result 4 in the screenshot above.
Rendering with :menuselection:`Export audio (automatic)`  (result 3  in the screenshot above) or with  *Export audio* checked will produce files with Audio tracks.


Encoder Threads
---------------

.. image:: /images/Kdenlive_Encoder_threads.png
   :align: left
   :alt: Kdenlive_Encoder_threads


Determines the value of *Encoding threads* passed to melt.  For encoding to certain codecs, namely MPEG-2, MPEG-4, H.264, and VP8, kdenlive can use more than one thread and thus make use of multiple cores. Increase this number to take advantage of this feature on multi-core machines.  See `melt doco - threads <http://www.mltframework.org/bin/view/MLT/ConsumerAvformat#threads>`_ and `melt FAQ <http://www.mltframework.org/bin/view/MLT/Questions#Does_MLT_take_advantage_of_multi>`_ on multi-threading.


Scanning Dropdown
-----------------

.. image:: /images/Kdenlive_Render_scanning.png
   :alt: Kdenlive_Render_scanning


This option controls the frame scanning setting the rendered file will have. 
Options are *Force Progressive*, *Force Interlaced* and  *Auto*. 

:menuselection:`Auto` causes the rendered file to take the scanning settings that are defined in the :ref:`project_settings`. Use the other options to override the setting defined in the project settings.
