.. meta::
   :description: Kdenlive Tips & Tricks - Smooth Keyframe Interpolation
   :keywords: KDE, Kdenlive, tips, tricks, tips & tricks, useful information, smooth, keyframe, interpolation, editing, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - TheDiveO
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             
   :license: Creative Commons License SA 4.0


.. |geogebra| raw:: html

   <a href="https://www.geogebra.org/" target="_blank">GeoGebra</a>


.. _the_smooth_keyframe_interpolation:

Smooth Keyframe Interpolation
=============================

Did you ever wonder why Kdenlive's **smooth interpolation mode may overshoot** between keyframes? And how to tell Kdenlive to avoid such situations?

Let's start to look behind the scenes and introduce you to the strange world of smoothness. Do not worry, there will not be any mathematics for you to learn and understand. Just watch the figures. We will also show you how to avoid such overshots in those situations you do not want it. And for the really curious who want to know what the mathematics behind “smooth” interpolation are there is some :ref:`further reading <ski_further_reading>` in the **Notes** section at the bottom of this page.

The Fade-In Ramp
----------------

.. figure:: /images/tips_and_tricks/kdenlive2308_smooth_keyframes_1a.webp
   :align: left
   :width: 350px
   :figwidth: 350px

   Keyframes in the :doc:`/effects_and_filters/video_effects/color_image_correction/brightness_keyframable` effect

Let's start with a simple ramp, as shown here. We use two keyframes\ [1]_, one with a low value setting, and the other with a high value setting. The particular values do not matter. We set both keyframes to the interpolation mode :guilabel:`smooth`.

| 

.. rst-class:: clear-both

.. figure:: /images/tips_and_tricks/kdenlive2308_smooth_keyframes_1b.webp
   :align: left
   :width: 350px

   Color clip keyframe display

The effect display inside the timeline clip looks like a straight ramp. But if you watch the interpolated values closely while scrubbing the timeline, you should notice that the slope of the ramp varies. At the end and beginning the slope is smaller than in the middle, where it is higher.

But what exactly is going on here?

| 

.. rst-class:: clear-both


.. figure:: /images/tips_and_tricks/kdenlive2308_catmull-rom_1.webp
   :align: left
   :width: 350px
   :figwidth: 350px

   GeoGebra visualization of the Catmull-Rom interpolation

There is this online open source tool |geogebra| for trying out the mathematics inside Kdenlive's MLT engine.

This figure shows two keyframes P1=0 and P2=1, which is a fairly typical ramp up setting. In case you are already wondering: it does not matter at which exact frames the individual keyframes are.

.. rst-class:: clear-both

The smooth interpolation that :abbr:`MLT (Media Lovin' Toolkit - An open source software multimedia framework designed and developed for tv broadcasting)` will calculate is drawn as a thick green line. It is bent a little bit like the capital letter S, but then, not really too much.

And if you look closely, then beginning and ending slope of the green line are not horizontal - at least what could be expected at first.

You may wonder what the two other keyframes P0 and P3 are good for? Well, the math underneath always requires four keyframes in order to interpolate segment-wise between any two adjacent keyframes. And if there is no preceding (P0) or trailing (P1) keyframe, then we will simple repeat the left (P1) or right (P2) keyframe.

Ramp-Up, and … Overshoot
------------------------

.. figure:: /images/tips_and_tricks/kdenlive2308_smooth_keyframes_2a.webp
   :align: left
   :width: 350px
   :figwidth: 350px

   Keyframes in the :doc:`/effects_and_filters/video_effects/color_image_correction/brightness_keyframable` effect

Now let's add a third keyframe, so this looks like a ramp with a plateau. This is shown in the screenshots.

| 
| 
| 
| 

.. figure:: /images/tips_and_tricks/kdenlive2308_smooth_keyframes_2b.webp
   :align: left
   :width: 350px

   Color clip keyframe display

And now, the ramp gets a clearly visible bump instead of a sharp bend. Well, this looks smooth, but not exactly what we may have intended? So why is this the way it is?

.. rst-class:: clear-both

.. figure:: /images/tips_and_tricks/kdenlive2308_catmull-rom_2.webp
   :align: left
   :width: 350px
   :figwidth: 350px

   GeoGebra visualization of the Catmull-Rom interpolation

This is now our ramp with a plateau: P0=0, P1=1, P2=2. Do not worry about the keyframe numbering, though.

Did you expect the plateau to be, well a *straight* plateau? Of course you did. But you may have already noticed that Kdenlive does not exactly behave like this. Instead, the interpolation math causes the interpolated values to overshoot, as you can easily see in the figure.

What the underlying math does is this: the interpolation is smooth, so that the slope to the *left* of P1 is the same as to the *right* of P1. Yeah, that is a slightly different “smooth” from what you might have been expecting.

If you want the plateau to be straight instead, then you must set the interpolation mode of the keyframe P1 to :guilabel:`linear` instead. By the way, this does not change the *previous* smooth segment in any way. And this results in a “rough bent” at P1, but luckily you probably will not notice in most situations.

.. rst-class:: clear-both

Ramp Up-Flat-Down
-----------------

.. figure:: /images/tips_and_tricks/kdenlive2308_smooth_keyframes_3a.webp
   :align: left
   :width: 350px

   Keyframes in the :doc:`/effects_and_filters/video_effects/color_image_correction/brightness_keyframable` effect

.. figure:: /images/tips_and_tricks/kdenlive2308_smooth_keyframes_3b.webp
   :align: left
   :width: 350px

   Color clip keyframe display

Let's add another, fourth keyframe, so we have: ramp-up first, then flat, then ramp-down. A fairly typical fade-in and fade-out keyframe template.

| 
|
|

And look, what is happening: we have got a hump, but not a nice and flat middle section.

.. figure:: /images/tips_and_tricks/kdenlive2308_catmull-rom_3.webp
   :align: left
   :width: 350px
   :figwidth: 350px

   GeoGebra visualization of the Catmull-Rom interpolation

This time, we look at the middle section P1-P2. To the left, we see the up ramp, to the right, the down ramp.

Again, smooth now means that there is no sharp bend in the segments. Instead, the left and right slopes are continuous at P1 and P2; that is, in the middle section. And this causes our interpolated value to overshoot.
  
.. rst-class:: clear-both

Make Flat Great Again
---------------------

.. figure:: /images/tips_and_tricks/kdenlive2308_smooth_keyframes_4a.webp
   :align: left
   :width: 350px
   :figwidth: 350px

   Smooth keyframes in the :doc:`/effects_and_filters/video_effects/color_image_correction/brightness_keyframable` effect

.. figure:: /images/tips_and_tricks/kdenlive2308_smooth_keyframes_4b.webp
   :align: left
   :width: 350px

Now, how do we get a flat top? Fortunately, that is easy to achieve, as you can see from the screenshots.

| 1. keyframe: smooth,
| 2. keyframe: linear (interpolated!),
| 3. keyframe: smooth,
| 4. keyframe: smooth (albeit that does not really matter if there are no further keyframes).

.. rst-class:: clear-both



.. rubric:: Notes

.. |mlt_framework| raw:: html

   <a href="https://www.mltframework.org/" target="_blank">MLT Multimedia Framework</a>

.. |smooth_interpolation| raw:: html

   <a href="https://www.mltframework.org/blog/v0.9.0_released_with_new_property_animation_api/" target="_blank">smooth interpolation</a>

.. |source_code| raw:: html

   <a href="https://github.com/mltframework/mlt/blob/e8b92affcafbc206a5af0d446c446ed339d79a8b/src/framework/mlt_property.c#L1087" target="_blank">source code</a>

.. |cr_spline| raw:: html

   <a href="https://en.wikipedia.org/wiki/Centripetal_Catmull%E2%80%93Rom_spline" target="_blank">Catmull-Rom spline</a>

.. |kdenlive_org| raw:: html

   <a href="https://kdenlive.org/en/project/the-smooth-keyframe-interpolation/" target="_blank">kdenlive.org</a>

.. _ski_further_reading:

**Further Reading**
  As you may (or rather may not) remember, Kdenlive's rendering engine is the |mlt_framework|. While :abbr:`MLT (Media Lovin' Toolkit - An open source software multimedia framework designed and developed for tv broadcasting)` has |smooth_interpolation| since around mid-2013, Kdenlive only later caught up and now supports all three interpolation modes linear, discrete, and smooth. As can be seen from the MLT |source_code|, smooth interpolation is done using a |cr_spline|. In particular, MLT uses the so-called *uniform* variant, because it is so simple. The downside is that this smoothing sometimes has the unwanted property of overshooting, especially when you least expect it.

**Sources**
  The original text was submitted by user *TheDiveO* to the now defunct kdenlive.org blog. For this documentation it has been lifted from |kdenlive_org|, updated and adapted to match the overall style.

----

.. [1] You may notice that there are three keyframes: one at frame 0 of the clip, and the two we created for this screenshot. Kdenlive always sets a keyframe at frame 0 of a clip, and we chose to ignore that one for the purpose of this demonstration.