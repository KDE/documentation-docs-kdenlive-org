.. meta::
   :description: Kdenlive Tips & Tricks - Waveform and RGB Parade
   :keywords: KDE, Kdenlive, tips, tricks, tips & tricks, scopes, waveform, RGB parade, editing, timeline, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Simon "Granjow" Eugster <simon.eu@gmail.com>
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |afterimages| raw:: html

   <a href="https://en.wikipedia.org/wiki/Afterimage" target="_blank">Afterimages</a>

.. |digikam| raw:: html
   
   <a href="https://www.digikam.org/" target="_blank">digikam</a>
   
.. |rawtherapee| raw:: html
   
   <a href="http://www.rawtherapee.com/" target="_blank">RawTherapee</a>

.. |high_key| raw:: html

   <a href="https://www.diyphotography.net/lighting-high-key-and-low-key/" target="_blank">High-Key</a>


.. _scopes-waveform_and_rgb_parade:

Waveform and RGB Parade 
=======================

**Waveform** and **RGB Parade** are two closely related scopes. They do the same - Waveform for :term:`Luma`, RGB Parade for the :abbr:`RGB (Red Green Blue)` components. Therefore, we will not always explicitly point out what properties hold for both scopes and speak of Waveform only.

.. .. image:: /images/kdenlive-colorscopes-waveform.png

.. figure:: /images/tips_and_tricks/kdenlive2308_waveform_rgb_parade_01.webp
   :width: 650px

   Kdenlive Waveform :term:`widget`


How the Waveform Works
----------------------

The Waveform is kind of a 3D Histogram. That has nothing to do with the fact that the above image looks kind of 3D. So where are the three dimensions?

1. The most obvious dimension is :term:`Luma`: Dark pixels are at the bottom, bright ones are at the top. So if all pixels in the Waveform stick at the very top, your video is most likely white.

2. The second dimension is the horizontal position of the pixel in the original image. That is one of the things that makes the Waveform cool. Pixels in the first column of your input video will also be painted in the first column of the Waveform. This goes on until the scope reaches the last column of the input video, which will be painted in the last column of the Waveform.

3. The third dimension is the brightness of a pixel in the Waveform. The brighter a point there, the more pixels in this column share this specific brightness value.

Waveform Example 1: Sunset
--------------------------

.. .. image:: /images/kdenlive-colorscopes-waveform-sunset.png

.. figure:: /images/tips_and_tricks/kdenlive2308_waveform_rgb_parade_02.webp
   :width: 650px

   Waveform example 1

The Waveform looks quite impressive here. But what can we learn about the image?

- In the left third we have got some clipping. There are some bright spots which are the sun and the clouds.

- The last third of the image is dark, but not black (no crushing). This means that there is still a chance for color information. The image confirms that: The tree does not look neutral but green with an orange touch. Or is it the other way round?

That is where the RGB Parade drops in now.

.. .. image:: /images/kdenlive-colorscopes-rgbparade-sunset.png

.. figure:: /images/tips_and_tricks/kdenlive2308_waveform_rgb_parade_03.webp
   :width: 650px

   Kdenlive RGB Parade :term:`widget`

What we see is very slight crushing for blue on the tree, and more or less equal parts of red and green as well. So if you thought the tree were green, your brain fooled you. It is not. (Actually there is no green at all in the image.) Also, blue nearly does not clip at all, even in the sun. So it is still a little bit orange, which is great.

Now, did the Histogram not show clipping and crushing as well? Yes, it did. But it did not show where. That is a big benefit. As in some cases, if you see that there is some clipping on a light bulb, you perhaps do not mind increasing the overall brightness of the image. It does increase clipping as seen on the Histogram, but the Waveform shows that only the light bulb is clipped a little more, which you can afford in our imaginary case.

RGB Parade Example: Light Bulb
------------------------------

Wait … imaginary? Actually there is a short clip with light bulbs. Which is quite interesting, not only due to the wrong white balance. See the how-to guide :doc:`/tips_and_tricks/how-tos/tutorial-white_balance_lms` for more details about white balance and how to use it in Kdenlive.

.. .. image:: /images/kdenlive-colorscopes-rgbparade-fluorescent.png

.. figure:: /images/tips_and_tricks/kdenlive2308_waveform_rgb_parade_04.webp
   :width: 650px

   RGB Parade example 1

The RGB Parade reveals two things at first glance. You will at least recognize the first one as well.

- The fluorescent lamps are clipped. All channels are at 255 there, so they are totally white.

- The white balance is wrong. This can be told for sure. The ceiling is white in reality. And the left-most quarter of the image consists exclusively of the ceiling. This part should look equal in the RGB Parade, but when e.g. comparing Red to Blue, you see that Red starts at 19 whereas Blue starts at 0. Furthermore, the Blue channel is much more compressed. Its height in this area is 25, whereas the height of the Red channel is about 50.

To achieve proper white balance here we make use of a new effect called :doc:`/effects_and_filters/video_effects/color_image_correction/sat`. :doc:`/effects_and_filters/video_effects/color_image_correction/curves` would work as well (actually curves could do everything), but let's use a new effect here.

The first thing to decide is how bright the darkest spot should be. This can be controlled with the :guilabel:`Offset` parameter. Reference is again the left part of the Parades, the soon-to-be white ceiling. You can use your mouse to make the Waveform or RGB Parade draw a horizontal line and display the value there. All channels were lifted to around 50 in this example:

.. note::
   The :doc:`/effects_and_filters/video_effects/color_image_correction/sat` uses a different scale than the RGP Parade :term:`widget`. The lifting of the channels refers to the RGB Parade scale (0...255) as one can see in the :guilabel:`Min` in the RGB Parade display. The idea is to lift the channels so that their bottoms are aligned.

.. .. image:: /images/kdenlive-colorscopes-rgbparade-fluorescent-offset.png

.. figure:: /images/tips_and_tricks/kdenlive2308_waveform_rgb_parade_05.webp
   :width: 650px

   Using the :doc:`/effects_and_filters/video_effects/color_image_correction/sat` to change the color tone

Second step is stretching the channels. This is done with the :guilabel:`Slope` sliders. The goal is again to find a neutral spot in the RGB Parade and use it as reference. We could again use the ceiling on the left, but after some testing it turned out that the little wave in the middle of the scope works as well. Its advantage is that it is slightly brighter than the ceiling allowing to correct the color cast more precisely.

.. .. image:: /images/kdenlive-colorscopes-rgbparade-fluorescent-slope.png

.. figure:: /images/tips_and_tricks/kdenlive2308_waveform_rgb_parade_06.webp
   :width: 650px

   Using the :doc:`/effects_and_filters/video_effects/color_image_correction/sat` to adjust white balance

And voilà, exposure and white balance are corrected.

When taking a look at the full-sized image (or when trying it yourself with the sample clip available for download at the end of this article) you will notice color waves in the image. This is the result of the stretching: We have blown up the ceiling on the left from 25px height to nearly 100px. If the clip had been exposured and white-balanced correctly when shooting, we would have 100 distinct values there, but now there are only 25 different blue levels causing these steps. Also in the histogram the image looks torn apart. (Another reason might be the high compression of the Nikon D90 clips.) This effect is called *Posterization*\ [#f1]_.

This is one of the reasons why more expensive cameras (and with that we mean *really* expensive ones, like the *RED One*\ [#f2]_, to name an extreme example) record videos in higher bit depth\ [#f3]_. Perhaps all clips you will ever encounter only store 8 bits per channel, so there are 2\ :sup:`8` = 256 possible values for each channel. Having for example 10 bits per channel would already result in 2\ :sup:`10` = 1024 possible values. This would already have solved our problem.

But before you buy a *RED One* now - Kdenlive does not support more than 8 bit (yet).

Where you already can play with more than 8 bits per channel are :abbr:`RAW (The RAW file format is digital photography's equivalent of a negative in film photography: it contains untouched, raw pixel information straight from the digital camera's sensor)` images from :abbr:`DSLR (DSLR stands for Digital Single-Lens Reflex)` cameras. Supported by many image processing applications such as |digikam| or |rawtherapee|.

Waveform Example 2: Leaf with Hidden Clipping
---------------------------------------------

.. .. image:: /images/kdenlive-colorscopes-waveform-leaf.png

.. figure:: /images/tips_and_tricks/kdenlive2308_waveform_rgb_parade_07.webp
   :width: 650px

   Waveform example 2

Looks perfect. Good exposure (says the eye and the Waveform), beautiful colors.

Nevertheless, there is some clipping. It is just hidden by the Luma calculation: For Luma, only pixels that are totally white are at the top of the Waveform.

.. .. image:: /images/kdenlive-colorscopes-rgbparade-leaf.png

.. figure:: /images/tips_and_tricks/kdenlive2308_waveform_rgb_parade_08.webp
   :width: 650px

   RGB Parade exposes clipping

Although the green leaf looks much brighter than the red tip, it is the Red channel which clips at the tips. The thing is that our eyes are most sensitive to Green, less to Red, and even less to Blue. That is also the reason why the beam of a green laser is visible in the night sky, but a red one is not - unless you've got a really strong one.

Waveform Example 3: High Key Clip
---------------------------------

.. .. image:: /images/kdenlive-colorscopes-waveform-highkey.png

.. figure:: /images/tips_and_tricks/kdenlive2308_waveform_rgb_parade_09.webp
   :width: 650px

   Waveform example 3

This is a classical |high_key| shot. Bright subject (but not clipped yet), white background.

Waveform Options
----------------

- *Paint Mode* - Changes the paint mode for the Waveform. Usually changes its brightness as well. Green also highlights pixels with values 0 or 255.

- *Luma mode* (Context menu) - As for the Histogram you can choose how to calculate Luma (Rec.601 or Rec.709).

.. .. image:: /images/kdenlive-colorscopes-waveform-green.png

.. figure:: /images/tips_and_tricks/kdenlive2308_waveform_rgb_parade_10.webp
   :width: 650px

   Waveform :term:`widget` with paint mode Green

Interesting detail: When color grading, some colorists prefer scopes with neutral colors and basically with neutral everything. Just greyscale except for the video itself. Why is that? Quick answer and fun fact: |afterimages|. If you look at a green surface and then immediately color grade an image by eye, there will be too much green in it.

RGB Parade Options
------------------

- *Paint Mode* - Changes the paint mode; see above.

- *Draw Axis* (Context menu) - Draws an axis with 10 steps

- *Gradient reference line* (Context menu) - Draws a line from bottom left to top right. This is useful when testing color correction on a linear gradient clip (Black on the left, White on the right), to observe changes in each channels.

To explain the last point a little more in detail: A black/white gradient draws a line from the bottom left to top right on the Waveform. When changing the colors, e.g. with the :doc:`/effects_and_filters/video_effects/color_image_correction/sat` effect or with :doc:`/effects_and_filters/video_effects/color_image_correction/curves`, the line will change.

.. attention::
   Effects working on the saturation will not have any effect on a grayscale gradient!

.. .. image:: /images/kdenlive-colorscopes-waveform-gradient.png

.. figure:: /images/tips_and_tricks/kdenlive2308_waveform_rgb_parade_11.webp
   :width: 650px

   Playing with the :doc:`/effects_and_filters/video_effects/color_image_correction/sat` and a gradient

In this gradient above a :doc:`/effects_and_filters/video_effects/color_image_correction/sat` effect was applied to give the blacks a blueish touch and the mids and highs a warm touch. You can play around with the gradient file and some color correction effects on the gradient file as well. What the above is good for will be in the next part.


.. rubric:: Summary

**Waveform** and **RGB Parade** are powerful scopes. Especially the RGB Parade. Correcting the exposure is easy, and with these scopes you can always keep track of the levels of each color component. It is also possible to do white balance by adjusting blacks first and whites afterwards because the horizontal axis in the Scopes correspond to the horizontal axis in the video which allows to detect spots that should be neutral.



.. rubric:: Notes

.. |cambridge_in_colour| raw:: html

   <a href="https://cambridgeincolour.com" target="_blank">Cambridge in Colour</a>

.. |posterization| raw:: html

   <a href="https://www.cambridgeincolour.com/tutorials/posterization.htm" target="_blank">posterization</a>

.. |bit_depth| raw:: html

   <a href="https://www.cambridgeincolour.com/tutorials/bit-depth.htm" target="_blank">bit-depth</a>

.. |red| raw:: html

   <a href="https://en.wikipedia.org/wiki/Red_Digital_Cinema" target="_blank">Red Digital Cinema</a>

.. |web_archive| raw:: html

   <a href="https://web.archive.org/web/20160319050009/http://kdenlive.org/users/granjow/introducing-color-scopes-waveform-and-rgb-parade" target="_blank">web.archive.org</a>

**Sources**
  - :download:`windy-sunset.avi <http://granjow.net/uploads/kdenlive/samples/windy-sunset.avi>` (22 MB; 720/24p)
  - :download:`fluorescent-wrong-whitebalance.avi <http://granjow.net/uploads/kdenlive/samples/fluorescent-wrong-whitebalance.avi>` (22 MB; 720/24p)
  - :download:`red-leaf-tips.avi <http://granjow.net/uploads/kdenlive/samples/red-leaf-tips.avi>` (13.5 MB; 720/24p)
  - :download:`highkey.avi <http://granjow.net/uploads/kdenlive/samples/highkey.avi>` (13 MB; 720/24p)
  - :download:`Gradient_1080.png <http://granjow.net/uploads/kdenlive/samples/Gradient_1080.png>` (10 kB, 1920x1080)

  .. note:: Depending on your browser settings you may get an error that the file download is insecure.
  
  The original text was submitted by *Simon A. Eugster (Granjow)* on Tue, 09/14/2010 - 15:01 to the now defunct kdenlive.org blog. For this documentation it has been lifted from |web_archive| and adapted to match the overall style.

----

.. [#f1] See this tutorial about |posterization| from |cambridge_in_colour|
.. [#f2] For more details see the Wikipedia page about |red|
.. [#f3] See this tutorial about |bit_depth| from |cambridge_in_colour|