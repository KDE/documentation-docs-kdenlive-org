.. meta::
   :description: Kdenlive Tips & Tricks - Shooting with Your DSLR
   :keywords: KDE, Kdenlive, tips, tricks, tips & tricks, shooting tips, shooting, DSLR, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Simon "Granjow" Eugster <simon.eu@gmail.com>
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. attention:: This article was published on November 14\ :sup:`th`\ , 2010. A lot has changed since then in the digital camera field. Nevertheless, the fundamental statements about digital photography are still valid.
   

Shooting With Your DSLR
=======================

This article is going to give some tips regarding shooting video with your :abbr:`DSLR (Digital Single Lens Reflex)` and editing it in Kdenlive afterwards.

Camera Hardware
---------------

Lens
~~~~

|pic1|  |pic2|

.. |pic1| image:: /images/tips_and_tricks/shooting_nikon_50mm.webp
   :width: 30%

.. |pic2| image:: /images/tips_and_tricks/shooting_nikon_35mm.webp
   :width: 30%


Generally Primes are preferred over zooms in video. (Some people, prefer it over zooms as well for photography — but this is a matter of taste and of how you work.) Why is that? A psychological reason is that eyes cannot zoom either, so zooming is hardly ever used in video. The technical reason is that Primes are cheaper to build whilst offering better quality: Better sharpness, bigger aperture (for limiting the :abbr:`DOF (Depth of Field)`). Opening the aperture gives you a very nice look.
    
Examples for very popular primes are the Nikon 50mm f/1.8D and the Canon 50mm f/1.8 II.
    
If you own such a lens, just do not forget that you should not always shoot at f/1.8. ;)

Filter
~~~~~~

.. figure:: /images/tips_and_tricks/shooting_nd-filter.webp
   :align: right
   :width: 200px
   :figwidth: 200px

   :abbr:`NDF (Neutral Density Filter)` (the piece of kneaded eraser is not part of the filter)

Directly related to the previous point about lenses. Shooting with an open aperture works well as long as it is dark. In bright sunlight it will fail because there is too much light falling on the sensor. Furthermore you are forced to use a high shutter speed which makes movements look jerky; Most of the time you will want to have some kind of motion blur because it looks more natural to our eyes.
    
If you ever tried to follow a bird or another animal with your eyes in dawn, you will know that our eyes do support motion blur.
    
So the trick is to remove some light with a filter called Neutral Density Filter.


Shooting
--------

Aperture, Shutter, and ISO
~~~~~~~~~~~~~~~~~~~~~~~~~~

|pic3|  |pic4|

.. |pic3| image:: /images/tips_and_tricks/shooting_motion-low.webp
   :width: 30%

.. |pic4| image:: /images/tips_and_tricks/shooting_motion-high.webp
   :width: 30%

The same as for shooting stills. Really? Not quite. As written above you will usually want to have the shutter speed lower than for photography in order to get motion blur — around 1/50 s. (This is just a rule of thumb, as all rules in video are - made to be broken.)
    
Also, some additional problems may arise due to the sensor being read out line-wise. One I would like to mention are Rolling Shutter effects. Longer exposure can, but need not, prevent such problems. It does if you are shooting with fluorescent lamps. Shooting at high shutter speed shows wave patterns from top to bottom of the screen, lowering it hides them if you hit the correct shutter speed.
    
On the right: Two images shot with the Nikon D90 of the author, the left one at lowest ISO possible, the right one at highest possible.

Exposure
~~~~~~~~

|pic5|  |pic6|

.. |pic5| image:: /images/tips_and_tricks/shooting_low-ISO.webp
   :width: 30%

.. |pic6| image:: /images/tips_and_tricks/shooting_high-ISO.webp
   :width: 30%

The image should be exposed as bright as possible (without too much clipping!) if enough light is available. If you do not need to boost the brightness too much in post-production, you can avoid some noise in dark areas. 

White Balance
~~~~~~~~~~~~~

|pic7|  |pic8|

.. |pic7| image:: /images/tips_and_tricks/shooting_whitebalance-post.webp
   :width: 30%

.. |pic8| image:: /images/tips_and_tricks/shooting_whitebalance-pre.webp
   :width: 30%

The White Balance should be set as accurate as possible because DSLRs only support 8 bit per color channel (see also the chapter about the :doc:`Waveform Monitor </tips_and_tricks/scopes/waveform_and_rgb_parade>`). If done wrong, much of the color information is lost.
    
DSLRs also offer different camera profiles with different contrast, saturation and other settings. Usually low saturation is preferred over high saturation — especially because raising the saturation can be done in post, and because high in-camera saturation settings can lead to color clipping.
    
In the example images on the right you can see the difference. The left one looked blueish due to wrong white balance and was corrected in post; much of the tonal range of the blue colors has been lost. The right one has been shot with proper white balance.

Autofocus
~~~~~~~~~

The in-camera autofocus may be fast enough to focus, but it will fail in the most important moment. It is useful for getting the initial focus point, but while shooting it should stay switched off.


Camera Specific Tips
--------------------

Nikon D90
~~~~~~~~~

.. |nikon-d90| raw:: html
   
   <a href="https://web.archive.org/web/20160403024219/https://kdenlive.org/video-editor/nikon-d90" target="_blank">Nikon D90 page</a>

.. |movie_mode| raw:: html

   <a href="https://web.archive.org/web/20160208161124/http://www.dvxuser.com/V6/showthread.php?146661-Understanding-and-Optimizing-the-Nikon-D90-D-Movie-Mode-Image" target="_blank">Understanding and Optimizing the Nikon D90 D-Movie Mode Image</a>

The Nikon D90 was the first DSLR offering video: 720/24p (:abbr:`AVI (Audio Video Interleave)` container).

D90 videos at 720p are scaled awfully. That is why you can see stair-stepping in sharp, skew lines. If this becomes perturbing for a clip, you can apply the :doc:`/effects_and_filters/video_effects/utility/nikon_d90_stairstepping_fix` filter. Written (but not invented) by the original author *Granjow*. See our |nikon-d90| for an example of how stairstepping looks like (before and after correction).

There is an extensive overview over the D90 video function at dvxuser.com: |movie_mode|.


Canon EOS 550D/Ti2 (and Co.)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These cameras shoot 1080p (H.264 encoded, MOV container) — but record video with a height of 1088 pixels. Prior to MLT 0.5.6 you have/had to crop the additional 8 pixels with a crop effect from the top or the bottom of the video, newer versions of MLT do this automatically.


DSLR Related Links
------------------

.. |basics| raw:: html

   <a href="https://www.radford.edu/content/dam/departments/administrative/CITL/DSLR_VIDEO_TIPS.pdf" target="_blank">DSLR HD Video Tips: Shooting Basics</a>

.. |philip_bloom| raw:: html

   <a href="https://philipbloom.net/blog/shooting-video-with-a-dslr/" target="_blank">Philip Bloom Gives Photographers A Basic Video Shooting Tip</a>

.. |seven_tips| raw:: html

   <a href="https://www.sportsshooter.com/news/2376" target="_blank">7 Tips To Get Better Video from a DSLR Camera</a>

.. |hurlbut| raw:: html

   <a href="https://vimeo.com/groups/28231/videos/15635719" target="_blank">Hurlbut Visuals Camera Protocol</a>

.. |david_h_stewart| raw:: html

   <a href="https://www.popphoto.com/how-to/2010/07/pro-dslr-video-tips-david-harry-stewart/" target="_blank">Pro DSLR Video Tips from David Harry Stewar</a>

.. |dslr_guide_1| raw:: html

   <a href="https://webcache.googleusercontent.com/search?q=cache:3CJdJI0nNW4J:https://gadgetwise.blogs.nytimes.com/2010/04/15/tips-on-shooting-video-with-a-d-s-l-r/+&cd=1&hl=de&ct=clnk&gl=ch" target="_blank">Tips on Shooting Video With a D.S.L.R</a>

.. |dslr_guide_2| raw:: html

   <a href="https://tubularinsights.com/hd-video-dslr-camera/" target="_blank">How To Guide For Shooting HD Video With A DSLR Camera</a>


One can find tons of information about shooting in the internet. Some helpful links listed below.

- |basics| — Introduction to DSLR video shooting

- |philip_bloom| — How to get from photo to video

- |seven_tips| — Tips on shooting (not tech only)

- |hurlbut| — Professional shooting workflow

- |david_h_stewart| — Interview containing several tips

- |dslr_guide_1| — Various tips

- |dslr_guide_2| — Various tips



.. rubric:: Notes

.. |webarchive| raw:: html

   <a href="https://web.archive.org/web/20160319101730/https://kdenlive.org/users/granjow/shooting-your-dslr" target="_blank">kdenlive.org</a>

**Sources**
  The original text was submitted by user *Granjow* to the now defunct kdenlive.org blog. For this documentation it has been lifted from kdenlive.org via |webarchive|, updated and adapted to match the overall style.