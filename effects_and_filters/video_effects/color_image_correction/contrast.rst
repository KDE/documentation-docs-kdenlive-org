.. meta::

   :description: Kdenlive Video Effects - Contrast
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, contrast

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Contrast
========

.. figure:: /images/effects_and_compositions/effects-contrast-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-contrast-2504.webp

.. sidebar:: |kdenlive-show-video| Contrast

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      contrast0r
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter adjusts the contrast of a source image. It controls the tonal range of the source which maps pixel values below a specified value to black, and those above a specified value to white. It is best used in conjunction with :ref:`view-rgb_parade` and the :ref:`view-histogram`. Values below 250 decrease the contrast between dark and light areas, values above 250 increase it.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Contrast
     - Integer
     - Set the contrast. Allowed values are from 0 to 1000, default value is 250.
