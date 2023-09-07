.. meta::
   :description: Introduction to Kdenlive's User Interface
   :keywords: KDE, Kdenlive, user interface, documentation, user manual, video editor, open source, free, learn, easy, user interface, layout, widget

.. metadata-placeholder

   :authors: - Eugen Mohr
             - Maris Stalte (https://userbase.kde.org/User:limerick)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             
   :license: Creative Commons License SA 4.0

.. _user_interface:

##############
User Interface
##############

This section introduces the Kdenlive user interface (UI), explains the various :ref:`elements <ui_elements>`, :ref:`icons <ui_elements-icons>` and :ref:`buttons <ui_elements-icons>`, the :ref:`menu options <menu>`, the default :ref:`keyboard shortcuts <ui-keyboard_shortcuts>` that can speed up your editing work, and how you can :ref:`customize the layout <ui-workspace_layouts>` to fit your specific post-production workflow.

After starting Kdenlive the window should look similar to the image below. Kdenlive’s user interface is consistent across all platforms, so it doesn't matter whether your operating system is Linux, Windows or MacOS. Of course, icons and text look different.

Kdenlive’s user interface is separated into four main parts:

[A] The Workspace with the various :term:`widgets<widget>` that can be arranged to your needs. See the :ref:`view_menu` and :ref:`ui-workspace_layouts` for more details.

[B] The Menu Bar with the :ref:`Menu <menu>` and list of :ref:`ui-workspace_layouts`.

[C] The :ref:`toolbars` below the menu bar and above the :ref:`timeline`.

[D] The :ref:`status_bar` at the bottom of the screen.

.. figure:: /images/user_interface/kdenlive2304_ui-screen_layout.webp
   :width: 650px
   :alt: kdenlive2304_ui-screen_layout

   Kdenlive’s default screen layout (example uses the Editing view): Menu Bar (blue), Toolbars (yellow), Workspace (green) and Status Bar (red).

..

.. rubric:: Workspaces

The Workspace model follows the video editing workflow and can be adapted to your individual style and preferences. By default, Kdenlive starts with the Editing workspace model that looks like this:

.. figure::  /images/user_interface/kdenlive2304_ui-workspaces.webp
   :width: 650px
   :alt: kdenlive2304_ui-workspaces

   Kdenlive’s default workspaces (example uses the Editing view)

..

1. **Project Bin**, **Library**

   This is where you keep your source files (video clips, images and image sequences, title and color clips, animations, audio files). In this screenshot the :term:`widgets<widget>` for :ref:`Undo History <undo_history>`, :ref:`Compositions <transitions_compositions>`, and :ref:`Effects <effects-effects_tab>` have been added to this section.

2. **Clip Monitor**

   This is where the clip selected in the project bin is displayed. In this screenshot the widget for :term:`Library` has been added to this section. See the chapter :ref:`ui-monitors_clip_monitor` for more details.

3. **Project Monitor**

   This is where the content of the :term:`timeline` is being displayed with all effects and compositions applied. In this screenshot the widgets for :ref:`Speech Editor <effects-speech_to_text>` and :ref:`Project Notes <notes>` have been added to this section. See the chapter :ref:`ui-monitors_project_monitor` for more details.

4. **Timeline**

   Most of the action is taking place in the timeline. Here you put your sources in the order in which they will appear in the final video, make your :ref:`edits <editing>` (cuts and trimmings), :ref:`apply effects <effects-apply_effects>`, add :ref:`compositions <transitions_compositions>` and :ref:`transitions <transitions_compositions>`, and add audio and sound tracks. See the chapter :ref:`timeline` for more details.

5. **Timeline Toolbar**

   This is where you find all the tools you need to edit your video project. See the chapter :ref:`timeline_toolbar3` for more details.

6. **Audio Mixer**

   This section holds the :ref:`audio mixing panel <effects-audio_tools>` where you control the volume and pan of the various audio tracks and the master.

7. **Menu Bar** and main **Toolbar**

   At the top of the screen you have access to the menu (see :ref:`menubar` and :ref:`Menu <menu>` for more details), the :ref:`ui-workspace_layouts` and the :ref:`main_toolbar`. The menu bar can be switched on and off with :kbd:`Ctrl+M`.

8. **Status Bar**

   Kdenlive displays context-specific information or hints on the left-hand side of the status bar depending on where you hover the mouse pointer. In the middle you see the names of the clips you hover over in the timeline. This is also where error messages come up when working with clips in the timeline. On the right-hand side Kdenlive displays the currently selected timeline :ref:`edit tool <timeline_edit_tools>` and the icons to toggle various timeline features. See the sections about :ref:`status bar icons <ui_elements-status_bar_icons>` and the :ref:`status bar <status_toolbar>` for more details.


.. toctree::
   :hidden:
   :glob:

   user_interface/ui_elements
   user_interface/shortcuts
   user_interface/monitors
   user_interface/timeline
   user_interface/toolbars
   user_interface/menu
   user_interface/workspace_layouts
   user_interface/customizing_interface
