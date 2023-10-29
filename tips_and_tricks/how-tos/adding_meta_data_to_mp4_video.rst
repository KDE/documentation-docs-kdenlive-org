.. meta::
   :description: Kdenlive Tips & Tricks - How to Add Meta Data to MP4 Video
   :keywords: KDE, Kdenlive, tips, tricks, tips & tricks, adding meta data, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - TheDiveO
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             
   :license: Creative Commons License SA 4.0


.. |ffmpeg| raw:: html

   <a href="https://ffmpeg.org" target="_blank">ffmpeg</a>

.. |ffmpeg_metadata| raw:: html

  <a href="https://ffmpeg.org/doxygen/trunk/group__metadata__api.html" target="_blank">meta data</a>

.. |matroska| raw:: html

  <a href="https://en.wikipedia.org/wiki/Matroska" target="_blank">Matroska</a>

.. |audio_video_interleave| raw:: html

  <a href="https://en.wikipedia.org/wiki/Audio_Video_Interleave" target="_blank">Audio Video Interleave</a>


Adding Meta Data to MP4 Video
=============================

Adding a useful information to your video files - such as title, authors, the date of production, and some description - can be quite helpful to both yourself and your customers. This additional data - or *meta data* - can be used by media players to organize your many video files.

Project Meta Data
-----------------

.. figure:: /images/tips_and_tricks/kdenlive2308_meta_data.webp
   :align: left
   :alt: kdenlive2308_meta_data.webp
   :width: 350px

   Adding a new meta data field

Kdenlive allows you to specify the meta information that should be added to a rendered file. Just go to :menuselection:`Menu --> Project --> Project Settings`, then select the second tab named :guilabel:`Metadata`.

Double-click any existing meta data entry to change it.

Click on |list-add| to add a new meta data entry (see the list of possible and permissable tags below).

.. rst-class:: clear-both

For your convenience, Kdenlive automatically adds the following four elements to each new project:

- **Title**
- **Author** - does not work for .mp4 containers, but for .mov containers; you may use **artist** instead with .mp4 containers.
- **Copyright**
- **Year** - please note that this element does not work for video rendered into MP4 containers (such as .mov and .mp4). See below for more details. Use a date element instead. This *year* element is actually quite pesky: you can delete it, but it will automatically reappear. So simply ignore it … as ffmpeg does too.

But there are more elements that you actually may use with your MP4 containers.
 

MP4 Containers
--------------

Unfortunately, there are competing sets of meta data when working with MP4 containers. The older, standard MP4 set is rather limited in what additional meta data can be used. Then, there is Apple iTunes, and that brings in a lot of meta data, and even changes the allowed set from time to time. We will come back to this difference in a second.

.. Unfortunately, information about what meta data can be used in which situation is rather scarce, sometimes outdated, and sometimes plainly wrong. Of course, this may also apply to this Toolbox article, but I’ve taken much effort to cross-check things in real life. As Kdenlive uses `ffmpeg <https://www.ffmpeg.org/>`_ for encoding, one would think that there’s plenty of information - unfortunately, it’s not, and the scarce information is sometimes plainly wrong. At some point, I’ve resorted to reading the source code in order to find out which so-called MP4 atoms actually are supported and through which element names (the magic happens inside `mov_write_ilst_tag()` in `moveenc.c <https://github.com/FFmpeg/FFmpeg/blob/5a8b41b4a76fc6586ff6afff78e5f0aa7b25068a/libavformat/movenc.c#L2996>`__). Luckily, you don’t need to dive into the source anymore.

.. note:: Other container formats, such as |matroska| (``.mkv``) or |audio_video_interleave| (``.avi``), support yet other sets of meta data elements.

Ffmpeg Supported MP4 Container Meta Information
-----------------------------------------------

But now for the real meat: here come the available meta data elements that |ffmpeg| supports.

.. note:: You must use the |ffmpeg| meta data keys from the second column in the table below as the metadata keys in Kdenlive's Project Metadata dialog.

.. note:: |Ffmpeg| supports different |ffmpeg_metadata| elements, based on the type of container. And this container type normally gets derived from the container filename suffix: in particular, ``.mp4`` and ``.mov``.

.. list-table::
  :header-rows: 1
  :width: 100
  :widths: 10 10 50 10 10 10
  :class: table-wrap

  * - Element
    - ffmpeg Meta Data Key
    - Description (data type\ [1]_\ )
    - MOV
    - MP4
    - Tag
  * - Title
    - title
    - The title of this video. (String)
    - ✔
    - ✔
    - ©nam
  * - Year
    - date
    - The date of production. Please note that the ffmpeg documentation is totally wrong here, there is no key named year, but only date. (String)
    - ✔
    - ✔
    - ©day
  * - Copyright
    - copyright
    - The copyright of your video. (String)
    - ✔
    - ✔
    - ©cpy
  * - Artist
    - artist
    - The name of the (video) artist. Please do not use this element for the composer, as there is a dedicated element especially for the composer, see below. (String)
    - ✔
    - ✔
    - ©ART
  * - Album Artist
    - album_artist
    - The name of the album artist: this may be a guest artist or a featured artist. This element can also be left out or be the same name as the artist. (String)
    - 
    - ✔
    - aART
  * - Author
    - author
    - The author of the video. (String)
    - ✔
    - 
    - ©aut
  * - Composer
    - composer
    - The name of the composer. (String)
    - 
    - 
    - ©wrt
  * - Album
    - album
    - The title or the name of this album. (String)
    - ✔
    - 
    - ©alb
  * - Description
    - comment
    - A (content) description of this video. For a synopsis, please see the separate element instead. (String)
    - 
    - ✔
    - desc
  * - Comment
    - comment
    - A (short) comment on your video. This will probably a comment set by the audience, not at the time of production. (String)
    - ✔
    - 
    - ©des
  * - Comment
    - comment
    - Same as before, but encoded in a separate element. (String)
    - ✔
    - ✔
    - ©cmt
  * - Synopsis
    - synopsis
    - A synopsis, a longer description of this video. (String)
    - 
    - ✔
    - ldes
  * - Genre
    - genre
    - The genre this video belongs to. (String)
    - ✔
    - ✔
    - ©gen
  * - Make
    - make
    - (String)
    - ✔
    - 
    - ©mak
  * - Model
    - model
    - (String)
    - ✔
    - 
    - ©mod
  * - Location
    - location
    - (String)
    - ✔
    - 
    - ©xyz
  * - Grouping
    - grouping 
    - The name of a group of videos somehow belonging together. In contrast to the album element, grouping happens inside (that is, below) the album level. (String)
    - 
    - ✔ 
    - ©grp
  * - Show
    - show
    - The name of the TV show, if applicable. (String)
    -
    - ✔
    - tvsh
  * - Episode
    - episode_id
    - Either the episode name or episode number, for display. If necessary, use the separate, yet optional episode number element for correct sorting. (String)
    -
    - ✔
    - tven
  * - Episode (Sorting)
    - episode_sort
    - This element is for sorting only, but never displayed. It allows numerical sorting of episode names that are strings, but not (necessarily) numbers. The valid range is limited to 0 to 255 only, so this doesn’t support all those endless telenovas, it seems… (Int8)
    -
    - ✔
    - tves
  * - Season
    - season_number
    - The season number, in the range of 0 to 255 only. (Int8)
    -
    - ✔
    - tvsn
  * - Lyrics
    - lyrics
    - Optional lyrics for badly sung sing-along… (String)
    -
    - ✔
    - ©lyr
  * - Compilation
    - compilation
    - If 1, then this video file is part of a compilation. 0 otherwise. (Int8)
    -
    - ✔
    - cpil
  * - Network
    - network
    - (String)
    -
    - ✔
    - tvnn
  * - Media Type
    - media_type
    - (Int8)
    -
    - ✔
    - stik
  * - HD Video
    - hd_video
    - (Int8)
    -
    - ✔
    - hdvd
  * - Gapless Playback
    - gapless_playback
    - (Int8)
    -
    - ✔
    - pgap
  * - Encoding Tool
    - encoder
    - Not available to us users, as it gets automatically set by ffmpeg itself; this is set to the libavformat version string. 	
    - ✔
    -
    - ©swr
  * - Encoding Tool
    - encoding_tool
    - Not available to us users, as it gets automatically set by ffmpeg itself; this is set to the libavformat version string. 	
    -
    - ✔
    - ©too



.. rubric:: Notes

.. |atomic_parsley| raw:: html

   <a href="https://sourceforge.net/p/atomicparsley/wiki/Home/" target="_blank">AtomicParsley</a>

.. |moveenc| raw:: html

   <a href="https://github.com/FFmpeg/FFmpeg/blob/5a8b41b4a76fc6586ff6afff78e5f0aa7b25068a/libavformat/movenc.c#L2996" target="_blank">moveenc.c</a>

.. |howto_id3| raw:: html

  <a href="https://jmesb.com/how_to/create_id3_tags_using_ffmpeg" target="_blank">How To: Create/Write ID3 tags using ffmpeg</a>

.. |howto_dump| raw:: html

  <a href="https://jmesb.com/how_to/dump_and_load_metadata_with_ffmpeg" target="_blank">How To: Dump and Load metadata with ffmpeg</a>

.. |ffmpeg_meta_data| raw:: html

  <a href="https://wiki.multimedia.cx/index.php?title=FFmpeg_Metadata" target="_blank">FFmpeg Metadata</a>

.. |kdenlive_org| raw:: html
   
   <a href="https://kdenlive.org/en/project/adding-meta-data-to-mp4-video/" target="_blank">kdenlive.org</a>

.. |multimediawiki| raw:: html

  <a href="https://wiki.multimedia.cx/index.php?title=Main_Page" target="_blank">MultimediaWiki</a>


* There is no way to add cover art or DVD art to MP4 containers through |ffmpeg|, and in consequence, in Kdenlive. Instead, you need to resort to other video container tagging tools, such as |atomic_parsley|.

* Kdenlive leverages ffmpeg for encoding, so if ffmpeg does not support certain atoms there is no way for Kdenlive to get it into the rendered output file.

**Further Reading**
  The following references give some more background information on |ffmpeg| and meta data in .mov/.mp4 containers.

  1. First, and foremost, the ffmpeg source code for reference, and |moveenc| in particular.

     a) ``mov_write_ilst_tag()`` is responsible to write the iTunes-compatible tags for .mp4 containers
     b) ``mov_write_udta_tag()`` write the MPEG-standard tags instead, when using a .mov container

  2. |howto_id3| by Jon Hall. This article finally got the author on the right track. However, beware of a few incorrect ffmpeg keys in Jon's table (such as the TIT3 key, which the author thinks is not correct); these may be due to later changes in ffmpeg (or whatever). In the end, since some of Jon's keys didn't work, the author went for the ffmpeg source code which is the authoritative source, of course. Nevertheless, the author is very thankful to Jon who is some of the rare really good sources with good insight into the topic. Most other source just tell you how to press some buttons on some application, but do not give you any clue as to what is actually going on behind the scenes.
  3. |howto_dump| by Jon Hall. Sheds more light on how to work with meta data when it comes to ffmpeg.
  4. |ffmpeg_meta_data| article from the |multimediawiki|.

**Sources**
  The original text was submitted by user *TheDiveO* to the now defunct kdenlive.org blog. For this documentation it has been lifted from |kdenlive_org|, updated and adapted to match the overall style.

----

.. [1] The data types are (String)=string, (Int8)=integer (8-bit)