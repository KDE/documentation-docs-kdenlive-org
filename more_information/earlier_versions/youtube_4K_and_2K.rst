.. meta::
   :description: Kdenlive Tips & Tricks - How to Produce 4K and 2K Videos for YouTube
   :keywords: KDE, Kdenlive, tips and trick, how to, how-to, produce 4k and 2k video, YouTube, editing, timeline, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - marcozambi
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             
   :license: Creative Commons License SA 4.0


..
   Copy/paste from EXCEL sheet direct into the online converter.
   Grid tables online converter: https://www.tablesgenerator.com/text_tables
   On top of the converter click on tab "text"
   On the bottom set "to reStructuredText syntax". Now the table header line is bold.

   Or use the .. list-table:: directive
   

.. |yt_specs| raw:: html

   <a href="https://support.google.com/youtube/answer/1722171" target="_blank">YouTube recommended upload encoding settings</a>


.. _how-to_youtube_4K_and_2K:

.. attention:: This page is not maintained anymore and contains information referring to features or functions from earlier versions of Kdenlive that are deprecated or have been superseded by something else.

How to Produce 4K and 2K Videos for YouTube
===========================================

This guide shows how to

a. Produce a 4K video as adherent as possible to the standards for this format
b. Publish the video on YouTube, that supports resolutions up to both 4K and 2K

Specifications
--------------

YouTube is describing quite accurately all the minimum requirements for uploading your material with the |yt_specs|.

Briefly, for the 4K and 2K cases we have:

.. original table
   +------------+------------+------------+--------------+-----------+------------------+
   | Type       | Video      | Mono Audio | Stereo Audio | 5.1 Audio | Resolution and   |
   |            | Bitrate    | Bitrate    | Bitrate      | Bitrate   | aspect ratio     |
   +============+============+============+==============+===========+==================+
   | 2160p (4k) | 35-45 Mbps | 128 kbps   | 384 kbps     | 512 kbps  | 3840x2160 - 16/9 |
   +------------+------------+------------+--------------+-----------+------------------+
   | 1440p (2k) | 10 Mbps    | 128 kbps   | 384 kbps     | 512 kbps  | 2560x1440 - 16/9 |
   +------------+------------+------------+--------------+-----------+------------------+

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 16 17 15 15 15 24
   :class: table-wrap

   * - Type
     - Video Bitrate
     - Mono Audio Bitrate
     - Stereo Audio Bitrate
     - 5.1. Audio Bitrate
     - Resolution and Aspect Ratio
   * - 2160p (4K)
     - 35-45 Mbps
     - 128 kbps
     - 384 kbps
     - 512 kbps
     - 3840x2160 (16:9)
   * - 1440p (2K)
     - 10 Mbps
     - 128 kbps
     - 384 kbps
     - 512 kbps
     - 2560x1440 (16:9)

.. Since the link to the YT settings contains all of that we do not need to repeat it here.
   Furthermore, in case YT changes them we need to update this section

   Codec settings: recommended bitrates, codecs, and resolutions, and more...

   a. Container: .mp4

      1. No Edit Lists (or you may lose AV sync)
      2. moov atom at the front of the file (Fast Start)
   
   b. Audio codec: AAC-LC

      1. Channels: Stereo or Stereo + 5.1
      2. Sample rate 96khz or 48khz
   
   c. Video codec: H.264

      1. Progressive scan (no interlacing)
      2. High Profile
      3. 2 consecutive B frames
      4. Closed GOP. GOP of half the frame rate.
      5. CABAC
      6. Variable bitrate. No bitrate limit required, though we offer recommended bit rates below for reference
      7. Chroma subsampling: 4:2:0
   
   d. Frame rate

      1. Content should be encoded and uploaded in the same frame rate it was recorded.
      2. Common frame rates include: 24, 25, 30, 48, 50, 60 frames per second (other frame rates are also acceptable).
      3. Interlaced content should be deinterlaced before uploading. For example, 1080i60 content should be deinterlaced to 1080p30, going from 60 interlaced fields per second to 30 progressive frames per second.


.. note:: Newer versions of Kdenlive already have 2K project profiles (:abbr:`QHD (Quad-HD)`) and 4K project profiles for :abbr:`UHD (Ultra High Definition)` and :abbr:`DCI (Digital Cinema Initiative)` with a variety of frame rates. Therefore, the following steps are only needed if your Kdenlive version does not have them (seriously consider an upgrade) or if you want to change certain parameters.


Step 1: Create Custom Project Settings
--------------------------------------

Under :menuselection:`Menu --> File --> Project Settings` create a new custom project settings as follows.

For 4K
   a. Size: 3840x2160
   b. Frame rate: 60/1
   c. Pixel aspect ratio: 1/1
   d. Display aspect ratio: 16/9
   e. Colorspace: ITU-R 709

For 2K
   a. Size: 2560x1440
   b. Frame rate: 60/1
   c. Pixel aspect ratio: 1/1
   d. Display aspect ratio: 16/9
   e. Colorspace: ITU-R 709

Notice that the settings for :guilabel:`Project Folder`, :guilabel:`Video Tracks`, :guilabel:`Audio Tracks` and :guilabel:`Thumbnail` should reflect your personal needs.


|pic1| |pic2|

.. |pic1| image:: /images/earlier_versions/project_setting_4K.png
   :alt: Project setting 4K
   :width: 45%

.. |pic2| image:: /images/earlier_versions/project_setting_2K.png
   :alt: Project setting 2K
   :width: 45%


Step 2: Create Custom Consumer Profile
--------------------------------------

We are going to create a total of four profiles: two for 4K and two for 2K. This is necessary because despite their recommendations YouTube will **not** display videos in 2K nor 4K unless they are rendered at 30fps. Therefore, it is recommended to keep separate profiles for 2K and 4K, one each for 30 and 60fps.

.. note:: The profiles have been created for Ubuntu 14.10 64bit, other distributions may have a different default directory for storing consumer profiles.

Under ``/usr/share/mlt/presets/consumer/avformat/Youtube_Advanced`` (Linux) or ``C:\Program Files\kdenlive\share\mlt\presets\consumer\avformat\`` (Windows) create the following files:

``4K_60fps``

  .. code:: cfg

   description=4K 60fps
   f=mp4
   frame_rate_num=60
   frame_rate_den=1
   width=3840
   height=2160
   progressive=1
   vcodec=libx264
   vb=40M
   g=30
   bf=2
   acodec=aac
   ab=384k
   pix_fmt=yuv420p
   threads=4
   coder=1
   movflags=+faststart
   meta.preset.extension=mp4
   meta.preset.name=4K 60fps


``4K_YouTube``

  .. code:: cfg

   description=4K Youtube
   f=m4
   frame_rate_num=30  <-- Pay attention here (30fps is crucial
   frame_rate_den=1
   width=3840
   height=2160
   progressive=1
   vcodec=libx264
   vb=40M
   g=15 <-- Pay attention here (this has to be half the frame rate)
   bf=2
   acodec=aac
   ab=384k
   pix_fmt=yuv420p
   threads=4
   coder=1
   movflags=+faststart
   meta.preset.extension=mp4
   4meta.preset.name=4K Youtube


``2K_60fps``

  .. code:: cfg

   description=2K 60fps
   f=mp4
   frame_rate_num=60
   frame_rate_den=1
   width=2560
   height=1440
   progressive=1
   vcodec=libx264
   vb=10M
   g=30
   bf=2
   acodec=aac
   ab=384k
   pix_fmt=yuv420p
   threads=4
   coder=1
   movflags=+faststart
   meta.preset.extension=mp4
   meta.preset.name=2K 60fps


``2K_YouTube``

  .. code:: cfg

   description=2K YouTube
   f=mp4
   frame_rate_num=30 <-- Pay attention here (30fps is crucial)
   frame_rate_den=1
   width=2560
   height=1440
   progressive=1
   vcodec=libx264
   vb=10M
   g=15 <-- Pay attention here (this has to be half the frame rate)
   bf=2
   acodec=aac
   ab=384k
   pix_fmt=yuv420p
   threads=4
   coder=1
   movflags=+faststart
   meta.preset.extension=mp4
   meta.preset.name=2K YouTube



Step 3: Create Custom Rendering Profile
---------------------------------------

In the Rendering window create a new profile.

.. image:: /images/earlier_versions/rendering_profile.png
   :alt: rendering-profile
   :width: 45%

In the **Profile** window write the following values:

**For 4K 60fps rendering**

.. list-table::
   :width: 80%
   :widths: 20 40
   :header-rows: 1
   :class: table-wrap

   * - Parameter
     - Value
   * - Destination
     - File rendering
   * - Group
     - MP4
   * - Profile Name
     - 4K 60fps
   * - Extension
     - mp4
   * - Parameters
     - properties=4K_60fps vb=%quality+'k' ab=%audiobitrate+'k'
   * - Video qualities
     - 35000,40000,45000
   * - Default quality
     - 40000
   * - Audio Bitrates
     - 384,256,192,160,128
   * - Default Audio Bitrate
     - 256


**For 4K Youtube standard (30fps) rendering**

.. list-table::
   :width: 80%
   :widths: 20 40
   :header-rows: 1
   :class: table-wrap

   * - Parameter
     - Value
   * - Destination
     - File rendering
   * - Group
     - MP4
   * - Profile Name
     - 4K Youtube
   * - Extension
     - mp4
   * - Parameters
     - properties=4K_YouTube vb=%quality+'k' ab=%audiobitrate+'k'
   * - Video qualities
     - 35000,40000,45000
   * - Default quality
     - 40000
   * - Audio Bitrates
     - 384,256,192,160,128
   * - Default Audio Bitrate
     - 256


**For 2K 60fps rendering**

.. list-table::
   :width: 80%
   :widths: 20 40
   :header-rows: 1
   :class: table-wrap

   * - Parameter
     - Value
   * - Destination
     - File rendering
   * - Group
     - MP4
   * - Profile Name
     - 2K 60fps
   * - Extension
     - mp4
   * - Parameters
     - properties=2K_60fps vb=%quality+'k' ab=%audiobitrate+'k'
   * - Video qualities
     - 10000
   * - Default quality
     - 10000
   * - Audio Bitrates
     - 384,256,192,160,128
   * - Default Audio Bitrate
     - 256


**For 2K Youtube standard (30fps) rendering**

.. list-table::
   :width: 80%
   :widths: 20 40
   :header-rows: 1
   :class: table-wrap

   * - Parameter
     - Value
   * - Destination
     - File rendering
   * - Group
     - MP4
   * - Profile Name
     - 2K YouTube
   * - Extension
     - mp4
   * - Parameters
     - properties=2K_YouTube vb=%quality+'k' ab=%audiobitrate+'k'
   * - Video qualities
     - 10000
   * - Default quality
     - 10000
   * - Audio Bitrates
     - 384,256,192,160,128
   * - Default Audio Bitrate
     - 256

.. image:: /images/earlier_versions/rendering_profile_4K.png
   :alt: rendering profile 4K
   :width: 45%


.. |video| raw:: html

   <a href="http://www.youtube.com/watch?v=sGXXrXoN74E" target="_blank">video</a>

To see the results of using the above project and render profiles watch this |video|.


.. rubric:: Notes

.. |forum| raw:: html

   <a href="https://forum.kde.org/viewtopic.php%3Ff=272&t=124869.html#p329129" target="_blank">KDE Kdenlive forum</a>

**Sources**
  This How-to was written and published in the |forum| on February 8th, 2015 by user *marcozambi*. It was adapted slightly to fit the style of this documentation.
