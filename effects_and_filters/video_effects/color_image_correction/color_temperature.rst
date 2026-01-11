.. meta::

   :description: Kdenlive Video Effects - Color Temperature
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, color temperature

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Color Temperature
=================

.. figure:: /images/effects_and_compositions/effects-color_temperature-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-show-video| Color Temperature

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      avfilter
   :**Source filter**:
      colortemperature
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter adjusts the color :term:`temperature` in video or images to simulate an ambient color temperature.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 10 65
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Temperature
     - Float
     - Set the temperature in :term:`Kelvin<kelvin>`. Allowed values are from 1,000 to 40,000, default is 6,500K
   * - Mix
     - Float
     - Set the mix with filtered output. Allowed values are from 0.0 to 1.0, default value is 1.0.
   * - Saturation
     - Float
     - Set the color :term:`saturation`. Allowed values are from 0 to 1, default value is 0.5.
   * - Preserve lightness
     - Float
     - Set the amount of preserving :term:`lightness`. Allowed values are from 0 to 1, default value is 0.

.. rst-class:: clear-both


.. rubric:: Notes

Color temperature is measured in degrees Kelvin. Lower values correct for "warmer" lighting, higher values correct for "cool" lighting. The default value of +6,500K is unity.
