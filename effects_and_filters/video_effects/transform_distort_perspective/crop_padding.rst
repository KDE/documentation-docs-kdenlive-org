.. meta::

   :description: Kdenlive Video Effects - Crop by Padding
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, crop by padding

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             - Eugen Mohr

   :license: Creative Commons License SA 4.0


Crop by Padding
===============

.. figure:: /images/effects_and_compositions/effects-crop_by_padding-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-crop_by_padding-2504.webp

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
   :**Color depth**:
      8bit
   :**Tutorial**:
      :ref:`Yes<tutorials-crop_padding>` |view-presentation|

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter crops the image to a rounded rectangle or circle by padding the edges with a specified color. It can be :ref:`controlled directly on the monitor <ui-monitors_effect_direct_control>`.

.. tip:: This effect can be used for picture-in-picture effects. Very effective when used in combination with the :doc:`/effects_and_filters/video_effects/generate/drop_shadow` effect. See the tutorial.


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

The parameters :guilabel:`Position X`, :guilabel:`Y`, :guilabel:`Size W`, :guilabel:`H`, :guilabel:`Scale` can be used to move and/or scale the rectangle or circle within the frame in order to crop a specific portion of the image.
