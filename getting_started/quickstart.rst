.. meta::
   :description: Do your first steps with Kdenlive video editor
   :keywords: KDE, Kdenlive, quick start, first steps, video editor, help, learn, easy

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Alberto Villa (https://userbase.kde.org/User:Alberto Villa)
             - Simon Eugster <simon.eu@gmail.com>
             - Till Theato <root@ttill.de>
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Vgezer (https://userbase.kde.org/User:Vgezer)
             - Xipmix (https://userbase.kde.org/User:Xipmix)
             - Jack (https://userbase.kde.org/User:Jack)
             - Xyquadrat (https://userbase.kde.org/User:Xyquadrat)
             - Carl Schwan <carl@carlschwan.eu>
             - Eugen Mohr
             - Kon (https://userbase.kde.org/User:Kon)
             - Smolyaninov (https://userbase.kde.org/User:Smolyaninov)
             - Paul R Worrall (https://userbase.kde.org/User:Paul R Worrall)
             - Tenzen (https://userbase.kde.org/User:Tenzen)
             - Roanna (https://userbase.kde.org/User:Roanna)
			 - Bernd Jordan

   :license: Creative Commons License SA 4.0

.. _quickstart:

Quick Start
===========


Creating a new project
----------------------

.. figure:: /images/getting_started/kdenlive_folder_structure.webp
  :align: left
  :width: 250px
        
  Kdenlive directory structure

The first step is creating a new (empty) folder for our new project. We will call it :file:`quickstart-tutorial/` in this tutorial. Then get some sample video clips, or download them from here :download:`Kdenlive-tutorial-videos-2011-avi.zip </files/Kdenlive-tutorial-videos-2011-avi.zip>` (7 MB)\ [1]_  and extract them to e.g. a :file:`quickstart-tutorial/Videos/` subfolder inside the project folder.


The image on the left shows the suggested directory structure: Each project has its own directory, with video files in the :file:`Videos` subdirectory, audio files in the :file:`Audio` directory, etc. (see also chapter :doc:`/project_and_asset_management/file_management/folder_structure`)

.. note:: The tutorial from now on assumes that you use the sample videos provided, but it works with any.


.. figure:: /images/getting_started/kdenlive2104_new_project_window.webp
  :align: left
  :width: 250px
    
  New Project dialog


Open **Kdenlive** and create a new project :menuselection:`File --> New`. 

Choose the previously created project folder (:file:`quickstart-tutorial/`) and select an appropriate project profile. The video files provided above are 720p, 23.97 fps.\ [#]_  If you are using your own files and do not know which one to use, **Kdenlive** will suggest an appropriate one when the first clip is added [#]_  , so you can leave the field on whatever it is.

If you like you can change to the dark theme: :menuselection:`Menu --> Settings --> Colour Theme --> Breeze-Dark`.


Adding clips
------------

.. figure:: /images/getting_started/kdenlive2304_add_clips.webp
  :align: left
  :width: 250px
    
  Project Bin: Adding video clips

Now that the project is ready, let us start adding some clips (i.e. the ones you downloaded). This is done via the *Project Bin widget*; a click on the |kdenlive-add-clip|\ :menuselection:`Add Clip or Folder` icon directly opens the file dialog, a click on the small arrow shows a list of additional clip types that can be added as well. Video clips, audio clips, images, and other **Kdenlive** projects can be added via the default :menuselection:`Add Clip or Folder` dialog.

.. container:: clear-both

   .. figure:: /images/getting_started/kdenlive_main_window.webp
      :align: left
      :width: 400px
      
      Kdenlive window with the tutorial files

After loading the clips, **Kdenlive** will look similar to this. On the top left there is the already known Project Bin. To the right of it are the monitors that show video: The clip monitor displays video from the original clips, the project monitor shows how the output video will look with all effects, transitions, etc. applied. The third, also very important, item is the timeline (below the monitors): This is the place where the video clips will be edited. There are two different types of tracks: Video and audio. Video tracks can contain any kind of clip, audio tracks as well but when dropping a video file to the audio track, only the audio will be used.


.. figure:: /images/getting_started/kdenlive_save_project.webp
  :align: left
  :width: 400px
    
  Saving a Kdenlive project


Let us save the work via :menuselection:`Menu --> File --> Save`. This saves our project, i.e. where we placed the clips on the timeline, which effects we applied, and so on. It can *not* be played.\ [#]_  The process of creating the final video is called *Rendering*.

.. rst-class:: clear-both

Timeline
--------

.. note:: In this Quick Start section we will not go into the details of the timeline and its components. More detailed information is available in the :ref:`timeline` section of this documentation.

Now comes the actual editing. Project clips are combined to the final result on the timeline. They get there by drag and drop\ [#]_: Drag some Napoli (assuming you are using the files provided above, as in the rest of this quick start tutorial; if not, please make sure your screen is waterproof, and perhaps tomatoproof) from the project bin and drop it onto the first track in the timeline. In this case track V2.

.. figure:: /images/getting_started/kdenlive_timeline_clips.webp
  :align: left
  :width: 400px
    
  First clips in the timeline


Since some cutlery is needed as well, grab the spoon clip and drop it on the first track as well (track V2). Then drag the Napoli to the beginning of the timeline (otherwise the rendered video would start with some seconds of plain black), and the Spoon right after the Napoli, such that it looks like in the image on the left. (Where I have zoomed in with :kbd:`Ctrl+MW`.) 

.. figure:: /images/getting_started/kdenlive_timeline_cursor.webp
  :align: left
    
  Timeline cursor


The result can already be previewed by pressing :kbd:`Space` (or the :guilabel:`Play` button in the project monitor). You will see the Napoli directly followed by a Spoon. If the timeline cursor is not at the beginning, the project monitor will start playing somewhere in the middle; you can move it by dragging it either on the timeline ruler or in the project monitor. If you prefer keyboard shortcuts, :kbd:`Ctrl+Home` does the same for the monitor that is activated. (Select the :menuselection:`Project Monitor` if it is not selected yet before using the shortcut.)


.. figure:: /images/getting_started/kdenlive_resize_marker.webp
  :align: left
    
  Resize marker


Since after eating comes playing, there is a Billiards clip. Add it to the timeline as well (track V1). For the first 1.5 seconds nothing happens in the clip, so it should perhaps be **cut** to avoid the video becoming boring. An easy way\ [#]_  for this is to move the timeline cursor to the desired position (i.e. the position where you want to cut the video), then drag the left border of the clip when the resize marker appears. It will snap in at the timeline cursor when you move close enough.


.. figure:: /images/getting_started/kdenlive_overlap_clips.webp
  :align: left
    
  Overlapping clips


To add a *transition* between eating (the Spoon) and playing billiards, the two clips need to overlap. To be precise: place the second clip above or below the first one. The first clip should end some frames after the second one begins. Zooming in until the ticks for single frames appear helps here; it also makes it easy to always have the same transition duration, five frames in this case.


You can zoom in by either using the :menuselection:`zoom slider` at the bottom right corner of the **Kdenlive** window, or with :kbd:`Ctrl+Mousewheel`. **Kdenlive** will zoom to the timeline cursor, so first set it to the position which you want to see enlarged, then zoom in.


.. figure:: /images/getting_started/kdenlive_add_transition.webp
  :align: left
  :width: 375px
    
  Transition marker


Now that the clips overlap, the transition can be added. This is done either by right-clicking on the upper clip and choosing :menuselection:`Insert a Composition` and choose :menuselection:`Wipe` or, easier, by hovering the mouse over the lower right corner of the Spoon clip until the pointing-finger pointer is shown and the message "Click to add composition" appears. The latter, by default, adds a wipe transition, which is in this case the best idea anyway since the Spoon is not required for playing.

The wipe transitions fades the first clip into the second one. See also :doc:`Wipe </compositing/transitions>`.

.. image:: /images/getting_started/kdenlive_add_last_clip.webp
  :align: left
  :width: 375px
  
Let us now add the last clip, the Piano, and again apply a wipe transition. When adding it on the first track of the timeline (track V2), you need to click on the new clip's lower left edge to add the transition to the previous clip.


Effects
~~~~~~~

.. figure:: /images/getting_started/kdenlive_add_effect.webp
  :align: left
  :width: 375px
    
  Effect List


The Piano can be colorized by adding an *effect* to it.  Click on the effect view (if effect view is not visible enable the view: :menuselection:`Menu --> View --> Effects`). Type *rgb* in the search field, then double-click the :menuselection:`RGB Adjustment` effect.

.. container:: clear-both

   .. image:: /images/getting_started/kdenlive_effect_flag.webp
      :align: left
      :width: 375px
      
   Once the effect has been added, click on an empty part in the timeline and you see its name on the timeline clip. It will also be shown in the :menuselection:`Effect/Composition Stack` widget.

.. container:: clear-both

   .. figure:: /images/getting_started/kdenlive_effect_stack.webp
      :align: left
      :width: 375px
      
      Effect Stack with RGB adjustment


To get a warm yellow-orange tone on the image, fitting the comfortable evening, blue needs to be reduced and red and green improved.

The values in the Effect/Composition Stack widget can be changed by using the slider (middle mouse button resets it to the default value), or by entering a value directly by double-clicking the number to the right of the slider. 

The Effect/Composition Stack widget always refers to the timeline clip that is currently selected. Each effect can be temporarily disabled by clicking the eye icon, or all effects for that clip can be disabled using the check box at the top of the Effect/Composition Stack widget (the settings are saved though). This is e.g. useful for effects that require a lot of computing power, so they can be disabled when editing and enabled again for rendering.

For some effects like the one used there it is possible to add keyframes. The framed watch icon indicates this. Keyframes are used for changing effect parameters over time. In our clip this allows us to fade the piano's color from a warm evening color to a cold night color. 

.. figure:: /images/getting_started/kdenlive_keyframes.webp
  :align: left
  :width: 375px
    
  Keyframes for effects


After clicking the :menuselection:`keyframe` icon (the clock icon framed in the previous image), the Properties widget will re-arrange. By default there will be two keyframes, one at the beginning of the timeline clip and one at the end. Move the timeline cursor to the end of the timeline clip, such that the project monitor actually shows the new colors when changing the parameters of the keyframe at the end. 

Make sure the last keyframe is selected in the Properties list. Then you are ready to flood the piano with a deep blue.

Moving the timeline cursor to the beginning of the project and playing it (with :kbd:`Space`, or the :guilabel:`Play` button in the :menuselection:`Project Monitor`), the piano should now change the colour as desired.

Keyframing was the hardest part of this tutorial. If you managed to do it, you will master **Kdenlive** easily!

.. note:: In this Quick Start section we brushed over the effects very quickly. More details about effects and an explanation of each effect is available in the :ref:`Effects and Filters <effects_and_filters>` section of this documentation.


Music
~~~~~

.. figure:: /images/getting_started/kdenlive_fadeout.webp
  :align: left
  :width: 375px
    
  Audio fadeout


Since the clips do not provide any audio, let us search for some nice piece of music from your local collection or on web pages like |jamendo|. After adding the audio clip to the Project Bin, it should be dragged to an audio track on the timeline.

The audio clip can be resized on the timeline the same way as video clips can. The cursor will snap in at the end of the project automatically. To add a fade out effect at the end of the audio clip (except if you found a file with exactly the right length) you can hover over the top right (or left) edge of the timeline clip and drag the red shaded triangle to the position where fading out should start.\ [#]_ 

.. |jamendo| raw:: html

   <a href="https://www.jamendo.com" target="_blank">Jamendo</a>


Rendering
---------

.. figure:: /images/getting_started/kdenlive_renderer.webp
  :align: left
  :width: 300px
    
  Rendering dialog


A few minutes left, and the project is finished! Click the Render button (or go to :menuselection:`Menu --> File --> Render`, or press :kbd:`Ctrl+Enter`) to get the dialog shown on the left. Select the desired output file for our new video with all effects and transitions, choose MP4 (works nearly everywhere), select the output file location and press the :guilabel:`Render to File` button. 

.. container:: clear-both

   .. figure:: /images/getting_started/kdenlive_rendering.webp
      :align: left
      :width: 300px
      
      Rendering progress

   After some seconds rendering will be finished and your first **Kdenlive** project is completed. Congratulations!

.. rst-class:: clear-both


----

.. [1] If you prefer Theora (which you probably do not since Ogg Video usually causes problems), you can alternatively download :download:`kdenlive-tutorial-videos-2011-ogv.tar.bz2 </files/kdenlive-tutorial-videos-2011-ogv.tar.bz2>`.
.. [#] |wiki_720p| is the video height, **p** stands for |wiki_prog| (in contrast to |wiki_inter|), and the fps number denotes the number of full frames per second.
.. [#] Provided Configure Kdenlive Settings under :doc:`Misc</getting_started/configure_kdenlive/configuration_misc>` is set to *Check if first added clip matches project profile*
.. [#] To be correct, it *can* be played using ``melt yourproject.kdenlive``, but this is not the way you would want to present your final video since it is (most likely) too slow. Additionally, it only works if melt is installed.
.. [#] Besides drag and drop you can use :doc:`../user_interface/shortcuts` and clip zones to insert clips into the timeline. See :ref:`3-point editing <three_point_editing>` and :ref:`using clip zones <ui-monitors_cm_clip_zone>` for more details.
.. [#] Writing it this way suggests that there are several ways of cutting a clip. This is in fact true.
.. [#] This shaded triangle is a shorthand for adding the effect :menuselection:`Fade --> Fade out`. Both ways lead to the same result.

.. |wiki_720p| raw:: html

   <a href="https://en.wikipedia.org/wiki/720p" target="_blank">720</a>
   
   
.. |wiki_prog| raw:: html

   <a href="https://en.wikipedia.org/wiki/Progressive_scan" target="_blank">progressive scan</a>
   
   
.. |wiki_inter| raw:: html

   <a href="https://en.wikipedia.org/wiki/Interlaced_video" target="_blank">interlaced video</a>
   
