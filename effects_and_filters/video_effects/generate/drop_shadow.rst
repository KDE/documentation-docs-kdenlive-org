.. meta::

   :description: Kdenlive Video Effects - Drop Shadow
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, generate, drop shadow

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |dropshadow| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterDropshadow/" target="_blank">dropshadow</a>


Drop Shadow
===========

.. .. versionadded:: 24.12.2
  New XML file

.. figure:: /images/effects_and_compositions/effects-drop_shadow-2412.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-drop_shadow-2412

.. sidebar:: |kdenlive-show-video| Drop Shadow

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      mlt
   :**Source filter**:
      |dropshadow|
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

Creates a shadow effect for the clip 


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Blur Radius
     - Integer
     - The amount to blur the edge of the shadow
   * - X Offset
     - Integer
     - The relative horizontal position of the shadow. Positive values create a shadow to the right, negative values create a shadow top the left of the clip.
   * - Y Offset
     - Selection
     - The relative vertical position of the shadow. Positive values create a shadow below, negative values create a shadow above the clip.
   * - Color
     - Selection
     - The color of the shadow including alpha. The lower the value in :guilabel:`Alpha`, the more transparent the shadow color. A value of 255 makes the shadow a solid color. The :guilabel:`Blur Radius` is not affected by that.

