.. meta::

   :description: Kdenlive Video Effects - FFT-based FIR
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, FFT-based FIR

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |fir_filter| raw:: html

   <a href="https://www.collimator.ai/reference-guides/what-is-an-fir-filter" target="_blank">What is an FIR filter?</a>

.. |fft_introduction| raw:: html

   <a href="https://legacy.imagemagick.org/Usage/fourier/#introduction" target="_blank">introduction</a>


FFT-based FIR
=============

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-fft-based_fir.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-fft-based_fir

.. sidebar:: |kdenlive-show-video| FFT-based FIR

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      fftfilt
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter applies arbitrary expressions to samples in frequency domain. It is a Finite Impulse Response (FIR)\ [1]_ filter using Fast Fourier Transform (FFT)\ [2]_.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Gain in Y / U / V plane
     - Integer
     - Set the gain value for the Y (:term:`luma`), U (1st :term:`chroma`) or V (2nd chroma) plane. Allowed values are 0 to 250, default is 0.
   * - Luminance Y / U / V plane
     - Float
     - Set the frequency domain weight value for the Y (:term:`luma`), U (1st :term:`chroma`) or V (2nd chroma) plane. Allowed values are 0.000 to 5.000, default is 1.000.
   * - Evaluate
     - Selection
     - Set when the expressions are evaluated.

The following selection items are available:

:guilabel:`Evaluate`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - init
     - Only evaluate expressions once during filter initialization (default)
   * - frame
     - Evaluate expressions for each incoming frame


.. warning::
   If :guilabel:`Evaluate` is set to **frame** render times will be significantly longer as each frame is evaluated individually.


----

.. [1] For more information about FIR see this article: |fir_filter|

.. [2] This is a good |fft_introduction| to Fourier Transforms in image processing.
