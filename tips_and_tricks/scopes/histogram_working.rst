.. meta::
   :description: Kdenlive Tips & Tricks - How the Histogram works
   :keywords: KDE, Kdenlive, tips, tricks, tips & tricks, scopes, histogram, editing, timeline, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Simon "Granjow" Eugster <simon.eu@gmail.com>
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |cambridge_in_colour| raw:: html

   <a href="https://cambridgeincolour.com" target="_blank">Cambridge in Colour</a>

.. |tones_and_contrast| raw:: html
   
   <a href="https://www.cambridgeincolour.com/tutorials/histograms1.htm" target="_blank">Understanding Camera Histograms: Tones and Contrast</a>

.. |luminance_and_color| raw:: html

   <a href="https://www.cambridgeincolour.com/tutorials/histograms2.htm" target="_blank">Camera Histograms: Luminosity & Color</a>

.. |digikam| raw:: html

   <a href="https://www.digikam.org/" target="_blank">digiKam</a>

.. |gimp| raw:: html

   <a href="https://www.gimp.org/" target="_blank" target="_blank">GIMP</a>
   

.. _scopes-histogram_working:

How the Histogram Works
=======================

When the Histogram receives an updated image from one of the monitors, each of these pixels consists of a Red, Green, and Blue component. Each of these values lies within a range of 0 and 255, which are the numbers you can represent with one Byte. 0 means that the component is not shining at all (i.e. it is black), 255 means that it is shining as bright as possible.

The histogram is merely statistics: it shows how often a component of a certain brightness occurs. So what the histogram then does is actually quite simple:

1. Take the first pixel
2. Look at the Red value (= *x*) of the pixel. Increase the height of the bar at position *x* of the histogram by 1. Example: If the red value is 0, increase the height of the bar at position 0 (that is at the very left) of the histogram by 1. If it is 42, increase bar 42 by 1. And so on.
3. Repeat the previous step with Green and Blue.
4. Look at R, G, and B together and calculate the :term:`Luma` value. Luma is the perceived luminance of this pixel. See :ref:`further below <scopes-luma_calc>` how it is calculated.
5. Repeat these steps for all other pixels on the image.

What the Histogram Shows
------------------------

The Histogram only shows the distribution of the luminance of the selected components - nothing more, nothing less. Also when looking at the RGB channels separately instead of at the calculated Luma component only, you cannot really guess the colors in the image. Take a look at these two images:

.. figure:: /images/tips_and_tricks/kdenlive2308_histogram_01.webp
   :width: 650px
   :alt: kdenlive2308_histogram_01.webp

   Histogram for a simple greyscale gradient image

.. figure:: /images/tips_and_tricks/kdenlive2308_histogram_02.webp
   :width: 650px
   :alt: kdenlive2308_histogram_02.webp

   Histogram for a simple color gradient image

Exactly the same Histogram. Totally different colors. (What you can do is guessing the color tone; see below.) But what is the histogram good for now?

To answer this question, it is best to refer you to this article from |cambridge_in_colour|: |tones_and_contrast| and the second part |luminance_and_color|. Although written for digital photo cameras, exactly the same applies for digital video cameras. Both articles are easy to read and understand and may also be of interest for experienced users.

Example 1: Candlelight
----------------------

.. figure:: /images/tips_and_tricks/kdenlive2308_histogram_03.webp
   :width: 650px
   :alt: kdenlive2308_histogram_03.webp

   Histogram example with a candlelight image

Two special things about this histogram.

- Most pixels are dark, according to the Luma component (white). Though there is no total black: Notice that the Luma component shows «min: 8». Nevertheless, the blue component does reach 0. This means that the darkest pixels are still slightly orange and didn't lose all color information yet. 

- There is quite some clipping. A lot of R values are sticking at the very right, at 255. Having a peak at 255 usually means that we lost information because some regions were too bright for the camera sensor with the current sensitivity settings. This could have been solved by lowering the sensitivity, but then the book and nearly everything else would be black. In this case the candles cause the clipping. (Not too bad here, because the lost detail isn't important for the image.)

The RGB components also show very well that the shadows are not neutral grey but orange, otherwise the color heaps on the left would, as in the gradient histogram above, have their center at the same position. There isn't a lot to correct here, what could be done is raising the shadows with a :doc:`/effects_and_compositions/video_effects/color_image_correction/curves` effect, but this is a matter of taste and the intended mood for the final movie.

.. figure:: /images/tips_and_tricks/kdenlive2308_histogram_04.gif
   :width: 650px
   :alt: kdenlive2308_histogram_04.gif

   Histogram before and after applying some color correcting with the :doc:`/effects_and_compositions/video_effects/color_image_correction/curves` effect

Example 2: Underexposed ABC
---------------------------

.. figure:: /images/tips_and_tricks/kdenlive2308_histogram_05.webp
   :width: 650px
   :alt: kdenlive2308_histogram_05.webp

   Histogram example 2 with an underexposed image

We immediately notice two things:

- The RGB peaks are at the same position, near the middle. The white wall is the brightest part, so these peaks are from the white wall. As they are not shifted, the white balance should be okay (the image confirms that). Note that the Histogram is not very accurate for white balance. Later we will introduce a much more accurate scope.
 
- The image is too dark. The brightest component, red, only reaches a value of 170. The white wall is actually grey.

Monitoring correct exposure is the histogram's strength! The exposure can be corrected with :doc:`/effects_and_compositions/video_effects/color_image_correction/curves` as well, but this time we will use the :doc:`/effects_and_compositions/video_effects/color_image_correction/levels` effect.

.. figure:: /images/tips_and_tricks/kdenlive2308_histogram_06.gif
   :width: 650px
   :alt: kdenlive2308_histogram_06.gif

   Histogram before and after applying the :doc:`/effects_and_compositions/video_effects/color_image_correction/levels` effect to correct exposure

We have lowered the input white level of the luma channel until one of the RGB components reached 255. Lowering the input white level further would cause clipping on the wall and loss of image information. (Which may be desired in certain circumstances!)

This process is called *Stretching* of the tonal range.

Histogram Options
-----------------

The Histogram can be adjusted as follows:

- Components - They can be enabled individually. For example, you might only want to see the Luma component, or you want to hide the Sum display.
  
   - :guilabel:`Y` or Luma is the best known histogram. Every digital camera shows it, |digikam|, |gimp|, etc. know it. See :ref:`below <scopes-luma_calc>` how it is calculated.
   
   - :guilabel:`Sum` is basically a quick overview over the individual :abbr:`RGB (Red Green Blue)` channels. If it shows e.g. 5 as the minimum value, you know that none of the RGB components goes lower than 5.
   
   - :guilabel:`R / G / B` show the histogram for the individual channels.

- Unscaled (Context menu) - Does not scale the width of the histogram (unless the widget size is smaller). Just a goodie if you want to have it 256px wide.

.. _scopes-luma_calc:

- Luma mode (Context menu) - This option defines how the Luma value of a pixel is calculated. Two options are available:
   
   - Rec. 601 uses the formula ``Y' = 0.299 R' + 0.587 G' + 0.114 B'``
   
   - Rec. 709 uses ``Y' = 0.2126 R' + 0.7152 G' + 0.0722 B'``

Most of the time you will want to use Rec. 709 which is mostly used in digital video today. 

.. rubric:: Summary

The Histogram is a great tool for exposure correction, together with the Curves and the Levels effects. It helps to avoid clipping (burned out areas) and crushed blacks (the opposite) when applying effects.



.. rubric:: Notes

.. |web_archive| raw:: html

      <a href="https://web.archive.org/web/20160319081747/https://kdenlive.org/users/granjow/introducing-color-scopes-histogram" target="_blank">web.archive.org</a>

**Sources**
  - :download:`Histogram-bw.png <http://granjow.net/uploads/kdenlive/samples/Histogram-bw.png>`
  - :download:`Histogram-col.png <http://granjow.net/uploads/kdenlive/samples/Histogram-col.png>`   
  - :download:`abc-underexposed.avi <http://granjow.net/uploads/kdenlive/samples/abc-underexposed.avi>` (26 MB; 720/24p)
  - :download:`candlelight.avi <http://granjow.net/uploads/kdenlive/samples/candlelight.avi>` (14 MB; 720/24p)
 
  The original text was submitted by *Simon A. Eugster (Granjow)* on Mon, 8/30/2010 - 23:10 to the now defunct kdenlive.org blog. For this documentation it has been lifted from |web_archive|, updated and adapted to match the overall style.