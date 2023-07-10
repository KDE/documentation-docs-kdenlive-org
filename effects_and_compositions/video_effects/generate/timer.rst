.. meta::

   :description: Do your first steps with Kdenlive video editor, using timer effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, generate, timer

.. metadata-placeholders

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-timer:

Timer
=====

This effect/filter overlays a timer onto the video. The timer can count up or down.

The effect has keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-timer.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-timer

   Timer effect

* **Font Family / Size / Weight** - Select the font and its attributes for the text. **Font Weight** seems to behave differently depending on the selected font family.

* **Outline Width** - Set the width of the outline in pixels to 0, 1, 2 or 3

* **Padding** - The number of pixels to pad the background rectangle beyond the edges of text

* **Horizontal / Vertical Alignment** - Set the horizontal and vertical alignment within the geometry rectangle

* **Format** - The time format of the timer text

* **Start** - The time that the timer will start counting up or down. The text will be frozen at 00:00:00.000 from the start of the filter until the start time has elapsed.

* **Duration** - The maximum elapsed duration of the timer after the start time has elapsed. The text will be frozen at the duration time after the duration has elapsed.

* **Offset** - An offset to be added to the timer value. When the direction is "down", the timer will count down to "offset" instead of 00:00:00.000. When the direction is up, the timer will count up starting from "offset".

* **Direction** - Whether the counter should count **up** from 00:00:00.000 or **down** from the duration time.

* **X / Y / W / H / Size / Opacity** - X and Y coordinates, Width and Height, Size and Opacity of the overlay rectangle. You can use these parameters to fine tune the position, size and :term:`opacity` of the overlay.

* **Foreground / Background / Outline Color** - Specify the colors for the text (foreground), the background rectangle defined by :guilabel:`Padding` and the outline color (if :guilabel:`Outline Width` is greater than 0).

.. rst-class:: clear-both


The following formats are available:

* HH:MM:SS
* HH;MM:SS.S
* MM:SS
* MM:SS.SS
* MM:SS.SSS
* SS
* SS.S
* SS.SS
* SS.SSS


.. hint:: In order to use a semi-transparent background color, click on the color panel, click on :guilabel:`+` and use the horizontal slider to change the transparency.

