.. meta::

   :description: Kdenlive Video Effects - Brightness
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, brightness

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Mmaguire (https://userbase.kde.org/User:Mmaguire)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |frei0r_brightness| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-brightness/" target="_blank">brightness</a>


Brightness
==========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-brightness.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-brightness

.. sidebar:: |kdenlive-show-video| Brightness

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      |frei0r_brightness|
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect adjusts the brightness of the clip.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Brightness
     - Integer
     - Sets the brightness of the clip. Values range from 0 (completely dark) to 1000 (glaringly bright).

.. rst-class:: clear-both

.. note:: 
   This brightness effect works differently than the :doc:`/effects_and_filters/video_effects/color_image_correction/brightness_keyframable` effect.
