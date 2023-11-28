.. meta::

   :description: Kdenlive Video Effects - vignette_effect effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, generate, vignette_effect

.. metadata-placeholders

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Vignette Effect
===============

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-vignette_effect.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-vignette_effect

.. sidebar:: |kdenlive-show-video| Vignette Effect

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      vignette
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter creates an adjustable vignette. It is similar to the :ref:`effects-vignette` effect but lacks the adjustment of the aspect ratio.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - use cos instead of linear
     - Switch
     - If selected makes the fall-off area appear denser by applying a cosine curve instead of a linear function
   * - smooth
     - Integer
     - Set the size of the fall-off area. Higher values make the center darker and the edges lighter. If **smooth** is set to zero, the vignette is like a black matte with a distinct edge.
   * - radius
     - Integer
     - Set the radius of the vignette
   * - x / y
     - Integer
     - Define the X and Y coordinates for the center point of the vignette (X = 0, Y = 0 defines the top-left corner of the screen)
   * - opacity
     - Integer
     - Set the :term:`opacity` of the black parts of the vignette
