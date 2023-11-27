.. meta::

   :description: Kdenlive Video Effects - Gamma
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, gamma

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Mmaguire (https://userbase.kde.org/User:Mmaguire)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Gamma
=====

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-gamma.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-gamma

.. sidebar:: |kdenlive-show-video| Gamma

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      frei0r
   :**Source filter**:
      gamma
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter adjusts the :term:`gamma` value of a source image.

The effect does not have keyframes. Use :doc:`/effects_and_compositions/video_effects/color_image_correction/gamma_keyframe` if you need keyframes.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Gamma
     - Float
     - Decrease (<0.250) or increase (>0.250) gamma of the image. Default is 1.0, which increases gamma significantly.
