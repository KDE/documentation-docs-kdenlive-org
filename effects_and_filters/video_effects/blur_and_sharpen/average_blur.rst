.. meta::

   :description: Kdenlive Video Effects - Average Blur
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, blur and sharpen, average blur

   :authors: - Roger (https://userbase.kde.org/User:Roger)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Average Blur
============

.. .. versionadded:: 24.02 keyframeable

.. figure:: /images/effects_and_compositions/effects-average_blur-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-average_blur-2504.webp

.. sidebar:: |kdenlive-show-video| Average Blur

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      avfilter
   :**Source filter**:
      avgblur
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

Blurs the clip based on the settings for :guilabel:`X size` and :guilabel:`Y size`. By default, all :term:`planes<plane>` will be affected. By setting the blur effect to different planes (e.g. red, green or blue) interesting artistic effects can be achieved. 


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - X size
     - Integer
     - Amount of horizontal blur
   * - Y size
     - Integer
     - Amount of vertical blur
   * - Planes
     - Selection
     - Sets the color space plane the effect is applied to

The following selection items are available:

:guilabel:`Planes`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Alpha
     - Alpha channel
   * - Y
     - Luminance
   * - U
     - Chroma (U plane)
   * - V
     - Chroma (V plane)
   * - Red
     - Red channel
   * - Green
     - Green channel
   * - Blue
     - Blue channel
   * - All
     - All planes will be affected by the blur amount (default)
