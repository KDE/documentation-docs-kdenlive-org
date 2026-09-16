.. meta::

   :description: Kdenlive Video Effects - typewriter
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, typewriter, typing

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0

.. .. versionadded:: 26.08


Typewriter
==========

.. figure:: /images/effects_and_compositions/effects-typewriter-2608.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| typewriter

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      MLT
   :**Source filter**:
      typewriter
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter displays texts from a title clip in a typewriter-style character by character, word by word, or line by line.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 30 10 60
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Frames step
     - Integer
     - Defines how many frames it takes to display the next character, word, or line
   * - Fluctuation
     - Integer
     - Inserts some randomness to the displaying of the characters, words, or lines.
   * - Random seed
     - Integer
     - Seed value for the random generator
   * - Type
     - Selection
     - Determines the type of display

The following selection items are available:

:guilabel:`Type`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Char by char
     - Displays the text character by character (a space is considered a character)
   * - Word by word
     - Displays the text word by word (spaces are not counted)
   * - Line by line
     - Displays the text line by line


.. note:: The :ref:`Title Editor <title-editor>` has this effect :ref:`built-in <title-text_typewriter>` already. There it can be set for each text object individually. Using the effect on a title clip in the timeline or bin applies the typewriter effect to **all** text objects in the title clip. That means that if set to character-by-character, for example, the characters of all text objects in the title clip will be displayed *one by one*, but *from all text objects at the same time*.

.. hint:: This can be combined with a typewriter sound effect from Freesound which is part of the :doc:`Online Resources</project_and_asset_management/project_bin/online_resources>` functionality.
