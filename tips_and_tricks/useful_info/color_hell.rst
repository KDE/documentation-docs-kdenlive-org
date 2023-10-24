.. meta::
   :description: Kdenlive Tips & Tricks - Color Hell: ffmpeg Transcoding and Preserving BT.601
   :keywords: KDE, Kdenlive, tips, tricks, tips & tricks, useful information, ffmpeg, transcoding, bt.601, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - TheDiveO
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             
   :license: Creative Commons License SA 4.0


.. |mlt| raw:: html

   <a href="https://www.mltframework.org/" target="_blank">MLT</a>

.. |ffmpeg| raw:: html

   <a href="https://www.ffmpeg.org/" target="_blank">ffmpeg</a>

.. |ffprobe| raw:: html

   <a href="https://www.ffmpeg.org/ffprobe.html" target="_blank">ffprobe</a>

.. |mediainfo| raw:: html

   <a href="https://mediaarea.net/en/MediaInfo" target="_blank">MediaInfo</a>

.. |explicitly_tag| raw:: html

   <a href="https://video.stackexchange.com/questions/16840/ffmpeg-explicitly-tag-h-264-as-bt-601-rather-than-leaving-unspecified" target="_blank">ffmpeg: explicitly tag h.264 as bt.601, rather than leaving unspecified?</a>


.. _color_hell_ffmpeg_transcoding_and_preserving_BT.601:

Color Hell: Ffmpeg Transcoding and Preserving BT.601
====================================================

From time to time, you may get into weird digital video territory quite unexpectedly. For instance, you just want to cut some screen records made on mobile devices, such as tablets or mobile phones, only to find out that something is wrong with the colors.


Run-of-the-Mill Footage
-------------------------

The drama starts with screen recording footage that seems quite innocent and normal at first sight. It may have been recorded on Android 7 devices using a screen recording app (such as «AZ Screen Recording», but not the “Pro” fake). And this footage has two slightly unusual properties:

* a *highly variable frame rate*,
* it is using :abbr:`BT.601 (A standard from 1982 defining how RGB color primaries get turned into the YCbCr channels used by modern codecs)`\ [#f1]_, instead of :abbr:`BT.709 (A standard from 1990 which doies the same at BT.601 but the transfer coefficients are slightly different)`\ [#f2]_ like so much HD footage these days.

Should cause no problems, right? Well…

As it turns out, Kdenlive's media engine |mlt| can exhibit some issues with video footage that has a highly variable frame rate, such as between 0.001 and 100+ :abbr:`fps (frames per second)`. The symptoms are subtle, yet endanger production quality: it seems as if MLT may well pick a future frame which is way off in regions with a low framerate. While this is not an issue for a suitably high framerate, this causes odd results in other places. For instance, user touch interaction shows up even a few seconds before the interaction will appear. This is probably caused by a very low fps during the inactivity period just before the user interaction.

Transcoding to a fixed frame rate surely is one of |ffmpeg|'s easy tasks (this example assumes a constant project frame rate of 25 fps):

.. code-block:: bash 
   
   ffmpeg -i raw.mp4 -r 25 -crf 18 screen-rec.mp4

The constant frame rate cures the issues mentioned above, so the results are as to be expected. Except…


Easy Transcoding: Color Me Bad
------------------------------

.. image:: /images/tips_and_tricks/transcoding_color_change.webp
   :align: left
   :alt: transcoding_color_change.webp
   :width: 350px

Unfortunately, the resulting video now shows shifted colors! It might not be too obvious in the first place, but it can be quite prominent when you work more with your footage. And it gets clearly visible to your audience in case you are going to mix this footage side-by-side with further processed versions of it, such as extracted frames for stills.

A closer inspection either using Kdenlive's built-in clip properties pane or |ffprobe| reveals that the *transcoded file* **lacks the BT.601 color profile indication**. Yet, |ffmpeg| did *not transform the colors* at all during transcoding, and simply dropped the correct color profile information!

.. rst-class:: clear-both

Makeshift Measures
------------------

.. figure:: /images/tips_and_tricks/kdenlive2308_clip_properties_color_space.webp
   :align: left
   :alt: kdenlive2308_clip_properties_color_space.webp
   :width: 350px

   Clip Properties color space override

Of course, there is always Kdenlive's ability to overwrite source clip properties using the built-in clip properties :term:`widget`.

Simply select the transcoded video clip in the project bin. Then go to clip properties and select its “Force Properties” tab |document-edit|. Check :guilabel:`Colorspace` and then select **ITU-R 601**. Kdenlive now applies the correct color profile.

.. rst-class:: clear-both

While very easy, this method has its limitations: It is fine while you keep working solely inside the Kdenlive editor and its MLT renderer. But as soon as you need to pull in external video tools, such as |ffmpeg| for image extraction you will loose because these tools do not know about Kdenlive's source clip property overrides. We thus need to get the correct color profile information right into the transcoded video files themselves.

Preserving BT.601 in Transcoding
--------------------------------

To make this matter worse, the seemingly obvious color profile transformation 

.. code:: bash 
   
   -vf colormatrix=bt601:bt601
   
simply does not work: |ffmpeg| complains about not being able to transform between the same input and output color profile.

The missing puzzle piece can be found on Stack Exchange's Video Production Q&A site in a post from 2015 asking "|explicitly_tag|".

There is a catch to watch out for: BT.601 comes in :abbr:`PAL (Phase Alternating Line - a colour encoding system for analogue television)` and :abbr:`NTSC (National Television Standard Committee - defined the TV system used in the United States, Japan and many other countries)` flavors which feature slightly different primary chromaticities, transfer curves, and colorspaces. So check your raw footage first using |ffprobe| (or |mediainfo|) which one has been used during recording in your case. Please note that it does not matter that your screen recording has not standard definition (SD) resolution at all, but it does matter when it comes to encoding color.

PAL and NTSC DNA
----------------

So how do we find out if a given video recording file, say ``raw.mp4``, uses the PAL or NTSC color space? Of course, |ffprobe| comes to our rescue. But in order to not get lost in all the nitty-gritty details |ffprobe| will throw at you, we need to tame it using a few options and :abbr:`grep (A Unix command-line utility for searching plain-text data sets for lines that match a regular expression)`:

.. code:: bash
   
   ffprobe -v error -show_streams raw.mp4 | grep color_

This should give you something along these lines:

.. code:: cfg
   
   color_range=tv
   color_space=bt470bg
   color_transfer=smpte170m
   color_primaries=bt470bg

The line ``color_space=...`` tells us whether we re dealing with PAL (bt470bg) or NTSC (smpte170m).

PAL
~~~

If it is **PAL chromaticities** (``color_space=bt470bg``), we then need to transcode as follows:

.. code:: bash

   ffmpeg -i raw.mp4
   -color_primaries bt470bg -color_trc gamma28 -colorspace bt470bg
   -r 25 -crf 18 screen-rec.mp4

NTSC
~~~~

For **NTSC chromaticities** (``color_space=smpte170m``), we will need a different set of primaries, transfer curve, and colorspace:

.. code:: bash

   ffmpeg -i raw.mp4
   -color_primaries smpte170m -color_trc smpte170m -colorspace smpte170m
   -r 25 -crf 18 screen-rec.mp4

.. figure:: /images/tips_and_tricks/transcoding_comparison.webp
   :align: left
   :alt: transcoding_comparison.webp
   :width: 350px

In any case, Kdenlive/MLT now correctly see the transcoded video using the BT.601 color profile. In addition, other media tools correctly detect the color profile too - unless they are broken in that they do not understand BT.601 at all.



.. rubric:: Notes

.. |bt601| raw:: html

   <a href="https://en.wikipedia.org/wiki/Rec._601" target="_blank">BT.601</a>

.. |bt709| raw:: html

   <a href="https://en.wikipedia.org/wiki/Rec._709" target="_blank">BT.709</a>

.. |kdenlive_org| raw:: html

   <a href="https://kdenlive.org/en/project/color-hell-ffmpeg-transcoding-and-preserving-bt-601/" target="_blank">kdenlive.org</a>

**Sources**
  The original text was submitted by user *TheDiveO* to the now defunct kdenlive.org blog. For this documentation it has been lifted from |kdenlive_org| and adapted to match the overall style.

----

.. [#f1] For more details see the Wikipedia article about |bt601|
.. [#f2] For more details see the Wikipedia article about |bt709|