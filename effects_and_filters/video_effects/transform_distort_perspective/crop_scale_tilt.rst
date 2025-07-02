.. meta::

   :description: Kdenlive Video Effects - Crop, Scale and Tilt
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, crop scale tilt

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Roger (https://userbase.kde.org/User:Roger)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Crop, Scale and Tilt
====================

.. figure:: /images/effects_and_compositions/effects-crop_scale_tilt-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-crop_scale_tilt-2504.webp

.. sidebar:: |kdenlive-show-video| Crop, Scale and Tilt\ [1]_

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      scale0tilt
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No
   :**Color depth**:
      8bit
   :**Tutorial**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter crops, scales and tilts an image.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 10 65
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Crop Left / Right
     - Integer
     - Number of pixels to crop from the left / right
   * - Crop Top / Bottom
     - Integer
     - Number of pixels to crop from the top / bottom
   * - Scale X / Y
     - Integer
     - Set the scale factor in % along X / Y axis
   * - Tilt X / Y
     - Integer
     - Position to move the image along the X / Y axis. Defaults to the center based on the project resolution settings (e.g. X=960, Y=540 for a 1920x1080 project).


----

.. [1] This effect was previously called *Scale and Tilt* and *Crop, Scale and Position*.


.. https://youtu.be/WV4bocj7ygw
