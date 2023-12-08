.. meta::

   :description: Kdenlive Video Effects - Video Waveform Monitor
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, utility, video waveform monitor

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Video Waveform Monitor
======================

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-video_waveform_monitor.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-video_waveform_monitor

.. sidebar:: |kdenlive-show-video| Video Waveform Monitor

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      waveform
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter plots color component intensity. By default luminance only. Each column of the waveform corresponds to a column of pixels in the source video.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 10 65
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Mode
     - Selection
     - Select the orientation of the waveform
   * - Intensity
     - Float
     - Set intensity. Smaller values are useful to find out how many values of the same luminance are distributed across input rows/columns. Default value is 0.04. Allowed range is [0, 1].
   * - Mirror
     - Switch
     - Set mirroring mode. In mirrored mode, higher values will be represented on the left side for row mode and at the top for column mode. Default is **Off**.
   * - Display
     - Selection
     - Set display mode
   * - Components
     - Integer
     - Set which color components to display. Numerical values represent different :term:`planes <plane>` (see below).
   * - Envelope
     - Selection
     - Set envelope
   * - Filter
     - Selection
     - Set the filter to apply
   * - Graticule
     - Selection
     - Select which graticule to display
   * - Graticule Opacity
     - Float
     - Set graticule opacity
   * - Flags
     - Selection
     - Set graticule flags
   * - Scale
     - Selection
     - Set scale used for displaying graticule
   * - Background Opacity
     - Float
     - Set background opacity


The following selections are available:

:guilabel:`Mode`

.. list-table::
   :width: 100%
   :widths: 25 75
   :class: table-simple

   * - Row
     - Graph on the left side represents color component value 0 and the right side represents value = 255
   * - Column
     - Top side represents color component value = 0 and bottom side represents value = 255.


:guilabel:`Display`

.. list-table:: 
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


:guilabel:`Components`

.. list-table:: 
   :header-rows: 1
   :width: 100%
   :widths: 25 75

   * - **Value**
     - **Description**
   * - **1** (default)
     - Y (:term:`luma` or luminance)
   * - **2**
     - U (blue minus luma)
   * - **3**
     - YU
   * - **4**
     - V (red minus luma)
   * - **5**
     - YV
   * - **6**
     - UV
   * - **7**
     - YUV


:guilabel:`Envelope`

.. list-table:: 
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


:guilabel:`Filter`

.. list-table:: 
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


:guilabel:`Graticule`

.. list-table:: 
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


:guilabel:`Flags`

.. list-table:: 
   :header-rows: 1
   :width: 100%
   :widths: 25 75

   * - **Value**
     - **Description**
   * - **numbers** (default)
     - Draw numbers above lines
   * - **dots**
     - Draw dots instead of lines


:guilabel:`Scale`

.. list-table:: 
   :header-rows: 1
   :width: 100%
   :widths: 25 75

   * - **Value**
     - **Description**
   * - **digital** (default)
     - 
   * - **millivolts**
     - 
   * - **ire**
     - 
