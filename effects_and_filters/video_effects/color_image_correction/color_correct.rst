.. meta::

   :description: Kdenlive Video Effects - Color Correct
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, color correct

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Color Correct
=============

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-color_correct.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-color_correct

.. sidebar:: |kdenlive-show-video| Color Correct

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      avfilter
   :**Source filter**:
      colorcorrect
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter adjusts the color white balance selectively for blacks and whites. This filter operates in :term:`YUV` color space.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 10 65
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Analyze mode
     - Selection
     - If set to anything other than **manual** it will analyze every frame and use derived parameters for filtering the output frame.
   * - Red shadow spot
     - Float
     - Set the red shadow spot. Default is 0.0. Allowed range is from -1.0 to 1.0.
   * - Blue shadow spot
     - Float
     - Set the blue shadow spot. Default is 0.0. Allowed range is from -1.0 to 1.0.
   * - Red highlight spot
     - Float
     - Set the red highlight spot. Default is 0.0. Allowed range is from -1.0 to 1.0.
   * - Blue highlight spot
     - Float
     - Set the blue highlight spot. Default is 0.0. Allowed range is from -1.0 to 1.0.
   * - Saturation
     - Float
     - Set the amount of :term:`saturation`. Default value is 1.0. Allowed range is from -3.0 to 3.0.

The following selection items are available:

:guilabel:`Analyze mode`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Manual
     - (default)
   * - Average
     - 
   * - Minmax
     - 
   * - Median
     - 

