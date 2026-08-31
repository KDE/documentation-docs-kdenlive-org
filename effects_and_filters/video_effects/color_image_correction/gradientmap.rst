.. meta::

   :description: Kdenlive Video Effects - Gradientmap 
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color image correction, color, image, correction, gradientmap, gradient, map

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0

.. .. versionadded:: 26.08


Gradient Map
============

.. figure:: /images/effects_and_compositions/effects-gradientmap-2604.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Gradient Map

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      gradientmap
   :**Available**:
      |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter creates a gradient map for the selected clip.

By default, the effect has a gradient that goes from black to white turning the clip into a black-and-white image. The effct supports an alpha channel which will be shown as a light/dark checkerboard pattern behind any translucent stop.


.. rubric:: Parameters

You can define up to 32 gradient stops.

.. rubric:: Usage

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 30 70
   :class: table-wrap

   * - Action
     - Result
   * - Add a stop
     - Left-clicking anywhere on or directly below the gradient bar
   * - Delete a stop
     - Right-click the stop
   * - Move a stop
     - Drag the stop to the new position
   * - Change the color at the stop
     - Double-click the stop and select the color from the color selection window

.. rubric:: Examples

This gradient map

.. figure:: /images/effects_and_compositions/effects-gradientmap_example_1-2604.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. rst-class:: clear-both

Results in this:

.. figure:: /images/effects_and_compositions/effects-gradientmap_example_2-2604.webp
   :width: 803px
   :figwidth: 453px
   :align: left

Note the split screen: The left half shows the gradientmap effect applied, the right half the original image.
