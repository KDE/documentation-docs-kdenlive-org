.. meta::

   :description: Kdenlive Video Effects - Monochrome
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, monochrome

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Monochrome
==========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-monochrome.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-monochrome

.. sidebar:: |kdenlive-show-video| Monochrome

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      avfilter
   :**Source filter**:
      monochrome
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter converts video to gray using custom color filter.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Chroma blue spo
     - Float
     - Set the :term:`chroma` blue spot. Allowed range is from -1 to 1. Default value is 0.
   * - Chroma red spot
     - Float
     - Set the :term:`chroma` red spot. Allowed range is from -1 to 1. Default value is 0.
   * - Color filter size
     - Float
     - Set the color filter size. Allowed range is from .1 to 10. Default value is 1.
   * - Highlights strength
     - Float
     - Set the highlights strength. Allowed range is from 0 to 1. Default value is 0.
