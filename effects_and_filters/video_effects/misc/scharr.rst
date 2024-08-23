.. meta::

   :description: Kdenlive Video Effects - Scharr 
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, misc, miscellaneous, scharr, operator

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Scharr
======

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-scharr.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-scharr

.. sidebar:: |kdenlive-show-video| Scharr

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      scharr
   :**Available**:
      |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter applies the Scharr\ [1]_ operator to the input video stream.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - av.planes
     - Integer (see below)
     - Set which :term:`planes<plane>` will be processed, unprocessed planes will be copied. Default value **15** (all planes).
   * - av.scale
     - Float
     - Set value which will be multiplied with filtered result.
   * - av.delta
     - Float
     - Set value which will be added to filtered result.


The values for :guilabel:`av.planes` represent the :term:`plane` as follows:

.. list-table::
   :align: left
   :header-rows: 1
   :width: 100%
   :widths: 10 90
   :class: table-wrap

   * - Value
     - Plane
   * - 0
     - None
   * - 1
     - Y
   * - 2
     - U
   * - 3
     - YU
   * - 4
     - V
   * - 5
     - YV
   * - 6
     - UV
   * - 7
     - YUV
   * - 8..15
     - repeat 0 thru 7


----

.. |scharr| raw:: html

   <a href="https://en.wikipedia.org/wiki/Sobel_operator#Alternative_operators" target="_blank">Alternative Operators</a>


.. [1] For more (mathematical) details refer to the Wikipedia article about Sobel, and there specifically about |scharr|.
