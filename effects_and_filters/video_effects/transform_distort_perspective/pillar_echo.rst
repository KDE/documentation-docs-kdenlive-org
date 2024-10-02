.. meta::

   :description: Kdenlive Video Effects - Pillar Echo
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, pillar echo

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             - Eugen Mohr

   :license: Creative Commons License SA 4.0


Pillar Echo
===========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-pillar_echo.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-pillar_echo

.. sidebar:: |kdenlive-show-video| Pillar Echo

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      pillar_echo
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter creates an echo effect (blur) outside of an area of interest. It is very useful for using vertical video sources (like recorded on a smartphone) in a horizontal project. It can be :ref:`controlled directly on the monitor <ui-monitors_effect_direct_control>`.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Blur
     - Percentage
     - Set the blur amount in %
   * - X / Y / W / H / Size
     - Various
     - Adjusts the area where the blur is applied and visible
