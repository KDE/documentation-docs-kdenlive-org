.. meta::

   :description: Kdenlive Video Effects - Limiter
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, limiter

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Limiter
=======

.. figure:: /images/effects_and_compositions/effects-limiter-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Limiter

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      limiter
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter limits the pixel components values to the specified range.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Min
     - Integer
     - Lower bound. Defaults to the lowest allowed value for the input.
   * - Max
     - Integer
     - Upper bound. Defaults to the highest allowed value for the input.
   * - Planes
     - Selection
     - Specifies which :term:`planes<plane>` will be processed

The following selection items are available:

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - None
     - 
   * - Y
     - 
   * - YU
     - 
   * - V
     - 
   * - YV
     - 
   * - UV
     - 
   * - YUV
     - Default
   * - Alpha
     - 
