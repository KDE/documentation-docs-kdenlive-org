.. meta::
   :description: Kdenlive Tips & Tricks - Improved Handling of Library Clips
   :keywords: KDE, Kdenlive, tips, tricks, tips & tricks, useful information, library, editing, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - TheDiveO
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             
   :license: Creative Commons License SA 4.0


.. _library_clips:

Improved Handling of Library Clips
==================================

.. .. versionadded:: 16.12.0

Kdenlive 16.12.0 introduced further improvements to its :term:`library` clip expansion feature (and, in consequence, to :abbr:`MLT (Media Lovin' Toolkit - An open source software multimedia framework designed and developed for tv broadcasting)` playlist import). Not every Kdenlive user may have noticed the improved functionality, as it affects only library clips where the same image sequence or title is used multiple times.

In particular, if you (re)use the same image sequence clip, title clip, or even color clip multiple times **in the same library clip**, such image sequences and titles  **will only be added once to your project bin**. Before Kdenlive 16.12.0, multiple instances of the same clip in the timeline unfortunately resulted in these clips getting added multiple times to the project bin. To emphasize, this undesired behavior only affected image sequences, titles, and color clips.

When :ref:`expanding a library clip <library-expand_library_clip>`, Kdenlive checks image sequences, titles, and color clips in the timeline for their content, clip name, and original bin folder location. If there is a match, then such a timeline clip will be added only once to your project bin.

.. note::

   A “library clip” is a clip with the “.mlt” suffix, and in particular, a clip that has been added to your personal Kdenlive library. They show up in Kdenlive's library pane.

   Internally, when you select some clips & transitions from the timeline and add them to Kdenlive's library, these clips and transitions are stored in the file system in a “.mlt” file (which is an MLT playlist to be precise), and shown in the library widget as a new library clip.

   Technically, Kdenlive projects are also MLT playlist files. When you add a clip from the library pane to your project this simply adds the underlying MLT playlist file to your project. But in contrast to other clips, such as an MP4 video, you can “expand” library (that is, MLT playlist) clips to get back the individual clips and transitions inside it.



.. rubric:: Notes

.. |kdenlive_org| raw:: html

   <a href="https://kdenlive.org/en/project/library-clips-with-image-sequences-titles-color-clips/" target="_blank">kdenlive.org</a>

**Sources**
  The original text was submitted by user *TheDiveO* to the now defunct kdenlive.org blog. For this documentation it has been lifted from |kdenlive_org|, updated and adapted to match the overall style.