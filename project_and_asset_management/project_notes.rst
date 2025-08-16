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
             - Eugen Mohr

   :license: Creative Commons License SA 4.0


   
Project Notes
=============

For complex or big projects, it is good practice to keep notes about the footage and the scenes. As they are saved with the project, the notes can be used effectively for collaboration between different people working on the project. Or, sometimes, you simply want to keep some notes about your project to remember ideas or things to do.

You enable the Project Notes widget from the Kdenlive :menuselection:`Menu --> View --> Project Notes`. You can move it around and dock it where it fits your working style and workflow. For more details about adjusting the workspace see the chapters about :doc:`/user_interface/workspace_layouts` and :doc:`/user_interface/customizing_interface`.

.. figure:: /images/project_and_asset_management/project_and_asset_management-project_notes-2508.webp
   :width: 360px
   :figwidth: 360px
   :align: left

   The Project Notes widget with open search function

It is basically a small text editor, but also has the ability to create links to some places in your project's timeline.

.. rst-class:: clear-both

:1: |list-add|\ :guilabel:`Add Project Note`

:2: |document-import|\ :guilabel:`Reassign selected timecodes to current Bin clip`

.. .. versionadded:: 25.08

:3: |link|\ :guilabel:`Reassign selected timecodes to current timeline clip`

:4: |bookmark-new|\ :guilabel:`Create markers from selected timecodes`. Creates markers in the timeline from the selected timecodes (doesn’t matter if other text is selected too).

.. .. versionadded:: 25.04

:5: |edit-find|\ :guilabel:`Search`, :kbd:`Ctrl+F`. When the search text is found the search background changes from red to green.

:6: |go-up|\ :guilabel:`Find Previous`, :kbd:`Shift+F3`

:7: |go-down|\ :guilabel:`Find Next`, :kbd:`F3`

:8: Notes area

Taking notes just takes entering text into the notes area (4). If you want to add timecodes, move the playhead in the timeline to the desired position, and click on |bookmark-new|\ :guilabel:`Add Project Note`. Kdenlive inserts the timecode as a link. You can then add text to further describe the timecode. Click the timecode link to position the playhead to that precise point in the timeline.

.. figure:: /images/project_and_asset_management/project_notes_examples.webp
   :width: 360px
   :figwidth: 360px
   :align: left

   Project Notes examples

This example has two notes with timecodes, and one just as simple text.

.. rst-class:: clear-both

A neat feature is the ability to create :doc:`markers</cutting_and_assembling/markers>` from the timecodes in the notes. Select a timecode (it does not matter if you select the additional text), and click on |list-add|\ :guilabel:`Create markers from selected timecodes`, and Kdenlive creates a marker at that precise point in the timeline.