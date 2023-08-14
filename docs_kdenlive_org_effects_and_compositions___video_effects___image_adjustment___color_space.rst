.. meta::

   :description: Do your first steps with Kdenlive video editor, using color space effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, image adjustment, color space

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |color_space_descriptions| raw:: html

   <a href="https://www.kernel.org/doc/html/v4.9/media/uapi/v4l/pixfmt-007.html" target="_blank">Color Space Descriptions</a>


.. _effects-color_space:

Color Space
===========

This effect/filter converts :term:`color space`, transfer characteristics or color primaries. Input video needs to have an even size.

The filter converts the transfer characteristics, color space and color primaries to the specified user values. The output value, if not specified, is set to a default value based on the :guilabel:`Color properties` property. If that property is also not specified, the filter will log an error. The output color range and format default to the same value as the input color range and format. The input transfer characteristics, color space, color primaries and color range should be set on the input data. If any of these are missing, the filter will log an error and no conversion will take place.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-color_space.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-color_space

   Color Space effect

* **Color properties** - Specify all color properties at once. Options are **BT.709**, **BT.470M**, **BT.470BG**, **BT601-6 525**, **BT601-6 625**, **SMPTE-170M**, **SMPTE-240M**, and **BT.2020**.

* **Output Color Space** - Specifies output color space. Options are **BT.709**, **FCC**, **BT.470BG** (BT.470BG or BT.601-6 625), **SMPTE-170M** (SMPTE-170M or BT.601-6 525), **SMPTE-240M**, **YCgCo**, and **BT.2020 non-constant luma**.

* **Output transfer characteristics** - Specifies output transfer characteristics. Options are **BT.709**, **BT.470M**, **BT.470BG**, **Constant Gamma of 2.2**, **Constant Gamma of 2.8**, **SMPTE-170M** (SMPTE-170M, BT.601-6 525 or BT.601-6 525), **SMPTE-240M**, **SRGB**, **iec61966-2-1**, **iec61966-2-4**, **xvycc**, **BT.2020 for 10-bits constant** and **BT.2020 for 12-bits constant**.

* **Output Color Primaries** - Specifies output color primaries. Options are **BT.709**, **BT.470M**, **BT.470BG** (BT.470BG or BT.601-6 625), **SMPTE-170M** (SMPTE-170M or BT.601-6 525), **SMPTE-240M**, **Film**, **BT.2020**, **SMPTE-431**, **SMPTE-432**, and **JEDEC-PT22 phosphors**.

* **Output Color Range** - Specifies output color range. Options are **TV (restricted range)**, **MPEG (restricted range)**, **PC (FULLrange)**, and **JPEG (FULL range)**.

* **Output Color Format** - Specifies output color format. Options are **YUV 4:2:0 planar 8-bits / 10-bits / 12-bits**, **YUV 4:2:2 planar 8-bits / 10-bits / 12-bits**, and **YUV 4:4:4 planar 8-bits / 10-bits / 12-bits**

* **Fast Conversion** - Do a fast conversion, which skips gamma/primary correction. This will take significantly less CPU, but will be mathematically incorrect. To get output compatible with that produced by the :ref:`effects-color_matrix` filter, switch it on.

* **Dithering Mode** - Specifies dithering mode **No dithering** or **Floyd-Steinberg dithering**

* **Whitepoint adaption mode** - Specifies whitepoint adaptation mode **Identity whitepoint adaptation (no whitepointadaptation)**, **Bradford whitepoint adaptation** or **von Kries whitepoint adaptation**

* **Override all input properties at once** - Same options as :guilabel:`Color properties`

* **Override input colorspace** - Same options as :guilabel:`Output color space`

* **Override input color primaries** - Same options as :guilabel:`Output color primaries`

* **Override input transfer characteristics** - Same options as :guilabel:`Output transfer characteristics`

* **Override input color range** - Same options as :guilabel:`Output color range`

For the technical inclined there is a list of detailed |color_space_descriptions| available in the Linux Kernel documentation.
