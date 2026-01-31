.. meta::
   :description: Kdenlive Documentation - Using the Project Bin - Clip Context Menu
   :keywords: KDE, Kdenlive, project bin, working, using, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jack (https://userbase.kde.org/User:Jack)
             - Roger (https://userbase.kde.org/User:Roger)
             - Carl Schwan <carl@carlschwan.eu>
             - Eugen Mohr
             - Smolyaninov (https://userbase.kde.org/User:Smolyaninov)
             - Tenzen (https://userbase.kde.org/User:Tenzen)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |extract_audio| replace:: :guilabel:`Extract Audio`

.. |media_jobs| replace:: :guilabel:`Media Jobs`

.. |clip_in_timeline| replace:: |go-jump|\ :guilabel:`Clip in Timeline`

.. |locate_clip| replace:: |find-location|\ :guilabel:`Locate Clip`

.. |reload_clip| replace:: |view-refresh|\ :guilabel:`Reload Clip`

.. |replace_clip| replace:: |edit-find-replace|\ :guilabel:`Replace Clip`

.. |replace_clip_in_timeline| replace:: |edit-find-replace|\ :guilabel:`Replace Clip in Timeline`

.. |duplicate_clip| replace:: |edit-copy|\ :guilabel:`Duplicate Clip`

.. |transcode| replace:: |edit-copy|\ :guilabel:`Transcode to Edit Friendly Format`

.. |proxy_clip| replace:: :guilabel:`Proxy Clip`

.. |clip_properties| replace:: |document-edit|\ :guilabel:`Clip Properties`

.. |edit_clip| replace:: |document-open|\ :guilabel:`Edit Clip`

.. |rename_clip| replace:: |document-edit|\ :guilabel:`Rename`

.. |delete_clip| replace:: |edit-delete|\ :guilabel:`Delete Clip`

.. |wav_48khz| replace:: :guilabel:`Wav 48000Hz`

.. |my_custom_job| replace:: :guilabel:`My Custom Job`

.. |scene_split| replace:: :guilabel:`Automatic Scene Split`

.. |stabilize| replace:: :guilabel:`Stabilize`

.. |duplicate_clip_speed| replace:: :guilabel:`Duplicate Clip with Speed Change`

.. |configure_clip_jobs| replace:: |configure|\ :guilabel:`Configure Clip Jobs`

.. |track_timecode| replace:: :guilabel:`V2: 00:00:22:15`


.. ====================================================================================================
   This file is being .. include(d):: in project_bin_use.rst and the chapter title designation follows the structure of the parent file. Hence the use of --- and ~~~ as chapter designation
   ====================================================================================================


Context Menu
------------

Right-click on any asset or item in the Project Bin to get a context menu with several and different options depending on the asset or item you used it on. The menu is also available via :menuselection:`Menu --> Clip`.

.. container:: clear-both

   .. figure:: /images/project_and_asset_management/project_bin_context_menu.webp
   
      The context menu for bin items

.. rst-class:: clear-both

|extract_audio|:
   Extracts the audio stream of the clip and adds a :file:`.wav` file with a sample rate of 48kHz to the project bin. Is only available if the clip is of type :file:`audio` or a video file with an audio stream. For further details see the chapter :ref:`extract_audio`.

|media_jobs|:
   Opens a flyout with additional options
   
   * |my_custom_job| runs the clip job *My Custom Job*

   * |scene_split| runs a clip job that detects scene changes and creates individual clips for each detected scene. For further details see the chapter :ref:`automatic_scene_split`.

   * |stabilize| runs a stabilizer. See also the chapter :ref:`stabilize`.

   * |duplicate_clip_speed| creates a copy of the selected clip and applies a speed change you can specify in a dialog window. For further details see the chapter  :ref:`duplicate_clip_with_speed_change`.

   * |configure_clip_jobs| opens a window to manage clip jobs. See also the chapter :ref:`configure_clip_jobs`

|clip_in_timeline|:
   Opens a flyout with a list of all the instances of the selected clip in the timeline. For example |track_timecode| indicates that this clip is in video track `V2` at position (timecode) `00:00:22:15` (format is :abbr:`hh:mm:ss:ff(hours:minutes:seconds:frames)`) 
   
|locate_clip|:
   Opens the folder in your file system where the selected clip is located in your OS default file manager. See also the chapter :ref:`locate_clip`.

|reload_clip|:
   Reloads the selected clip from the file system. See also the chapter :ref:`reload_clip`.

|replace_clip|:
   Opens your OS file manager. Select the file you want to replace the selected clip with. See also the chapter :ref:`replace_clip`.

|replace_clip_in_timeline|:
   You need to select two clips in the bin for this action. The clip you right-clicked on will be replace by the other. See also the chapter :ref:`replace_clip`.

|duplicate_clip|:
   Creates a copy of the selected clip. See also the chapter :ref:`duplicate_clip`.

|transcode|:
   Opens a window with the selected clips where you can select the format to transcode the clips to. See also the chapter :ref:`transcode_to_edit_friendly_format`.

|proxy_clip|:
   If checked indicates that the selected clip is a proxy clip* :ref:`make_proxy_clip`. If the option is greyed out, proxy clips are not enabled for the project. Go to the :doc:`/project_and_asset_management/project_settings/proxy_settings` tab in the Project Settings (:menuselection:`Menu --> File --> Project Settings`) and enable proxy clips.

|clip_properties|:
   Opens the widget for the Clip Properties. For more details refer to the chapter :ref:`media_menu-clip_properties`.

|edit_clip|:
   Opens the application associated with the type of the selected clip. See also the chapter :ref:`edit_clip`.

|rename_clip| (default keyboard shortcut :kbd:`F2`):
   Opens the clip name field in the bin for editing. This does not change the filename in the file system.

|delete_clip|:
   Deletes the selected clips. If the clips are being used in the timeline or in sequences, a warning windows is opened where you need to confirm that the clips' instances in the timeline will also be deleted. See also the chapter :ref:`delete_clip`.
