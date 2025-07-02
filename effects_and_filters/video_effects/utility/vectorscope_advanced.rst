.. meta::

   :description: Kdenlive Video Effects - Vectorscope (advanced) 
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, utility, vectorscope (advanced)

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Vectorscope (advanced)
======================

.. figure:: /images/effects_and_compositions/effects-vectorscope_advanced-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-vectorscope_advanced-2504.webp

.. sidebar:: |kdenlive-show-video| Vectorscope (advanced)

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      vectorscope
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No
   :**Color depth**:
      10bit |color-management|
   :**Tutorial**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter draws and overlays a vectorscope of the video data. Compared to the :doc:`/effects_and_filters/video_effects/utility/vectorscope` effect it offers parameters to control the display mode and a few other things.

This is different from the :ref:`view-vectorscope` from the :ref:`view_menu` because the *Effect* version writes the vectorscope into the output video, whereas the *View Menu* version displays the vectorscope in a separate widget while you still can preview your project.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Mode
     - Selection
     - Set the vectorscope mode. See below for available options.
   * - Tint 1 / Tint 2
     - Float
     - Set color tint for gray/tint vectorscope mode. By default both options are zero. This means no tint, and output will remain gray.
   * - X / Y
     - Integer
     - Set which color component will be represented on X / Y axis
   * - Intensity
     - Float
     - Set intensity used by modes **gray**, **color**, **color3** and **color5** for increasing brightness of color component which represents frequency of (X, Y) location in graph
   * - Envelope
     - Selection
     - Set whether the scope draws an edge or not and how the edge behaves. See below for available options.
   * - Graticule
     - Selection
     - Set what kind of graticule to draw. See below for available options.
   * - Graticule Opacity
     - Float
     - Set graticule opacity
   * - Graticule Flags
     - Selection
     - Set graticule flags. See below for available options.
   * - Background Opacity\ [1]_
     - Float
     - Set background opacity
   * - Low Threshold
     - Float
     - Set low threshold for color component not represented on X or Y axis. Values lower than this value will be ignored. Default is **0**. Note this value is multiplied with the actual max possible value one pixel component can have. So for 8-bit input and low threshold value of 0.1 the actual threshold is 0.1 * 255 = 25.
   * - High Threshold
     - Float
     - Set high threshold for color component not represented on X or Y axis. Values higher than this value will be ignored. Default is **1**. Note this value is multiplied with the actual max possible value one pixel component can have. So for 8-bit input and high threshold value of 0.9 the actual threshold is 0.9 * 255 = 230.
   * - Color Space
     - Selection
     - Set what kind of :term:`color space` to use when drawing graticule


The following selection items are available:

:guilabel:`Mode`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - Gray
     - 
   * - Tint
     - 
   * - Color
     - 
   * - Color 2
     - 
   * - Color 3
     - default
   * - Color 4
     - 
   * - Color 5
     - 

:guilabel:`Envelope`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - None
     - default
   * - Instant
     - Even darkest single pixel will be clearly highlighted
   * - Peak
     - To hold maximum and minimum values presented in graph over time (this way you can still spot out-of-range values without constantly looking at the vectorscope)
   * - Peak+Instant
     - For peak and instant envelope combined together

:guilabel:`Graticule`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - None
     - 
   * - Color
     - default
   * - Green
     - 

:guilabel:`Graticule Flags`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - White
     - Draw graticule for white point
   * - Black
     - Draw graticule for black point
   * - Name
     - Draw color points short names (default)

:guilabel:`Color Space`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - Auto
     - default
   * - Rec.601 (interleaved)
     - 
   * - Rec.709 (progressive)
     - 


----

.. [1] Does not seem to work; the vectorscope overlays the background completely.


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
