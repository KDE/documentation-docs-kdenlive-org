.. meta::

   :description: Do your first steps with Kdenlive video editor, using scharr effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, misc, miscellaneous, scharr, operator

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |scharr| raw:: html

   <a href="https://en.wikipedia.org/wiki/Sobel_operator#Alternative_operators" target="_blank">Alternative Operators</a>


.. _effects-scharr:

Scharr
======

This effect/filter applies the Scharr\ [1]_ operator to the input video stream.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-scharr.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-scharr

   Scharr effect

* **av.planes** - Set which :term:`planes<plane>` will be processed, unprocessed planes will be copied. Default value 15 (all planes).

* **av.scale** - Set value which will be multiplied with filtered result.

* **av.delta** - Set value which will be added to filtered result.

.. rst-class:: clear-both


.. list-table::
   :align: left
   :header-rows: 1

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
     - repeat

.. rst-class:: clear-both


**Notes**

.. [1] For more (mathematical) details refer to the Wikipedia article about Sobel, and there specifically about |scharr|
