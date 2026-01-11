.. meta::

   :description: Kdenlive Video Effects - Lens Correction (frei0r)
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, lens correction, frei0r

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |avfilter.lc| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-lenscorrection/" target="_blank">avfilter.lenscorrection</a>

.. |frei0r.lc| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-lenscorrection/" target="_blank">frei0r.lenscorrection</a>


Lens Correction (frei0r)
========================

.. figure:: /images/effects_and_compositions/effects-lens_correction_frei0r-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Lens Correction

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      lenscorrection
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No
   :**Color depth**:
      8bit
   :**Tutorial**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter allows compensation of lens distortion. It can be used to create an "old TV set or monitor" curving effect.

See also :doc:`/effects_and_filters/video_effects/transform_distort_perspective/lens_correction_avfilter` if you need to specify a color for unmapped pixels or need to render in 10bit color.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Horizontal Center
     - Float
     - Set relative center X
   * - Vertical Center
     - Float
     - Set relative center Y
   * - Center Correction
     - Float
     - Set correction near the center
   * - Edges Correction
     - Float
     - Set correction near the edges
   * - Brightness
     - Float
     - Set brightness increase


.. note:: 
   This effect may produce different results than :doc:`/effects_and_filters/video_effects/transform_distort_perspective/lens_correction_avfilter` although the name may suggest the only difference is the effects library. **Lens Correction (frei0r)** uses |frei0r.lc|, whereas :doc:`/effects_and_filters/video_effects/transform_distort_perspective/lens_correction_avfilter` uses |avfilter.lc|. There are different options available in each effect.


.. https://youtu.be/axQdm482Uto

.. https://youtu.be/cEwZzNRiVks
