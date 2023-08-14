.. meta::
   :description: Editing in Kdenlive video editor
   :keywords: KDE, Kdenlive, useful information, howto, produce 4k and 2K video, YouTube, editing, timeline, documentation, user manual, video editor, open source, free, learn, easy


.. metadata-placeholder

   :authors: - marcozambi
             - Eugen Mohr
             
   :license: Creative Commons License SA 4.0

.. moved from https://forum.kde.org/viewtopic.php%3Ff=272&t=124869.html#p329129

..
  Copy/paste from EXCEL sheet direct into the online converter.
  Grid tables online converter: https://www.tablesgenerator.com/text_tables 
  On top of the converter click on tab "text"
  On the bottom set "to reStructuredText syntax". Now the table header line is bold.
   

.. _how_to_produce_4k_and_2K_videos_for_youtube:

How to produce 4k and 2K videos for YouTube
===========================================

(created by marcozambi on Sun Feb 08, 2015 2:30 pm. Moved from user forum)

Hello everybody,

I am a long time Kdenlive user, a fantastic software tool that was my Swiss knife in so many projects that I lost the count. So I think it is time to give something back to the community and share some experiences with fellow video producers out there.
Few days ago I started a quest to understand how to produce a 4K (and 2K) video, with these objectives:

   a. Produce a 4K video as adherent as possible to the standards for this format
   b. Publish the video on YouTube, that supports resolutions up to both 4K and 2K.

I realized that two fundamental tools were missing in Kdenlive:

   a. pre-defined Project Setting for starting the production
   b. pre-defined Rendering profile for exporting the video with the proper settings

I couldn't find any guide available for this to implement in Kdenlive, so I started reading and playing around until I got what I wanted, and this is exactly what I am sharing with you.

Specifications
--------------

YouTube is describing quite accurately all the minimum requirements for uploading your material. These specs are here: -> https://support.google.com/youtube/answer/1722171

Briefly, For the 4K and 2K cases we have:

+------------+------------+------------+--------------+-----------+------------------+
| Type       | Video      | Mono Audio | Stereo Audio | 5.1 Audio | Resolution and   |
+============+============+============+==============+===========+==================+
|            | Bitrate    | Bitrate    | Bitrate      | Bitrate   | aspect ratio     |
+------------+------------+------------+--------------+-----------+------------------+
| 2160p (4k) | 35-45 Mbps | 128 kbps   | 384 kbps     | 512 kbps  | 3840x2160 - 16/9 |
+------------+------------+------------+--------------+-----------+------------------+
| 1440p (2k) | 10 Mbps    | 128 kbps   | 384 kbps     | 512 kbps  | 2560x1440 - 16/9 |
+------------+------------+------------+--------------+-----------+------------------+

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

Step 1) Create custom project settings
--------------------------------------

Under Project -> Project Settings menu, create a new custom project settings as follows.

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

Notice that the Project **Folder**, **Video Tracks**, **Audio Tracks** and **Thumbnail** settings should reflect your personal needs.


|pic1| |pic2|

.. |pic1| image:: /images/project_setting_4K.png
   :alt: Project setting 4K
   :width: 45%

.. |pic2| image:: /images/project_setting_2K.png
   :alt: Project setting 2K
   :width: 45%


Step 2) create custom consumer profile
--------------------------------------

Following the novelties introduced with Kdenlive 9.10, we can now create a custom consumer profile, that will be than used when setting up the Rendering profile, as described later on.

We are going to create a total of 4 profiles: 2 for 4K and 2 for 2K. This is necessary because despite their recommendations YouTube will NOT display videos in 2K nor 4K unless they are rendered at 30fps. Therefore I've choosen to keep separate profiles for 2K and 4K, one each for 30 and 60fps.
Notice also that these profiles has been created for Ubuntu 14.10 64bit, other distributions may have a different default directory for storing consumer profiles.

Under /usr/share/mlt/presets/consumer/avformat/Youtube_Advanced create the following files

**4K_60fps**

+---------------------------+
| description=4K 60fps      |
+---------------------------+
| f=mp4                     |
+---------------------------+
| frame_rate_num=60         |
+---------------------------+
| frame_rate_den=1          |
+---------------------------+
| width=3840                |
+---------------------------+
| height=2160               |
+---------------------------+
| progressive=1             |
+---------------------------+
| vcodec=libx264            |
+---------------------------+
| vb=40M                    |
+---------------------------+
| g=30                      |
+---------------------------+
| bf=2                      |
+---------------------------+
| acodec=aac                |
+---------------------------+
| ab=384k                   |
+---------------------------+
| pix_fmt=yuv420p           |
+---------------------------+
| threads=4                 |
+---------------------------+
| coder=1                   |
+---------------------------+
| movflags=+faststart       |
+---------------------------+
| meta.preset.extension=mp4 |
+---------------------------+
| meta.preset.name=4K 60fps |
+---------------------------+

**4K_YouTube**

+------------------------------------------------------------------+
| description=4K Youtube                                           |
+------------------------------------------------------------------+
| f=mp4                                                            |
+------------------------------------------------------------------+
| frame_rate_num=30  <-- Pay attention here (30fps is crucial      |
+------------------------------------------------------------------+
| frame_rate_den=1                                                 |
+------------------------------------------------------------------+
| width=3840                                                       |
+------------------------------------------------------------------+
| height=2160                                                      |
+------------------------------------------------------------------+
| progressive=1                                                    |
+------------------------------------------------------------------+
| vcodec=libx264                                                   |
+------------------------------------------------------------------+
| vb=40M                                                           |
+------------------------------------------------------------------+
| g=15 <-- Pay attention here (this has to be half the frame rate) |
+------------------------------------------------------------------+
| bf=2                                                             |
+------------------------------------------------------------------+
| acodec=aac                                                       |
+------------------------------------------------------------------+
| ab=384k                                                          |
+------------------------------------------------------------------+
| pix_fmt=yuv420p                                                  |
+------------------------------------------------------------------+
| threads=4                                                        |
+------------------------------------------------------------------+
| coder=1                                                          |
+------------------------------------------------------------------+
| movflags=+faststart                                              |
+------------------------------------------------------------------+
| meta.preset.extension=mp4                                        |
+------------------------------------------------------------------+
| meta.preset.name=4K Youtube                                      |
+------------------------------------------------------------------+

**2K_60fps**

+---------------------------+
| description=2K 60fps      |
+---------------------------+
| f=mp4                     |
+---------------------------+
| frame_rate_num=60         |
+---------------------------+
| frame_rate_den=1          |
+---------------------------+
| width=2560                |
+---------------------------+
| height=1440               |
+---------------------------+
| progressive=1             |
+---------------------------+
| vcodec=libx264            |
+---------------------------+
| vb=10M                    |
+---------------------------+
| g=30                      |
+---------------------------+
| bf=2                      |
+---------------------------+
| acodec=aac                |
+---------------------------+
| ab=384k                   |
+---------------------------+
| pix_fmt=yuv420p           |
+---------------------------+
| threads=4                 |
+---------------------------+
| coder=1                   |
+---------------------------+
| movflags=+faststart       |
+---------------------------+
| meta.preset.extension=mp4 |
+---------------------------+
| meta.preset.name=2K 60fps |
+---------------------------+

**2K_YouTube**

+------------------------------------------------------------------+
| description=2K YouTube                                           |
+------------------------------------------------------------------+
| f=mp4                                                            |
+------------------------------------------------------------------+
| frame_rate_num=30 <-- Pay attention here (30fps is crucial)      |
+------------------------------------------------------------------+
| frame_rate_den=1                                                 |
+------------------------------------------------------------------+
| width=2560                                                       |
+------------------------------------------------------------------+
| height=1440                                                      |
+------------------------------------------------------------------+
| progressive=1                                                    |
+------------------------------------------------------------------+
| vcodec=libx264                                                   |
+------------------------------------------------------------------+
| vb=10M                                                           |
+------------------------------------------------------------------+
| g=15 <-- Pay attention here (this has to be half the frame rate) |
+------------------------------------------------------------------+
| bf=2                                                             |
+------------------------------------------------------------------+
| acodec=aac                                                       |
+------------------------------------------------------------------+
| ab=384k                                                          |
+------------------------------------------------------------------+
| pix_fmt=yuv420p                                                  |
+------------------------------------------------------------------+
| threads=4                                                        |
+------------------------------------------------------------------+
| coder=1                                                          |
+------------------------------------------------------------------+
| movflags=+faststart                                              |
+------------------------------------------------------------------+
| meta.preset.extension=mp4                                        |
+------------------------------------------------------------------+
| meta.preset.name=2K YouTube                                      |
+------------------------------------------------------------------+


Step 3) create custom renderer profile
--------------------------------------

In the Rendering window create a new Profile.

.. image:: /images/rendering_profile.png
   :alt: rendering-profile
   :width: 45%

In the **Profile** window write the following values:

**For 4K 60fps rendering**

   1. Destination: File rendering
   2. Group: MP4
   3. Profile Name: 4K 60fps
   4. Extension: mp4
   5. Parameters: properties=4K_60fps vb=%quality+'k' ab=%audiobitrate+'k' <-- (Notice: in properties=<consumer_profile_name> goes the filename of one of the consumer profile files created at step 2)
   6. Video qualities: 35000,40000,45000
   7. Default quality: 40000
   8. Audio Bitrates: 384,256,192,160,128
   9. Default Audio Bitrate: 256


**For 4K Youtube standard (30fps) rendering**

   1. Destination: File rendering
   2. Group: MP4
   3. Profile Name: 4K Youtube
   4. Extension: mp4
   5. Parameters: properties=4K_YouTube vb=%quality+'k' ab=%audiobitrate+'k' <-- (Notice: in properties=<consumer_profile_name> goes the filename of one of the consumer profile files created at step 2)
   6. Video qualities: 35000,40000,45000
   7. Default quality: 40000
   8. Audio Bitrates: 384,256,192,160,128
   9. Default Audio Bitrate: 256


**For 2K 60fps rendering**

   1. Destination: File rendering
   2. Group: MP4
   3. Profile Name: 2K 60fps
   4. Extension: mp4
   5. Parameters: properties=2K_60fps vb=%quality+'k' ab=%audiobitrate+'k' <-- (Notice: in properties=<consumer_profile_name> goes the filename of one of the consumer profile files created at step 2)
   6. Video qualities: 10000
   7. Default quality: 10000
   8. Audio Bitrates: 384,256,192,160,128
   9. Default Audio Bitrate: 256


**For 2K Youtube standard (30fps) rendering**

   1. Destination: File rendering
   2. Group: MP4
   3. Profile Name: 2K YouTube
   4. Extension: mp4
   5. Parameters: properties=2K_YouTube vb=%quality+'k' ab=%audiobitrate+'k' <-- (Notice: in properties=<consumer_profile_name> goes the filename of one of the consumer profile files created at step 2)
   6. Video qualities: 10000
   7. Default quality: 10000
   8. Audio Bitrates: 384,256,192,160,128
   9. Default Audio Bitrate: 256

.. image:: /images/rendering_profile_4K.png
   :alt: rendering profile 4K
   :width: 45%

Final notes
-----------

You can now start to create your productions, unleashing the pixel greedy beast.
This guide wants to be a living document: please let me know in whether you find any inconsistency or error, and whether any step need clarification or betterment.
Thank you all!

P.S. The video I created is here: http://www.youtube.com/watch?v=sGXXrXoN74E
