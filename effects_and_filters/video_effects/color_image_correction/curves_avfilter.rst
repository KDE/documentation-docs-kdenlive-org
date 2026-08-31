.. meta::

   :description: Kdenlive Video Effects - Curves (avfilter)
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, curves, avfilter

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0

.. ..versionadded: 26.08


Curves (avfilter)
=================

.. figure:: /images/effects_and_compositions/effects-curves_avfilter-2608.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-show-video| Curves (avfilter)

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      curves
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter adjusts shadows, midtones and highlights of an image using curves. It is similar to the :doc:`/effects_and_filters/video_effects/color_image_correction/color_levels` or :doc:`/effects_and_filters/video_effects/color_image_correction/levels` effects but with the option to create additional points along the curve allowing for pinpoint accuracy when adjusting brightness values.


.. rubric:: Tabs

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - Tab
     - Description
   * - All
     - The curve applies to all color channels equally
   * - R
     - The curve applies to the red channel only
   * - G
     - The curve applies to the green channel only
   * - B
     - The curve applies to the blue channel only

.. rst-class:: clear-both

.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - Parameter
     - Description
   * - In
     - The X coordinate of the selected point. Defines the luma input value. Use this input field for very fine adjustments of the curve.
   * - Out
     - The Y coordinate of the selected point. Defines the luma output value. Use this input field for very fine adjustments of the curve.
   * - Reset curve
     - Resets the curve in the selected tab to a straight line

.. rst-class:: clear-both

You can adjust the curve by dragging any point of the curve. This will create a new handle (indicated by a red dot) that can be adjusted any time later.

Existing points can be deleted with :kbd:`RMB` |input-mouse-click-right|

.. rubric:: Example

.. figure:: /images/effects_and_compositions/effects-curves_avfilter_example-2608.webp

  Curves (avfilter) with all channels adjusted differently



.. hint:: 
  It is recommended to use this effect while in Color layout as this comes with :ref:`RGB Parade <view-rgb_parade>` and :ref:`view-histogram` already switched on. If you want to use the effect while in Editing or Effects layout, turn on the Histogram :term:`widget` with :menuselection:`Menu --> View --> Histogram`.

.. hint::
  Use the split-screen function of the effect panel to compare the effect with the original. You can enable it with |view-split-left-right|. See :ref:`effect_stack_functions`.

.. seealso::
  :doc:`/effects_and_filters/video_effects/color_image_correction/curves_frei0r` does the same thing but only allows one channel to be adjusted.

.. seealso:: 
  The :doc:`Bezier Curves </effects_and_filters/video_effects/color_image_correction/bezier_curves>` effect does the same but has the ability to adjust the steepness/flatness of the curves.
  