.. meta::

   :description: Kdenlive Video Effects - 3D FFT Denoiser
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, grain and noise, 3d_fft_denoiser, 3D FFT denoiser

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


3D FFT Denoiser
===============

.. figure:: /images/effects_and_compositions/effects-3d_fft_denoiser-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| 3D FFT Denoiser

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      fftdnoiz
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No
   :**Color depth**:
      10bit |color-management|
   :**Tutorial**:
      :ref:`Yes <tutorials-3d_fft_denoiser>` |view-presentation|

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter denoises frames using 3D FFT (Fast Fourier Transform) frequency domain filtering\ [1]_.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Sigma
     - Integer
     - Set the noise sigma constant. This sets denoising strength. Default value is 1. Allowed range is from 0 to 30. Using very high sigma with low overlap may give blocking artifacts.
   * - Amount
     - Float
     - Set amount of denoising. By default all detected noise is reduced. Default value is 1. Allowed range is from 0 to 1.
   * - Block
     - Integer
     - Set size of block in pixels, Default is 4, can be 2 to 6.
   * - Overlap
     - Float
     - Set block overlap. Default is 0.5. Allowed range is from 0.2 to 0.8.
   * - Method
     - Selection
     - Set denoising method
   * - Add previous frame to temporal denoise
     - Switch
     - Check to include previous frame in denoising. Default is off.
   * - Add next frame to temporal denoise
     - Switch
     - Check to include next frame in denoising. Default is off.
   * - Planes
     - Selection
     - Set :term:`planes<plane>` which will be filtered, by default all available are filtered except alpha.

The following selection items are available:

:guilabel:`Method`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Wiener
     - Default
   * - Hard
     - 

:guilabel:`Planes`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - None
     - 
   * - Y
     - 
   * - U
     - 
   * - YU
     - 
   * - V
     - 
   * - YV
     - 
   * - UV
     - 
   * - All
     - Default


----

.. |fdf| raw:: html

   <a href="https://www.geeksforgeeks.org/frequency-domain-filters-and-its-types/" target="_blank">this article</a>


.. [1] For more details on Frequency Domain Filters and their types see |fdf| on geeksforgeeks.org
