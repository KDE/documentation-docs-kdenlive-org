.. meta::

   :description: Kdenlive Video Effects - Dilation 
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, image adjustment, dilation

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Dilation
========

.. figure:: /images/effects_and_compositions/effects-dilation-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-dilation-2504.webp

.. sidebar:: |kdenlive-show-video| Dilation

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      dilation
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter simulates image dilation, an effect which will enlarge the lightest pixels in the image by replacing the pixel by the local (3x3) maximum. It is the opposite of the :doc:`Erosion</effects_and_filters/video_effects/image_adjustment/erosion>` effect.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - 1st / 2nd / 3rd / 4th Plane Threshold
     - Integer
     - Limit the maximum change for each :term:`plane`, default is 65535. If 0, plane will remain unchanged.
   * - Coordinates
     - Integer
     - Flag which specifies the pixel to refer to. Default is 255, i.e. all eight pixels are used.


.. rubric:: Notes

The local 3x3 matrix looks like this (**P** represents the pixel):

   | 1 2 3
   | 4 P 5
   | 6 7 8

The parameter :kbd:`Coordinates` is the decimal value of the binary-notation of this matrix. Each point in the matrix is represented as a bit in a binary number\ [1]_ with 8 bits.

Example 1:
 Pixels #1, 2, and 3 are to be used for the dilation effect. :kbd:`Coordinates` must be set to 00000111\ :sub:`2`, or 2\ :sup:`2` + 2\ :sup:`1` + 2\ :sup:`0` = 4 + 2 + 1 = 7\ :sub:`10`

Example 2:
 Pixels #1, 3, 6, and 8 are to be used. :kbd:`Coordinates` must be set to 10100101\ :sub:`2`, or 2\ :sup:`7` + 2\ :sup:`5` + 2\ :sup:`2` + 2\ :sup:`0` = 128 + 32 + 4 + 1 = 165\ :sub:`10`


----

.. [1] Binary number's digits have 2 symbols: zero (0) and one (1). Each digit of a binary number counts a power of 2.

     Binary number example:
     1101\ :sub:`2` = 1×2\ :sup:`3` + 1×2\ :sup:`2` + 0×2\ :sup:`1` + 1×2\ :sup:`0` = 13\ :sub:`10`