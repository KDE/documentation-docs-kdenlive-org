.. meta::
   :description: Kdenlive's User Interface - Media Menu
   :keywords: KDE, Kdenlive, media, project, menu, media menu, jobs, transcode, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jack (https://userbase.kde.org/User:Jack)
			 - Roger (https://userbase.kde.org/User:Roger)
             - Carl Schwan <carl@carlschwan.eu>
             - Karlfee (https://userbase.kde.org/User:Karlfee)
             - Tenzen (https://userbase.kde.org/User:Tenzen)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             - Eugen Mohr

             

   :license: Creative Commons License SA 4.0

.. |glaxnimate| raw:: html

   <a href="https://glaxnimate.mattbas.org/" target="_blank">Glaxnimate</a>


.. _media_menu:

Media Menu
==========

.. .. versionchanged:: 25.12 Reorder menu structure and content 

The functions in this menu affects media that is selected in the Timeline **or** in the Project Bin. Menu functions are available depending on whether a clip is selected in the Project Bin or in the Timeline.

.. figure:: /images/user_interface/menu_reference/menu_reference-media_menu-2512.webp
   :align: left
   :scale: 77%
      
   Kdenlive Media Menu

- :ref:`add_media`
- :ref:`create_folder`
- :ref:`extract_audio`
- :ref:`media_jobs`
- :ref:`transcode_to_edit_friendly_format`
- :ref:`transcode_clips`
- :ref:`transcode`
- :ref:`locate_clip`
- :ref:`reload_clip`
- :ref:`replace_clip`
- :ref:`replace_clip_in_timeline`
- :ref:`duplicate_clip`
- :ref:`Proxy Clip <make_proxy_clip>`
- :ref:`clip_in_timeline`
- :ref:`Clip Properties <media_menu-clip_properties>`
- :ref:`edit_clip`
- :ref:`delete_clip`
- :ref:`adjust_profile_to_current_clip`
- :ref:`remove_unused_media`

.. rst-class:: clear-both


.. _add_media:

Add Media
---------

.. figure:: /images/user_interface/menu_reference/menu_reference-add_media_menu-2512.webp
   :align: left
   :scale: 77%
      
   Kdenlive Add Media Menu

- :ref:`add_clip_or_folder`
- :ref:`add_color_clip`
- :ref:`add_image_sequence`
- :ref:`add_title_clip`
- :ref:`add_template_title`
- :ref:`create_animation`
- :ref:`add_sequence`
- :ref:`generators`

.. rst-class:: clear-both

The purpose of this sub-menu is to allow you to add different types of media to the project bin.


.. _add_clip_or_folder:

Add Clip or Folder
~~~~~~~~~~~~~~~~~~

This function allows you to add video, audio and (single) image files from your file system. It is also available from the menu bar of the Project Bin or by right-click or double-click on empty space in the Project Bin.

.. Currently, the following formats are supported: <list of formats>

.. figure:: /images/user_interface/menu_reference/kdenlive2304_add_clip_window.webp
   :align:  left
   :width: 360px
   :figwidth: 360px
   
   Adding a clip or entire folder
   
A more detailed explanation of this function is available in the :doc:`clips</project_and_asset_management/project_bin/clips>` section of this documentation.

.. rst-class:: clear-both


.. _add_color_clip:

Add Color Clip
~~~~~~~~~~~~~~

This function allows you to create a clip with a single color.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_add_color_clip_window.webp
   :align:  left
   :height: 250px
   
   Adding a Color Clip

It is also available from the menu bar of the Project Bin and by right-clicking on empty space in the Project Bin.

For more details refer to the :doc:`Color Clips </project_and_asset_management/project_bin/color_clip>` section of this documentation.

.. rst-class:: clear-both


.. _add_image_sequence:

Add Image Sequence
~~~~~~~~~~~~~~~~~~

This function adds a series of still images as one clip to the Project Bin. 

.. figure:: /images/user_interface/menu_reference/kdenlive2304_add_image_sequence_window.webp
   :align:  left
   :width: 360px
   :figwidth: 360px
   
   Adding an Image Sequence

It is also available from the menu bar of the Project Bin and by right-click on empty space in the Project Bin.

For more details refer to the :doc:`Image Sequence </project_and_asset_management/project_bin/image_sequence>` section of this documentation.

.. rst-class:: clear-both


.. _add_title_clip:

Add Title Clip
~~~~~~~~~~~~~~

This function adds a Title Clip to the Project Bin. First, it opens the title editor in a separate window where you create the Title Clip. Once saved it shows up in the Project Bin.

A more detailed documentation of the title editor is available in the :doc:`/titles_and_graphics/titles/titles` section of the documentation.

This function is also available from the menu bar of the Project Bin and by right-click on empty space in the Project Bin.


.. _add_template_title:

Add Template Title
~~~~~~~~~~~~~~~~~~

This function creates a Title Clip based on a Template Title.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_add_template_title_window.webp
   :align:  left
   :width: 360px
   :figwidth: 360px
   
   Adding a Template Title
   
You build the template in the Titler application like a normal Title Clip. The key is the placeholder :code:`%s`. It will be replaced by the text you enter here.

This function is also available from the menu bar of the Project Bin and by right-click on empty space in the Project Bin.

Please refer to the :doc:`/titles_and_graphics/titles/title_template_titles` section of this documentation for more details about Titles and Templates.

.. rst-class:: clear-both


.. _create_animation:

Create Animation
~~~~~~~~~~~~~~~~

This function creates an animation clip in the Project Bin and calls |glaxnimate|, the application to actually create the animation.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_create_animation_window.webp
   :align:  left
   :width: 360px
   :figwidth: 360px
   
   Creating an animation

Glaxnimate has to be installed on your computer and the path to it must be set in :menuselection:`Menu --> Settings --> Configure Kdenlive --> Environment --> Default Apps`.

This function is also available from the menu bar of the Project Bin and by right-click on empty space in the Project Bin.

.. rst-class:: clear-both


.. _add_sequence:

Add Sequence
~~~~~~~~~~~~

This function creates a new Sequence in the Project Bin.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_add_sequence_window.webp
   :align:  left
   :height: 250px
   
   Add a new Sequence

Sequences were introduced with version 23.04 and are needed for nested timelines where you can edit clips separately and independently.

This function is also available from the menu bar of the Project Bin and by right-click on empty space in the Project Bin.

Please refer to the :ref:`sequence` section of this documentation for more details.

.. rst-class:: clear-both


.. _generators:

Generators
~~~~~~~~~~

This function allows to create :doc:`generated clips</project_and_asset_management/project_bin/generators>` in your Project Bin for

* Counter
* Color Bars (old TV test display)
* White Noise

This function is also available from the menu bar of the Project Bin and by right-click on empty space in the Project Bin. See the :doc:`Clips</project_and_asset_management/project_bin/clips>` section in this documentation for more details.


.. _create_folder:

Create Folder
-------------

This function creates a new folder in the Project Bin.

The folder is a virtual folder and very useful to keep your assets organized. You can also create separate bins from each folder (see the :doc:`Multiple Bins</project_and_asset_management/project_bin/project_bin_use_multiple_bins>` section)

This function is also available from the menu bar of the Project Bin and by right-click on empty space in the Project Bin.

More details are available in the :doc:`Create Folder</project_and_asset_management/project_bin/project_bin_use_folders>` section of this documentation.

.. tip:: A good way to keep your Project Bin neat and tidy is to have bin folders or separate bins for your footage (main video), B-roll, audio, still images, SFX and VFX, titles and so on.


.. =============================================================================================
   Automatic Transition
   --------------------

   When a transition is selected, this menu item allows you toggle the transition to and from :ref:`transitions_compositions` mode.

   I am not sure this is true anymore. I could not get that menu item to be available regardless of what I did or had selected. Is this still a valid menu item?

   Secondly, a transition is a Composition and this section should be rephrased



.. _extract_audio:

Extract Audio
-------------

Only available if the selected clip is a video clip with an audio track. This function extracts the audio from the clip and adds it as a 48kHz :file:`wav` file to the Project Bin. The process runs as a Clip Job in the Project Bin and may take some time. A small progress bar underneath the clip indicates the progress.

This function is also available via the right-click menu of the clip in the Project Bin.


.. _media_jobs:

Media Jobs
----------

.. .. versionchanged:: 23.04

.. .. versionchanged:: 23.08

Opens a flyout to select different options:

.. figure:: /images/user_interface/menu_reference/menu_reference-media_jobs_menu-2512.webp
   :align:  left
   :scale: 77%
   
   Media Jobs Menu

* My Custom Job (this may look different in your environment)

* `Automatic Scene Split`_

* `Stabilize`_

* `Duplicate Clip with Speed Change`_ [1]_

* `Configure Clip Jobs`_

.. rst-class:: clear-both

This function is also available via the right-click menu of the clip in the Project Bin.

Select a clip which has running jobs, details of the jobs will appear in the clip monitor as overlay. Click on the :guilabel:`X` on the clip jobs overlay will cancel the clip job. To enable the clip job overlay :ref:`see here <ui-monitors_cm_rightclick>`.


.. .. versionchanged:: Extend Marker System with Range/Duration Support

.. _automatic_scene_split:

Automatic Scene Split
~~~~~~~~~~~~~~~~~~~~~

.. figure:: /images/user_interface/menu_reference/clip_job-scene_split-2512.webp
   :align: left
   :scale: 77%

   Scene Detection
   
This job detects scene changes in the clip and creates markers and/or range marker and/or cuts the clip into sub-clips. The :guilabel:`Change threshold` determines the difference in the video stream to be considered a scene change. You may need to experiment with this parameter to get satisfactory results for your specific situation and source material.

If you want Kdenlive to create sub-clips for each scene check the :guilabel:`Cut scenes`.

.. figure:: /images/user_interface/menu_reference/kdenlive2104_clip_job-scene_split_markers.webp
   :align: left
      
   Automatic Scene Detection with markers

.. figure:: /images/user_interface/menu_reference/kdenlive2104_clip_job-scene_split_cuts.webp
   :align: left
     
   Automatic Scene Detection with cuts

.. rst-class:: clear-both


.. _stabilize:

Stabilize
~~~~~~~~~

.. |vid.stab|  raw:: html

   <a href="http://public.hronopik.de/vid.stab/features.php?lang=en" target="_blank">the docs here</a>
   
.. |demo| raw:: html

   <a href="http://public.hronopik.de/vid.stab/files/skiing_veryshaky_short_vs_longsmoothing_above.ogv" target="_blank">Demo of the difference</a>
   
.. |example| raw:: html
   
   <a href="http://public.hronopik.de/vid.stab/files/skiing_veryshaky_visualized8_short.ogv" target="_blank">example</a>
   
.. |Side by side| raw:: html

   <a href="https://youtu.be/HYE3KAl8RAQ" target="_blank">Side by side</a>

.. |Deshaked| raw:: html

   <a href="https://youtu.be/c3CEm8bgVQ0" target="_blank">Deshaked</a>

.. |Original| raw:: html

   <a href="https://youtu.be/cRA5H1LYzM4" target="_blank">Original</a>

   
This feature applies image stabilization algorithms to the clip which can reduce the shakiness of a bit of footage. It is also available via the right-click menu of the clip in the Project Bin.

.. figure:: /images/user_interface/menu_reference/kdenlive2112_clip_job-stabilize_dialog.webp
   :align: left
      
   Stabilize Clip dialog in version 21.12

Based on the tooltips from this screen and |vid.stab| this is what all the options mean:

Accuracy
   Accuracy of shakiness detection. Should be >= shakiness factor. 1: low (fast processing). 15: high (slow processing). Default: 4. Recommended: 8.

Shakiness
   How shaky is the video? And how quick is the camera? 1: little (fast processing). 10: very strong/quick (slow processing). Default = 4. Note: large values may also reduce the accuracy. This is due to the internals of the movement detection. Typically you do not need a value greater than 7.

Stepsize
   Step size of search process. Region around minimum is scanned with 1 pixel resolution. Default = 6.

Min. contrast
   Below this contrast the field is discarded. Range 0-1. Default = 0.3. You may want to use a smaller value for a really low contrast clip.

Smoothing
   Controls the amount of smoothing/stabilization. The larger the value for smoothing the more camera movements are compensated. The resulting clip has a lower change in camera speed.
   Technically it is the number of frames for lowpass filtering = (smoothing * 2) + 1.

   For example, with a with 25 fps clip, a value of 12 for the smoothing factor means we would smooth over one second - 12 frames behind the current frame + the current frame (1) + 12 frames after the current frame. Default =   10.

   |demo| (top:3, bottom: 30).

Max shift
   Maximum number of pixels to translate image. Default = -1 (no limit)

Max angle
   Maximum angle to rotate in radians. Default = -1 (no limit).

Crop
   Unchecked means the border of the transformed frames contains the pixels from previous frames. Checked = black background. Default is unchecked.

Zoom
   Additional zoom during transform. Percentage to zoom > 0 = zoom in, < 0 = zoom out. The zoom specified here is in addition to the optimum zoom calculated by the program when optzoom is checked. Default = 0.

Optimal Zoom
   Use optimal zoom (calculated from transforms). Causes video to zoom until 90% of transformations are hidden. Default is checked. Hint: You can further zoom in with the zoom option.

Optimal Zoom Speed
   Zoom per frame (used when "Optimal Zoom" = 2)

Sharpen
   Sharpens transformed image. Amount of sharpening: 0 = no sharpening. Uses filter unsharp with 5x5 matrix. Default = 0.8.

Show fields
   0 = draw nothing, 1 or 2 = show fields and transforms. Use 1 or 2 to preview what the process is going to do. Check this |example|. Default = 0. Non-zero values of this parameter are not relevant in the **Kdenlive** implementation - use zero.

Tripod
   Virtual tripod mode (=relative=0, smoothing=0)

Here are examples of the effect of running stabilize - transcoded by the original author - Georg Martius.

.. csv-table:: 
   :widths: 20 20 20
   
   |Side by side|,|Deshaked|,|Original|


.. _duplicate_clip_with_speed_change:

Duplicate Clip with Speed Change
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This function is only available for clips selected in the Project Bin, and can be selected from the right-click menu of a clip. [1]_

.. figure:: /images/user_interface/menu_reference/kdenlive2304_clip_job-duplicate_speed_change.webp
   :width: 350px
   :figwidth: 350px
   :align: left
      
   Duplicate Clip with Speed Change

Values above 100% speed the clip up, values below 100% slow it down. The sound in the clip is also reversed.

Select :guilabel:`Pitch compensation` to avoid the Mickey Mouse effect in speech when speeding up the clip.
If you check :guilabel:`Add clip to "Speed Change" folder` a folder named "Speed Change" is created in the Project Bin and the clip added to it.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_clip_job-clip_added.webp
   :width: 350px
   :figwidth: 350px
   :align: left
      
   Duplicate Clip with speed change in Project Bin   

.. figure:: /images/user_interface/menu_reference/kdenlive2304_clip_job-clip_added_folder.webp
   :width: 350px
   :figwidth: 350px
   :align: left
      
   Same as above but with Speed Change folder

When you click on :guilabel:`Save` a new clip is created in the Project Bin. It has the filename you supplied in the dialog with the :file:`.mlt` extension.

You can add this clip to the Timeline just like any other, and when you play it the video of the original source clip will be played but at the new speed (or in reverse if a negative % value was entered).

.. rst-class:: clear-both


.. _configure_clip_jobs:

Configure Clip Jobs
~~~~~~~~~~~~~~~~~~~

.. .. versionadded:: 23.04

.. .. versionchanged:: 23.08

.. figure:: /images/user_interface/menu_reference/kdenlive2308_clip_jobs.webp
   :align: left
   :width: 400px
      
   Manage Bin Clip Jobs dialog
   
This opens the **Manage Bin Clip Jobs** dialog. Here you can create and manage your own jobs that can then be applied to clips in the Project Bin. Select the executable you want to be called and enter the arguments to be passed to the executable. ``%1`` will be replaced by the path of the source clip. If you do not specify an output file extension the extension of the source file will be used.

Unless you want the original clip to be replaced with the result, select whether the resulting clip is :guilabel:`Placed in the original clip folder`, :guilabel:`Placed at the top level`, or Kdenlive shall :guilabel:`Use a subfolder` to save it. In the latter case you need to enter a folder name.

.. rst-class:: clear-both

You can have the source clip path {source} as well as 2 configurable parameters {param1} and {param2}. The output file will replace the {output}. The arguments should be: {source} {param1} {output}

Click on |list-add| to create a new custom clip job. In order to delete one, select it first then click on |edit-delete|.


.. _transcode_to_edit_friendly_format:

Transcode to Edit Friendly Format
---------------------------------

.. figure:: /images/user_interface/menu_reference/kdenlive2304_clip_job-transcode_edit_friendly.webp
   :align: left
   :width: 400px
      
   Transcode clip to edit-friendly format
   
This opens a dialog window where you can select an edit-friendly format in case your source material is not suitable for non-linear video editing. This function is also available via the right-click menu for the clip(s) selected in the Project Bin.

You can select more than one clip in the Project Bin for this function.

There are several formats available, some are lossless (producing huge files), some produce a slight degradation in quality.

.. rst-class:: clear-both


.. _transcode_clips:

Transcode Clips
---------------

.. container:: clear-both

   .. figure:: /images/user_interface/menu_reference/kdenlive2304_transcode_2.webp
     :align: left
     :width: 300px
  
     Transcode clips


   Use this to convert a video or audio clip from one codec/format to another.

   Choose one source file or multiple source files and a profile that represents the desired destination codec/format. Optionally change the destination path and file name and hit :guilabel:`Start`. Otherwise, hit :guilabel:`Abort` to close the windows.

   Transcoding a clip should be faster than loading the clip into the timeline and re-encoding it into a different format.

   * :guilabel:`Add clip to project` controls if after the conversion, the new clip is added to the :doc:`Project Bin </project_and_asset_management/project_bin>`.

   * :guilabel:`Close after encode` Uncheck this checkbox if there is the need to convert to another format after the conversion.

.. rst-class:: clear-both


.. _transcode:

Transcode
---------

.. |ffmpeg| raw:: html

   <a href="http://www.ffmpeg.org" target="_blank">ffmpeg</a>
   
Use this function to transcode your source material into a wide variety of other formats. This function is also available via the right-click menu for the clip(s) selected in the Project Bin.

Choose a transcode profile from the available list to transcode the selected clip into a different video format. The options are controlled by :doc:`Transcode Settings</getting_started/configure_kdenlive/configuration_transcode>`. The transcoding is done by the |ffmpeg| program.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_transcode_clips.webp
   :align: left
   :width: 400px
      
   Transcoding job running

While the transcode job is running, the Project Bin will display a progress bar on the thumbnail of the clip(s), and a job list menu item will appear at the top of the Project Bin.

.. rst-class:: clear-both


.. _locate_clip:

Locate Clip
-----------

Locate Clip opens up the system's file browser at the location of the file system where the selected clip is stored. Useful for tracking down the sources of clips in the Project Bin.

This function is also available via the right-click menu of a clip selected in the Project Bin.

Please note that depending on the type of clip certain menu items are not shown.


.. _reload_clip:

Reload Clip
-----------

Reload Clip will re-import the clip from the file system into Kdenlive. This is useful when you edit a clip outside of Kdenlive and want Kdenlive to update it in the project.

This function is also available via the right-click menu of a clip selected in the Project Bin.


.. _replace_clip:

Replace Clip
------------

Replace Clip will allow you to select a different file but keep all of the uses on the Timeline. This can be useful if you work  with placeholder clips (e.g. low resolution or in project templates) and at the end, before rendering, you replace the clip with the final clip.

.. .. versionadded:: 24.02

If you select an audio file only, Kdenlive ask you if you want to change the audio part of the clip only (or vice versa). This is helpful if you have optimized the audio with an external program and you will update the video clip.

.. figure:: /images/user_interface/menu_reference/kdenlive2402_replace_clip_question.webp
   :align: left
   
   Question if you only want to change the audio part of your clip

.. rst-class:: clear-both

This function is also available via the right-click menu of a clip selected in the Project Bin.

.. note:: Make sure the clip replacement is at least of the same length/duration. Otherwise it may lead to unwanted gaps in the Timeline. If effects are used on these clips the replacement clips should have the same dimensions to avoid unwanted behaviour of effects.


.. _replace_clip_in_timeline:

Replace Clip In Timeline
------------------------

With this function you can replace a clip which is in the timeline with another clip. This is helpful when you are working with placeholders or low resolution clips which you like to exchange with the final clip before rendering.

You need to select 2 clips (the replacement clip and the original clip) for this replacement


.. _duplicate_clip:

Duplicate Clip
--------------

This function will create a copy of the clip in the Project Bin. This can be useful when applying effects to clips and allowing you to have the same source file with two different sets of applied effects, or one with the other without effects.

This function is also available via the right-click menu of a clip selected in the Project Bin.


.. _make_proxy_clip:

Proxy Clip
----------

.. figure:: /images/user_interface/menu_reference/kdenlive2304_proxy_clip.webp
   :align: left
   :width: 400px

   Proxy Clip

If Proxy Clips are enabled in the project settings this function will create a proxy clip for the selected clip(s). A yellow square with the letter P will indicate that the clip in the Project Bin is in fact a proxy clip (expect lower quality for playback in the Clip or Project Monitor). During the final render proxy clips will be replaced by the original source files.

This menu item is a toggle, meaning that if the selected clip is already a proxy clip Kdenlive will revert back to the original source clip.

.. rst-class:: clear-both

This function is also available via the right-click menu of a clip selected in the Project Bin.


.. _clip_in_timeline:

Clip in Timeline
----------------

This function is useful for quickly locating all the places where a clip is used in the Timeline. It is also available via the right-click menu for the clip selected in the Project Bin.

.. figure:: /images/user_interface/menu_reference/kdenlive_clip-in-timeline.webp
   :align: left
   :width: 400px
   
   Locating all occurencies of a clip

Selecting the :guilabel:`Clip In Timeline` menu item brings up a flyout that lists all instances of the selected clip, identified by their track (A for audio, V for video) and position in the Timeline. Clicking on an entry in the list will reposition the playhead to the beginning of the indicated clip.

In the example we have clicked on the third video entry which is located on video track 1 at the 00:35;09 mark and the playhead is now located at the start of that clip.

.. rst-class:: clear-both

This option will be greyed out if the clip is not being used in the Timeline.

See also :guilabel:`Clip in Project Bin` available in the :ref:`right-click menu <right_click_menu>` on a clip in the Timeline.


.. _media_menu-clip_properties:

Clip Properties
---------------

.. figure:: /images/user_interface/menu_reference/kdenlive2304_clip_properties_2.webp
   :align: left
   
   Properties of the clip
   
This menu item opens the Clip Properties widget and displays the properties of the selected clip in the Project Bin. Depending on the type of clip it includes information about the audio stream, video stream, aspect ratio, dimensions or frame size, frame rate, etc.

This function is also available via the right-click menu of a clip selected in the Project Bin.

For more details see the chapter :doc:`Clip Properties</project_and_asset_management/project_bin/clip_properties>`.

.. rst-class:: clear-both


.. _edit_clip:

Edit Clip
---------

.. .. versionadded:: 22.08 animation

This function is available for the following clip types:

- audio

- image

- animation

It opens the clip in an external software specified in :menuselection:`Menu --> Settings --> Configure Kdenlive --> Environment -->` :ref:`Default Apps <configure_environment_default_apps>` ready for editing.

This function is also available via the right-click menu of a clip selected in the Project Bin.

If the path is not set a pop-up window appears to define the path to the external software on your computer:

.. figure:: /images/user_interface/menu_reference/kdenlive2208_missing_glaxnimate_path.webp
   
   Missing path for Glaxnimate

Once the path is set, the application starts and opens the clip you had selected. The entered path gets added automatically to the default apps in :menuselection:`Menu --> Settings --> Configure Kdenlive`.

More details for installing the needed external software and how to set the path refer to the :ref:`configure_environment_default_apps` chapter.

.. hint:: The option is greyed out for video clips because **Kdenlive** is the video editor - only audio, image and animation clips are edited by external software.


.. _delete_clip:

Delete Clip
-----------

This function removes the clip from the Project Bin. It does not delete it from the file system. If the clip is being used in the Timeline a warning message will appear, and if you click on :guilabel:`Continue` any occurrence of that clip in the Timeline will be deleted.

This function is also available via the right-click menu of a clip selected in the Project Bin.


.. _adjust_profile_to_current_clip:

Adjust Profile to Current Clip
------------------------------

This function offers up a suggested Project Profile that would be most suitable for the currently selected clip in the Project Bin.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_adjust_profile.webp
   :align:  left
   :width: 480px
   
   Adjusting the project profile to the clip properties
   
.. rst-class:: clear-both


.. _remove_unused_media:

Remove Unused Media
-------------------

This function can be used to remove any unused clips from the Project Bin.

.. figure:: /images/user_interface/menu_reference/kdenlive2304_clean_project.webp
   :align:  left
   :width: 360px
   :figwidth: 360px
   
   Clean up the project

You can undo this action with :menuselection:`Menu --> Edit --> Undo`, through the :ref:`undo_history` or with the default keyboard shortcut :kbd:`Ctrl+Z`.

.. rst-class:: clear-both

.. note::
   This is different from the :doc:`Project Settings</project_and_asset_management/project_settings>` dialog button :guilabel:`Delete Files` in the :doc:`Project Files</project_and_asset_management/project_settings/tab_project_files>` tab which deletes files not used by the project from the hard drive.


----

.. [1] This feature used to be *Reverse Clip* and was first available in version 0.9.6 of Kdenlive. Since version 17.04 it can still be used to reverse the clip by entering a speed of minus 100%. 