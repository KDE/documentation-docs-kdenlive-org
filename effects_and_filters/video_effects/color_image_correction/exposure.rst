.. meta::

   :description: Kdenlive Video Effects - Exposure
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, exposure

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |wikipedia_exposure| raw:: html

   <a href="https://en.wikipedia.org/wiki/Exposure_value" target="_blank">Exposure Value</a>


Exposure
========

.. figure:: /images/effects_and_compositions/effects-exposure-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-exposure-2504.webp

.. sidebar:: |kdenlive-show-video| Exposure

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      avfilter
   :**Source filter**:
      exposure
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter adjusts the exposure of the image or video stream.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Exposure
     - Float
     - Set the exposure correction in EV\ [1]_. Allowed values are from -3.0 to 3.0 EV, default is 0 EV.
   * - Radius
     - Float
     - Set the black level correction. Allowed values are from -1.0 to 1.0, default is 0.


----

.. [1] Exposure Value. A number that represents a combination of a camera's shutter speed and f-number. For more details refer to the |wikipedia_exposure| article on Wikipedia.
