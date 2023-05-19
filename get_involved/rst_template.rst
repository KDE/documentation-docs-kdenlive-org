.. meta::
   :description: Do your first steps with Kdenlive video editor, adjust this description to the content of this rst file
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, add here more words that search engines find the Kdenlive documentation

.. metadata-placeholder

   :authors: - add your name here

   :license: Creative Commons License SA 4.0

..  This is a remark and only show up in the file itself


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
* 2 empty lines after a :ref: or before a reference

After a command with .. next line must be indented by 3 blank spaces to make the below line is part of the command. The number of indent spaces must be always the same. 

.. figure:: /images/getting_started/kdenlive_add_last_clip.webp
   :align: left
   :width: 450px 
   :alt: Optional text which appears when the picture is not found
      
   Description of the picture (caption or legend)

The `rst-class:: clear-both` resets floating text before a new chapter 

.. rst-class:: clear-both


Images side by side

|pic1| any text |pic2|

.. |pic1| image:: /images/nikon-50mm.jpg
   :alt: nikon-50mm
   :width: 30%

.. |pic2| image:: /images/nikon-35mm.jpg
   :alt: nikon-35mm
   :width: 30%

| These lines are
| broken exactly like in
| the source file.

Exponent
2 :sup:`8` = 256

This is a footnote [1]_ 

This is a next footnote [#]_ 

Link to a file :file:`quickstart-tutorial/Videos/`

Download link :download:`kdenlive-tutorial-videos-2011-ogv.tar.bz2 </files/kdenlive-tutorial-videos-2011-ogv.tar.bz2>`

This is a link to :ref:`template` and shows the text below the link

This is a link to `edit_an-animation` and show the word "here" :ref:`here <edit_an-animation>` 

.. note::
   This shows a note 

.. attention::
   This shows an attention window

.. tip::
   This shows a tip window

.. hint::
   This shows a hint window

.. Warning::
   This shows a warning window 


This is **bold text**

This is *italic text*

backquotes ``text`` for code samples.

Use for menu selection :menuselection:`File --> New` (This is used to mark a complete sequence of menu selections, including selecting submenus and choosing a specific operation) 

This shows an icon |kdenlive-add-clip| (all linked icons check substitutions in `conf.py`)

This is a keyboard shortcut :kbd:`Ctrl+Wheel` (keep the 2 keys inside 1 \` \` due to translation reasons)

This is a text in the GUI :guilabel:`Play` (Including button labels, window titles, field names, menu and menu selection names, and even values in selection lists)

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


.. [1] Text of footnote 1
.. [#] Text of footnote 2

Toctree (Toc = Table of Content) adds the content on the left side sidebar. Only needed if there are subfolders.

.. toctree::
   :hidden:
   :glob: 
   
   get_involved/*