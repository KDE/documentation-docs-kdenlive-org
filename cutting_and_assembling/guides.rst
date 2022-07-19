.. meta::
   :description: Set guides in Kdenlive video editor
   :keywords: KDE, Kdenlive, set guides, DVD, youtube, editing, timeline, documentation, user manual, video editor, open source, free, learn, easy


.. metadata-placeholder

   :authors: - Annew (https://userbase.kde.org/User:Annew)
             - Claus Christensen
             - Yuri Chornoivan
             - Gallaecio (https://userbase.kde.org/User:Gallaecio)
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Dbolton (https://userbase.kde.org/User:Dbolton)
             - Jack (https://userbase.kde.org/User:Jack)
             - Eugen Mohr

   :license: Creative Commons License SA 4.0



.. _guides:

Guides
======

.. contents::




.. image:: /images/Kdenlive_Add_guide.png
   :align: left
   :alt: Kdenlive_Add_guide

Guides are labels on the timeline that can be added by right-clicking at a spot on the timeline ruler and choosing :menuselection:`Add/Remove Guide` or press :kbd:`G`. You can put a comment in the guide and make the comment display by choosing :ref:`editing` in the :menuselection:`Timeline` menu or by clicking on the :ref:`editing` button.

.. rst-class:: clear-both

.. versionadded:: 21.08
   
:guilabel:`Guides Locked`: See :ref:`move_guides_with_spacer_tool`  

.. versionadded:: 22.04

:guilabel:`Set Zone In/Out`. See :ref:`timeline-preview-rendering`

:guilabel:`Add Project Notes`: See :ref:`notes`



.. versionadded:: 20.12

:guilabel:`Add Subtitle`: See :ref:`subtitle`

Guides in the picture below are the purple flags. Not to be confused with :ref:`clips` (gold in the picture below). Guides are static on the timeline and are stationary when clips are moved around. Markers are inside the clips and move with the clips.


.. image:: /images/Kdenlive_Markers_and_guides_crop.png
   :align: left
   :alt: Kdenlive_Markers_and_guides_crop


Guides can be used to define regions for rendering. See :ref:`rendering`.


Guides can also be used as chapters for DVD videos. See :ref:`rendering`.

.. versionadded:: 22.08

**Export guides as chapter description**

Guides can mark chapters or different sections of a video while editing. Uploading edited videos to platforms like YouTube, the guides can be exported as chapter marks that are supported by YouTube. This can be done by :guilabel:`Copy to Clipboard` and paste then into YouTube.

Right click in the timeline ruler and choose :guilabel:`Export Guides` or :menuselection:`Timeline -> Guides -> Export Guides`. Then the window `Export guides as chapters description` appears.

.. image:: /images/Kdenlive_export_guides.png
   :alt: Kdenlive_export_guides

:guilabel:`Marker Type`: Choose one of the guide types to mark chapters and use other types to do other things.

:guilabel:`Offset`: This adds the ability to set a general offset (hh:mm:ss:ff) to each guide.

:guilabel:`Format`: This defines how the chapter marks are exported. If using the default format string, Kdenlive check if the chapter marker matches YouTube's guideline, and display a notice if it doesn't match.

{{nexttimecode}}: Allow describe chapter time range in a single line (default).

{{comment}}: Show the guide text (default).

{{frame}}: Adds the frame number of each guide.

:guilabel:`Exported`: Shows what get exported. To change the guide text you have to edit the guide in the timeline.

:guilabel:`Copy to Clipboard`: Copy the data viewed in :guilabel:`Exported` into the clipboard to use it in other applications (Youtube).

.. _move_guides_with_spacer_tool:

Move Guides with Spacer Tool
----------------------------

.. versionadded:: 21.08.0

Easily moves Guides along with clips using the Spacer Tool by using the new :menuselection:`Guides Locked` option.


.. image:: /images/guidemove.gif
   :align: left
   :alt: guidemove
  


