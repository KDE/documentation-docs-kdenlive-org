.. meta::

   :description: Kdenlive Video Effects - Video Waveform Monitor
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, utility, video waveform monitor

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Video Waveform Monitor
======================

.. figure:: /images/effects_and_compositions/effects-video_waveform-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-video_waveform-2504.webp

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
   :**Color depth**:
      10bit |color-management|
   :**Tutorial**:
      :ref:`Yes <tutorials-waveform>` |view-presentation|

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter plots color component intensity. By default luminance only. Each column of the waveform corresponds to a column of pixels in the source video.

.. seealso:: :doc:`/tips_and_tricks/scopes/waveform_and_rgb_parade`

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
     - Select the orientation of the waveform: rows or columns
   * - Intensity
     - Float
     - Set intensity. Smaller values are useful to find out how many values of the same luminance are distributed across input rows/columns. Default value is 0.04. Allowed range is [0, 1].
   * - Mirror
     - Switch
     - Set mirroring mode. In mirrored mode, higher values will be represented on the left side for row mode and at the top for column mode. Default is **Off**.
   * - Display
     - Selection
     - Set display mode. See below for options and explanation.
   * - Components
     - Integer
     - Set which color components to display. Values represent different :term:`planes <plane>` (see below).
   * - Envelope
     - Selection
     - Set envelope. See below for options and explanation.
   * - Filter
     - Selection
     - Set the filter to apply. See below for options and explanation.
   * - Graticule
     - Selection
     - Select which graticule to display. See below for options.
   * - Graticule Opacity
     - Percentage
     - Set graticule opacity
   * - Flags
     - Selection
     - Set graticule flags. See below for options.
   * - Scale
     - Selection
     - Set scale used for displaying graticule. See below for options.
   * - Background Opacity
     - Percentage
     - Set background opacity


The following selections are available:

:guilabel:`Mode`

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 75
   :class: table-wrap

   * - **Value**
     - **Description**
   * - Row
     - Graph on the left side represents color component value 0 and the right side represents value = 255
   * - Column
     - Top side represents color component value = 0 and bottom side represents value = 255.


:guilabel:`Display`

.. list-table:: 
   :header-rows: 1
   :width: 100%
   :widths: 25 75
   :class: table-wrap

   * - **Value**
     - **Description**
   * - Overlay
     - Presents information identical to **Parade**, except that the graphs representing color components are superimposed directly over one another. This display mode makes it easier to spot relative differences or similarities in overlapping areas of the color components that are supposed to be identical, such as neutral whites, grays, or blacks.
   * - Stack (default)
     - Display separate graph for the color components side by side in row mode or one below the other in column mode.
   * - Parade
     - Display separate graph for the color components side by side in column mode or one below the other in row mode. Using this display mode makes it easy to spot color casts in the highlights and shadows of an image, by comparing the contours of the top and the bottom graphs of each waveform. Since whites, grays, and blacks are characterized by exactly equal amounts of red, green, and blue, neutral areas of the picture should display three waveforms of roughly equal width/height. If not, the correction is easy to perform by making level adjustments to the three waveforms.


:guilabel:`Components`

.. list-table:: 
   :header-rows: 1
   :width: 100%
   :widths: 25 75
   :class: table-wrap

   * - **Value**
     - **Description**
   * - Y
     - Y (:term:`luma` or luminance)
   * - U
     - U (blue minus luma)
   * - YU
     - YU
   * - V
     - V (red minus luma)
   * - YV
     - YV
   * - UV
     - UV
   * - All
     - YUV (default)


:guilabel:`Envelope`

.. list-table:: 
   :header-rows: 1
   :width: 100%
   :widths: 25 75
   :class: table-wrap

   * - **Value**
     - **Description**
   * - None (default)
     - No envelope
   * - Instant
     - Instant envelope, minimum and maximum values presented in graph will be easily visible even with small step value.
   * - Peak
     - Hold minimum and maximum values presented in graph across time. This way you can still spot out of range values without constantly looking at waveforms.
   * - Peak+Instant
     - Peak and instant envelope combined together


:guilabel:`Filter`

.. list-table:: 
   :header-rows: 1
   :width: 100%
   :widths: 25 75
   :class: table-wrap

   * - **Value**
     - **Description**
   * - Lowpass (default)
     - No filtering
   * - Flat
     - :term:`Luma` and :term:`chroma` combined together
   * - Aflat
     - Similar as above, but shows difference between blue and red chroma.
   * - Xflat
     - Similar as above, but use different colors.
   * - Yflat
     - Similar as above, but again with different colors.
   * - Chroma
     - Displays only chroma
   * - Color
     - Displays actual color value on waveform
   * - Acolor
     - Similar as above, but with luma showing frequency of chroma values.


:guilabel:`Graticule`

.. list-table:: 
   :header-rows: 1
   :width: 100%
   :widths: 25 75
   :class: table-wrap

   * - **Value**
     - **Description**
   * - None
     - Do not display graticule
   * - Green (default)
     - Display green graticule showing legal broadcast ranges
   * - Orange
     - Display orange graticule showing legal broadcast ranges
   * - Invert
     - Display invert graticule showing legal broadcast ranges


:guilabel:`Flags`

.. list-table:: 
   :header-rows: 1
   :width: 100%
   :widths: 25 75
   :class: table-wrap

   * - **Value**
     - **Description**
   * - Show numbers (default)
     - Draw numbers above lines
   * - Draw dots
     - Draw dots instead of lines


:guilabel:`Scale`

.. list-table:: 
   :header-rows: 1
   :width: 100%
   :widths: 25 75
   :class: table-wrap

   * - **Value**
     - **Description**
   * - Digital (default)
     - 
   * - Millivolts
     - 
   * - IRE
     - 


.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Icons used here (remove comment indent to enable them for this document)
   
   .. |linux| image:: /images/icons/linux.png
   :width: 14px
   :alt: Linux
   :class: no-scaled-link

   .. |appimage| image:: /images/icons/kdenlive-appimage_3.svg
   :width: 14px
   :alt: appimage
   :class: no-scaled-link

   .. |windows| image:: /images/icons/windows.png
   :width: 14px
   :alt: Windows
   :class: no-scaled-link

   .. |apple| image:: /images/icons/apple.png
   :width: 14px
   :alt: MacOS
   :class: no-scaled-link
