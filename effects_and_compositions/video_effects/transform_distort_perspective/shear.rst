.. meta::

   :description: Kdenlive Video Effects - Shear
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, shear

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |link| raw:: html

   <a href="link_URI" target="_blank">link_text</a>


Shear
=====

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-shear.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-shear

.. sidebar:: |kdenlive-show-video| Shear

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      avfilter
   :**Source filter**:
      shear
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      Yes (see warning)

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter applies a shear transformation to the clip.

The effect has keyframes but only for the :guilabel:`Background fill color`.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - X shear factor
     - Integer
     - Set the shear factor. Range is from -2 to 2.
   * - Y shear factor
     - Integer
     - Set the shear factor. Range is from -2 to 2.
   * - Interpolation mode
     - Selection
     - Set the interpolation mode
   * - Background fill color
     - Picker
     - Set the background fill color if the shear reveals the background. Default is **black**

The following selection items are available:

:guilabel:`Interpolation mode`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Nearest
     - default
   * - Bilinear
     - 


.. warning:: 
   As of this writing and version 23.04 the shear parameters are integer values, not float, hence the very much limited use of the effect. A bug report has been created. Until this is fixed use the :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/rotate_and_shear` effect.
