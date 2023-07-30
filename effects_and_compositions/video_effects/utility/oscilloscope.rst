.. meta::

   :description: Do your first steps with Kdenlive video editor, using oscilloscope effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, utility, oscilloscope

.. metadata-placeholder

   :authors: - Roger (https://userbase.kde.org/User:Roger)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-oscilloscope:

Oscilloscope
============

This effect/filter creates a 2D video oscilloscope overlay. Useful to measure spatial impulse, step responses, chroma delays, etc.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-oscilloscope.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-oscilloscope

   Oscilloscope effect

* **av.x / av.y** - Set scope center x / y position

* **av.s** - Set scope size, relative to frame diagonal

* **av.t** - Set scope tilt/rotation

* **av.o** - Set scope opacity

* **av.tx / av.ty** - Set trace center x /y position

* **av.tw / av.th** - Set trace width / height, relative to width / height of frame

* **av.c** - Set which components to trace. By default it traces YUV components.

.. rst-class:: clear-both


.. rubric:: Components Matrix

.. list-table::
   :header-rows: 1

   * - av.c Value
     - Component
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
   * - 7 (default)
     - YUV
   * - 8..15
     - repeat
