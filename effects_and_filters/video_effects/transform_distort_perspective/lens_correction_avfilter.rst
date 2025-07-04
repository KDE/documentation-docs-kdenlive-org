.. meta::

   :description: Kdenlive Video Effects - Lens Correction (avfilter)
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, lens correction, avfilter, 10bit

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |avfilter.lc| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterAvfilter-lenscorrection/" target="_blank">avfilter.lenscorrection</a>

.. |frei0r.lc| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-lenscorrection/" target="_blank">frei0r.lenscorrection</a>


Lens Correction (avfilter)
==========================

.. figure:: /images/effects_and_compositions/effects-lens_correction_avfilter-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-lens_correction_avfilter-2504.webp

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
   :**Color depth**:
      10bit |color-management|
   :**Tutorial**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter corrects radial lens distortion. It can be used to create an "old TV set or monitor" curving effect.

See :doc:`/effects_and_filters/video_effects/transform_distort_perspective/lens_correction_frei0r` if you need to adjust brightness.


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
     - Float
     - Set relative center X
   * - Focal point relative-Y coord
     - Float
     - Set relative center Y
   * - Quadratic correction coeff.
     - Float
     - Set quadratic distortion factor
   * - DoubleQuadratic correction coeff.
     - Float
     - Set double quadratic distortion factor


.. note:: 
   This effect may produce different results than :doc:`/effects_and_filters/video_effects/transform_distort_perspective/lens_correction_frei0r` although the name may suggest the only difference is the effects library. **Lens Correction (frei0r)** uses |frei0r.lc|, whereas :doc:`/effects_and_filters/video_effects/transform_distort_perspective/lens_correction_frei0r` uses |avfilter.lc|. There are different options available in each effect.


.. https://youtu.be/axQdm482Uto

.. https://youtu.be/cEwZzNRiVks


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