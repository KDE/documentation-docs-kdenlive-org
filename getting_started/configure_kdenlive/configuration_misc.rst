.. meta::
   :description: Kdenlive Documentation - Configuration Miscellaneous
   :keywords: KDE, Kdenlive, documentation, user manual, configuration, preferences, misc, miscellaneous, video editor, open source, free, learn, easy


.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Misc
----

The **Misc** (Miscellaneous) section contains settings for the general behavior of Kdenlive, how to handle clip import and effects, and the default duration for the various clip types.

.. figure:: /images/getting_started/configure_misc_2412.webp
   :width: 700px
   :figwidth: 700px
   :alt: configure_misc_2412

   The miscellaneous section

:1: :guilabel:`Open last project on startup`. If checked, Kdenlive will open the project file that was last edited and saved before closing Kdenlive. If unchecked, Kdenlive will create a new project using the :doc:`Project Default</getting_started/configure_kdenlive/configuration_project_defaults>` settings.

:2: :guilabel:`Activate crash recovery (auto save)`. If checked, Kdenlive will automatically create a backup of the current project file three seconds after you perform an action that cannot be undone. This only happens if no other action is performed within those three seconds. See also AUTO_SAVE

:3: :guilabel:`Check if first added clip matches project profile`. If checked, Kdenlive compares the dimensions and fps values of the first clip added to the project bin with the respective settings in project profile. If they differ, Kdenlive asks if the project settings should be adjusted to match the values of the clip.

:4: :guilabel:`Automatically import all streams in multi-stream clips`. If checked, all video and audio streams of a clip are imported. This is useful if a video has multiple video streams for the different camera angles. If unchecked, the first video and audio streams are imported.

:5: :guilabel:`Automatically import image sequence`. If checked, Kdenlive will import multiple selected images as an image sequence, and not as individual images.Please note that an image sequence cannot be broken into individual images.

:6: :guilabel:`Get clip metadata created by Magic Lantern`. If checked, Kdenlive will try to read to read any metadata created by that tool and display it in the clip properties widget.

:7: :guilabel:`Ignore subfolder structure on import`. If checked, importing a whole folder will ignore any subfolder structure and bring all supported files contained in any subfolder straight into the project bin. If unchecked, Kdenlive will create folders and subfolders in the project bin to reflect the folder structure in your file system and add the imported files accordingly.

:8: :guilabel:`Disable parameters when the effect is disabled`. If checked, you cannot change the parameters when the effect is disabled. If unchecked, changing parameter is possible but the video playback doesn't change. You need to enable the effect to see the changes.

:9: :guilabel:`Enable built-in effects`. If checked, clips will have parameters of the Flip and Transform effects automatically added and displayed in the effects stack. This eliminates the need to add those effects manually.

:10: :guilabel:`Tab position`. This determines where the tabs for stacked widgets are displayed. Options are Bottom (default), Top, Left, and Right.

:11: :guilabel:`Preferred track compositing composition`. Determines the method for compositing the tracks. Track compositing takes place even without the explicit use of a composition. In that sense tracks are like layers with lower track numbers being underneath tracks with higher numbers. Options are qtblend (default), auto, and frei0r.cairoblend. Qtblend delivers the best performance and stability.

:12: :guilabel:`Default Durations`. These define the default duration for the various clip types upon their creation. Any of those clips can be adjusted in the project bin or timeline, of course, but if you consistently want to have title clips, for example, to be 10 seconds long, you can change it here. The notation for the value is hh:mm:ss,ff with hh meaning hours, mm minutes, ss seconds, and ff frames.