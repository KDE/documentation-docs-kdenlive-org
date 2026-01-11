.. meta::

   :description: Kdenlive Video Effects - Brightness (keyframable)
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, brightness (keyframable)

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Mmaguire (https://userbase.kde.org/User:Mmaguire)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |brightness| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterBrightness/" target="_blank">brightness</a>


.. ..versionchanged:: 25.04
   Brightness (keyframable --> Intensity)

Intensity
=========

.. figure:: /images/effects_and_compositions/effects-intensity-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-show-video| Intensity

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      |brightness|
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect adjusts the intensity of the clip.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Intensity
     - Integer
     - Sets the intensity of the clip. Values range from 0 (completely dark) to 400 (bright colors)

.. rst-class:: clear-both

.. note:: 
   This effect was called *Brightness (keyframable)* before. It works differently than the :doc:`/effects_and_filters/video_effects/color_image_correction/brightness` effect. At full intensity (400), the clip is not glaringly bright (or white) but just has bright colors.
