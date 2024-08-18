.. meta::

   :description: Kdenlive Video Effects - Timeout Indicator
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, utility, timeout indicator

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |ex1_kf1| image:: /images/effects_and_compositions/kdenlive2304_effects-timeout_indicator_ex1_kf1.webp
   :width: 200px

.. |ex1_kf2| image:: /images/effects_and_compositions/kdenlive2304_effects-timeout_indicator_ex1_kf2.webp
   :width: 200px

.. |ex2_kf1| image:: /images/effects_and_compositions/kdenlive2304_effects-timeout_indicator_ex2_kf1.webp
   :width: 170px

.. |ex2_kf2| image:: /images/effects_and_compositions/kdenlive2304_effects-timeout_indicator_ex2_kf2.webp
   :width: 170px

.. |ex2_kf3| image:: /images/effects_and_compositions/kdenlive2304_effects-timeout_indicator_ex2_kf3.webp
   :width: 170px

.. |ex2_kf4| image:: /images/effects_and_compositions/kdenlive2304_effects-timeout_indicator_ex2_kf4.webp
   :width: 170px


Timeout Indicator
=================

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-timeout_indicator.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-timeout_indicator

.. sidebar:: |kdenlive-show-video| Timeout Indicator

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      timeout
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter displays a kind of countdown bar in the current frame's bottom right-hand corner. You need to set keyframes and the time value for the effect to work. The default settings simply display a blueish bar.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Indicator color
     - 
     - Set the color for the countdown (or count-up) indicator
   * - Time
     - 
     - Set the time value. Range is from 0 (default, bar is full or at 100%) to 1000 (bar is gone or at 0%).
   * - Transparency
     - 
     - Define the transparency of the indicator


.. rubric:: Examples

1. Count down/count up for the entire length of the clip

 Create a keyframe at the end of the clip and change the :guilabel:`Time` value to 1000. For count up swap the :guilabel:`Time` values.

 |ex1_kf1| |ex1_kf2|

|

2. Countdown starts 3 seconds before the end of the clip and the indicator goes from yellow to red

 Go to the first (default) keyframe and set the :guilabel:`Time` value to 1000 and the :guilabel:`Indicator color` to yellow. Go to the last frame, create a keyframe and set the :guilabel:`Time` value to 1000 and the :guilabel:`Indicator color` to red. Go back 3 minutes in the timeline, create a keyframe and set the :guilabel:`Time` value to 0 and the :guilabel:`Indicator color` to yellow. Go back one frame (:kbd:`Left Arrow`), create a keyframe and set the :guilabel:`Time` value to 1000.

 |ex2_kf1| |ex2_kf2| |ex2_kf3| |ex2_kf4|
