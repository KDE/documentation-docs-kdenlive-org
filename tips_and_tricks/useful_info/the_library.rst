.. meta::
   :description: Kdenlive Tips & Tricks - The Library: Copy & Paste Between Projects
   :keywords: KDE, Kdenlive, tips, tricks, tips & tricks, useful information, library, copy paste between projects, editing, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - TheDiveO
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             
   :license: Creative Commons License SA 4.0


The Library: Copy & Paste Between Projects
==========================================

.. .. versionadded:: 16.12.0

The **Library** is Kdenlive's way to copy and paste sets of clips and transitions between different projects. It is not just a clipboard, but instead it is a library for all the things you use in more than a single project. The Library came to life around Kdenlive 15.04 or so. Let's dive right into how to use the library in your daily Kdenlive workflow!

.. _library-copy_to_library:

Step 1: Copy Stuff to Your Library
----------------------------------

.. figure:: /images/tips_and_tricks/kdenlive2308_library_widget_01.webp
   :align: left
   :alt: library-pane
   :width: 350px

   Library with example folders

The **Library** is Kdenlive's central place **for copying and pasting between projects**.

If you do not see the library :term:`widget`, enable it in :menuselection:`Menu --> View --> Library`.

By default, the library is empty. For illustration purposes folders for **Audio**, **Video** and **Stock** footage have been created.

.. note:: The library should look slightly familiar, as it works and behaves similar to the project bin. However, while the project bin changes with each project, the library is independent of your projects. It is always the same library, there is only one of it.

.. tip:: A quite useful :doc:`workspace layout </user_interface/workspace_layouts>` is to group the library together with the project bin, and optionally the project notes. This way, you do not need extra screen space for the library, yet it is no further away than just a single click.

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_library_timeline_01.webp
      :align: left
      :alt: kdenlive2308_library_timeline_01.webp
      :width: 350px

      Timeline with clips selected for the library

   Next, select some clips, as well as transitions/compositions, in the timeline. You can load an existing project and select some timeline clips and transitions at any time in order to copy it into your library. There is no separate import. Simply load a project or create a new one. 

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_library_widget_01a.webp
      :align: left
      :alt: kdenlive2308_library_widget_01a.webp
      :width: 350px

      Library widget

   Switch to the library :term:`widget`, if you have not yet done so. Then press the :guilabel:`Add Timeline Selection to Library` |bookmark| button.

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_library_widget_03.webp
      :align: left
      :alt: kdenlive2308_library_widget_03.webp
      :width: 250px

      Enter name for new library item

   Kdenlive now asks you to **name your new library item**. Give it some name, and click :guilabel:`OK` to copy the selected timeline clips (with effects) and transitions into your library.

.. not sure why this note is here:
   **Please note**: at this time, the names of library item need to be valid filenames.

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_library_widget_04.webp
      :align: left
      :alt: kdenlive2308_library_widget_04.webp
      :width: 350px

      Library with the newly created item

   Of course, you can even **neatly organize** your library items **into folders**, and subfolders. This is similar to what you may have come to known from Kdenlive's (project) bin, where you also can use folders to organize your project (source) clips.

   Use the :guilabel:`Add Folder` |folder-new| button at the bottom of the library to create a new folder. You can rearrange library items and folders at any time by simple dragging them into their new place.\ [1]_

|

.. _library-paste_from_library:

Step 2: Paste Library Item into (New) Project
---------------------------------------------

.. container:: clear-both
   
   .. figure:: /images/tips_and_tricks/kdenlive2308_library_widget_04a.webp
      :align: left
      :alt: kdenlive2308_library_widget_04a.webp
      :width: 350px

      Library with new item to be copied to project bin

   Now switch to another Kdenlive project by loading it, or alternatively start with a fresh project from scratch. Next, go to the library pane and **select the library item** you want to paste into your project. Then, press the :guilabel:`Add Clip to Project` |kdenlive-add-clip| button (up to Kdenlive 16.08.1 this is instead the :guilabel:`+` button, located in the same place).

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_library_project_bin_01.webp
      :align: left
      :alt: kdenlive2308_library_project_bin_01.webp
      :width: 350px

      Project bin with the new library item as a separate clip

   Your project bin now contains the new library item you have just added.

   You can rename library items at any time: :kbd:`RMB`, then :guilabel:`Rename Library Clip`.\ [2]_

.. rst-class:: clear-both


.. _library-drag_from_library:

Step 3: Drag Library Item into Timeline
---------------------------------------

.. figure:: /images/tips_and_tricks/kdenlive2308_library_timeline_02.webp
   :align: left
   :alt: kdenlive2308_library_timeline_02.webp
   :width: 350px

   Timeline with the library clip as a single clip

The selected library item has now been added to your project bin. You will see this by switching to the project bin :term:`widget`. You still have only a **single (library) clip** at this stage. You can now drag it into the timeline, wherever you want.

.. note:: You cannot directly drag a library item from the library into your timeline. You always need to add it to your project bin first.

.. rst-class:: clear-both


.. _library-expand_library_clip:

Step 4: Expand Library Clip
---------------------------

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_library_expand_clip.webp
      :align: left
      :alt: kdenlive2308_library_expand_clip.webp
      :width: 350px

      :menuselection:`Menu --> Timeline`

   Often, you want to edit the contents of a library clip right after after you have placed it on the timeline. **Expanding** means that you want to break up a library clip into its contents for further editing. So, simply select the library clip in the timeline. Then choose :menuselection:`Menu --> Timeline --> Current Clip --> Expand Clip`. Alternatively, you can create a keyboard shortcut for that.

.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_library_timeline_03.webp
      :align: left
      :alt: kdenlive2308_library_timeline_03.webp
      :width: 350px

      Timeline with the expanded library clip

   You can now edit the expanded contents as you would edit any other timeline content.


.. container:: clear-both

   .. figure:: /images/tips_and_tricks/kdenlive2308_library_project_bin_02.webp
      :align: left
      :width: 300px
      :alt: kdenlive2308_library_project_bin_02.webp

      Project bin with expanded library Clip

   Kdenlive has expanded all the clips inside the library item into the bin folder :guilabel:`Pasted clips`. You can rename the folder if you want. Another library clip will expand into a new :guilabel:`Pasted clips` folder. So you may want to keep those separate. Your choice.

   After successful expansion, you may now remove the original library clip from your bin. It is not needed anymore (as you can also tell from the missing reference count).

.. rst-class:: clear-both


.. _library-clip_expansion_details:

Clip Expansion Details
----------------------

.. figure:: /images/tips_and_tricks/kdenlive2308_library_timeline_04.webp
   :align: left
   :alt: kdenlive2308_library_timeline_04.webp
   :width: 350px

   Timeline with library clip (1) and expanded (2)

Library clips will be expanded **from the bottom up**. This means that in case a library clip contains multiple tracks, then you need to place the library on a track with enough room (i.e. tracks) above for the clip to expand.

.. rst-class:: clear-both

If there are not enough tracks above the library clip, yet there are enough tracks in the timeline, then Kdenlive will attempt to **shuffle the library clip down** a number of tracks before expanding it.

.. attention:: In any case, to expand a library clip into its contents, you will always need **necessary free space in the timeline**. This means that there cannot be any clips or transitions within the start and end of the library clip on as many adjacent tracks as are needed when expanding a multi-track library item. Simply put: just make sure that the library item has room to expand. There can be other clips and transitions above and below the library clip, they just need to be outside of the area of expansion.

.. figure:: /images/tips_and_tricks/kdenlive2308_library_timeline_05.webp
   :align: left
   :alt: kdenlive2308_library_timeline_05.webp
   :width: 350px
   :figwidth: 350px

   Timeline with expanded library clip abutting a clip with a transition in the top-most track

You can also **expand a library immediately below a transition**; that is, the library clip is on the next lower track in the timeline. This is useful for such cases where you, for instance, have a clip running the full length of your project on the topmost track and showing your company logo, channel logo, or something similar. If you then use an explicit transition added to this clip over compositing, you can still correctly expand the library clip on the second-topmost track.

.. rst-class:: clear-both

.. _library-configure_library_storage_location:

Configuring Your Library Storage Location
-----------------------------------------

All items in your Kdenlive library are stored in a user-configurable place inside your file system. The default location, unless configured otherwise, is where your other semi-temporary caching data is stored. Typically, this is :file:`$HOME/.local/share/kdenlive/library` (Linux) and :file:`%APPDATA%\\Roaming\\kdenlive\\library` (Windows). Your library clips are then stored inside this directory, as well as in subdirectories in case you also use library folders.

.. figure:: /images/tips_and_tricks/kdenlive2308_settings_library_location.webp
   :align: left
   :alt: kdenlive2308_settings_library_location.webp
   :width: 350px

   Setting the library folder location

To change the location of your library, go to :menuselection:`Menu --> Settings --> Configure Kdenlive`. Next, select the section :guilabel:`Environment`. Switch to the :guilabel:`Default folders` tab. Locate the part titled :guilabel:`Library folder`, and deselect the option :guilabel:`Use default folder`. Select or enter another location for your Kdenlive library.

.. attention:: Kdenlive will not move existing library files to the new location you have set. You will need to do this manually using a file browser or from the command line.



.. rubric:: Notes

.. |kdenlive_org| raw:: html

   <a href="https://kdenlive.org/en/project/the-library-copy-paste-between-projects/" target="_blank">kdenlive.org</a>

**Sources**
  The original text was submitted by user *TheDiveO* to the now defunct kdenlive.org blog. For this documentation it has been lifted from |kdenlive_org|, updated and adapted to match the overall style.

----

.. [1] You can use the file manager of your choice to manage your library. Kdenlive simply reads the contents of the directory you specified in the settings. For more complex file management this is the recommended way. Changes to the library folder made outside of Kdenlive are reflected in near real-time.

.. [2] For more complex renaming tasks use the file manager or bulk rename utility if your choice. Changes to the library folder made outside of Kdenlive are reflected in near real-time.