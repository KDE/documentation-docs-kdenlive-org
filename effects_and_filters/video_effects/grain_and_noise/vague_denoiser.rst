.. meta::

   :description: Kdenlive Video Effects - Wavelet Denoiser
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, grain and noise, vague, wavelet, denoiser

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Wavelet Denoiser
================

.. figure:: /images/effects_and_compositions/effects-wavelet_denoiser-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-wavelet_denoiser-2504.webp

.. sidebar:: |kdenlive-show-video| Wavelet Denoiser

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      vaguedenoiser
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No
   :**Color depth**:
      10bit |color-management|
   :**Tutorial**:
      No

.. rst-class:: clear-both


.. rubric:: Description

Wavelet\ [1]_ based denoiser. It transforms each frame from the video input into the wavelet domain, using Cohen-Daubechies-Feauveau 9/7\ [2]_. Then it applies some filtering to the obtained coefficients. It does an inverse wavelet transform after. Due to wavelet properties, it should give a nice smoothed result and reduced noise without blurring picture features.

.. attention:: The effect works best with smaller threshold values. It is easy to over-filter this effect.

.. note:: Using different planes and/or higher threshold values can be used for artistic manipulation of the image.

.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Method
     - Selection
     - The filtering method the filter will use. See below.
   * - Threshold Type
     - Selection
     - The threshold type the filter will use. See below.
   * - Threshold
     - Integer
     - The filtering strength. The higher, the more filtered the video will be. Hard thresholding can use a higher threshold than soft thresholding before the video looks overfiltered.
   * - Steps
     - Integer
     - Number of times the wavelet will decompose the picture. Picture cannot be decomposed beyond a particular point (typically, 8 for a 640x480 frame - as 2^9 = 512 > 480).
   * - Percentage
     - Percent
     - Partial of full denoising (limited coefficients shrinking)
   * - Planes
     - Selection
     - Select the planes to process. See below.

The following selection items are available:

:guilabel:`Method`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - Soft
     - All values under the threshold will be zeroed. All values above will be reduced by the threshold.
   * - Hard
     - All values under the threshold will be zeroed
   * - Garrote
     - Scales or nullifies coefficients - intermediary between (more) soft and (less) hard thresholding (default)

:guilabel:`Threshold Type`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - Universal
     - Threshold used is same for all decompositions (default)
   * - Bayes
     - Threshold used depends also on each decomposition coefficients

:guilabel:`Planes`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - None
     - 
   * - Y (Luminance)
     - 
   * - U (Chroma red-diff)
     - 
   * - YU
     - 
   * - V (Chroma blue-diff)
     - 
   * - YV
     - 
   * - UV
     - 
   * - All
     - Default
   * - Alpha
     - 


----

.. |wavelet| raw:: html

   <a href="https://en.wikipedia.org/wiki/Wavelet" target="_blank">https://en.wikipedia.org/wiki/Wavelet</a>

.. |cohen-daubechies-feauveau| raw:: html

   <a href="https://en.wikipedia.org/wiki/Cohen%E2%80%93Daubechies%E2%80%93Feauveau_wavelet" target="_blank">https://en.wikipedia.org/wiki/Cohen%E2%80%93Daubechies%E2%80%93Feauveau_wavelet</a>


.. [1] |wavelet|

.. [2] |cohen-daubechies-feauveau| (heavy on the math behind it)