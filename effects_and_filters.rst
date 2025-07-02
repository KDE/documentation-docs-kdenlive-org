.. meta::
   :description: Kdenlive Documentation - Effects and Filters
   :keywords: KDE, Kdenlive, effects, audio, video, title, subtitle, speech to text, color correction, documentation, user manual, video editor, open source, free, learn, easy

   :authors: - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             
   :license: Creative Commons License SA 4.0


.. |frei0r| raw:: html

   <a href="https://frei0r.dyne.org/" target="_blank">frei0r</a>

.. |avfilter| raw:: html

   <a href="https://www.mltframework.org/plugins/PluginsFilters/" target="_blank">avfilter</a>


.. _effects_and_filters:

###################
Effects and Filters
###################

Effects and Filters are very important components in video editing. In Kdenlive, effects and filters are provided by |frei0r| or |avfilter| (Kdenlive does not have built-in effects or filters of its own).

.. .. seealso:: :doc:`Compositions </compositing>`

Effects are used to change the appearance of or manipulate a clip. For example, the **Transform** effect allows to scale and move the clip; the **Brightness** effect changes the brightness of the clip; effects in the *Alpha, Mask and Keying* category provide very specific filters for masking or rotoscoping.

.. ==============================================================================================
   This text has moved to its own section "Compositing"
   Compositions are used to combine several visual elements from different sources into a single video. In Kdenlive, you put the different sources into tracks in the Timeline and use compositions to tell Kdenlive how to combine them. For example, the **Dissolve** composition fades out one clip while fading in another over a certain number of frames. That is why Compositions are often referred to as Transitions. Keep in mind that while Compositions are very often used to transition from one video to another they can be used to create artistic and aesthetic effects when combining several clips (e.g. Darken, Dodge, Burn).
   ==============================================================================================

Kdenlive has two groups of effects: :ref:`Video Effects <effects-video_effects>` and :ref:`Audio Effects <effects-audio_effects>`.

There are several ways to apply effects:

1. On the clip in the Project Bin, which makes the effect available in all instances of that clip in the Timeline

#. On the clip in the Timeline, which makes the effect only applicable for that clip in the Timeline at that point

#. On the track, which applies the effect to all clips in that particular track

#. On Master, which applies that effect to all clips in all tracks

.. note:: Not all effects can be used at the track or Master level nor does it make sense.


.. _builtin-effects:

Built-in Effects
================

.. .. versionadded:: 24.12

When dragging a clip into the timeline, the :doc:`Flip </effects_and_filters/video_effects/transform_distort_perspective/flippo>` and :doc:`Transform </effects_and_filters/video_effects/transform_distort_perspective/transform>` effects are always added to the video part of the clip; for the audio part the :doc:`Volume </effects_and_filters/audio_effects/volume_and_dynamics/volume_keyframable>` effect is added by default.

These are the most used effects which you now have at your fingertips without the need to add them manually.

|video-effect| < video part | audio part > |audio-effect|

.. |video-effect| image:: /images/effects_and_compositions/kdenlive2412_builtin-video-effect.webp
   :alt: builtin-video-effect
   :width: 30%

.. |audio-effect| image:: /images/effects_and_compositions/kdenlive2412_builtin-audio-effect.webp
   :alt: builtin-audio-effect
   :width: 30%

The built-in effects are disabled by default. So you have to enable it before you can use it.

Built-in effects can be used in three places:

- on the timeline when a clip is available

- on the track header (only :doc:`Flip </effects_and_filters/video_effects/transform_distort_perspective/flippo>` on video track and :doc:`Volume </effects_and_filters/audio_effects/volume_and_dynamics/volume_keyframable>` on audio track)

- as master effect (only :doc:`Flip </effects_and_filters/video_effects/transform_distort_perspective/flippo>` and :doc:`Volume </effects_and_filters/audio_effects/volume_and_dynamics/volume_keyframable>`)

All built-in effects can be disabled/enabled globally in :menuselection:`Settings --> Configure Kdenlive -> Misc`

.. figure:: /images/effects_and_compositions/kdenlive2412_builtin-effect_disable.webp
   :align: left
   :width: 80%
   :figwidth: 80%
   :alt: builtin-effect_disable
      
   Under **Misc** you can disable/enable all built-in effects. Default is **disabled**.

.. rst-class:: clear-both


.. _effects-effects_tab:

Effects Tab
===========

.. .. versionchanged:: 24.12

Make the Effects widget visible in :menuselection:`Menu --> View --> Effects`.

The Effects widget has eight control icons that show or hide the different effect categories:

.. figure:: /images/effects_and_compositions/kdenlive2412_effects_tab.webp
   :align: left
   :width: 400px
   :figwidth: 400px
   :alt: kdenlive_effects_tab

   Kdenlive Effects widget as a tab in the Project Bin area

|show-all-effects| :guilabel:`Main effects` shows all video and audio effects (default view)

|kdenlive-show-video| :guilabel:`Show all video effects` shows all video effect categories only

|kdenlive-audio| :guilabel:`Show all audio effects` shows all audio effects categories only

|kdenlive-custom-effect| :guilabel:`Show all custom effects` shows all effects :ref:`you have created <effects-custom>` by saving an effect stack.

.. TODO: See :ref:`Save Effect <effects-save_effect>` for more details.

|favorite| :guilabel:`Show all favorite items` shows all effects that were flagged as a favorite effect. This is the same list that appears when selecting :guilabel:`Insert an effect` from the right-click menu of a clip in the Timeline, or by clicking the :guilabel:`Favorite Effects` in the Timeline toolbar.

|edit-download| :guilabel:`Download New Effects` opens a dialog window where effect templates are listed from the KDE Store

|view-filter| :guilabel:`Only show reviewed assets` toggles between the effects which are reviewed and tested by the Kdenlive team and not tested effects (still in test phase)

|help-about| :guilabel:`Show/hide description of effects` toggles the information display below the effect list where a short description of what the effect does is displayed when on. Click on the blue effect text opens the online documentation to this effect.


.. _effects-effect_stack:

Effect/Composition Stack
========================

This widget is also known as the Properties Tab as it lists all effects applied to the currently selected clip as well as each effect's settings or properties. If a Composition is selected the widget displays the composition's settings or properties.

|effect| < effect | composition > |composition|

.. |effect| image:: /images/effects_and_compositions/kdenlive2304_effects-effect_stack.webp
   :alt: effect_stack
   :width: 200px

.. |composition| image:: /images/effects_and_compositions/kdenlive2304_effects-composition_stack.webp
   :alt: composition_stack
   :width: 200px

.. note:: Only Effects can be stacked, Compositions cannot.


.. _effect_stack_functions:

Effect/Composition Stack Functions
----------------------------------

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-effect_stack.webp
   :align: left
   :width: 400px
   :alt: kdenlive2304_effects-effect_stack

   Kdenlive Effect Stack

|document-save-all| Save Effect - Opens a dialog window for entering a name for the effect stack under which it will be listed in the *Custom* effect category and a comment which will be displayed in the information display

|view-split-left-right| Compare Effect - Splits the Preview Monitor vertically to do a side-by-side comparison of the clip with and without effects

|visibility| Effects enabled - Switches the effect stack on or off. This is equivalent to disabling all effects in the effect stack.

|keyframe-disable| Hide/Show keyframes in Timeline - Switches the display of keyframes in the clip in the Timeline on or off

.. rst-class:: clear-both

.. .. versionadded:: 24.02

When an effect is applied to a clip in the timeline you can click on the effect button to enable/disable the clip stack of this clip. When disabled the effect name on the clip is strikeout.

.. figure:: /images/effects_and_compositions/kdenlive2402_effects-effect_stack_disabled.webp
   :align: left
   :width: 400px
   :alt: kdenlive2402_effects-effect_stack_disabled

   Kdenlive Effect Stack disabled by click on the effect of a clip

.. see :ref:`disable-enable_clip_stack`

.. rst-class:: clear-both


.. _effect_functions:

Effect Functions
----------------

.. .. versionchanged:: 24.12

.. |selection-raise| image:: /images/icons/selection-raise.png

.. |selection-lower| image:: /images/icons/selection-lower.png

.. |adjustlevels2| image:: /images/icons/adjustlevels.png

.. figure:: /images/effects_and_compositions/kdenlive2412_effects-effect_panel.webp
   :align: left
   :width: 400px
   :alt: kdenlive2304_effects-effect_panel

   Kdenlive Effect Panel

.. .. versionadded:: 25.04

|go-down| Expand/collapse the effect panel. :kbd:`Shift + click` to expand/collapse all effects 

|keyframe-disable| Hide/show keyframes - Turns the display of the keyframe ruler off or on

|zoom-fit-width| Use effect zone - Toggles the display to show the :ref:`effect zone <effects-effect_zones>`

|visibility| Disable effect - Turns the effect off or on. The effect stays in the stack but is not applied during playback or rendering.

|adjustlevels2| Presets - Opens a list of advanced options to manage presets for the effect (e.g. reset the effect to its default parameters).

|document-save| Save effect - Opens a dialog window for entering a name for the effect under which it will be listed in the *Custom* effect category and a comment which will be displayed in the information display

|help-about| Open effect documentation in browser  - This opens the online documentation to this effect

|selection-raise| Move effect up - Moves the effect up one notch in the list (effect sequence from top to bottom is important)

|selection-lower| Move effect down - Moves the effect down one notch in the list (effect sequence from top to bottom is important)

|edit-delete| Delete effect - Removes the effect from the effect stack

.. rst-class:: clear-both


.. _effects-apply_effects:

Applying an Effect
==================

Where to apply an effect
------------------------

An effect can be applied at four different levels of your project:

- On a clip in the timeline: it will affect only this clip
- On an clip in the bin: it will affect all the occurrences of this clip in the timeline
- On a track: it will affect all the clips on this track
- On the Master: it will affect your global output

How to apply an effect
----------------------

For applying an effect to a clip in the Project Bin or in the Timeline, you can choose one from the Effects Tab and drag it onto the clip.

You can also double-click on an effect in the Effects Tab which adds the effect to the clip in the Project Bin which appears in the clip monitor. In the Timeline, it adds the effect to the clips which are selected. So you can apply an effect to several clips at once in the timeline.

Another method is to use the |favorite|:guilabel:`Favorite Effect` icon in the Timeline toolbar and select the effect from there (you add an effect to the favorite effects by right-click on the effect in the Effects Tab and select :guilabel:`Add to favorites`).

Alternatively, you can use :menuselection:`Menu --> Timeline --> Add Effect` to select an effect from the various categories and add it to the selected clip(s) in the Timeline.

And last but not least you can copy effects with all their settings from any clip (Timeline or Project Bin) and paste them to other clips.

For applying an effect to a track, see :ref:`Track Effect <effects-track_effect>`.

For applying an effect to the Master, see :ref:`Master Effect <effects-master_effect>`.

.. note:: Effects are always added at the bottom of the effect stack, and since the effect order is important, can be re-arranged.


.. _effects-keyframes:

Keyframes in Effects
====================

Many effects use the concept of "Keyframes". Keyframes are user-defined points in your clip where you want an effect to start, stop or change. You can set the parameters for your effects to different values at different keyframes and **Kdenlive** will then gradually change the parameters between the two keyframes so that by the time the video has arrived at the next keyframe it will have adjusted the parameter to match that keyframe. It interpolates between keyframes.


.. _effects-keyframe-types-interpolation:

Keyframes types, interpolation
------------------------------

Select the keyframe interpolation icon for selecting the keyframe type. See :ref:`quickstart` for an example on keyframing the :doc:`RGB adjustment</effects_and_filters/video_effects/color_image_correction/rgb_adjustment>` effect.

.. figure:: /images/effects_and_compositions/kdenlive2402_effects-keyframe_types.webp
   :align: left
   :width: 400px
   :alt: kdenlive2402_effects-keyframe_panel

   Kdenlive keyframe types

The first three keyframes are: **Linear**, **Discrete** and **Smooth** (Centripetal Catmull-Rom spline interpolation). This are standard keyframes. More details about keyframes are :ref:`here <the_smooth_keyframe_interpolation>`.

.. .. versionadded:: 24.02

The next ten keyframes are easing keyframes which calculations are based on Robert Penners equations\ [2]_.

Objects in real life don't just start and stop instantly, and almost never move at a constant speed. When we open a drawer, we first move it quickly, and slow it down as it comes out. Drop something on the floor, and it will first accelerate downwards, and then bounce back up after hitting the floor.

.. rst-class:: clear-both

**Easing keyframes:** The left end is the start of the movement, and the segments in blue and green represent faster movement.

.. Picture taken from: https://easings.net/en in dark mode

.. figure:: /images/effects_and_compositions/kdenlive2402_effects-ease-bounce.webp
   :align: left
   :width: 400px
   :alt: kdenlive2402_effects-ease-bounce

.. figure:: /images/effects_and_compositions/kdenlive2402_effects-ease-cubic.webp
   :align: left
   :width: 400px
   :alt: kdenlive2402_effects-ease-cubic

.. figure:: /images/effects_and_compositions/kdenlive2402_effects-ease-exponential.webp
   :align: left
   :width: 400px
   :alt: kdenlive2402_effects-ease-exponential

.. figure:: /images/effects_and_compositions/kdenlive2402_effects-ease-circular.webp
   :align: left
   :width: 400px
   :alt: kdenlive2402_effects-ease-circular

.. figure:: /images/effects_and_compositions/kdenlive2402_effects-ease-elastic.webp
   :align: left
   :width: 400px
   :alt: kdenlive2402_effects-ease-elastic

.. rst-class:: clear-both

**Smooth (deprecated):** Is the smooth Catmull-Rom spline interpolation keyframe before Kdenlive 24.02.


.. _effects-keyframes-ruler:

Keyframe ruler
--------------

.. .. versionadded:: 20.08.0

The keyframe ruler has zoom bars which makes adjusting keyframes a lot easier if the clip's duration is relatively long and the effect stack widget is too narrow to display all keyframes nicely spaced.

.. figure:: /images/Zoombar-effects.gif
   :alt: Zoombar-effects


.. .. versionadded:: 20.12.0

.. image:: /images/keyframe_toolbar_copy-paste.png
   :alt: keyframe toolbar

Keyframes can be copied and pasted between effects and even across clips using the standard shortcuts :kbd:`Ctrl+C`, :kbd:`Ctrl+V`


.. _effects-curve-editor:

Keyframe Curve Editor
---------------------

.. .. versionadded:: 24.08

Implemented with version 24.08 the keyframe curve editor is still in alpha state. Improvements will come with upcoming versions.

The curve editor is showing the keyframe type and their curves.

.. figure:: /images/curve-editor_enabling.webp
   :alt: curve editor enabling

To switch to the curve editor click on |switch-to-curve-editor-view|:guilabel:`Switch to curve editor view`.

The curve editor can only be enabled on effects which have the following parameters: X, Y, width, height, opacity (alpha, optional) and rotation. For all other effects the curve editor is greyed out.

By double clicking into the window new keyframes get added. Hovering over a keyframe, the cursor changes to a cross and you can:

- move the keyframe to change the value, depending on which tab you are (X position, Y position, Width, Height, Opacity, Rotation). Hold :kbd:`Ctrl` moves the keyframe vertically only.
- click on the keyframe and change the keyframe type

.. figure:: /images/curve-editor_example-view.webp
   :alt: curve editor example view

In this example, the cursor enables the second keyframe and you can either change the values by moving the keyframe or change the values directly in the boxes below the curve editor view.

.. figure:: /images/curve-editor_switch-back.webp
   :alt: curve editor switch back

To switch back to the timeline view click on |switch-to-timeline-view|:guilabel:`Switch to timeline view`.


.. _effects-working_with_keyframes:

Working with Keyframes in the Effect Stack
------------------------------------------

.. .. versionadded:: 21.04.0

The effect keyframe panel allows comprehensive manipulation of keyframes:

.. image:: /images/Move-kf-to-cursor.gif
   :width: 220px
   :align: left
   :alt: move-kf-to-cursor

1. Select the keyframe you want to move
2. Move the cursor to the position where you want to move the keyframe to
3. Click on |align-horizontal-center|:guilabel:`Move selected keyframe to cursor`

.. container:: clear-both

   .. image:: /images/Duplicate-keyframe.gif
      :width: 220px
      :align: left
      :alt: duplicate-keyframe

   1. Select the keyframe you want to duplicate
   2. Click on |edit-copy|:guilabel:`Copy keyframe`
   3. Move the cursor to the position where you want to insert the new keyframe
   4. Click on |edit-paste|:guilabel:`Paste keyframe`

.. container:: clear-both

   .. image:: /images/Apply-value-to-selected-kf.gif
      :width: 220px
      :align: left
      :alt: apply-value-to-selected-kf

   1. Select all keyframes you want to apply the value on
   2. Go to one of the selected keyframes and change the value(s) as you want
   3. Click on |application-menu|:guilabel:`Options` and select :guilabel:`Apply current position value to selected keyframes`
   4. Select the parameters you want to apply and click on :guilabel:`OK`

.. container:: clear-both

   .. image:: /images/Kf-ctrl-select.gif
      :width: 220px
      :align: left
      :alt: kf-ctrl-select

   Select multiple individual keyframes with :kbd:`Ctrl+LMB`

.. container:: clear-both

   .. image:: /images/Kf-rubber-select.gif
      :width: 220px
      :align: left
      :alt: kf-rubber-select

   Select contiguous keyframes with :kbd:`Shift+LMB`

.. container:: clear-both

   .. figure:: /images/Multiple-kf-move.gif
      :width: 220px
      :align: left
      :alt: multiple-kf-move

   Moving multiple keyframes at once

   .. rst-class:: clear-both


.. _effects-keyframes_types:

Keyframe Types
--------------

.. .. versionadded:: 24.02

.. |rp_easing_func| raw:: html

   <a href="http://robertpenner.com/easing/" target="_blank">Robert Penner's Easing Functions</a>

Easing functions are based on |rp_easing_func|.


.. _effects-exchange_keyframes:

Exchanging Keyframes Across Effects
-----------------------------------

.. .. versionadded:: 21.04.0

You can import and export keyframes from/to the clipboard. This feature is not only useful to copy keyframes from one clip to another, it can also be used for example to copy the results of the motion tracker to the Transform effect.

To export the keyframes to the clipboard click on |application-menu|:guilabel:`Options` in the keyframe panel\ [1]_ and choose :guilabel:`Copy keyframes to clipboard`.

.. figure:: /images/Kdenlive_import_keyframes_dialog.png
   :align: left
   :alt: Import keyframes dialog

   Importing keyframes

To import keyframes from the clipboard click on |application-menu|:guilabel:`Options` inside the keyframe panel\ [1]_ and choose :guilabel:`Import keyframes from clipboard`. If you have valid data on your clipboard you should see this dialog window where you can adjust the mapping of the data.

For most use cases the default settings suffice. But you may want to copy only a subset of the data and perhaps enter an offset value, for example.

.. rst-class:: clear-both


.. _effects-track_effect:

Track Effect
============

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-track_effect.webp
   :align: left
   :width: 90%
   :figwidth: 240px
   :alt: kdenlive2304_effects-track_effect

   Track effect indicators

Effects can be added to an entire track affecting all clips in that track. Simply drag an effect from the Effects Tab to the header of the desired track, or click on the |tools-wizard|:guilabel:`Track Effect` icon and drag the effect to the track's effect stack.

.. rst-class:: clear-both


.. _effects-master_effect:

Master Effect
=============

.. .. versionadded:: 19.12..0

If you want to apply audio or video effects throughout the whole video. Click on the :guilabel:`Master` button above the track headers to see the Master Effect Stack where you can add effects just like with clips or tracks.

.. figure:: /images/effects_and_compositions/master.gif
   :alt: master
   :width: 100%

   Adding a Sepia effect to the entire video

There are specific effects and filters that work :ref:`effects-on_master` only.

.. .. toctree::
   :maxdepth: 1
   :glob:

   effects_and_filters/video_effects/on_master


.. _effects-effect_zones:

Effect Zones
============

.. .. versionadded:: 21.04.0

Effect Zones allow you to apply effects to specific regions of tracks or the timeline. Zones can be set from the effect zone bar in the Timeline or from the interface in the effect panel.

.. figure:: /images/Track-effect-zone.gif
   :alt: track-effect-zone
   :width: 80%

   Track Effect Zone


.. figure:: /images/Timeline-effect-zone.gif
   :alt: timeline-effect-zone
   :width: 80%

   Master Effect Zone


.. _effects-masking_effects:

Masking Effects
===============

.. .. versionadded:: 21.08.0

This feature allows to apply effects only to specific regions of a clip by using masks. In its current implementation the process requires three steps:

1. Add one of the three available masks: :guilabel:`Shape alpha (mask)`, :guilabel:`Rotoscoping (mask)` or :guilabel:`Alpha shapes (mask)`.
2. Add an effect (or effects) to be applied to the masked region
3. Add the :guilabel:`Mask Apply` effect to activate the mask to the effects in step 2

.. figure:: /images/mask.gif
   :alt: mask
   :width: 80%

Using Rotoscoping (mask) to apply the Saturation effect in one specific region only

You can apply more than one mask per clip by following the same three-step process.

.. the following section is obsolete but I don't know since what version
   Seek To Active Frame
   --------------------

   Some keyframe controls have a *seek to active frame* button

   .. image:: /images/kdenlive_Seek_to_Active_frame_button.png
      :align: left
      :alt: Seek to active frame button

   (Labeled 1 in screenshot A below). When *seek to active frame* is toggled on and you click on one of the keyframes in the keyframe list, Kdenlive will scroll the preview window to that keyframe. In the example of the screenshot, we have selected the keyframe at 9:20 in A and the clip position caret (highlighted in red box) shows the location of this keyframe. Clicking the keyframe at 10:00 in B shows how the clip position has moved.

   .. image:: /images/Kdenlive_Seek_to_active_frame.png
      :align: right
      :alt: Seek to active frame


.. _effects-video_effects:

Video Effects
=============

The video effects are divided into the following categories:

.. toctree::
   :maxdepth: 1
   :glob:

   effects_and_filters/video_effects/*

The available effects are defined by :file:`.xml` files found in :file:`.local/share/kdenlive/effects` (e.g. :file:`/usr/share/kdenlive/effects`).

These :file:`.xml` files contain the default values for the effects parameters. So if you don't like the default values for the effects in Kdenlive, you can modify the defaults by editing these :file:`.xml` files.

See also :doc:`here <effects_and_filters/effects_and_filters_list>` for an alphabetical list of effects and filters.


.. _effects-audio_effects:

Audio Effects
=============

The audio effects are divided into the following categories:

.. toctree::
   :maxdepth: 1

   effects_and_filters/audio_effects/audio/index
   effects_and_filters/audio_effects/channels/index
   effects_and_filters/audio_effects/cmt_plugins/index
   effects_and_filters/audio_effects/eq_and_filters/index
   effects_and_filters/audio_effects/ladspa_plugins/index
   effects_and_filters/audio_effects/modulators/index
   effects_and_filters/audio_effects/pitch_and_time/index
   effects_and_filters/audio_effects/reverb_echo_delays/index
   effects_and_filters/audio_effects/swh_plugins/index
   effects_and_filters/audio_effects/stereo_and_binaural_images/index
   effects_and_filters/audio_effects/tap_plugins/index
   effects_and_filters/audio_effects/tools/index
   effects_and_filters/audio_effects/volume_and_dynamics/index

The available effects are defined by :file:`.xml` files found in :file:`.local/share/kdenlive/effects` (e.g. :file:`/usr/share/kdenlive/effects`).

These :file:`.xml` files contain the default values for the effects parameters. So if you don't like the default values for the effects in Kdenlive, you can modify the defaults by editing these :file:`.xml` files.

See also :doc:`here <effects_and_filters/effects_and_filters_list>` for an alphabetical list of effects and filters.


.. ====================================================================================================
   This section has moved to its own chapter

   .. _effects-compositions:

   Compositions
   ============

   .. toctree::
      :maxdepth: 1
      :glob:

      effects_and_compositions/transitions
   ====================================================================================================

.. .. _effects-effects_and_transitions_list:

Alphabetical List of all Effects and Filters
============================================

.. toctree::
   :maxdepth: 1
   :glob:

   effects_and_filters/effects_and_filters_list


.. .. _effects-audio_tools:

Audio Tools
===========

.. toctree::
   :maxdepth: 1
   :glob:

   effects_and_filters/audio


.. _effects-time_remapping:

Time Remapping
==============

.. .. versionadded:: 21.08.0

The Time Remap feature allows to keyframe the speed of a clip to achieve effects like speed ramping.

.. figure:: /images/timeremap.gif
   :alt: timeremap
   :width: 80%

   Example of using Time remapping for speed ramping

See also :ref:`this tutorial<tutorials-time_remapping>`.


.. .. _effects-speech_to_text:

Speech-to-Text
==============

.. toctree::
   :maxdepth: 1
   :glob:

   effects_and_filters/speech_to_text


.. .. _effects-subtitles:

Subtitles
=========

.. toctree::
   :maxdepth: 1
   :glob:

   effects_and_filters/subtitles


.. .. _effects-titles:

..   Titles
   ======

   .. toctree::
   :maxdepth: 1
   :glob:

   effects_and_filters/titles


.. _effects-effects_demos:

Effects Demos
=============

.. |video_1| raw:: html

   <a href="https://youtu.be/C6oeu2Yc64I" target="_blank">https://youtu.be/C6oeu2Yc64I</a>

.. |video_2| raw:: html

   <a href="https://youtu.be/jrC4F_G64jA" target="_blank">https://youtu.be/jrC4F_G64jAg</a>

.. |video_3| raw:: html

   <a href="https://youtu.be/XMoSgHHbA4k" target="_blank">https://youtu.be/XMoSgHHbA4k</a>

.. |video_4| raw:: html

   <a href="https://youtu.be/capV7lUzbOw" target="_blank">https://youtu.be/capV7lUzbOw</a>

.. |video_5| raw:: html

   <a href="http://www.youtube.com/playlist?list=PLc1VErdvjnSFE6w6sryFWIu4lfKavhnvz" target="_blank">Franz M.P.</a>


The following three YouTube videos display the results of a number of the video effects available in **Kdenlive** (Spanish captioning).

* |video_1|

* |video_2|

* |video_3|


Another YouTube video (English Captions).

* |video_4|


See also this YouTube play list from |video_5|


.. _effects_notes:

----

.. [1] If you do not see a keyframe panel check whether the keyframe panel has been switched off for this effect (|keyframe-disable| icon in the effect toolbar) or perhaps the effect is simply not keyframable.

.. [2] Robert Penners equations: http://robertpenner.com/easing/