.. meta::
   :description: Kdenlive Documentation - Clip Properties
   :keywords: KDE, Kdenlive, editing, documentation, user manual, add clips, project bin, asset, management, clip properties, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - TheDiveO
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             
   :license: Creative Commons License SA 4.0


Clip Properties
===============

You can display and edit clip properties by selecting a clip in the :doc:`Project Bin</project_and_asset_management/project_bin>` and using the :menuselection:`Menu --> Media --> Clip Properties`, or selecting :guilabel:`Clip Properties` from the right-click clip context menu.

Clip Properties are displayed in their own widget. You enable it from the :menuselection:`Menu --> View --> Clip Properties`. If it is not enabled when selecting :guilabel:`Clip Properties` as described above, Kdenlive will automatically enable it. By default, the widget is part of the same workspace dock as the project bin. As with any other widget, you can move it around within the same dock or put it to another or even into its own dock. See the chapter about :doc:`Workspace Layout</user_interface/workspace_layouts>`.

The Clip Properties widget has several tabs\ [1]_:

* |edit-find|\ :guilabel:`File Info` - displays general :ref:`file_info`
* |document-edit|\ :guilabel:`Properties` - allows editing some :ref:`properties`
* |kdenlive-audio|\ :guilabel:`Audio Properties` - displays properties of the :ref:`audio <audio_properties>` stream

.. ================================================================================================
   Metadata doesn't display anything and probably has never really worked
   Analysis used to list the motion vector data files created by the motion tracker

   * |drag-surface|\ :guilabel:`Metadata` - displays metadata from the clip (see notes below)
   * |view-visible|\ :guilabel:`Analysis` - displays :doc:`motion tracker</effects_and_filters/video_effects/alpha_mask_keying/motion_tracker>` effect `analysis data <analysis>`_

   =============================================================================================


.. _file_info:

File Info
---------

The first tab is the **File Info** tab. It displays general information about the file, its streams, and other technical data.

.. figure:: /images/project_and_asset_management/clip_properties_info.webp
   
   The File Info tab

At the top, the filename with its full path is displayed as a link. Clicking it opens your OS file manager at that particular location.


.. _properties:

Properties
----------

The **Properties** tab displays those properties of the clip that Kdenlive allows you to change.

.. figure:: /images/project_and_asset_management/clip_properties_edit.webp
   :align: left

   Editable properties of the selected file

Check the property you want to change, and then enter or select the new value.

.. rst-class:: clear-both

:guilabel:`Duration`:
   The duration of the original clip. Not really useful for video clips, but color clips, title clips, images, and image sequences. However, if set for a video clip the following rules apply: If the new duration is shorter than the clip duration, then the clip is **trimmed**. If the new duration is longer than the clip duration, then the last image is repeated (freeze frame) until the new duration is reached.

:guilabel:`Aspect Ratio`:
   The current aspect ratio of the clip

:guilabel:`Proxy clip`:
   If proxy clips are enabled for the project (see the chapter :doc:`Project Settings</project_and_asset_management/project_settings>`), you create a proxy file for the selected clip. If a proxy file exists already, this is checked and the encoder format is displayed. Click on |edit-delete|\ :guilabel:`Delete proxy file` to delete the proxy file. The |application-menu| icon opens a flyout with additional options:

:guilabel:`Frame rate`:
   The current frame rate in :abbr:`fps(frames per second)`

:guilabel:`Scanning`:
   The current scan format (interlaced or progressive)

:guilabel:`Field order`:
   The current field order (only applicable to *interlaced* scanning)

:guilabel:`Disable auto-rotate`:
   If checked will prevent the image to be rotated according to its embedded rotation setting (not present in all images)

:guilabel:`Color space`:
   The current :term:`color space` of the clip

:guilabel:`Color range`:
   The current :term:`color range` of the clip. This is mostly relevant for videos intended for broadcasting.


.. _sequence_properties:

Sequence Properties
-------------------

.. .. versionadded:: 25.08

.. figure:: /images/project_and_asset_management/clip_properties-sequence-2508.webp
   :scale: 75%

When a sequence is selected in the project bin you can change the timecode offset. More details see under :ref:`sequence timecode offset <sequence_timecode_offset>`.


.. _audio_properties:

Audio Properties
----------------

.. figure:: /images/project_and_asset_management/clip_properties_audio.webp
   :align: left
   
   The Audio properties tab

Choose which audio channel\ [2]_ should be enabled or disabled.

Rename with double click.

.. rst-class:: clear-both

Select each channel in the list individually to perform any of the following functions:

:guilabel:`Normalize`:
   Normalize the channel

:guilabel:`Swap channels`:
   Swap the channels

:guilabel:`Copy channel`:
   Copy a channel on the other one

:guilabel:`Gain`:
   Adjust the volume

Adjusting the :guilabel:`Audio sync` in increments of one millisecond (1 ms) applies to all channels.



.. ================================================================================================
   Analysis
   --------

   .. figure:: /images/Kdenlive_Clip_properties_analysis.png
      :align: left
   
   You can view and delete motion vector data that is associated with the clip from here. This is data created by :doc:`/effects_and_filters/video_effects/alpha_mask_keying/motion_tracker`

   Button 1 Will delete the selected analysis data, Button 2 will allow you to export the data (semi colon delimited text file), Button 3 will allow you to import analysis data.

   .. rst-class:: clear-both


.. rubric:: Notes

.. .. versionchanged:: 22.12

The **Marker** tab has been removed. Clip markers are shown in their own widget **Marker**. You enable it in :menuselection:`Menu --> View --> Markers`. More details see :ref:`markers`.


----

.. [1] The **Metadata** and **Analysis** tabs do not display anything at the moment.

.. [2] There is a difference between audio streams and audio channels. Kdenlive does display the different audio streams with a list. Consumer video camera mostly have only 1 audio stream with i.e. 6 channels, like 5.1 audio. Kdenlive does not allow manipulation of the audio channels.