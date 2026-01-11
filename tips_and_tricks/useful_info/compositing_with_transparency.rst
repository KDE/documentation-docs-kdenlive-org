.. meta::
   :description: Kdenlive Tips & Tricks - Compositing with Transparency
   :keywords: KDE, Kdenlive, tips, tricks, tips & tricks, useful information, compositing, transparency, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - TheDiveO
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             
   :license: Creative Commons License SA 4.0


.. To Do:
   + Update screenshots
   + Correct *Affine*
   + Move images to new folder


.. _compositing_with_transparency:

Compositing with Transparency
=============================

When transparency is involved in both frames processed by one of Kdenlive's dynamic compositing transitions, the outcome may be surprising to some of us users. Luckily, things are not as inexplicable as they appear, so let's dive right into transparency and transitions.

Transparency & Dynamic Transitions
----------------------------------

When it comes to handling transparency, Kdenlive's :doc:`transitions </compositing/transitions>` fall into two categories:

1. **Affine** uses the so-called **atop** compositing operator
2. **Composite**, **Composite & Transform**, **Cairo (Affine) Blend** use the **over** compositing operator instead

So what does **atop** and **over** really mean? Let's discover what these compositing operators do using a typical title and semi-transparent background example. For simplicity, we first will ignore the **opacity** parameter of the aforementioned transitions to keep things easier to grasp. And after we have mastered this step, we will finally look at how the opacity parameter fits into the full picture.


Affine: Atop Compositing
------------------------

.. container:: clear-both

   .. image:: /images/affine-transition-atop.png
      :align: left
         :width: 350px

   The result of the **atop** compositing is best explained at first by showing its outcome: Text from the topmost title clip (partly) vanishes in those regions where the underlying clip on the middle track is (semi) transparent.

   The checkerboard clip on the bottom track just serves for illustrational purposes, so we can better see the transparent regions.

   Please notice how the two **Affine** transitions are chained: first, the upper Affine composites the title clip onto the gradient background. Then, the lower Affine composites the result onto the checkboard background.

.. container:: clear-both

   .. image:: /images/Alpha-Compositing-1.jpg
      :align: left
         :width: 350px

   But how does the **Affine** transition exactly handle transparency? Let's look at this hand-made illustration, where we have two pixels with some transparency each (the alpha values, αA and αB). It is important to **not** confuse pixel transparency with the opaque parameter of transitions.

   Our red pixel comes from the upper track frame (B), whereas the green pixel stems from the lower track frame (A). An alpha of 0 means a completely transparent pixel, whereas an alpha of 1.0 (or 255) means totally opaque pixel.

   The **Affine** transition now simply ignores the transparency information from the upper frame pixel (the red one).

   It solely uses the transparency information (green) contained in the lower track frames! Or more mathematical: α = αA

   And that is the explanation why in our example above the title text vanishes in those regions where the middle clip is transparent.

.. rst-class:: clear-both


Composite & Co: Over Compositing
--------------------------------

.. container:: clear-both

   .. image:: /images/composite-transition-over.png
      :align: left
         :width: 350px

   Again, we basically use the same setup as before, but this time we use **Composite & Transform** in place of **Affine** transitions. We chain the transitions as before, so that the lower transition works on the outcome of the upper transition.

   But look: The outcome is different! The result of the **over** operator is probably more to the expectations of most users. Now, the top title clip does not get (*sorry*) clipped anymore. 

.. container:: clear-both

   .. image:: /images/Alpha-Compositing-2.jpg
      :align: left
         :width: 350px

   As the **over** operation produces results more to the expectations of many users, how does it handle transparency exactly?

   **Simply spoken:** if you paint some semi-transparent pixel over another semi-transparent pixel, then **the result will be less transparent**. It will be even less transparent than the lower frame pixel transparency. This is what we would probably expect from painting with semi-opaque paint.

   Calculating the resulting transparency for two given pixels from an upper frame (B) and a lower frame (A) is thus more involved this time.

   Again, we start with the transparency of the lower frame pixel (green) as a base. But this time, we cannot ignore the transparency of the (red) upper frame pixel. But simply adding both transparencies would not yield sensible results; what does a transparency of 2.0 or 511 mean?

   So the red pixel transparency is **scaled** - you may think of shrinking the original 0-1.0 scale into the available space above the green transparency value. The resulting transparency then is the sum of the green base alpha value, plus the rescaled red alpha value. Remember, we kind of paint over the lower frame. For the formular-affine: α = αA + αB (1-αA)

.. rst-class:: clear-both

Transition Parameter Opacity
----------------------------

The dynamic compositing transitions also feature a parameter called **Opacity**. It is easy to confuse it with pixel transparency, but it is something different. The opacity parameter applies to the upper frames (B) only. It is kind of a master control but how does it work?

.. container:: clear-both

   .. image:: /images/Alpha-Compositing-3.jpg
      :align: left
         :width: 350px

   Let's start with the **Affine** transition, again. Above, we have seen that Affine ignores the transparency of the (red) upper frame pixels. And Affine also **ignores** the **opacity** parameter when calculating the result **pixel transparency**.

   Instead, the opacity parameter influences how the result **pixel color** gets calculated: this is a linear interpolation between the color of the upper frame (B) pixel and the lower frame (A) pixel. The opacity now controls the exact blending point. An opacity of 0.0 results in only the lower frame (B) pixel color, while 1.0 solely yields the upper frame pixel (A) color. 0.5 would be halfway between the two pixel colors.

   To sum up: in case of the **Affine** transition, **the opacity parameter solely affects color blending** between upper frame (B) and lower frame (A) pixels.

.. container:: clear-both

   .. image:: /images/Alpha-Compositing-4.jpg
      :align: left
         :width: 350px

   Next, let's look at the other transitions: **Composite** & Co.

   As for the color blending, the same procedure applies that we have just seen with the Affine transition: the opacity parameter controls how much upper frame (B) pixel color gets into the blend.

   But when we look at how the transparency of the resulting pixel gets calculated, things are starting to look different. We have seen that the transparency of the upper frame (B) pixel gets scaled down in reverse proportion of the lower frame (A) pixel transparency. The **opacity** parameter takes this even further: it additionally scales down the upper frame (B) pixel transparency. Please see also the illustration.

   In consequence, the opacity parameter thus controls how much opacity of an upper frame (B) pixel is applied at all. This way, you can fade in or out the upper frame.

   To sum up: in case of the **Composite** (& Co) transitions, **the opacity parameter affects both color blending** of upper frame (B) and lower frame (A) pixels, **as well as transparency of the upper frame (B)**.

.. rst-class:: clear-both



.. rubric:: Notes

.. |alpha_compositing| raw:: html

   <a href="https://en.wikipedia.org/wiki/Alpha_compositing" target="_blank">Alpha Compositing</a>

.. |svg_open_paper| raw:: html

   <a href="https://web.archive.org/web/20180726161540/http://www.svgopen.org/2005/papers/abstractsvgopen/" target="_blank">SVG Open 2015 paper</a>

.. |kdenlive_org| raw:: html

   <a href="https://kdenlive.org/en/project/compositing-with-transparency/" target="_blank">kdenlive.org</a>

**Further Reading**
  * Wikipedia article on |alpha_compositing|, with a reference to the original Porter Duff SIGGRAPH’84 paper on «Compositing Digital Images».
  
  * The |svg_open_paper| by Craig Northway on "Understanding Compositing and Color extensions in SVG 1.2 in 30 minutes!" - especially the Porter Duff operator table in chapter 6 with resulting alpha calculation column.

**Sources**
  The original text was submitted by user *TheDiveO* to the now defunct kdenlive.org blog. For this documentation it has been lifted from |kdenlive_org|, updated and adapted to match the overall style.