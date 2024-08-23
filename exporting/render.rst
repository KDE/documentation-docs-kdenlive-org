.. meta::
   :description: The Kdenlive User Manual
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, help, learn, render, render parameter, render zone, render multiple zone

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Nikerabbit (https://userbase.kde.org/User:Nikerabbit)
             - Simon Eugster <simon.eu@gmail.com>
             - Jean-Baptiste Mardelle <jb@kdenlive.org>
             - Earl fx (https://userbase.kde.org/User:Earl fx)
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Vincent Pinon <vpinon@kde.org>
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jessej (https://userbase.kde.org/User:Jessej)
             - Dbolton (https://userbase.kde.org/User:Dbolton)
             - Jack (https://userbase.kde.org/User:Jack)
             - Roger (https://userbase.kde.org/User:Roger)
             - KGHN (https://userbase.kde.org/User:KGHN)
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _render:

Rendering
=========

.. TODO:
   * How to choose the correct output format and bit rate? * What to do for rendering lossless, for an iPhone, or whatever? (Dropdown containing targets like lossless/HQ/player)


The rendering dialog is brought up by selecting |media-record| Render... from the :menuselection:`Menu --> Project`, or by the :kbd:`Ctrl+Enter` default keyboard shortcut.


Rendering Dialog
----------------

.. .. versionchanged:: 22.12
.. .. versionchanged:: 24.02
.. .. versionchanged:: 24.05
   
 
.. figure:: /images/exporting/kdenlive2405_rendering-render_dialog.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2402_rendering-render_dialog

   Rendering dialog window

* Output file - Enter the location in your file system where the video file will be stored

* |document-new| :ref:`Create new preset <manage_project_profiles>` - Opens the dialog to create a new preset based on the selected preset.

* |edit-download| :ref:`Download New Render Presets <download_new_render_profiles>` - Opens a window displaying user-created presets available from the KDE Store for download

* |document-save-as| Save Current Preset as :ref:`New Custom Preset <manage_project_profiles>` - Copies the selected preset and opens the dialog to modify this preset (will be saved under a new name)

* |document-edit| :ref:`Edit Preset <manage_project_profiles>`- Opens the dialog to modify the preset (only available for custom or downloaded presets)

* |edit-delete| - Delete preset (only for custom or downloaded presets)

.. rst-class:: clear-both

.. figure:: /images/exporting/kdenlive2405_rendering-render_dialog_2.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2405_rendering-render_dialog_2

   Rendering dialog window

* :guilabel:`Full project` - Render the entire project (default)

* :guilabel:`Selected zone` - Render only the defined timeline zone

* :guilabel:`Guide Zone` - Render only the zone defined by two selected guides

* :guilabel:`Guide Multi-Export` - Render individual files for the zones defined by the guides

* :guilabel:`More Options` - Folds out the dialog window to display more (advanced) options

* :guilabel:`Rendered File Length` - The length of the actual project selection when rendered

* :guilabel:`Render to File` - Click to start the rendering and file creation

* :guilabel:`Generate Script` - Click to just generate a script for later (batch) processing

.. rst-class:: clear-both


Rendering Preset Categories
----------------------------

**Kdenlive** offers many different rendering presets to choose from. They are grouped into categories.

.. figure:: /images/exporting/kdenlive2304_rendering-presets.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2405_rendering-presets

   Kdenlive Rendering Presets/Profiles

* **Audio only** - AC3, ALAC, FLAC, MP3, OGG, WAV

* **Video with Alpha** - Alpha MOV, Alpha VP8, Alpha VP9, Ut Video

* **Images sequence** - BMP, DPX, GIF, JPEG, PNG, PPM, TGA, TIFF, webp

* **Lossless/HQ** - FFV1 (ffva+flac), H.264 (libx264+aac), HuffYUV (huffyuv+flac), Ut Video (utvideo+pcm_s24le)

* **Generic (HD for web, mobile devices ...)** - GIF High Quality, MP4-H264/AAC, MPEG-2, WebM-VP8/Vorbis (libre)

* **Ultra-High Definition (4K)** - MP4-H265 (HEVC), WebM-AV1/Opus (libre), WebM-VP9/Opus (libre)

* **Old-TV definition (DVD...)** - MPEG4-ASP/MP3 (DivX compatible), WOB (DVD), Windows Media Player

* **Hardware Accelerated (experimental)** - NVENC H264 ABR, NVENC H264 VBR, NVENC H265 ABR, VAAPI AMD H264, VAAPI Intel H264

Click on |edit-download| to download more presets created by Kdenlive users. For more details about creating your own presets refer to the :ref:`Project Profiles <manage_project_profiles>` section of the documentation.

See also the :doc:`Render Profile Parameter </tips_and_tricks/useful_info/render_profile_parameters>` section for more details about the various settings in the presets.

.. rst-class:: clear-both


Full Project
------------

:guilabel:`Full Project` radio button is the default setting. **Kdenlive** renders from the start of the first clip until the end of the last clip in the timeline.


.. _rendering-selected_zone:

Selected Zone
-------------

:guilabel:`Selected Zone` radio button selected, **Kdenlive** will only render that portion of the project which has a selected zone created for it. See :ref:`ui-monitors`.


Guide Zone
----------

:guilabel:`Guide zone` radio button makes use of :ref:`guides` to define a region of the project that is to be rendered. For more details refer to the :ref:`rendering-guides` section of the documentation.


Guide Multi-Export
------------------

:guilabel:`Guide Multi-Export` radio button makes use of :ref:`guides` categories to be rendered. For more details refer to the :ref:`rendering-multi_export` section of the documentation.


.. _rendering-more_options:

More Options
------------

Video
~~~~~

Check this box to get a video track in the rendered file.

.. .. versionchanged:: 24.05

.. figure:: /images/exporting/kdenlive2405_rendering-video.webp
   :align: left
   :alt: kdenlive2405_rendering-video

   Rendering options for video

.. rst-class:: clear-both

|

.. .. versionadded: 24.02

.. figure:: /images/exporting/kdenlive2402_rendering-video_interpolation.webp
   :align: right
   :alt: kdenlive2402_rendering-video_interpolation

   Interpolation

:guilabel:`Interpolation` - Allow setting the default interpolation method for scaling operations on rendering

* Nearest-neighbour interpolation: Sharp but highly aliasing. 
* Bilinear interpolation: Fast and low quality. Reduces contrast. 
* Bicubic interpolation: Slower then Bilinear but better results.
* Lanzcos interpolation: Provides the best result for scaling

.. rst-class:: clear-both

|

.. .. versionadded: 24.02

.. figure:: /images/exporting/kdenlive2402_rendering-video_deinterlacer.webp
   :align: right
   :alt: kdenlive2402_rendering-video_deinterlacer

   Deinterlacer

:guilabel:`Deinterlacer` - Allow setting different deinterlacing algorithm method for interlaced footage on rendering

* One-Field: Render only one field so the rendered result is half in size.
* Linear blend: Render each half-picture like a full picture with linear interpolation: instead of rendering each line twice, line 2 is created as the average of line 1 and 3, etc. 
* YADIF - temporal only: Mode of checking fields. Skips spatial interlacing check. 
* YADIF: (Yet Another DeInterlacing Filter) It check pixels of previous, current and next frames to re-create the missed field by some local adaptive method (edge-directed interpolation) and uses spatial check to prevent most artifacts.
* BWDIF: (Bob Weaver Deinterlacing Filter): motion adaptive deinterlacing based on yadif with the use of w3fdif and cubic interpolation algorithms.

.. rst-class:: clear-both

:guilabel:`Render full color range` - Check this box if you need 10-bit color instead of 8-bit color. Please note that this does not work with effects (yet).

:guilabel:`Render at Preview Resolution` - Check this box if you want to use the same resolution as set in the Project Monitor. Useful for quick renderings to check or verify things.

.. .. versionadded: 24.02

:guilabel:`Use Proxy Clips` - Check this box if you want the use the proxy clips for rendering. Useful for quick renderings to check or verify things.

:guilabel:`Rescale` - Select this if you want the rendered video to have a different resolution than what is set in the Project Settings. Useful for quick renderings to check or verify things.

.. figure:: /images/exporting/kdenlive2304_rendering-video_overlay.webp
   :align: right
   :alt: kdenlive2304_rendering-video_overlay

   Render overlay

:guilabel:`Render Overlay` - This option overlays a time code or frame count over the rendered video. The overlay will be over the *entire* rendered project. Alternatively you can use the :doc:`/effects_and_filters/video_effects/generate/dynamic_text` effect to overlay selected regions of the video.

.. rst-class:: clear-both

.. .. versionadded:: 24.05

.. figure:: /images/exporting/kdenlive2405_rendering-video_aspect-ratio.webp
   :align: right
   :alt: kdenlive2405_rendering-video_aspect-ratio

   Aspect Ratio

:guilabel:`Aspect Ratio` - With this option you can choose your desired aspect ratio for the rendered video. It passes the selection to the rendering profile by cropping the video in the timeline to the desired aspect ratio.

.. rst-class:: clear-both


Audio
~~~~~

.. .. versionchanged:: 22.04
   The audio checkbox is simply a checkbox - no automatic audio export anymore

Check this box to have audio tracks in the rendered file.

.. figure:: /images/exporting/kdenlive2304_rendering-audio.webp
   :align: left
   :alt: kdenlive2304_rendering-audio

   Rendering options for audio

:guilabel:`Separate file for each audio track` - By default, Kdenlive creates a stereo audio track. Use this option if you want multiple audio tracks (for example for different languages or commentary) that can be selected in the player software. Use a third-party software to put the video and audio files together.

.. rst-class:: clear-both

Custom Quality
~~~~~~~~~~~~~~

.. figure:: /images/exporting/kdenlive2304_rendering-custom_quality.webp
   :align: left
   :alt: kdenlive2304_rendering-custom_quality

   Rendering options for custom quality

Check this box if you want to manually adjust the quality settings for the rendering process. Use the slider to dial in the quality settings. This has an influence on file size and rendering time.

.. rst-class:: clear-both

Encoder
~~~~~~~

.. figure:: /images/exporting/kdenlive2304_rendering-encoder.webp
   :align: left
   :alt: kdenlive2304_rendering-encoder

   Rendering options for encoder usage

Use the slider to change the speed setting from 'very slow' to 'ultra fast'.

If you have a CPU capable of multi-threading you can select the number of *Encoding threads* to be passed to melt [1]_. For encoding with certain codecs (MPEG-2, MPEG-4, H.264, and VP8) Kdenlive can use more than one thread and thus make use of multiple cores. Increase this number to take advantage of this feature on multi-core machines.

.. _render-more_options_parallel_processing:

Parallel Processing
~~~~~~~~~~~~~~~~~~~

.. figure:: /images/exporting/kdenlive2304_rendering-parallel_proc.webp
   :align: left
   :alt: kdenlive2304_rendering-parallel_proc

   Rendering options for parallel processing

Switch this on to further reduce rendering time. Once enabled you can select the number of threads to use. A good number is 50% of what your CPU's number of possible threads is (e.g. 8 threads for a 16-thread CPU).

.. warning:: Parallel Processing is still (version 23.04.1) somewhat experimental and may result in rendering artifacts, crashes during render or other unwanted effects.

Other Options
~~~~~~~~~~~~~

.. figure:: /images/exporting/kdenlive2304_rendering-other.webp
   :align: left
   :alt: kdenlive2304_rendering-other

   Other rendering options

:guilabel:`2 pass`

:guilabel:`Export metadata` - Check this box to have the metadata entered in the :ref:`project_settings` placed into the metadata of the rendered file.

.. container:: clear-both

   .. figure:: /images/exporting/kdenlive2304_project_settings_metadata.webp
      :align: left
      :width: 400px
      :figwidth: 400px
      :alt: kdenlive2304_project_settings_metadata

      Metadata for the project

   In this example, metadata was entered in the Project Settings dialog.

   You can edit this by clicking on the :guilabel:`Edit metadata` link in the rendering dialog (:guilabel:`More options` must be checked). For this example a new field **Kdenlive Version** was added (using :kbd:`+`) and a value of *23.04.1* entered.

.. rst-class:: clear-both

You can check the metadata in the rendered video by entering this in a terminal window:

.. code-block:: bash

  $ ffprobe <your_video>


.. figure:: /images/exporting/kdenlive2304_rendering-other.webp
   :align: left
   :alt: kdenlive2304_rendering-other

   Other rendering options

:guilabel:`Embed subtitles instead of burning them in` - Creates a stream for subtitles in the container (e.g. MKV)

:guilabel:`Open folder after export` - Opens the folder where the file was saved in the default file manager application

:guilabel:`Play after render` - Opens the default media player application and plays the rendered file

.. rst-class:: clear-both


.. _rendering-batch_mode:

Rendering in Batch Mode
=======================

If you have a lot of rendering jobs to do, you can use **Kdenlive** to create rendering scripts which you can accumulate and then execute in batch mode overnight. **Kdenlive** stores the scripts in the folder specified in :menuselection:`Menu --> Settings --> Configure Kdenlive --> Environment --> Default folders`.

Alternatively, once you have submitted a rendering job on a project and it is up and running in the **Job Queue**, you can drag the render window out of the way or even close it, and continue editing the project, or load a new project and render that one, too. Any subsequent render jobs will go into the **Job Queue**. Editing the project after a render job has been submitted will not change the settings on that job.

.. image:: /images/exporting/kdenlive2304_rendering-job_queue.webp
   :width: 400px
   :alt: Kdenlive_Rendering_job_queue

.. rst-class:: clear-both


.. _rendering-guides:

Rendering Using Guides
======================

:ref:`Guides <guides>` can help organize your project while you work on it and when you share it with the world. You can use guides to keep track of areas or to generate rendering scripts that will do the mundane task for you. This feature makes exporting sections of your project quite easy.

For more details about guides, how to add and manage them, refer to the :ref:`Guides <guides>` section of the documentation.

Using Guide Zones
-----------------

.. figure:: /images/exporting/kdenlive2304_rendering-guide_zones.webp
   :align: left
   :width: 400px
   :figwidth: 400px
   :alt: kdenlive2304_rendering-guide_zones

   Using guide zones to render a section

With this option you define the start and end point for the render by selecting specific guides.

.. rst-class:: clear-both

Generating Rendering Scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /images/exporting/kdenlive2304_rendering-guide_zones_5a.webp
   :align: left
   :width: 160px
   :alt: kdenlive2304_rendering-guide_zones_5a

.. image:: /images/exporting/kdenlive2304_rendering-guide_zones_5b.webp
   :align: left
   :width: 160px
   :alt: kdenlive2304_rendering-guide_zones_5b

Choose which guides will establish the regions of video you want to export using the pull down menus next to :guilabel:`From` and :guilabel:`to`. In this example *Section 1* to *Section 1 End* will be used to define the section to be rendered.

.. container:: clear-both

   .. image:: /images/exporting/kdenlive2304_rendering-guide_zones_6.webp
      :align: left
      :width: 345px
      :alt: kdenlive2304_rendering-guide_zones_6

   Now you can render this to a file or generate a script that will render this guide zone to a file. Click :guilabel:`Generate Script` and a dialog appears asking you to name the script. **Kdenlive** stores the clips in the folder specified in :menuselection:`Menu --> Settings --> Configure Kdenlive --> Environment --> Default Folders`.

.. rst-class:: clear-both

.. image:: /images/exporting/kdenlive2304_rendering-stored_playlist.webp
   :align: left
   :width: 400px
   :alt: kdenlive2304_rendering-stored_playlist

After saving the script, the top tab in the window switches to :guilabel:`Scripts`. This lists all the scripts you have generated, including scripts from other projects.

In this example three scripts were created based on the guides in the timeline. Be sure and keep the :file:`.mlt` extension otherwise the rendering script will not be generated.

.. rst-class:: clear-both

Starting Your Rendering Scripts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each script needs to be started individually by selecting the script and clicking the :guilabel:`Start Script` button.

.. image:: /images/exporting/kdenlive2304_rendering-job_queue.webp
   :align: left
   :width: 400px
   :alt: kdenlive2304_rendering-rendering_job_queue

After clicking each script, Kdenlive switches to the *Job Queue* tab. Here you will see what script is being run and how many more are waiting to be run. If you have a large queue and you want to run the rendering after hours, you can take advantage of the nifty checkbox in the bottom left: :guilabel:`Shutdown computer after renderings`

.. rst-class:: clear-both

Starting Your Rendering Scripts in a Command Line Terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For troubleshooting purposes there could be times that you want to run the render script from the terminal prompt. Rendering in the terminal can produce error logging information that can assist in debugging rendering issues.

To render the video in the terminal ...

* Note the location where **Kdenlive** has saved the script
* Open a terminal and change directories to the location of the :file:`.mlt` script
* Run melt with the :file:`.mlt` script

.. code-block:: bash

  $ cd /path/to/kdenlive/scripts

  $ melt your_script.mlt


.. _rendering-multi_export:

Using Guides for Multi-Export
-----------------------------

.. .. versionadded:: 22.04

With this option you use guides to divide the timeline in pieces that will be rendered as individual files on one go. You do not need to define each section or piece individually.

.. figure:: /images/exporting/render_guide_multi-export_example_22-04.png
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: render guide multi-export example 22-04

   Defined Guides to be used for multi-export

The selection of guide categories indicates which guides will be considered for rendering.

.. rst-class:: clear-both

In this example, there are the following options:

*	"All Categories": This leads to four files:

   * `projectname-begin.mp4` (from 00:00:00 to "guide1")
   * `projectname-guide1.mp4` (from "guide1" to "guide2")
   * `projectname-guide2.mp4` (from "guide2" to "guide3")
   * `projectname-guide3.mp4` (from "guide3" to the end)

*	"Category 0 (purple)": This leads to three files:

   * `projectname-begin.mp4` (from 00:00:00 to "guide1")
   * `projectname-guide1.mp4` (from "guide1" to "guide2")
   * `projectname-guide2.mp4` (from "guide2" to the end)

*	"Category 1 (blue)": This leads to two files:

   * `projectname-begin.mp4` (from 00:00:00 to "guide3")
   * `projectname-guide3.mp4` (from "guide3" to the end)

.. note::
   * If guides are behind the last timeline clip, they are ignored.
   * If a guide sits right at the beginning of the timeline, the name of that guide is used instead of "begin".
   * If two guides have the same name, an underscore and a number will be added to the file name.

.. note:: As of this writing, the appimage of version 23.04.1 is having issues with the scripts generated with this function. Only one of the scripts is executed successfully but the other scripts remain in status 'Waiting...'. Unfortunately, a manual start of the scripts is not possible either.


.. _rendering-sharing_video:

Sharing your Videos
===================

.. .. versionadded:: 22.04.1
   Option to share videos immediately after rendering

.. .. versionchanged:: 23.04.1
   Added upload to YouTube and NextCloud

If you want to share your work right after you finished rendering you can click on :guilabel:`Share` and select one of the options.

.. image:: /images/exporting/kdenlive2304_rendering-share_video.webp
   :align: left
   :alt: kdenlive2304_rendering-share_video

* **Send via Email** - Opens your default email application with the video file as an attachment in a new email window
* **Send to Device**
* **Send via Bluetooth**
* **YouTube** [2]_ - Opens a dialog window to enter your account, tags and a comment. You can upload directly from there.
* **Nextcloud** [2]_ - Opens a dialog window to select your account and enter the folder to upload to. You can upload directly from there.
* **Send via Telegram** - Opens the Telegram desktop app

.. rst-class:: clear-both


**Notes**

.. |melt| raw:: html

   <a href="https://www.mltframework.org/docs/melt/" target="_blank">Melt</a>

.. |melt_doc| raw:: html

   <a href="https://www.mltframework.org/plugins/ConsumerAvformat/#threads" target="_blank">Melt documentation</a>

.. |melt_faq| raw:: html

   <a href="https://www.mltframework.org/faq/#does-mlt-take-advantage-of-multiple-cores-or-how-do-i-enable-parallel-processing" target="_blank">Melt FAQ</a>

.. [1] Melt is the engine Kdenlive uses for compositing and effects rendering. It is part of the MLT framework. For more details refer to the |melt| documentation. See the |melt_doc| on threads and the |melt_faq| on multi-threading.

.. [2] May not be available in all distros and/or appimages
