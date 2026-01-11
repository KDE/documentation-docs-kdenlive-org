.. meta::

   :description: Kdenlive Video Effects - Threshold
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, threshold

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Threshold
=========

.. figure:: /images/effects_and_compositions/effects-threshold-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Threshold\ [1]_

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      threshold0r
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

This effect/filter thresholds a source image.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Threshold
     - Integer
     - Set the threshold in a range from 0 (white) to 255 (black)


----

.. |threshold0r| raw:: html

   <a href="https://mltframework.org/plugins/FilterFrei0r-threshold0r/" target="_blank">frei0r.threshold0r</a>


.. [1] This is the |threshold0r| filter that used to be called *threshold0r* in the Kdenlive video effects list.
