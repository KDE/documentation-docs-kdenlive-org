.. meta::

   :description: Do your first steps with Kdenlive video editor, using FFT-based FIR effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, FFT-based FIR

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |fir_filter| raw:: html

   <a href="https://www.collimator.ai/reference-guides/what-is-an-fir-filter" target="_blank">What is an FIR filter?</a>

.. |fft_introduction| raw:: html

   <a href="https://legacy.imagemagick.org/Usage/fourier/#introduction" target="_blank">introduction</a>


.. _effects-fft-based_fir:

FFT-based FIR
=============

This effect/filter applies arbitrary expressions to samples in frequency domain. It is a Finite Impulse Response (FIR) [1]_ filter using Fast Fourier Transform (FFT) [2]_.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-fft-based_fir.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-fft-based_fir

   FFT-based FIR effect

* **Gain in Y / U / V plane** - Set the gain value for the Y (:term:`luma`), U (1st chroma) or V (2nd chroma) plane. Allowed values are 0 to 250, default is 0.

* **Luminance Y / U / V plane** - Set the frequency domain weight value for the Y (:term:`luma`), U (1st chroma) or V (2nd chroma) plane. Allowed values are 0.000 to 5.000, default is 1.000.

* **Evaluate** - Set when the expressions are evaluated. Options are **init** (only evaluate expressions once during filter initialization) and **frame** (evaluate expressions for each incoming frame), default is **init**.

.. rst-class:: clear-both

.. warning:: If :guilabel:`Evaluate` is set to **frame** render times will be significantly longer as each frame is evaluated individually.


**Notes**

.. [1] For more information about FIR see this article: |fir_filter|

.. [2] This is a good |fft_introduction| to Fourier Transforms in image processing.
