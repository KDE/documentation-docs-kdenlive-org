.. meta::

   :description: Kdenlive Video Effects - Bilateral
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, blur and sharpen, bilateral

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |here| raw:: html

   <a href="https://en.wikipedia.org/wiki/Bilateral_filter" target="_blank">here</a>


Bilateral
=========

.. figure:: /images/effects_and_compositions/effects-bilateral-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-show-video| Bilateral

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      avfilter
   :**Source filter**:
      bilateral
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect applies a kind of blur filter with spatial smoothing while preserving edges. A more in-depth explanation including the mathematical definition is available |here| on Wikipedia.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Planes
     - Selection
     - Sets the color space plane the effect is applied to
   * - Spatial sigma
     - Float
     - Set sigma of Gaussian function to calculate spatial weight. Range is 0.000 to 512.000, default is 0.100
   * - Range sigma
     - Float
     - Set sigma of Gaussian function to calculate range weight. Range is 0.000 to 1.000, default is 0.100

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
