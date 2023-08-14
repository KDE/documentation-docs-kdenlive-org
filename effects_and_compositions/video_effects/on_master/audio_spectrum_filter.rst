.. meta::

   :description: Do your first steps with Kdenlive video editor, using the audio spectrum filter effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, on master, audio spectrum filter

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-audio_spectrum_filter:

Audio Spectrum Filter
=====================

This effect/filter is an audio visualization effect that draws an audio spectrum on the image.

.. versionadded:: 22.12
   The effect has keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-audio_spectrum_filter.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-audio_spectrum_filter

   Audio Spectrum Filter effect

* **Graph type** - Select the type of graph to display the levels. Option are **Line** (default) and **Bar**.

* **Fill** - If checked, fills the area under the graph. Only applies to :guilabel:`Graph type` **Line**.

* **Mirror** - If checked, mirrors the spectrum on the center line of the rectangle

* **Reverse** - If checked, draws the points starting with the highest frequency

* **Window size** - The number of samples that the FFT\ [1]_ will be performed on. If :guilabel:`Window size` is less than the number of samples in a frame, extra samples will be ignored. If :guilabel:`Window size` is more than the number of samples in a frame, samples will be buffered from previous frames to fill the window. The buffering is performed as a sliding window so that the most recent samples are always transformed.

* **Background Color** - Defines the background color to be applied to the entire frame

* **Foreground color** - Defines the color of the waveform

* **Line Thickness** - Defines the thickness of the bar or line in number of pixels

* **Angle** - Defines the rotation angle to be applied to the waveform

* **X / Y / W / H / Size / Opacity** - Defines the X and Y coordinates, Width and Height, Size and Opacity of the rectangle in which the waveform is drawn. The icons help in lining up the rectangle.

* **Line Tension** - Affects the amount of curve in the line interpolating between points. **0** draws a straight line between points; **100** draws very curved lines between points. Values below **0** and above **100** will cause loops in the lines. Only applies to :guilabel:`Graph type` **Line**.

* **Points** - Defines the number of bands to draw in the spectrum. Each band shows up as a data point in the graph.

.. rst-class:: clear-both


.. note:: The effect is not updated in the Project Monitor during scrubbing. You need to play back the project to see this effect.

.. rst-class:: clear-both


**Example**

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-audio_spectrum_filter_example.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-audio_spectrum_filter_example

   Example of the Audio Spectrum Filter effect

* :guilabel:`Line Thickness` set to **4**

.. rst-class:: clear-both


**Notes**

.. [1] FFT := Fast Fourier Transform
