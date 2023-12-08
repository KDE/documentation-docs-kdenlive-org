.. meta::

   :description: Kdenlive Video Effects - Stereoscopic 3D 
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, VR360 and 3D, stereoscopic 3D

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Stereoscopic 3D
===============

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-stereoscopic_3d.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-stereoscopic_3d

.. sidebar:: |kdenlive-show-video| Stereoscopic 3D

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      stereo3d
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter converts between different stereoscopic image formats.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 30 10 60
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Input format
     - Selection
     - Set the input format
   * - Output format
     - Selection
     - Set the output format


The following selection items are available:

:guilabel:`Input format`

.. list-table::
   :width: 100%
   :widths: 30 70
   :header-rows: 1
   :class: table-wrap

   * - Value
     - Description
   * - **side by side parallel** \*)
     - Source images are side by side parallel with left eye left and right eye right
   * - **side by side crosseye**
     - Source images are side by side crosseye with right eye left and left eye right
   * - **above-below (left above)**
     - Source images are stacked with left eye above and right eye below
   * - **above-below (right above)**
     - Source images are stacked with right eye above and left eye below
   * - **interleaved rows (left top)**
     - Source images are interleaved rows with left eye has top row, and right eye starts on next row
   * - **interleaved rows (right top)**
     - Source images are interleaved rows with right eye has top row, and left eye starts on next row
   * - **interleaved columns left eye first**
     - Source images are interleaved columns with left eye first, right eye next
   * - **interleaved columns right eye first**
     - Source images are interleaved columns with right eye first, left eye next

\*) default


:guilabel:`Output format`

.. list-table::
   :width: 100%
   :widths: 30 70
   :header-rows: 1
   :class: table-wrap

   * - Value
     - Description
   * - **side by side parallel**
     - left eye left, right eye right
   * - **side by side crosseye**
     - right eye left, left eye right
   * - **above-below left top**
     - left eye above, right eye below
   * - **above-below right top**
     - right eye above, left eye below
   * - **interleaved rows (left top)**
     - left eye has top row, right eye starts on next row
   * - **interleaved rows (right top)**
     - right eye has top row, left eye starts on next row
   * - **anaglyph red/blue gray**
     - red filter on left eye, blue filter on right eye
   * - **anaglyph red/green gray**
     - red filter on left eye, green filter on right eye
   * - **anaglyph red/cyan gray**
     - red filter on left eye, cyan filter on right eye
   * - **anaglyph red/cyan half colored**
     - red filter on left eye, cyan filter on right eye
   * - **anaglyph red/cyan color**
     - red filter on left eye, cyan filter on right eye
   * - **anaglyph red/cyan dubois** \*)
     - red filter on left eye, cyan filter on right eye, optimized with the least squares projection of dubois
   * - **anaglyph green/magenta gray**
     - green filter on left eye, magenta filter on right eye
   * - **anaglyph green/magenta half colored**
     - green filter on left eye, magenta filter on right eye
   * - **anaglyph green/magenta colored**
     - green filter on left eye, magenta filter on right eye
   * - **anaglyph green/magenta dubois**
     - green filter on left eye, magenta filter on right eye, optimized with the least squares projection of dubois
   * - **anaglyph yellow/blue gray**
     - yellow filter on left eye, blue filter on right eye
   * - **anaglyph yellow/blue half colored**
     - yellow filter on left eye, blue filter on right eye
   * - **anaglyph yellow/blue colored**
     - yellow filter on left eye, blue filter on right eye
   * - **anaglyph yellow/blue dubois**
     - yellow filter on left eye, blue filter on right eye, optimized with the least squares projection of dubois
   * - **mono output left**
     - left eye only
   * - **mono output right**
     - right eye only
   * - **checkerboard left eye first**
     -
   * - **checkerboard right eye first**
     -
   * - **interleaved columns left eye first**
     -
   * - **interleaved columns right eye first**
     -
   * - **HDMI frame pack**
     -

\*) default
