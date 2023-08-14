.. meta::

   :description: Do your first steps with Kdenlive video editor, using vectorscope (advanced) effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, utility, vectorscope (advanced)

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |link| raw:: html

   <a href="link_URI" target="_blank">link_text</a>


.. _effects-vectorscope_advanced:

Vectorscope (advanced)
======================

This effect/filter draws and overlays a vectorscope of the video data. Compared to the :ref:`effects-vectorscope` effect it offers parameters to control the display mode and a few other things.

This is different from the :ref:`view-vectorscope` from the :ref:`view_menu` because the Effect version writes the vectorscope into the output video, whereas the View Menu version displays the vectorscope in a separate widget while you still can preview your project.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-vectorscope_advanced.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-vectorscope_advanced

   Vectorscope (advanced) effect

* **Mode** - Set the vectorscope mode. See below for available options.

* **X / Y** - Set which color component will be represented on X / Y axis

* **Intensity** - Set intensity used by modes **gray**, **color**, **color3** and **color5** for increasing brightness of color component which represents frequency of (X, Y) location in graph

* **Envelope** - Select **None** (default), **Instant** envelope (even darkest single pixel will be clearly highlighted), **Peak** to hold maximum and minimum values presented in graph over time (this way you can still spot out of range values without constantly looking at vectorscope), or **Peak+Instant** for peak and instant envelope combined together

* **Graticule** - Set what kind of graticule to draw. Options are **none** (default), **color** and **green**.

* **Graticule Opacity** - Set graticule opacity

* **Flags** - Set graticule flags. Options are **White** (draw graticule for white point), **Black** (draw graticule for black point) and **Name** (default; draw color points short names).

* **Background Opacity** - Set background opacity

* **Low Threshold** - Set low threshold for color component not represented on X or Y axis. Values lower than this value will be ignored. Default is 0. Note this value is multiplied with the actual max possible value one pixel component can have. So for 8-bit input and low threshold value of 0.1 the actual threshold is 0.1 * 255 = 25.

* **High Threshold** - Set high threshold for color component not represented on X or Y axis. Values higher than this value will be ignored. Default is 1. Note this value is multiplied with the actual max possible value one pixel component can have. So for 8-bit input and high threshold value of 0.9 the actual threshold is 0.9 * 255 = 230.

* **Colorspace** - Set what kind of colorspace to use when drawing graticule. Options are **Auto** (default), **601** and **709**.
