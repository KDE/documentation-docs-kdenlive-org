.. meta::

   :description: Kdenlive Video Effects - Bezier Curves
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, bezier curves

   :authors: - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |frei0r_curves| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-curves/" target="_blank">curves</a>

.. |thediveo_grading| raw:: html

   <a href="http://thediveo-e.blogspot.de/2013/10/grading-of-hero-3-above-waterline.html" target="_blank">TheDiveO</a>


Bezier Curves
=============

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-bezier_curves.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-bezier_curves

.. sidebar:: |kdenlive-show-video| Bezier Curves

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      frei0r
   :**Source filter**:
      |frei0r_curves|
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect is used to adjust the color levels similar to the :doc:`/effects_and_compositions/video_effects/color_image_correction/3_point_balance` but with finer control. Although the effect defaults to the RGB channel, it is mostly used with the :term:`Luma` channel. See also the :doc:`/effects_and_compositions/video_effects/color_image_correction/curves` effect that does the same thing but does not have the curve handles.

Note the extended handles on the red dot in the middle with which you can adjust the steepness of the curve leading to and leaving the point.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Channel
     - Selection
     - Sets the channel to operate on
   * - Luma formula
     - Selection
     - Defines the :term:`color space` to operate in

The following selection items are available:

:guilabel:`Channel`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - | RGB
       | Red
       | Green
       | Blue
       | Alpha
       | Luma
       | Hue
       | Saturation
     - Default is RGB (all color channels)

:guilabel:`Luma formula`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Rec. 601
     - 
   * - Rec. 709
     - (default)

.. rst-class:: clear-both


.. rubric:: Notes
   
See |thediveo_grading| blog for an example of how to use this effect to color grade clips.
