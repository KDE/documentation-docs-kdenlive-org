.. meta::
   :description: Introduction to Kdenlive's window system and widgets
   :keywords: KDE, Kdenlive, user interface, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Eugen Mohr
   :author: - Maris Stalte
             
   :license: Creative Commons License SA 4.0

.. _user_interface:

##############
User interface
##############

After starting Kdenlive the Kdenlive window should look something similar to the image below; as Kdenlive’s user interface is consistent across all platforms.

Kdenlive’s interface is separated into four main parts:

:ref:`Menu` and :ref:`workspace_layouts` at the very top.

:ref:`Toolbars` at the top and above the timeline

:ref:`Window <view_menu>` in the middle.

:ref:`status_bar` at the bottom.

.. figure:: /images/interface_window_system_editing_screen.png
   :width: 650px
   :alt: interface_window-system_editing-screen

   Kdenlive’s default Screen Layout (example editing view). Topbar (blue), Toolbars (yellow), Window (green) and Status Bar (red).

.. toctree::
   :hidden:
   :maxdepth: 2
   :glob:

   user_interface/monitors
   user_interface/timeline
   user_interface/workspace_layouts
   user_interface/toolbars
   user_interface/shortcuts
   user_interface/menu
  
   ------------
   Kdenlive UI
   ------------
   
   This page introduces the Kdenlive user interface (UI), explaining where to find each group of features, and how the highly focused and tightly integrated Media, Edit, Color, Fairlight, and Deliver pages work together to let you pursue nearly any post-production workflow you can imagine.

Customizing interface
---------------------
The User interface model has a clear division between the different panes, that they work on allows you to reorder them, drag them out into separate windows or size them up as you will.

The interface is divided into many sections. The menu is on top and then on the left you can make a note about the project. All loaded clips and videos are in the project tree, the second section. Third section is the Effect list. You can apply many transaction effects on your video. You can always watch the project preview in the last section. You can create as many audio/video track as you need. This is impressive about Kdenlive. If you’re new to video editing then this is very useful. You can import multiple title clips inside video track.Remove/Adjust Sections

You won't notice on the spot, but the tabs that appear on the bottom of the panes aren't built in them, but change according to what panes you have aggregated into that particular frame. This way you can group functions that you don't expect to use simultaneously into a single place on the user interface, thus reducing clutter.

If you don’t want certain sections on the screen then you can simply delete them to make other sections wider. Just click the close button on that section and that section will be closed, by removing unnecessary video/audio tracks and now You can organize enough space to preview your project and all other necessary sections are wider.


.. figure:: /images/Kdenlive_user_interface.png
   :width: 650px
   :alt: interface_window-system_editing-screen

1. Project bin.
---------------
The top left section of the screen is known as the library, bin or browser, where clips, still images, audio files etc. are displayed, ready for use.Replicating the folder naming system within the editing software library will help keep everything organized. It may be helpful to label each clip with one or more descriptive keywords. These can be searched and are a useful way to rapidly locate the desired footage, especially with the use of many clips. It is preferable to edit using the same frame rate and frame size that the footage was shot with. 

2. Clip monitor.
----------------
The preview or canvas window (top centre) plays what is currently selected in the timeline.

3. Project Monitor.
-------------------
This screen shows all effects such as titles or transitions were be applied to the footage. To apply effects, select it from the effects menu and then drag and drop it between the two clips where it is.

4. Editing toolbar.
-------------------
Trimming and other editing tools do not alter or delete the original footage, they only adjust the copy that has been added to the timeline.

5. The timeline editor.
-----------------------
This is the area where clips are placed in the order in which they will appear in the final video and trimmed to the desired length and content. When assembling the initial “rough cut” of the video, users can place clips from the library into the timeline in the desired sequence. To reorder clips simply click and drag them to a new position. Trimming tools allow only the relevant footage to be used by marking the desired start and end (“in” and “out”) points on each clip, to shorten or lengthen it.

6. Audio Mixer.
---------------

The sound quality and volume can be adjusted, either for the entire sequence or selected sections. The editing software will display audio meters and generally any dialogue or narration in a video should be at about -10dB most of the time.
