.. meta::

   :description: Kdenlive Video Effects - Data Scope 
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, utility, data scope, data, scope

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Data Scope
==========

.. figure:: /images/effects_and_compositions/effects-datascope-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| DataScope

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      datascope
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      Yes
   :**Color depth**:
      10bit |color-management|
   :**Tutorial**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter analyses the video data and shows hexadecimal pixel values of parts of the video.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Size
     - Selection
     - Set output video size
   * - X / Y Offset
     - Integer
     - Set the x / y offset from where to pick the pixels
   * - Components
     - Selection
     - Set pixel components to display. By default all pixel components are displayed.
   * - Mode
     - Selection
     - Set scope mode
   * - Show Axis
     - Selection
     - If set to **On**, draws rows and columns numbers on left and top of video. Default is **Off**.
   * - Opacity
     - Float
     - Set background opacity\ [1]_
   * - Format
     - Selection
     - Set display number format

The following selection items are available:

:guilabel:`Size`

.. list-table::
   :width: 100%
   :widths: 25 75
   :class: table-wrap

   * - 128p
     - 
   * - 360p
     - 
   * - PAL SD
     - 
   * - NTSC SD
     - 
   * - 480p
     - 
   * - 720 HD
     - default
   * - 1080 Full HD
     - 
   * - 2K
     - 
   * - 4K
     - 

:guilabel:`Components`

.. list-table::
   :width: 100%
   :widths: 25 75
   :class: table-simple

   * - None
     - 
   * - Y (Luminance)
     - 
   * - U (Chroma red-diff)
     - 
   * - YU
     - 
   * - V (Chroma blue-diff)
     - 
   * - YV
     - 
   * - UV
     - 
   * - All
     - Default
   * - Alpha
     - 

:guilabel:`Mode`

.. list-table::
   :width: 100%
   :widths: 25 75
   :class: table-wrap

   * - Mono
     - Draw hexadecimal pixel values with white color on black background (default)
   * - Color
     - Draw hexadecimal pixel values with input video pixel color on black background
   * - Color2
     - Draw hexadecimal pixel values on color background picked from input video, the text color is picked in such way so its always visible

:guilabel:`Format`

.. list-table::
   :width: 100%
   :widths: 25 75
   :class: table-wrap

   * - Hex
     - Hexadecimal notation (default)
   * - Dec
     - Decimal notation


----

.. [1] Doesn't seem to work


.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Icons used here (remove comment indent to enable them for this document)
   
   .. |linux| image:: /images/icons/linux.png
   :width: 14px
      :class: no-scaled-link

   .. |appimage| image:: /images/icons/kdenlive-appimage_3.svg
   :width: 14px
      :class: no-scaled-link

   .. |windows| image:: /images/icons/windows.png
   :width: 14px
      :class: no-scaled-link

   .. |apple| image:: /images/icons/apple.png
   :width: 14px
      :class: no-scaled-link