.. meta::

   :description: Kdenlive Video Effects - Boxblur
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, blur and sharpen, boxblur

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


BoxBlur
========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-boxblur.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-boxblur

.. sidebar:: |kdenlive-show-video| BoxBlur

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      boxblur
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect blurs the image based on the horizontal and vertical multiplicator allowing uneven blurring or blurring in only one direction. Not be confused with the deprecated Box Blur effect.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Horizontal multiplicator
     - Percentage
     - Sets the amount of horizontal blur. Range is from 0% to 1000%, default is 1%.
   * - Vertical multiplicator
     - Percentage
     - Sets the amount of vertical blur. Range is from 0% to 1000%, default is 1%.
