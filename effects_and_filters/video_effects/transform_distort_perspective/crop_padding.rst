.. meta::

   :description: Kdenlive Video Effects - Crop by Padding
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, crop by padding

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             - Eugen Mohr

   :license: Creative Commons License SA 4.0


Crop by Padding
===============

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-crop_by_padding.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-crop_by_padding

.. sidebar:: |kdenlive-show-video| Crop by Padding

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      qtcrop
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter crops the image to a rounded rectangle or circle by padding the edges with a specified color. It can be :ref:`direct controlled on the monitor <ui-monitors_effect_direct_control>`.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Circle
     - Switch
     - If switched on, the :guilabel:`Radius` parameter creates a circular crop. Otherwise a rectangle is used. Default is **off**.
   * - Radius
     - Float
     - Amount of circular or rectangle rounding
   * - Padding Color
     - Picker
     - The color to be used for padding. Can be alpha.


.. rubric:: Notes

The parameters **X**, **Y**, **W**, **H**, and **Size** can be used to move and/or scale the rectangle or circle within the frame in order to crop a specific portion of the image.
