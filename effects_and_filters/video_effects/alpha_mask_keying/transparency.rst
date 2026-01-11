.. meta::

   :description: Kdenlive Video Effects - Transparency
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, alpha, mask, keying, transparency

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0

.. |frei0r.transparency| raw:: html

   <a href="https://www.mltframework.org/plugins/FilterFrei0r-transparency/" target="_blank">transparency</a>


Transparency
============

.. figure:: /images/effects_and_compositions/effects-transparency-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-show-video| Transparency

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      |frei0r.transparency|
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

Tunes the alpha channel. Can also be used to simply change the transparency of the clip.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Transparency
     - Float
     - Sets the transparency of the clip. Default is 1.00.

.. note:: The slider :guilabel:`Transparency` behaves inverted: If set to 0.00, the clip is fully transparent; if set to 1.00, the clip is fully opaque (not transparent).
