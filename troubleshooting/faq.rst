.. meta::
   :description: Troubleshooting Kdenlive - Frequently Asked Questions
   :keywords: KDE, Kdenlive, troubleshooting, documentation, user manual, video editor, open source, free, learn, easy, FAQ, help, question, answer

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Simon Eugster <simon.eu@gmail.com>
             - Jean-Baptiste Mardelle <jb@kdenlive.org>
             - Jack (https://userbase.kde.org/User:Jack)
             - Roger (https://userbase.kde.org/User:Roger)
             - Dadu042 (https://userbase.kde.org/User:Dadu042)
             - Carl Schwan <carl@carlschwan.eu>
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |mlt_framework| raw:: html

   <a href="https://www.mltframework.org/" target="_blank">MLT Multimedia Framework</a>

.. |melt| raw:: html

   <a href="https://www.mltframework.org/docs/melt/" target="_blank">melt</a>

.. |media_info| raw:: html

   <a href="https://mediaarea.net/MediaInfo/Download" target="_blank">here</a>

.. |avidemux| raw:: html

   <a href="https://avidemux.sourceforge.net/" target="_blank">Avidemux</a>

.. |ffmpeg| raw:: html

   <a href="https://ffmpeg.org/" target="_blank">ffmpeg</a>

.. |ffmpeg_split| raw:: html

   <a href="https://trac.ffmpeg.org/wiki/Seeking#Cuttingsmallsections" target="_blank">ffmpeg for splitting</a>

.. |vimeo_how-to_watermark| raw:: html

   <a href="http://vimeo.com/13610402" target="_blank">How to: Add a Watermark in Kdenlive</a>

.. |kde_store| raw:: html

   <a href="https://www.pling.com/browse?cat=686&ord=latest" target="_blank">KDE Store</a>

.. |lame| raw:: html

   <a href="https://lame.sourceforge.io/links.php" target="_blank">LAME</a>



.. _troubleshooting-faq:

Frequently Asked Questions
==========================

.. _faq_user_interface:

User Interface
--------------

Kdenlive is too large on my screen. I cannot make it smaller.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This usually happens when too many :term:`widgets<widget>` are open. Each widget label takes a minimum amount of space in width. Close some via :menuselection:`Menu --> View` or the close button in the widget's title bar (needs to be enabled via :menuselection:`Menu --> View --> Show Title Bars`) and consider using layouts. See the :ref:`ui-workspace_layouts` chapter for more details.


My monitor plays distorted images, or generally something it really should not.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please check your :menuselection:`Menu --> Settings --> Configure Kdenlive --> Playback` settings. Try to disable OpenGL if it is enabled, or use a different driver. Kdenlive may need to be restarted.



.. _faq_asset_management:

Asset Management
----------------

When I import a video clip into my 1920x1080 project a warning pops up asking me to create and switch to new profile. Why?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the standard behavior for Kdenlive for the **first clip** to be added to a new project if the clip's properties are different from the project's settings. For example, the project settings are 1920x1080 @ 30\ :abbr:`fps (frames per second)`, and the clip is 450x360 @ 24.86\ :abbr:`fps (frames per second)`. You can switch off the check in :menuselection:`Menu --> Settings --> Configure Kdenlive --> Misc` by unchecking :guilabel:`Check if first added clip matches project profile`.


I have a .mov file that is made with .png images and was able to import it into Kdenlive but now I only get an unusable audio track from it. How do I fix this?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This bug has been reported for version 23.04.3 and higher. Until a fix is available there is this as a temporary solution:

  1. Open the :file:`.kdenlive` project file in a text editor
  2. Look for this line: ``<property name=“set.test_image”>1</property>``
  3. Remove the line or change the ``1`` to ``0``
  4. Look for this line: ``<property name=“video_index”>-1</property>``
  5. Change the ``-1`` to ``0``
  6. Repeat steps 2 thru 5 for each file that is imported
  7. Save the file


.. _faq_editing:

Editing
-------

Everyone is talking about Edit Mode. How can I switch it on?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:term:`Edit Mode` is a feature of the :ref:`Project Monitor <ui-monitors_project_monitor>` and allows you to control size and position parameters of certain effects directly in the project monitor with the mouse. For example: When you select the :ref:`effects-transform` effect a red rectangle is displayed in the monitor. If you don't see the red rectangle, Edit Mode is switched off. Click on the |edit-mode| icon in the project monitor :ref:`toolbar <ui-monitors_controls_and_elements>` to switch it back on.


I have many tracks. Can I collapse them?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can collapse and expand each track individually by clicking on the |go-down| or |go-next| icon in the :ref:`track's header <track_header>`. If you hold :kbd:`Shift` while doing this you collapse or expand all tracks of the same type at the same time.

Alternatively, you can use the :ref:`fit_tracks_to_view_height` option to adjust the tracks' height to fit into the timeline view port. To do that right-click on the track header and select :guilabel:`Fit all Tracks to View`.


I want to trim videos without re-encoding them. How can I do this?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unfortunately, you cannot do this with Kdenlive. Please try |avidemux| or |ffmpeg| instead. The reason is that for splitting, files need to be treated in a very different manner: the file itself needs to be edited, whereas Kdenlive renders frames into a new file. Check the ffmpeg wiki for using |ffmpeg_split|.


Where can I get more effects?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Effects are provided by the MLT Framework in form of filters. Not all of them work with Kdenlive or are even useful for a video editor. There is no plugin capability for other third-party effects.

The Kdenlive community is a great place to learn from each other and exchange ideas and share. You can find Kdenlive Effect Templates in the |kde_store|. They are essentially effects/filters or a combination of effects and filters to achieve a certain look or, uhm, effect. KDE Store is integrated in Kdenlive so you can install effects directly from the :ref:`Effects tab <effects-effects_tab>`.


I want to apply an effect, for example a watermark, to the whole project. What is the best way to do this?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a new project with the same project profile and import the project to which you want to apply the effect as a clip with  :menuselection:`Menu --> Project --> Add Clip` or by clicking on |kdenlive-add-clip| in the project bin. See also this |vimeo_how-to_watermark| on Vimeo.


There is a black, semi-transparent background on some images. How can I get rid of that?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you used the :ref:`effects-position_and_zoom` effect to move them around or make them smaller or bigger simply replace the effect with the :ref:`effects-transform` effect. It does the same thing but does not have the compositing issues.


How to return normal sound after I changed the speed of a clip?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It looks like you forgot to check the :guilabel:`Pitch compensation` option in the :ref:`change_speed` dialog window. You may be able to undo the speed change or reverse the speed change by doing another speed change but in the opposite direction.

.. to do: update link to :ref:`effects-rubberband`

Another option is to use the **rubberband** audio effect to bring it back to normal.



.. _faq_audio:

Audio
-----

How do I fix Audio Sync Issues?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Often this is caused by having a mix of different audio sources in the project. Audio encoded with :abbr:`VBR (Variable Bit Rate)` (be it pure audio like MP3 or video with audio) can be problematic.

If your audio source is from a video file try extracting the audio from your video sources and transcoding the audio to WAV format. You can use the :ref:`extract_audio` feature of Kdenlive to do and it will create a :file:`.wav` file for you.

If you have a pure audio source try transcoding that to WAV with

.. code-block:: bash

   lame --decode file.mp3 file.wav


Please note that on Windows and MacOS you may need to download and install lame first. You can find the binaries on the official |lame| site.


I have a crackling noise at cuts. How can I fix that?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the **Audio Seam** filter. It works best as a track effect. It can eliminate cracks that can occur on clip cuts. Play with the :guilabel:`Discontinuity Threshold` value until the crackling is gone. The value determines the delta between the last sample of one clip and the first sample of the following clip that are spliced. If the delta is above the discontinuity threshold, then smoothing will be applied.


.. _faq_rendering:

Rendering / Exporting
---------------------

Kdenlive warns me about missing codecs, I cannot render in some formats ...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. .. image:: /images/icons/MissingCodec.png
   :align: left
   :alt: Missing Codec

You may get an error message like this: ``Unsupported audio codec: libmp3lame``. There are several possible reasons for this:

1. You have installed the :term:`codecs<codec>` after **Kdenlive's** installation. To force Kdenlive to check available codecs on your system, run the configuration wizard: :menuselection:`Menu --> Settings --> Run Config Wizard`. Complete the wizard and restart Kdenlive to be sure the codecs have been detected.

#. The codecs are not available on your system. Kdenlive uses the codecs from your **FFmpeg** or **Libav** library. Due to licensing issues some distributions do not provide all codecs by default, and you might need to install an extra package. On Ubuntu/Mint for example, you must install a package called ``libavcodec-extra-xx``. After that, check the codecs again as explained in the first step.

#. Last possibility is that your **FFmpeg** or **Libav** version is buggy and does not report all supported codecs. Kdenlive releases after 0.9.2 have an option to try using codecs even if they seem unsupported: :menuselection:`Menu --> Settings --> Configure Kdenlive` and check the :guilabel:`Bypass codec verification` option.


I want my 4K sources to be processed in 4K but exported in full HD, which resolution should I pick for the project?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want your export to be :abbr:`HD (High Definition)`, make your project in 4K and use the re-scale option in the render dialog window (enable :guilabel:`More options`). See the chapter about the :ref:`video options <rendering-more_options>` for more details. That way you can render your project in 4K later should you change your mind without having to change the project settings.

Regardless of the project settings you have access to the full resolution of your source clips, and any transformation (scale, rotation, shear or corners) is done on the original file.



.. _faq_other:

Other
-----

What components does Kdenlive use?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In effect, Kdenlive is a front end to |melt| which uses the |mlt_framework|. The MLT Multimedia Framework relies on the |ffmpeg| project. Kdenlive writes :file:`sh.mlt` :abbr:`XML (Extensible Markup Language)` files that code the edit points and transitions, and it then calls :file:`/usr/bin/kdenlive_render` and :file:`/usr/bin/melt` to render the video.


I have a lot of clips in the bin but don't use all of them. Can I clean up the bin?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes you can, and in two different ways:

1. :menuselection:`Menu --> Project --> Clean Project` deletes unused clips from the :term:`Project Bin`
2. :menuselection:`Menu --> Project --> Project Settings --> Project Files --> Delete Files` deletes unused files from the Project Bin **and** the storage medium (usually one of your disk drives)


I want to back out to a previous release.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see the chapter about :ref:`installation`.
