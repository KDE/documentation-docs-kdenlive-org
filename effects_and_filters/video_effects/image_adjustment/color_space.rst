.. meta::

   :description: Kdenlive Video Effects - Color Space
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, image adjustment, color space

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |color_space_descriptions| raw:: html

   <a href="https://www.kernel.org/doc/html/v4.9/media/uapi/v4l/pixfmt-007.html" target="_blank">Color Space Descriptions</a>


Color Space
===========

.. figure:: /images/effects_and_compositions/effects-color_space-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-color_space-2504.webp

.. sidebar:: |kdenlive-show-video| Color Space

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      colorspace
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter converts :term:`color space`, transfer characteristics or color primaries. Input video needs to have an even size.

The filter converts the transfer characteristics, color space and color primaries to the specified user values. The output value, if not specified, is set to a default value based on the :guilabel:`Color properties` property. If that property is also not specified, the filter will log an error. The output color range and format default to the same value as the input color range and format. The input transfer characteristics, color space, color primaries and color range should be set on the input data. If any of these are missing, the filter will log an error and no conversion will take place.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 40 10 50
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Color properties
     - Selection
     - Specify all color properties at once
   * - Output color space
     - Selection
     - Specifies output color space
   * - Output transfer characteristics
     - Selection
     - Specifies output transfer characteristics
   * - Output color primaries
     - Selection
     - Specifies output color primaries
   * - Output color range
     - Selection
     - Specifies output color range
   * - Output color format
     - Selection
     - Specifies output color format
   * - Fast conversion
     - Switch
     - Do a fast conversion, which skips gamma/primary correction. This will take significantly less CPU, but will be mathematically incorrect. To get output compatible with that produced by the :doc:`/effects_and_filters/video_effects/image_adjustment/color_matrix` filter, switch it on.
   * - Dithering mode
     - Selection
     - Specifies dithering mode
   * - Whitepoint adaption mode
     - Selection
     - Specifies whitepoint adaptation mode
   * - Override all input properties at once
     - Selection
     - 
   * - Override input color space
     - Selection
     - 
   * - Override input color primaries
     - Selection
     - 
   * - Override input transfer characteristics
     - Selection
     - 
   * - Override input color range
     - Selection
     - 

The following selection items are available:

:guilabel:`Color properties` :guilabel:`Override all input properties at once`

.. list-table::
   :width: 100%
   :widths: 50 50
   :class: table-wrap

   * - BT.709
     - Default
   * - BT.470M
     - 
   * - BT.470BG
     - 
   * - BT601-6 525
     - 
   * - BT601-6 625
     - 
   * - SMPTE-170M
     - 
   * - SMPTE-240M
     - 
   * - BT.2020
     - 


:guilabel:`Output color space` :guilabel:`Override input color space` 

.. list-table::
   :width: 100%
   :widths: 50 50
   :class: table-wrap

   * - BT.709
     - Default
   * - FCC
     - 
   * - BT.470BG (BT.470BG or BT.601-6 625)
     - 
   * - SMPTE 170M (SMPTE 170M or BT.601-6 525)
     - 
   * - SMPTE 240M
     - 
   * - YCgCo
     - 
   * - BT.2020 non-constant luma
     - 


:guilabel:`Output transfer characteristics` :guilabel:`Override input transfer characteristics`

.. list-table::
   :width: 100%
   :widths: 50 50
   :class: table-wrap

   * - BT.709
     - Default
   * - BT.470M
     - 
   * - BT.470BG
     - 
   * - Constant Gamma of 2.2
     - 
   * - Constant Gamma of 2.8
     - 
   * - SMPTE 170M (SMPTE 170M, BT.601-6 525 or BT.601-6 525)
     - 
   * - SMPTE 240M
     - 
   * - SRGB
     - 
   * - IEC 61966-2-1
     - 
   * - IEC 61966-2-4
     - 
   * - xvYCC
     - extended-gamut YCbCr
   * - BT.2020 for 10-bits constant
     - 
   * - BT.2020 for 12-bits constant
     - 


:guilabel:`Output color primaries` :guilabel:`Override input color primaries`

.. list-table::
   :width: 100%
   :widths: 50 50
   :class: table-wrap

   * - BT.709
     - Default
   * - BT.470M
     - 
   * - BT.470BG (BT.470BG or BT.601-6 625)
     - 
   * - SMPTE 170M (SMPTE 170M or BT.601-6 525)
     - 
   * - SMPTE 240M
     - 
   * - Film
     - 
   * - BT.2020
     - 
   * - SMPTE 431
     - 
   * - SMPTE 432
     - 
   * - JEDEC-PT22 phosphors
     - 


:guilabel:`Output color range`

.. list-table::
   :width: 100%
   :widths: 50 50
   :class: table-wrap

   * - TV (restricted range)
     - 
   * - MPEG (restricted range)
     - 
   * - PC (full range)
     - Default
   * - JPEG (full range)
     - 


:guilabel:`Output color format`

.. list-table::
   :width: 100%
   :widths: 50 50
   :class: table-wrap

   * - YUV 4:2:0 planar 8-bits / 10-bits / 12-bits
     - Default is 8-bits
   * - YUV 4:2:2 planar 8-bits / 10-bits / 12-bits
     - 
   * - YUV 4:4:4 planar 8-bits / 10-bits / 12-bits
     - 


:guilabel:`Dithering mode`

.. list-table::
   :width: 100%
   :widths: 50 50
   :class: table-wrap

   * - No dithering
     - Default
   * - Floyd-Steinberg dithering
     - 


:guilabel:`Whitepoint adaption mode`

.. list-table::
   :width: 100%
   :widths: 50 50
   :class: table-wrap

   * - Identity whitepoint adaptation (no whitepoint adaptation)
     - Default
   * - Bradford whitepoint adaptation
     - 
   * - von Kries whitepoint adaptation
     - 


For the technical inclined there is a list of detailed |color_space_descriptions| available in the Linux Kernel documentation.


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