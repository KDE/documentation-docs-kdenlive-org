.. meta::

   :description: Kdenlive Video Effects - CIE Scope 
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, utility, ciescope, scope, cie

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |cie_ntsc| raw:: html

   <a href="https://en.wikipedia.org/wiki/NTSC#Colorimetry" target="_blank">this page</a>



CIE Scope
=========

.. figure:: /images/effects_and_compositions/effects-cie_scope-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-cie_scope-2504.webp

.. sidebar:: |kdenlive-show-video| CIE Scope

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      ciescope
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

This effect/filter displays a :abbr:`CIE(Commission internationale de l'éclairage, French for International Commission on Illumination)` color diagram with overlaid input pixels.

.. tip:: The effect uses the pixel format of the clip it is applied on in compositing. By default, CIE Scope just displays the scope, so if you want to overlay it on the clip itself, you need to put the clip in the track below. If that clip does not have an alpha channel, the scope will not overlay but obscure the clip below. You can add an :doc:`/effects_and_filters/video_effects/alpha_mask_keying/alpha_shapes` effect to the clip, set the operations mode to :guilabel:`Min`, and adjust the size of the rectangle to the scope dimensions and thus get the CIE Scope to overlay the clip.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Color System
     - Selection
     - Set color system to use
   * - CIE System
     - Selection
     - Set CIE system to use
   * - Gamuts to Draw
     - Selection
     - Set what gamuts to draw
   * - Size
     - Integer
     - Set CIE Scope size, by default set to 512.
   * - Intensity
     - Float
     - Set intensity used to map input pixel values to CIE diagram
   * - Contrast
     - Float
     - Set contrast used to draw tongue colors that are out of active color system gamut
   * - Display Correct Gamma
     - Switch
     - Correct gamma displayed on scope, by default enabled
   * - Show White Point
     - Switch
     - Show white point on CIE diagram, by default disabled
   * - Input Gamma
     - Float
     - Set input gamma. Used only with xyY input color space.
   * - Fill with CIE Colors
     - Switch
     - Fill with CIE colors, by default enabled.

The following selection items are available:

:guilabel:`Color System`\ [1]_, :guilabel:`Gamuts to Draw`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - NTSC
     - American standard for color TV. For the color space relevance, refer to |cie_ntsc| in Wikipedia.
   * - BT.470M
     - Same as NTSC
   * - EBU
     - Color space used by the European Broadcasting Union (basically BT.601)
   * - BT.470BG
     - 
   * - SMPTE
     - Color space used by the Society of Motion Picture and Television Engineers (SMPTE)
   * - BT.240M
     -
   * - Apple
     - Color space as defined by Apple RGB\ [1]_
   * - Wide RGB
     - Wide Gamut RGB\ [2]_ as defined by Adobe
   * - CIE 1931
     - Color space as defined by CIE\ [3]_
   * - HD TV
     - Using the YCbCr color model (Rec. 709)
   * - Rec. 709
     - Same as HD TV
   * - UHD TV
     - Using the YCbCr color model (Rec. 2020)
   * - Rec. 2020
     - Same as UHD TV
   * - DCI-P3
     - Color space defined by :abbr:`DCI(Digital Cinema Initiative)`\ [4]_

:guilabel:`CIE System`\ [1]_

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - xyY
     - Using the CIE xyY\ [5]_ color space (derived from CIE XYZ).
   * - UCS
     - CIE 1960 UCS\ [6]_ color space
   * - LUV
     - CIELUV\ [7]_ (abbreviation for CIE 1976 L*, u*, v)


.. rubric:: Examples

.. figure:: /images/effects_and_compositions/effects-cie_scope_example_1-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-cie_scope_example_1-2504.webp

   CIE Scope Example 1 - Default settings

This shows the CIE Scope effect with the default settings. Depending on your source material the pixel distribution will look differently.

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/effects-cie_scope_example_2-2504.webp
      :width: 365px
      :figwidth: 365px
      :align: left
      :alt: effects-cie_scope_example_2-2504.webp

      CIE Scope Example 2

   This shows the CIE Scope effect with the following settings:

   .. container::

      | :guilabel:`Color System`: CIE 1931
      | :guilabel:`CIE System`: UCS
      | :guilabel:`Gamuts to Draw`: SMPTE

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/effects-cie_scope_example_3-2504.webp
      :width: 365px
      :figwidth: 365px
      :align: left
      :alt: effects-cie_scope_example_3-2504.webp

      CIE Scope Example 3

   This shows the CIE Scope effect with the following settings:
      
      .. container::

         | :guilabel:`Color System`: BT.470M
         | :guilabel:`CIE System`: LUV
         | :guilabel:`Gamuts to Draw`: Apple

.. rst-class:: clear-both


----

.. |rgb_color_space_models| raw:: html

   <a href="https://en.wikipedia.org/wiki/RGB_color_spaces#Color_space_specifications_employing_the_RGB_color_model" target="_blank">RGB Color Space Models</a>

.. |wide_gamut_rgb| raw:: html

   <a href="https://en.wikipedia.org/wiki/Wide-gamut_RGB_color_space" target="_blank">https://en.wikipedia.org/wiki/Wide-gamut_RGB_color_space</a>

.. |cie_1931| raw:: html

   <a href="https://en.wikipedia.org/wiki/CIE_1931_color_space" target="_blank">https://en.wikipedia.org/wiki/CIE_1931_color_space</a>

.. |dci_p3| raw:: html

   <a href="https://en.wikipedia.org/wiki/DCI-P3" target="_blank">https://en.wikipedia.org/wiki/DCI-P3</a>

.. |cie_xyy| raw:: html

   <a href="https://en.wikipedia.org/wiki/CIE_1931_color_space#CIE_xyY_color_space" target="_blank">https://en.wikipedia.org/wiki/CIE_1931_color_space#CIE_xyY_color_space</a>

.. |cie_ucs| raw:: html

   <a href="https://en.wikipedia.org/wiki/CIE_1960_color_space" target="_blank">https://en.wikipedia.org/wiki/CIE_1960_color_space</a>

.. |cie_luv| raw:: html

   <a href="https://en.wikipedia.org/wiki/CIELUV" target="_blank">https://en.wikipedia.org/wiki/CIELUV</a>


.. [1] For more information about the color space models, refer to the |rgb_color_space_models| page on Wikipedia

.. [2] |wide_gamut_rgb|

.. [3] |cie_1931|

.. [4] |dci_p3|

.. [5] |cie_xyy|

.. [6] |cie_ucs|

.. [7] |cie_luv|


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