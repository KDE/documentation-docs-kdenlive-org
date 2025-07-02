.. meta::

   :description: Kdenlive Video Effects - Timer
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, generate, timer

.. metadata-placeholders

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Timer
=====

.. figure:: /images/effects_and_compositions/effects-timer-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-timer-2504.webp

.. sidebar:: |kdenlive-show-video| Timer

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      timer
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No
   :**Color depth**:
      8bit
   :**Tutorial**:
      :ref:`Yes <tutorials-timer>` |view-presentation|

.. rst-class:: clear-both


.. rubric:: Description
   
This effect/filter overlays a timer onto the video. The timer can count up or down.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Font Family / Style / Size / Weight
     - Selection / Integer
     - Select the font and its attributes for the text. **Font Weight** seems to behave differently depending on the selected font family.
   * - Outline Width
     - Integer
     - Set the width of the outline in pixels to 0, 1, 2 or 3
   * - Padding
     - Integer
     - The number of pixels to pad the background rectangle beyond the edges of text
   * - Horizontal / Vertical Alignment
     - Selection
     - Set the horizontal and vertical alignment within the geometry rectangle
   * - Format
     - Selection
     - The time format of the timer text
   * - Start
     - Slider
     - The time that the timer will start counting up or down. The text will be frozen at 00:00:00.000 from the start of the filter until the start time has elapsed.
   * - Duration
     - Slider
     - The maximum elapsed duration of the timer after the start time has elapsed. The text will be frozen at the duration time after the duration has elapsed.
   * - Offset
     - Slider
     - An offset to be added to the timer value. When the direction is "down", the timer will count down to "offset" instead of 00:00:00.000. When the direction is up, the timer will count up starting from "offset".
   * - Direction
     - Selection
     - Whether the counter should count **up** from 00:00:00.000 or **down** from the duration time.
   * - X / Y / W / H / Size / Opacity
     - Integer / Percent
     - X and Y coordinates, Width and Height, Size and Opacity of the overlay rectangle. You can use these parameters to fine tune the position, size and :term:`opacity` of the overlay.
   * - Foreground / Background / Outline Color
     - Picker
     - Specify the colors for the text (foreground), the background rectangle defined by :guilabel:`Padding` and the outline color (if :guilabel:`Outline Width` is greater than 0).


The following selection items are available:

:guilabel:`Horizontal Alignment` :guilabel:`Vertical Alignment`

.. list-table::
   :width: 100%
   :widths: 20 80
   :header-rows: 1
   :class: table-simple

   * - Horizontal
     - Vertical
   * - Left
     - Top
   * - Center
     - Middle
   * - Right
     - Bottom

:guilabel:`Direction`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Up
     - Timer counts up
   * - Down
     - Timer counts down

:guilabel:`Format`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - HH:MM:SS
     - hours:minutes:seconds
   * - HH:MM:SS.S
     - hours:minutes:seconds.1/10th
   * - MM:SS
     - minutes:seconds
   * - MM:SS.SS
     - minutes:seconds.1/100th
   * - MM:SS.SSS
     - minutes:seconds.1/1000th (milliseconds)
   * - SS
     - seconds
   * - SS.S
     - seconds.1/10th
   * - SS.SS
     - seconds.1/100th
   * - SS.SSS
     - seconds.1/1000th (milliseconds)


.. hint::
   In order to use a semi-transparent background color, click on the color panel, click on :guilabel:`+` and use the horizontal slider to change the transparency.

