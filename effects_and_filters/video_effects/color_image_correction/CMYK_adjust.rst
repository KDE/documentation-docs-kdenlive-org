.. meta::

   :description: Kdenlive Video Effects - CMYK Adjust
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, CMYK adjust

   :authors: - Bernd Jordan

   :license: Creative Commons License SA 4.0


CMYK Adjust
===========

.. figure:: /images/effects_and_compositions/effects-cmyk_adjust-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-show-video| CMYK Adjust

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      selectivecolor
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect applies CMYK\ [1]_ adjustments to specific color ranges\ [2]_. The adjustment range is defined by the "purity" of the color (i.e. how saturated it already is).


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 10 65
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Correction Method
     - Selection
     - Select the color correction method
   * - Reds
     - Float
     - Adjustments for red pixels (pixels where the red component is the maximum)
   * - Yellows
     - Float
     - Adjustments for yellow pixels (pixels where the blue component is the minimum)
   * - Greens
     - Float
     - Adjustments for green pixels (pixels where the green component is the maximum)
   * - Cyans
     - Float
     - Adjustments for cyan pixels (pixels where the red component is the minimum)
   * - Blues
     - Float
     - Adjustments for blue pixels (pixels where the blue component is the maximum)
   * - Magentas
     - Float
     - Adjustments for magenta pixels (pixels where the green component is the minimum)
   * - Whites
     - Float
     - Adjustments for white pixels (pixels where all component are greater then 128)
   * - Neutrals
     - Float
     - Adjustments for all pixels except pure black and pure white
   * - Blacks
     - Float
     - Adjustments for black pixels (pixels where all component are less then 128)

The following selection items are available:

:guilabel:`Correction Method`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Absolute
     - Specified adjustments are applied "as-is" (default)
   * - Relative
     - Specified adjustments are relative to the original component value


.. rubric:: Notes

.. seealso:: 
  :doc:`/tips_and_tricks/how-tos/cmyk_adjust` how-to in the :doc:`Tips&Tricks </tips_and_tricks/index>` section.


----

.. [1] CMYK stands for Cyan, Magenta, Yellow, Black

.. [2] Color ranges are "reds", "yellows", "greens", etc.
