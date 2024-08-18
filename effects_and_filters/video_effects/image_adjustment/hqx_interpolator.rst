.. meta::

   :description: Kdenlive Video Effects - HQ*X Interpolator
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, image adjustment, hqx interpolator

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |hqnx| raw:: html

   <a href="https://en.wikipedia.org/wiki/Pixel-art_scaling_algorithms#hqnx_family" target="_blank">Maxim Stepin's hqnx</a>


HQ*X Interpolator
=================

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-hqx_interpolator.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-hqx_interpolator

.. sidebar:: |kdenlive-show-video| HQ*X Interpolator

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      hqx
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter scales the input stream by 2, 3 or 4 using the Hq*X\ [1]_ magnification algorithm designed for pixel art.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Interpolation factor
     - Selection
     - Sets the scaling factor
   * - Maximum number of threads
     - Integer
     - Sets the number of CPU threads to use for calculation
   * - Position to set the filter
     - Selection
     - Defines where in the render pipeline the filter will be applied. When set to **frame** this can result in significantly longer rendering times.

The following selection items are available:

:guilabel:`Interpolation factor`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - 2xHq*X
     - 
   * - 3xHq*X
     - Default
   * - 4xHq*X
     - 

:guilabel:`Position to set the filter`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - frame
     - default
   * - filter
     - 
   * - source
     - 
   * - producer
     - 

.. rst-class:: clear-both


----

.. [1] See the article in Wikipedia about |hqnx| family of algorithms.


.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Icons used here (remove comment indent to enable them for this document)
   
   .. |linux| image:: /images/icons/linux.png
   :width: 14px
   :alt: Linux
   :class: no-scaled-link

   .. |appimage| image:: /images/icons/kdenlive-appimage_3.svg
   :width: 14px
   :alt: appimage
   :class: no-scaled-link

   .. |windows| image:: /images/icons/windows.png
   :width: 14px
   :alt: Windows
   :class: no-scaled-link

   .. |apple| image:: /images/icons/apple.png
   :width: 14px
   :alt: MacOS
   :class: no-scaled-link