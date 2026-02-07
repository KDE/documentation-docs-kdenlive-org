.. meta::
   :description: Kdenlive Tips & Tricks - How to Fading In/Out of Titles
   :keywords: KDE, Kdenlive, tips, tricks, tips & tricks, how-to, how to, fading in, fading out, titles, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - TheDiveO
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             
   :license: Creative Commons License SA 4.0


.. |Kdenlive-Title-Fading| raw:: html
   
   <a href="https://files.kde.org/kdenlive/kdenlive-manual/Kdenlive-Title-Fading.mp4" target="_blank">Link to the video</a>


How to Fading In/Out of Titles
==============================

In this short *How-to* video, we show you how to (smoothly) fade in and out Kdenlive titles over a video clip, and fading from and to transparency. The key to success is to use a **Composite & Transform** transition with keyframes (**Affine** and **Composite** will work too). **Do not use** the Fade from/to Black effects though, as these effects remove the title transparency information. 

.. figure:: /images/tips_and_tricks/fading_inout_titles.webp
   :width: 418px
   :align: center
   
|Kdenlive-Title-Fading|

|

These are the individual steps shown in video:

1. Add a Composite & Transform transition to the title clip.
2. First keyframe: set :guilabel:`Opacity` to 0%. This marks the beginning of the fade in (ramp up).
3. Second keyframe: add a new keyframe where you want the title to be fully faded in, set :guilabel:`Opacity` to 100%. Set the type of the keyframe to :guilabel:`Linear`.
   
  a) The rationale to set this keyframe to :guilabel:`Linear` is that otherwise Kdenlive (MLT) calculates a smooth curve fitting to the previous and following keyframe, causing the opacity value to overshoot. With a maximum possible opacity of 100% you will not notice. However, when you use a maximum opacity of less than 100%, then this overshooting may become visible.
  b) Ensure that the first keyframe is Smooth. You can only adjust the type of the first keyframes after you have added a second keyframe.
  
4. Third keyframe: Add another keyframe near the end where you want to start fading out the title. Leave the opacity at 100%. Set the keyframe type to :guilabel:`Smooth`.
5. Fourth keyframe: Add a final keyframe, where you set :guilabel:`Opacity` to 0%.

For more information about mixing smooth and linear interpolated keyframes see this chapter about the :doc:`/tips_and_tricks/useful_info/smooth_keyframe_interpolation`.



.. rubric:: Notes

.. |kdenlive_org| raw:: html

   <a href="https://kdenlive.org/en/project/howto-fading-inout-kdenlive-titles/" target="_blank">kdenlive.org</a>

**Sources**
  The original text was submitted by user *TheDiveO* to the now defunct kdenlive.org blog. For this documentation it has been lifted from |kdenlive_org|, updated and adapted to match the overall style.