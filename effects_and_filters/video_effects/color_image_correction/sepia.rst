.. meta::

   :description: Kdenlive Video Effects - Sepia
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, sepia

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |wikipedia_sepia| raw:: html

   <a href="https://en.wikipedia.org/wiki/Sepia_(color)" target="_blank">Sepia</a>


Sepia
=====

.. figure:: /images/effects_and_compositions/effects-sepia-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-sepia-2504.webp

.. sidebar:: |kdenlive-show-video| Sepia

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      MLT
   :**Source filter**:
      sepia
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter turns clip colors to sepia\ [1]_.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Chrominance U
     - 
     - Changes the U :term:`plane` (blue projection). Allowed values are from 0 to 255, default is 75.
   * - Chrominance V
     - 
     - Changes the V :term:`plane` (red projection). Allowed values are from 0 to 255, default is 75.


.. rubric:: Notes
   
By using the :guilabel:`Chrominance` sliders you can adjust the level of brownish-ness to the look you want.


----

.. [1] See this article about |wikipedia_sepia| in Wikipedia.
