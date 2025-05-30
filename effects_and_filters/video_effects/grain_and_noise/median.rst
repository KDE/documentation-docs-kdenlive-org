.. meta::

   :description: Kdenlive Video Effects - Median
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, grain and noise, median

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Median
======

.. figure:: /images/effects_and_compositions/effects-median-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-median-2504.webp

.. sidebar:: |kdenlive-show-video| Median

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      avfilter
   :**Source filter**:
      median
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter picks the median pixel from a given rectangle defined by :guilabel:`Spatial sigma`.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 30 10 60
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Planes
     - Selection
     - Sets which :term:`planes<plane>` to process. Default is **All**.
   * - Spatial sigma
     - Float
     - Sets the horizontal radius size. Allowed values are from 1.000 to 127.000, default is 1.
   * - Median vertical radius
     - Float
     - Sets the vertical radius size. Allowed values are from 1.000 to 127.000, default is 0. If it is 0, value will be picked from :guilabel:`Spatial sigma` parameter.
   * - Median percentile
     - Float
     - Set median percentile. Default is 0.5. Default value will pick always median values, 0 will pick minimum values, and 1 maximum values.

The following selection items are available:

:guilabel:`Planes`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Alpha
     - 
   * - Y
     - Default
   * - U
     - 
   * - V
     - 
   * - Red
     - 
   * - Green
     - 
   * - Blue
     - 
   * - All
     - 
