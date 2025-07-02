.. meta::

   :description: Kdenlive Video Effects - HQ 3d Denoiser
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, grain and noise, miscellaneous, high quality, denoiser

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


HQ 3D Denoiser
==============

.. figure:: /images/effects_and_compositions/effects-denoise_hqdn3d-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-denoise_hqdn3d-2504.webp

.. sidebar:: |kdenlive-show-video| HQ 3D Denoiser

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      denoise_hqdn3d\ [1]_
   :**Available**:
      |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No
   :**Color depth**:
      8bit
   :**Tutorial**:
      :ref:`Yes <tutorials-hqdn3d>` |view-presentation|

.. rst-class:: clear-both


.. rubric:: Description

This is a high precision/quality 3d denoise filter. It aims to reduce image noise, producing smooth images and making still images really still. It should enhance compressibility.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Spatial
     - Float
     - Amount of spatial filtering
   * - Temporal
     - Float
     - Amount of temporal filtering



----

.. [1] This replaces frei0r.hqdn3d