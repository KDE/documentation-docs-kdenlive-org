.. meta::

   :description: Do your first steps with Kdenlive video editor, using the audio waveform filter effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, on master, audio waveform filter

.. metadata-placeholder

   :authors: - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-audio_waveform_filter:

Audio Waveform Filter
=====================

This effect/filter is an audio visualization effect that draws an audio waveform on the image.

.. versionadded:: 22.12
   The effect has keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-audio_waveform_filter.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-audio_waveform_filter

   Audio Waveform Filter effect

* **Fill** - If checked the area below the line will be filled using the color specified with :guilabel:`Foreground Color`.

* **Channel to draw** - Defines which channels in the audio track to draw. Options are **All** (default), **Merge**, **1** - **10**.

* **Background Color** - Defines the background color to be applied to the entire frame

* **Foreground Color** - Defines the color of the waveform

* **Line Thickness** - Defines the thickness of the line in number of pixels

* **Angle** - Defines the rotation angle to be applied to the waveform

* **X / Y / W / H / Size / Opacity** - Defines the X and Y coordinates, Width and Height, Size and Opacity of the rectangle in which the waveform is drawn. The icons help lining up the rectangle. :guilabel:`Opacity` cannot be changed.

.. rst-class:: clear-both


**Example**

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-audio_waveform_filter_example.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-audio_waveform_filter_example

   Example of the Audio Waveform Filter effect with default settings

..
