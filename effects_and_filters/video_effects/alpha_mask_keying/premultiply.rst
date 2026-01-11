.. meta::

   :description: Kdenlive Video Effects - Premultiply or Unpremultiply
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, alpha, mask, keying, premultiply, unpremultiply

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |alpha_blending| raw:: html

   <a href="https://developer.nvidia.com/content/alpha-blending-pre-or-not-pre" target="_blank">Alpha Blending</a>


Premultiply or Unpremultiply
----------------------------

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-premultiply.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-show-video| Premultiply or Unpremultiply

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      frei0r
   :**Source filter**:
      premultiply
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

Multiply (or divide) each color component by the pixel's alpha value.

Use this effect before any alpha effects if the result of your compositions using alpha has odd-looking colors.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - unpremultiply
     - Switch
     - Whether to unpremultiply instead (default is **On**)


.. rubric:: Notes

For more details see this article by Nvidia about |alpha_blending|.
