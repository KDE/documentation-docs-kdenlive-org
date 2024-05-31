.. meta::

   :description: Kdenlive Video Effects - Lens Correction (keyframable)
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, lens correction keyframable

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |avfilter.lc| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-lenscorrection/" target="_blank">avfilter.lenscorrection</a>

.. |frei0r.lc| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-lenscorrection/" target="_blank">frei0r.lenscorrection</a>


Lens Correction (keyframable)
=============================

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-lens_correction_keyframable.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-lens_correction_keyframable

.. sidebar:: |kdenlive-show-video| Lens Correction (keyframable)

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

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter allows compensation of lens distortion. It can be used to create an "old TV set or monitor" curving effect.

See :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/lens_correction` if you do not need to use keyframes.


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
     - Integer
     - Set relative center X
   * - Vertical Center
     - Integer
     - Set relative center Y
   * - Center Correction
     - Integer
     - Set correction near the center
   * - Edges Correction
     - Integer
     - Set correction near the edges
   * - Brightness
     - Integer
     - Set brightness increase


.. note:: 
   This effect may produce different results than :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/lens_correction` although the name may suggest the only difference is the keyframes. **Lens Correction (keyframable)** uses |frei0r.lc|, whereas :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/lens_correction` uses |avfilter.lc|.


.. https://youtu.be/axQdm482Uto

.. https://youtu.be/cEwZzNRiVks
