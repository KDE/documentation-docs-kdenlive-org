.. meta::

   :description: Kdenlive Video Effects - Oscilloscope (advanced)
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, utility, oscilloscope (advanced)

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |rms| raw:: html

   <a href="https://undergroundmathematics.org/glossary/root-mean-square" target="_blank">this article</a>


Oscilloscope (advanced)
=======================

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-oscilloscope_advanced.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-oscilloscope_advanced

.. sidebar:: |kdenlive-show-video| Oscilloscope (advanced)

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      pr0file
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter draws a 2D oscilloscope over the clip. It does the same as :doc:`/effects_and_filters/video_effects/utility/oscilloscope` but offers more parameters and features, such as drawing a line across the frame that is used for the computations.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 10 65
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Channel
     - Selection
     - Channel to numerically display at the bottom of the scope
   * - R / G / B trace
     - Switch
     - Show R / G / B trace on scope
   * - Y / Pr / Pb trace
     - Switch
     - Show Y' / Pr / Pb trace on scope
   * - Alpha trace
     - Switch
     - Show Alpha trace on scope
   * - Display average
     - Switch
     - If switched on, averages are displayed
   * - Display RMS
     - Switch
     - If switched on, the RMS\ [1]_ value is displayed
   * - Display minimum / maximum
     - Switch
     - If switched on, minimum and maximum values are displayed
   * - 256 scale
     - Switch
     - If switched on, the oscilloscope uses the range 0..255 instead of 0.0..1.0 for value display
   * - Color
     - Selection
     - Set :term:`color space` to use
   * - X / Y / Tilt / Length
     - Integer
     - X / Y position, Tilt and Length of the profile marker (the line in the middle of the screen indicating where the scope values are taken from)
   * - Marker 1 / 2
     - Integer
     - Position of marker 1 / 2 (starting on the left side)
   * - Crosshair color
     - Integer
     - Color of the profile marker


The following selection items are available:

:guilabel:`Channel`

.. list-table::
   :width: 100%
   :widths: 25 75
   :class: table-wrap

   * - R
     - Red
   * - G
     - Green
   * - B
     - Blue
   * - Y'
     - :term:`luma` (default)
   * - Pr
     - Difference between red and luma
   * - Pb
     - Difference between blue and luma
   * - Alpha
     - Alpha channel

:guilabel:`Color`

.. list-table::
   :width: 100%
   :widths: 25 75
   :class: table-wrap

   * - CCIR rec. 601
     - default
   * - CCIR rec. 709
     - 



----

.. [1] RMS = Root Mean Squared. Useful when trying to measure the average "size" of numbers, where their sign is not important, as the squaring makes all numbers positive. The most common case of using the root mean square is when calculating the standard deviation of a set of numbers. For the mathematical details, refer to |rms| in undergroundmathematics.org


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
