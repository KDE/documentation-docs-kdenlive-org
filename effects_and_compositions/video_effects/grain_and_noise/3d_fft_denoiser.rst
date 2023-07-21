.. meta::

   :description: Do your first steps with Kdenlive video editor, using 3D FFT denoiser effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, grain and noise, 3d_fft_denoiser, 3D FFT denoiser

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |fdf| raw:: html

   <a href="https://www.geeksforgeeks.org/frequency-domain-filters-and-its-types/" target="_blank">this article</a>


.. _effects-3d_fft_denoiser:

3D FFT Denoiser
===============

This effect/filter denoises frames using 3D FFT (Fast Fourier Transform) frequency domain filtering\ [1]_.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-3d_fft_denoiser.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-3d_fft_denoiser

   3D FFT Denoiser effect

* **Sigma** - Set the noise sigma constant. This sets denoising strength. Default value is 1. Allowed range is from 0 to 30. Using very high sigma with low overlap may give blocking artifacts.

* **Amount** - Set amount of denoising. By default all detected noise is reduced. Default value is 1. Allowed range is from 0 to 1.

* **Block** - Set size of block in pixels, Default is 4, can be 2 to 6.

* **Overlap** - Set block overlap. Default is 0.5. Allowed range is from 0.2 to 0.8.

* **Add previous frame to temporal denoise** - Check to include previous frame in denoising. Default is off.

* **Add next frame to temporal denoise** - Check to include next frame in denoising. Default is off.

* **Planes** - Set :term:`planes<plane>` which will be filtered, by default all available are filtered except alpha.

.. rst-class:: clear-both


**Notes**

.. [1] For more details on Frequency Domain Filters and their types see |fdf| on geeksforgeeks.org
