.. meta::
   :description: Kdenlive Tips & Tricks - Timeline Preview Rendering
   :keywords: KDE, Kdenlive, tips, tricks, tips & tricks, timeline, preview, rendering, render, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - TheDiveO
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             
   :license: Creative Commons License SA 4.0


Timeline Preview Rendering
==========================

.. .. versionadded:: 16.08

Timeline preview rendering is an outstanding feature of Kdenlive. It officially debuted in version 16.08.

Preview rendering allows you to render parts or your complete timeline in the background, so you can smoothly play it back. This is especially useful when you work with complex track compositions or use effects that are computationally intensive. Instead of stuttering playback, you now get smooth playback. This way you can check that your timing of keyframes and effect is working out nicely.


Full-FPS Preview of Effect-Heavy Timeline Clips
-----------------------------------------------

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_timeline_preview_rendering_01.webp
      :align: left
      :alt: kdenlive2308_timeline_preview_rendering_01.webp
      :width: 350px

      Raw source footage

   **Raw source footage**: a good example for Kdenlive's timeline preview rendering is this: say, you have some FullHD source footage. Raw, your system easily plays this clip back at its original frame rate of 25\ :abbr:`fps (frames per second)`. This is not even a job for proxy clips on a decent system.

   But this raw footage needs some serious processing before it can be shown to any audience.

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_timeline_preview_rendering_02.webp
      :align: left
      :alt: kdenlive2308_timeline_preview_rendering_02.webp
      :width: 350px

      Effects applied

   **Cue effects**. For production, we need to :doc:`de-fish </effects_and_filters/video_effects/transform_distort_perspective/defish>` this footage (action cams have this tendency). After defishing, we need some :doc:`sharpening </effects_and_filters/video_effects/blur_and_sharpen>`. And then, we also have to do some color grading (e.g. decompress the tonal :doc:`curve </effects_and_filters/video_effects/color_image_correction/curves>`, correct :doc:`saturation </effects_and_filters/video_effects/color_image_correction/saturation>`).

   With these innocent four effects applied, look at the playback rate that is shown in the bottom right corner of the monitor: a dismal six frames per second!

.. rst-class:: clear-both

Unfortunately, proxy clips do not help in this situation: proxy clips are low-res and low-quality variants of the source clips, without any effects applied. So our effects will also slow down proxy clips considerably.


Using Timeline Preview Rendering
---------------------------------

.. attention:: Timeline preview rendering does **not** speed up timeline *editing*. It speeds up the timeline *playback*.
   
.. note:: Preview rendering only deals with the video part of the timeline. Kdenlive renders audio always independent of the preview rendering. In particular, you can make audio changes at any time without affecting preview rendering. Any change to the video portion covered by the preview render zone triggers a new render pass.

.. figure:: /images/tips_and_tricks/kdenlive2308_timeline_preview_rendering_03.webp
   :align: left
   :alt: preview-menu
   :width: 250px

Timeline preview rendering is best controlled using the dedicated :guilabel:`Timeline Preview` menu in the timeline toolbar. In addition, you can find most of the menu items also in :menuselection:`Menu --> Timeline --> Timeline Preview` which opens a fly-out menu with all the options.

.. rst-class:: clear-both


Step 1: Set Preview Zone
~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /images/tips_and_tricks/kdenlive2308_timeline_preview_rendering_04.webp
   :align: left
   :alt: preview-timeline-step-set-zone
   :width: 350px

Set the timeline zone in (:kbd:`I`) and out (:kbd:`O`) points for the zone you want to render for preview.

.. rst-class:: clear-both

Next, select :guilabel:`Add Preview Zone` |preview-add-zone| (alternatively via :menuselection:`Menu --> Timeline --> Timeline Preview --> Add Preview Zone`).

For the first time, you will not see any change yet.


Step 2: Render Preview Zone in Background
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: /images/tips_and_tricks/kdenlive2308_timeline_preview_rendering_05.webp
   :align: left
   :alt: preview-timeline-step-render
   :width: 350px

Select Start Preview Render (:menuselection:`Menu --> Timeline --> Timeline Preview --> Start Preview Render`). Or press :kbd:`Shift+Return`, or click on |preview-render-on|.

.. note:: You can even add multiple, non-contiguous preview rendering zones.

A red bar appears between the timeline ruler and the topmost track. As background rendering progresses, this bar will slowly turn yellow then green, chunk by chunk.

You can continue to work at any part of your timeline while preview rendering is active. However, as soon as you edit clips or transitions that touch your preview zones, rendering will stop and the affected preview zones turn back to red. Simply restart rendering if needed.

The preview is divided into chunks of 25 frames each in size - this corresponds with one second of playback length for 25fps projects.

.. rst-class:: clear-both


Step 3: Enjoy Smooth Timeline Preview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_timeline_preview_rendering_06.webp
      :align: left
      :alt: preview-timeline-step-done
      :width: 350px

   All green chunks of your timeline will now play back at full speed. You should immediately notice that scrubbing such timeline zones will be much faster, too.

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_timeline_preview_rendering_07.webp
      :align: left
      :alt: kdenlive2308_timeline_preview_rendering_07.webp
      :width: 350px

      Preview Rendering enables smooth playback

   Timeline playback is now full 25fps, even as the corresponding timeline clip makes heave use of effects (especially de-fish is computational intensive).

.. rst-class:: clear-both


Good to Know
------------

Smart Preview Undo/Redo
~~~~~~~~~~~~~~~~~~~~~~~

Kdenlive is smart enough to support some levels of undo and redo. So you can check out the results of two different effect settings by quickly undoing and redoing the effect change without having to render the preview once again.


Preview Cache Storage
~~~~~~~~~~~~~~~~~~~~~

.. need an updated screenshot for the cache data (see bug https://bugs.kde.org/show_bug.cgi?id=475980)

.. figure:: /images/tips_and_tricks/preview-timeline-cache-data.png
   :align: left
   :alt: preview-timeline-cache-data
   :width: 350px

You can easily find out how much storage you are currently using for the timeline preview. Use :menuselection:`Menu --> Project --> Project Settings`, then select the tab :guilabel:`Cache Data`.

Kdenlive displays a pie chart showing the cache data disc space consumption. You can purge the cache used for the timeline preview by clicking on the |edit-delete| button next to :guilabel:`Timeline Preview`.

.. rst-class:: clear-both


Preview Profiles
~~~~~~~~~~~~~~~~

.. figure:: /images/tips_and_tricks/kdenlive2308_project_preview_settings.webp
   :align: left
   :alt: kdenlive2308_project_preview_settings.webp
   :width: 350px

   :menuselection:`Menu --> Project --> Project Settings`

Most of the time it should suffice to leave the preview profile set to :guilabel:`Auto`. Kdenlive then will select a suitable preview profile based on your project profile.

In some rare cases, as with unusual frame rates, or when you want to control the preview rendering encoding quality, you can change the preview profile or create your own preview profile. Use the :guilabel:`Show Profile Parameters` |configure| button next to the :guilabel:`Timeline Preview` profile selection.

.. rst-class:: clear-both


De-synchronized Preview
~~~~~~~~~~~~~~~~~~~~~~~

If, for some reason, the rendered preview should get out of sync with your timeline editing, simply remove the corresponding preview zone (|preview-remove-zone|) or all preview zones (|preview-remove-all|\ ). This gets you back to a sane preview state. Then add the zone(s) back again (using :kbd:`I` and :kbd:`O` and |preview-add-zone|), and rerender (|preview-render-on|).



.. rubric:: Notes

.. |kdenlive_org| raw:: html

   <a href="https://kdenlive.org/en/project/timeline-preview-rendering/" target="_blank">kdenlive.org</a>

**Sources**
  The original text was submitted by user *TheDiveO* to the now defunct kdenlive.org blog. For this documentation it has been lifted from |kdenlive_org|, updated and adapted to match the overall style.