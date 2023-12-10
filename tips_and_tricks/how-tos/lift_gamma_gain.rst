.. meta::
   :description: Kdenlive Tips & Tricks - How-to Lift/Gamma/Gain
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, color correction, useful information, tutorial, how-to, lift gamma gain, lift/gamm/gain, LGG

.. metadata-placeholder

   :authors: - micha  (https://discuss.kde.org/u/micha)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Lift/Gamma/Gain (LGG)
=====================

When it comes to color correction and color grading, Lift/Gamma/Gain (LGG) is the standard tool in all professional video editor applications. It is very much worth it to familiarize yourself with it because it is the one-stop-shopping tool to improve almost everything to do with colors in a video. Even complex and complicated lighting situations (for example, lighting with different color temperatures) can be tackled because the tool\ [1]_ allows you to independently improve or creatively adjust shadows using *Lift*, mid-tones using *Gamma* and highlights using *Gain*.

LGG does not do anything automatically, however. You have to adjust everything yourself, and - most importantly - know and understand where and how to change colors. In order to make it a bit easier, LGG uses color wheels instead of just abstract values for the primary colors R (red), G (green) and B (blue), so you can see what you are doing.

The first task is to find out what tint the image has. Then you move the circle in the center of the color wheel into the opposite direction of the perceived tint. The further away from the center the bigger the change. And sometimes it helps to overdo it a bit just to see the difference between the correct and the wrong color tone.

It is recommended to start with the midtones (*gamma*). After that you may need to use *gain* to slightly adjust the highlights, usually into the same direction as the midtones. And that's about it most of the time. You can leave the shadows as is, more often than not.

This sounds - and essentially is - rather simple and straightforward. The difficult part is to correctly judge the tint of the image. In case you did not judge it correctly you can reset your changes either individually using :kbd:`RMB` or :kbd:`MW` in the respective color circle or the slider, or reset the entire effect by clicking on |adjustlevels|\ :guilabel:`Presets` and selecting |view-refresh|\ :guilabel:`Reset Effect`. You can check the results of your changes and compare the before and after in two ways:

1. Click on |view-visible|\ :guilabel:`Disable Effect` and |view-hidden|\ :guilabel:`Enable Effect` to turn the effect on and off [2]_
2. Click on |view-split-left-right|\ :guilabel:`Compare Effect` to split the monitor into two panes: left with the effect, right without the effect. You can move the red vertical divider to change the size of the panes.

That helps in judging whether the changes improved the image or made it worse. If the changes made it look different but not necessarily better, it is good practice to reset the effect and start again.

LGG is rather intuitive and easy to use. But make no mistake, it takes a while to master it, and beginners should not get frustrated if the first clicks do not yield good results immediately. Success comes with patience, observation and lots of practice.

You may notice that moving the circle towards a color (e.g. (R) red) **does not increase** the value for that color but **reduces** the values of the opposite colors (e.g. (G) green and (B) blue). This is on purpose because it avoids clipping which can happen fairly quickly and easily when increasing the value of a color. That way you can focus on the colors and their changes without worrying about overamplifying the respective color channel. This said, moving the circle by definition makes the image darker which needs to be compensated by using the corresponding slider. It applies to all three primary colors (R, G, and B) equally and lifts or lowers their brightness. Make sure not to exceed the value of 255 (maximum brightness), otherwise you will lose tonal information.

Instead of using the color wheels you can change the values for R, G, or B directly by either entering a value, or by :kbd:`LMB` on the respective color value and using the :kbd:`MW` (mouse wheel) to change the values in 0.010 increments. Holding :kbd:`Ctrl` while turning the wheel increases the value in 0.100 increments.

.. attention:: Using the color values directly does increase the value for the color (contrary to reducing the value when using the color wheel as mentioned above) which can cause clipping.



.. rubric:: Notes

----

.. [1] Lift/Gamma/Gain is, of course, in fact a filter (or effect) and not a tool. But the filter is very powerful and important.
.. [2] This may look like an error but when |view-visible| is displayed the tool-tip says :guilabel:`Disable Effect` because clicking the icon disables the effect and turns the icon into |view-hidden|. And vice-versa.

.. ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Icons used here
   
   .. |view-visible| image:: /images/icons/view-visible.svg
   :width: 22px
   :class: no-scaled-link

   .. |view-hidden| image:: /images/icons/view-hidden.svg
   :width: 22px
   :class: no-scaled-link

   .. |view-split-left-right| image:: /images/icons/view-split-left-right.svg
   :width: 22px
   :class: no-scaled-link

   .. |adjustlevels| image:: /images/icons/adjustlevels.svg
   :width: 22px
   :class: no-scaled-link

   .. |view-refresh| image:: /images/icons/view-refresh.svg
   :width: 22px
   :class: no-scaled-link
