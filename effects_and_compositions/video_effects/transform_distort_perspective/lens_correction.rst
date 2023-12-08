.. meta::

   :description: Kdenlive Video Effects - Lens Correction
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, lens correction

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |avfilter.lc| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-lenscorrection/" target="_blank">avfilter.lenscorrection</a>

.. |frei0r.lc| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-lenscorrection/" target="_blank">frei0r.lenscorrection</a>


Lens Correction
===============

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-lens_correction.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-lens_correction

.. sidebar:: |kdenlive-show-video| Lens Correction

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      lenscorrection
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter corrects radial lens distortion. It can be used to create an "old TV set or monitor" curving effect.

See :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/lens_correction_keyframe` if you need to use keyframes.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Focal point relative-X coord
     - 
     - Set relative center X
   * - Focal point relative-Y coord
     - 
     - Set relative center Y
   * - Quadratic correction coeff.
     - 
     - Set quadratic distortion factor
   * - DoubleQuadratic correction coeff.
     - 
     - Set double quadratic distortion factor


.. note:: 
   This effect may produce different results than :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/lens_correction_keyframe` although the name may suggest the only difference is the keyframes. **Lens Correction** uses |avfilter.lc|, whereas :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/lens_correction_keyframe` uses |frei0r.lc|.


.. https://youtu.be/axQdm482Uto

.. https://youtu.be/cEwZzNRiVks
