.. meta::

   :description: Kdenlive Video Effects - Tint
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, tint, tint0r

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Tint0r
======

.. figure:: /images/effects_and_compositions/effects-tint0r-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-tint0r-2504.webp

.. sidebar:: |kdenlive-show-video| Tint0r

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      tint0r
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter maps the source image :term:`luminance` between two specified colors.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Map black to
     - Picker
     - The color to map source color with zero luminance
   * - Map white to
     - Picker
     - The color to map source color with full luminance
   * - Tint amount
     - Integer
     - Amount of color. Allowed values are from 0 to 1000, default is 250.


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
