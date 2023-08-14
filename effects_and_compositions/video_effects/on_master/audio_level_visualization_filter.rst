.. meta::

   :description: Do your first steps with Kdenlive video editor, using the audio level visualization effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, on master, audio level visualization

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-audio_level_visualization_filter:

Audio Level Visualization Filter
================================

This effect/filter is an audio visualization effect that draws an audio level meter on the image.

.. versionadded:: 22.12
   The effect has keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-audio_level_visualization_filter.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-audio_level_visualization_filter

   Audio Level Visualization effect

* **Graph type** - Select the type of graph to display the levels. Option are **Bar** (default) and **Segment**.

* **Mirror** - If checked, mirrors the spectrum on the center line of the rectangle

* **Reverse** - If checked, draws the points starting with the right channel

* **Gradient Orientation** - Sets the direction of the color gradient

* **Background Color** - Defines the background color to be applied to the entire frame

* **Gradient Color 1 / 2 / 3** - Defines color of the waveform gradient. Color 1 defines the top, 2 the middle and 3 the bottom of the gradient

* **Line Thickness** - Defines the thickness of the bar or segments in number of pixels

* **Angle** - Defines the rotation angle to be applied to the waveform

* **X / Y / W / H / Size / Opacity** - Defines the X and Y coordinates, Width and Height, Size and Opacity of the rectangle in which the waveform is drawn. The icons help lining up the rectangle.

* **Channels** - Defines the number of channels to show

* **Segment Gap** - Defines the space in pixels between segments

.. rst-class:: clear-both


**Example**

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-audio_level_visualization_filter_example.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-audio_level_visualization_filter_example

   Example of the Audio Level Visualization Filter effect

* :guilabel:`Line Thickness` set to **8**

* :guilabel:`Gradient Color 1 / 2 / 3` set to different colors for demonstration purposes
