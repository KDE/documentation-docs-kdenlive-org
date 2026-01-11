.. meta::

   :description: Kdenlive Video Effects - Spill Suppress
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, alpha, mask, keying, key, chroma, greenscreen, bluescreen, spill, suppress

.. metadata-placeholder

   :authors: - Roger (https://userbase.kde.org/User:Roger)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0

.. .. |spillsupress| raw:: html
   <a href="https://gstreamer.freedesktop.org/documentation/frei0r/frei0r-filter-spillsupress.html?gi-language=c" target="_blank">frei0r.spillsupress</a>


Spill Suppress
==============

.. figure:: /images/effects_and_compositions/effects-spillsuppress-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-show-video| Spill Suppress

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      frei0r
   :**Source filter**:
      spillsupress
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

Remove green or blue spill light from subjects shot in front of green or blue screen.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Suppress Type
     - Selection
     - Defines if green or blue screen spill suppress is applied
