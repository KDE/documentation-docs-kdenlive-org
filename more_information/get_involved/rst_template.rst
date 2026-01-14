.. _rst-template:

************
RST template
************

This template page can be used for a new document page or as a guide or just for reference.

If you are using this template for a new document delete all line until ``.. meta::`` is the top line.  


.. meta::
   :description: Do your first steps with Kdenlive video editor, adjust this description to the content of this rst file
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, add here more words that search engines find the Kdenlive documentation

.. metadata-placeholder

   :authors: - add your name here

   :license: Creative Commons License SA 4.0

.. This is a remark and only show up in the file itself

.. metadata-placeholder: must be placed before :authors: and :license: to avoid i18n translation.

.. _template:

**********
Main Title
**********


.. _template2:

Level 1 title
=============

Level 2 title
-------------

Level 3 title
~~~~~~~~~~~~~

Do not use level 4 title

File name:

* Not longer than 40 character incl. ".rst"
* No space in any file name (including pictures)!
* All in lowercase letters

Code quality

* 1 empty line between title or text paragraph
* 2 empty lines after a ``:ref:`` or before a reference

After a directive with ``..``, the next line must be indented by 3 blank spaces to make the below line part of the directive. The number of indent spaces must be always the same.

.. figures: Only use figures
   Screenshots:
   Use "webp" as file type
   Image name convention: "[sub_chapter]-<feature_name>-(4digit Kdenlive version).webp"
   Example:
   "configure-speech2text_vosk_drag-2412.webp"
   "rendering-render_dialog-2403.webp"
   "project_bin-create_animation-2208.webp"
   :align: make it possible that you have text on the right site of the figure  
   :with: restrict the figure size
   :figwith: the caption get a line break after 250px

.. figure:: /images/getting_started/kdenlive_add_last_clip.webp
   :align: left
   :width: 500px
   :figwidth: 500px
         
   Description of the picture (caption or legend)

.. sidebar:: |kdenlive-show-video| Motion Tracker

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      opencv
   :**Source filter**:
      tracker
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both

The ``rst-class:: clear-both`` directive resets floating text (``:align: left`` or ``right``) before a new chapter or a ``list-table`` directive.

The pipe character ``|`` is needed to execute ``rst-class:: clear-both`` when white space is following or in case of a ``list-table`` directive after a ``figure`` directive with ``:align: left`` or ``align: right`` in order for Google Chrome to properly display the table. If there is no ``:align: left`` or ``:align: right``, a ``list-table`` can follow the ``figure`` directive without the need for ``rst-class:: clear-both`` and the ``|`` pipe character. Try to avoid that and do not use ``:align:`` when a ``list-table`` follows.

|

.. list-table::
   :width: 100%
   :widths: 30 70
   :header-rows: 1
   :class: table-wrap

   * - UI Element
     - Description
   * - 1 :guilabel:`edit frame`
     - [Project Monitor only] Identifies the object or area of the effect. :term:`Edit Mode<edit mode>` needs to be enabled for the frame to show.
   * - 2 :guilabel:`edit frame handles`
     - Used to change the size (square handles) and move the frame (circle in the middle)


.. rubric:: Images side by side

Use ``.. rubric::`` if you want a section-like element that is not included in the table of contents.

|pic1| any text |pic2|

.. |pic1| image:: /images/tips_and_tricks/shooting_nikon_50mm.webp
   :width: 30%

.. |pic2| image:: /images/tips_and_tricks/shooting_nikon_35mm.webp
   :width: 30%

| These lines are
| broken exactly like in
| the source file.

four - (hyphen) in a row creates a horizontal line to visually separate content elements. Adding blank lines before and after.

----


Exponent
2 :sup:`8` = 256

This is a footnote\ [1]_ 

This is the next footnote\ [#]_ 

Link to a file :file:`quickstart-tutorial/Videos/`

Download link :download:`kdenlive-tutorial-videos-2011-ogv.tar.bz2 </files/kdenlive-tutorial-videos-2011-ogv.tar.bz2>`

This is a link to :ref:`template` and shows the text below the link

This is a link to `edit_an-animation` and shows the word "here" :ref:`here <edit_an-animation>` 

.. note:: This shows a note window

.. attention:: This shows an attention window

.. tip:: This shows a tip window

.. hint:: This shows a hint window

.. Warning:: This shows a warning window 


.. admonition:: Windows Only!

   This is a warning for Windows user only.


This is **bold text**

This is *italic text*

backquotes ``text`` for code samples.

Glossary Entry. Link a Term to its glossary entry :term:`Active Track`. Showing different text :term:`make a track active <Active Track>`

Use for menu selection :menuselection:`Menu --> File --> New` (This is used to mark a complete sequence of menu selections, including selecting submenus and choosing a specific operation)

This shows an icon |kdenlive-add-clip| (for all linked icons check substitutions in `conf.py`)

This is a keyboard shortcut :kbd:`Ctrl+Wheel` (keep the 2 keys inside 1 \` \` due to translation reasons)

This is a text in the GUI :guilabel:`Play` (including button labels, window titles, field names, menu and menu selection names, and even values in selection lists)

.. code-block:: bash

   This shows a code block
   SUBSYSTEMS"usb", ATTRS{idVendor}


.. versionadded:: 21.12
   This feature was **added** in version 21.12

.. versionchanged:: 22.12
   This feature was **changed** in version 22.12

.. deprecated:: 23.04
   This feature was **exchanged** or **removed** in version 23.04


.. Open a link in a new window in reStructuredText, https://stackoverflow.com/questions/11716781/open-a-link-in-a-new-window-in-restructuredtext

Web page link open in a new window |kde| 

.. |kde| raw:: html

   <a href="https://www.kde.org" target="_blank">KDE</a>

Web page link open in the same window `KDE store <https://store.kde.org/browse?cat=333&ord=latest>`_


* This is a bulleted list.
* It has two items, the second
  item uses two lines.

1. This is a numbered list.
2. It has two items too.

#. This is a numbered list.
#. It has two items too.

.. glossary::
   :sorted:

``.. glossary::`` and ``:sorted:``: Insert a glossary which is sorted.


.. [1] Text of footnote 1. The backslash at the end of the word moves the footnote number closer to the text
.. [#] Text of footnote 2

Toctree (Toc = Table of Content) adds the content on the left-side sidebar. Only needed if there are subfolders.

.. .. toctree::
   :hidden:
   :glob: 
   
   get_involved/*
