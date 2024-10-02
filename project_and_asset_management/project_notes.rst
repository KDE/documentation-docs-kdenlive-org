.. meta::
   :description: Kdenlive Documentation - Project Notes
   :keywords: KDE, Kdenlive, project notes, documentation, user manual, video editor, open source, free, learn, easy, project, asset, management, assets

.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Jean-Baptiste Mardelle <jb@kdenlive.org>
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Jack (https://userbase.kde.org/User:Jack)

   :license: Creative Commons License SA 4.0


   
Project Notes
=============

For complex or big projects, it is good practice to keep notes about the footage and the scenes. As they are saved with the project, the notes can be used effectively for collaboration between different people working on the project. Or, sometimes, you simply want to keep some notes about your project to remember ideas or things to do.

You enable the Project Notes widget from the Kdenlive :menuselection:`Menu --> View --> Project Notes`. You can move it around and dock it where it fits your working style and workflow. For more details about adjusting the workspace see the chapters about :doc:`/user_interface/workspace_layouts` and :doc:`/user_interface/customizing_interface`.

.. figure:: /images/project_and_asset_management/project_notes.webp
   :width: 360px
   :figwidth: 360px
   :align: left
   :alt: project_notes

   The Project Notes widget

It is basically a small text editor, but also has the ability to create links to some places in your project's timeline.

:1: |bookmark-new|\ :guilabel:`Add Project Note`

:2: |edit-find-replace|\ :guilabel:`Reassign selected timecode to current clip`

:3: |list-add|\ :guilabel:`Create markers from selected timecodes`

:4: Notes area

.. rst-class:: clear-both

Taking notes just takes entering text into the notes area (4). If you want to add timecodes, move the playhead in the timeline to the desired position, and click on |bookmark-new|\ :guilabel:`Add Project Note`. Kdenlive inserts the timecode as a link. You can then add text to further describe the timecode. Click the timecode link to position the playhead to that precise point in the timeline.

.. figure:: /images/project_and_asset_management/project_notes_examples.webp
   :width: 360px
   :figwidth: 360px
   :align: left
   :alt: project_notes_examples

   Project Notes examples

This example has two notes with timecodes, and one just as simple text.

.. rst-class:: clear-both

A neat feature is the ability to create :doc:`markers</cutting_and_assembling/markers>` from the timecodes in the notes. Select a timecode (it does not matter if you select the additional text), and click on |list-add|\ :guilabel:`Create markers from selected timecodes`, and Kdenlive creates a marker at that precise point in the timeline.