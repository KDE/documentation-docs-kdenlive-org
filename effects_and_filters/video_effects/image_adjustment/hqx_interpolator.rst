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

.. figure:: /images/effects_and_compositions/effects-hqx_interpolator-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
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

This effect/filter works best for pixel art. Scaling is done by a factor of 2, 3, or 4 using the Hq*X\ [1]_ magnification algorithm specifically designed for this.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Scale factor
     - Selection
     - Sets the scaling factor

The following selection items are available:

:guilabel:`Scale factor`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - 2x
     - 
   * - 3x
     - Default
   * - 4x
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
      :class: no-scaled-link

   .. |appimage| image:: /images/icons/kdenlive-appimage_3.svg
   :width: 14px
      :class: no-scaled-link

   .. |windows| image:: /images/icons/windows.png
   :width: 14px
      :class: no-scaled-link

   .. |apple| image:: /images/icons/apple.png
   :width: 14px
      :class: no-scaled-link