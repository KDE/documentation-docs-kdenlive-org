.. meta::
   :description: Kdenlive Documentation - Capturing Audio
   :keywords: KDE, Kdenlive, project bin, file, management, capturing, audio, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Jack (https://userbase.kde.org/User:Jack)
             - Eugen Mohr
             - Brylie Christopher Oxley (https://userbase.kde.org/User:Brylie Christopher Oxley)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0



Capturing Audio
===============

You can use Kdenlive to capture audio with a microphone while you are playing your project in the :doc:`project monitor</user_interface/monitors/project_monitor>`. This way you can record a voiceover. For more details see the chapter :ref:`audio-recording`

You configure audio capturing from :menuselection:`Menu --> Settings --> Configure Kdenlive -->` :doc:`Capture</getting_started/configure_kdenlive/configuration_capture>`.

You define the destination location for your captures by using :menuselection:`Menu --> Settings --> Configure Kdenlive --> Environment -->` :ref:`Default Folders<configure_environment_default_folders>`.

.. following explanation is related to an pre-refactoring version 
   Under the **Record Monitor**, choose *FFmpeg* capture and enable *Audio* only and hit the **Record** button. Then move back to the **Project Monitor** and hit **Play**. You can now record audio only while the clip is playing. (This feature has had some issues in the past. It has worked in ver 0.9.4 - see bug `#2910 <https://bugs.kdenlive.org/view.php?id=2910>`_)


.. .. versionadded:: 19.04

.. figure:: /images/project_and_asset_management/audio_capture_recording.gif
   :align: left
   :alt: audio_capture_recording

   Recording a voiceover 

The recording will be placed in the timeline where the playhead was when you started the recording. 

.. rst-class:: clear-both


.. hint::
   Depending on your recording device, this may record stereo audio. You can mix it down to mono using the Audio effect :doc:`/effects_and_filters/audio_effects/channels/copy_channels_to_stereo`.


.. _capturing_audio_target:

.. .. versionadded:: 24.05

By default, the :file:`.wav` file of the recording is put into the main project bin. If you want your recordings in one place, you can designate a :doc:`folder</project_and_asset_management/project_bin/project_bin_use_folders>` in the project bin as the target for the recordings.

.. figure:: /images/project_and_asset_management/kdenlive2405_audio-capture-folder.webp
   :width: 360px
   :figwidth: 360px
   :align: left
   :alt: kdenlive2405_audio-capture-folder

   Designating a folder in the bin for audio recordings

Right-click the respective folder in the project bin and enable :guilabel:`Default Target Folder for Audio Captures`.

.. rst-class:: clear-both


.. note:: 
   This folder is a folder in the project bin and not a folder in your file system. You can, however, define a folder in your file system where all recordings (video and audio) are stored. Go to :menuselection:`Menu --> Settings --> Configure Kdenlive --> Environment --> Default Folders`. For more details refer to the chapter :doc:`Settings</getting_started/configuration>`.