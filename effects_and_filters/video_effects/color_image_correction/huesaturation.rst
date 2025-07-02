.. meta::

   :description: Kdenlive Video Effects - Huesaturation
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, misc, miscellaneous, huesaturation

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Hue Saturation Intensity
========================

.. figure:: /images/effects_and_compositions/effects-hue_saturation_intensity-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-hue_saturation_intensity-2504.webp

.. sidebar:: |kdenlive-show-video| Hue Saturation Intensity

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      avfilter
   :**Source filter**:
      huesaturation
   :**Available**:
      |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      Yes\ [1]_ |tools-report-bug|
   :**Color depth**:
      10bit |color-management|
   :**Tutorial**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter applies hue-saturation-intensity adjustments to the input video stream.

This filter operates in :abbr:`RGB (Red, Green, Blue)` :term:`color space`.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Colors to Adjust
     - Selection
     - Set which primary and complementary colors are going to be adjusted
   * - Preserve lightness
     - Switch
     - Adjusting hues can change lightness\ [1]_ from original RGB triplet. When enabled, lightness is kept at same value.
   * - Hue shift
     - Degrees
     - Set the :term:`hue` shift in degrees to apply
   * - Saturation shift
     - Float
     - Set the :term:`saturation` shift. Allowed range is from -1.000 to 1.000. Default is 0.000.
   * - Intensity shift
     - Float
     - Set the intensity shift. Allowed range is from -1.000 to 1.000. Default is 0.000.
   * - Strength
     - Float
     - Set the strength of filter. Allowed range is from 0.0 to 100.0. Default is 1.0.
   * - Red / Green / Blue weight
     - Float
     - Set weight for each RGB component. This is used in saturation and lightness\ [1]_ processing.

The following selection items are available:

:guilabel:`Colors to Adjust`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Reds
     - Default
   * - Yellows
     - 
   * - Greens
     - 
   * - Cyans
     - 
   * - Blues
     - 
   * - Magentas
     - 
   * - All colors
     - 


----

.. [1] Lightness processing not yet implemented
