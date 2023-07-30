.. meta::

   :description: Do your first steps with Kdenlive video editor, using video waveform monitor effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, utility, video waveform monitor

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |link| raw:: html

   <a href="link_URI" target="_blank">link_text</a>


.. _effects-video_waveform_monitor:

Video Waveform Monitor
======================

This effect/filter plots color component intensity. By default luminance only. Each column of the waveform corresponds to a column of pixels in the source video.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-video_waveform_monitor.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-video_waveform_monitor

   Video Waveform Monitor effect

* **Mode** - Select **Row** or **Column** (default). In row mode, the graph on the left side represents color component value 0 and the right side represents value = 255. In column mode, the top side represents color component value = 0 and bottom side represents value = 255.

* **Intensity** - Set intensity. Smaller values are useful to find out how many values of the same luminance are distributed across input rows/columns. Default value is 0.04. Allowed range is [0, 1].

* **Mirror** - Set mirroring mode. In mirrored mode, higher values will be represented on the left side for row mode and at the top for column mode. Default is **Off**.

.. rst-class:: clear-both

* **Display** - Set display mode. See options below.

* **Components** - Set which color components to display. See options below

* **Envelope** - Set envelope. See options below.

* **Filter** - Set the filter to apply. See options below.

* **Graticule** - Select which graticule to display. See options below.

* **Graticule Opacity** - Set graticule opacity

* **Flags** - Set graticule flags. Options are **numbers** (default; draw numbers above lines) and **dots** (draw dots instead of lines)

* **Scale** - Set scale used for displaying graticule. Options are **digital** (default), **millivolts** and **ire**

* **Background Opacity** - Set background opacity


.. rubric:: Parameter Options

.. list-table:: Display
   :header-rows: 1
   :width: 100%
   :widths: 25 75

   * - **Value**
     - **Description**
   * - **overlay**
     - Presents information identical to **parade**, except that the graphs representing color components are superimposed directly over one another. This display mode makes it easier to spot relative differences or similarities in overlapping areas of the color components that are supposed to be identical, such as neutral whites, grays, or blacks.
   * - **stack** (default)
     - Display separate graph for the color components side by side in row mode or one below the other in column mode.
   * - **parade**
     - Display separate graph for the color components side by side in column mode or one below the other in row mode. Using this display mode makes it easy to spot color casts in the highlights and shadows of an image, by comparing the contours of the top and the bottom graphs of each waveform. Since whites, grays, and blacks are characterized by exactly equal amounts of red, green, and blue, neutral areas of the picture should display three waveforms of roughly equal width/height. If not, the correction is easy to perform by making level adjustments to the three waveforms.

.. list-table:: Components
   :header-rows: 1
   :width: 100%
   :widths: 25 75

   * - **Value**
     - **Description**
   * - 1 (default)
     - Y (:term:`luma` or luminance)
   * - 2
     - U (blue minus luma)
   * - 3
     - YU
   * - 4
     - V (red minus luma)
   * - 5
     - YV
   * - 6
     - UV
   * - 7
     - YUV

.. list-table:: Envelope
   :header-rows: 1
   :width: 100%
   :widths: 25 75

   * - **Value**
     - **Description**
   * - **none** (default)
     - No envelope
   * - **instant**
     - Instant envelope, minimum and maximum values presented in graph will be easily visible even with small step value.
   * - **peak**
     - Hold minimum and maximum values presented in graph across time. This way you can still spot out of range values without constantly looking at waveforms.
   * - **peak+instant**
     - Peak and instant envelope combined together

.. list-table:: Filter
   :header-rows: 1
   :width: 100%
   :widths: 25 75

   * - **Value**
     - **Description**
   * - **lowpass** (default)
     - No filtering
   * - **flat**
     - :term:`Luma` and :term:`chroma` combined together
   * - **aflat**
     - Similar as above, but shows difference between blue and red chroma.
   * - **xflat**
     - Similar as above, but use different colors.
   * - **yflat**
     - Similar as above, but again with different colors.
   * - **chroma**
     - Displays only chroma
   * - **color**
     - Displays actual color value on waveform
   * - **acolor**
     - Similar as above, but with luma showing frequency of chroma values.

.. list-table:: Graticule
   :header-rows: 1
   :width: 100%
   :widths: 25 75

   * - **Value**
     - **Description**
   * - **none** (default)
     - Do not display graticule
   * - **green**
     - Display green graticule showing legal broadcast ranges
   * - **orange**
     - Display orange graticule showing legal broadcast ranges
   * - **invert**
     - Display invert graticule showing legal broadcast ranges


.. note:: As of this writing and in version 23.04.3 this effect does not do anything. A bug report has been created.
