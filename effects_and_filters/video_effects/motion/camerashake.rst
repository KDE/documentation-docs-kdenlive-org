.. meta::

   :description: Kdenlive Video Effects - camerashake
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, motion, camerashake, shake

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0

.. .. versionadded:: 26.08


Camera Shake
============

.. figure:: /images/effects_and_compositions/effects-camerashake-2608.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| camerashake

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      camerashake
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter simulates a hand-held camera.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 30 10 60
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Amplitude X
     - Integer
     - Maximum horizontal shake amplitude. Maximum amplitude is 500 pixels.
   * - Amplitude Y
     - Integer
     - Maximum vertical shake amplitude. Maximum amplitude is 500 pixels.
   * - Rotation
     - Float
     - Maximum rotation shake (capped at 45 degrees either direction)
   * - Zoom
     - Percent
     - Zoom factor to hide black borders. This is in addition to 100%. For example: 0% means not additional zoom; 100% means image is twice as large (total of 200% of original size).
   * - Shake intensity
     - Float
     - Speed or frequency of the shake. This is not linear and values towards either end of the scale decrease the intensity. Maximum intensity is somewhere in the middle.
   * - Opacity
     - Percent
     - Opacity of the effect. 0% means fully transparent, 100% means fully opaque.
   * - Motion blur
     - Integer
     - Amount of motion blur measured in radius in pixels. Capped at 20 pixels.
   * - Color
     - Selection
     - Background color for exposed borders. Alpha channel is **not** supported.


.. note:: 
   Using motion blur slows down the shake effect significantly.
