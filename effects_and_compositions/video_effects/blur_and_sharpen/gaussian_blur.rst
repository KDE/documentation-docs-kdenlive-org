.. meta::

   :description: Kdenlive Video Effects - Gaussian Blur (gblur)
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, blur and sharpen, gaussian blur, gblur

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0



Gaussian Blur
=============

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-gaussian_blur.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-gaussian_blur

.. sidebar:: |kdenlive-show-video| Gaussian Blur

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      gblur
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect blurs the clip by applying a Gaussian function (known from statistics as an expression for the normal distribution). By default, all :term:`planes<plane>` will be affected. By setting the blur effect to different planes (e.g. red, green or blue) interesting artistic effects can be achieved.


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
     - Set horizontal sigma, standard deviation of Gaussian blur. Determines the strength of the blur. Default is 0.5.
   * - StepsX 
     - Selection
     - Set number of steps for Gaussian approximation
   * - Planes
     - Selection
     - Set which planes to filter. By default all planes are filtered (YUV).
   * - Vertical Sigma
     - Integer
     - Set vertical sigma, if negative it will be same as sigma. Default is -1.

The following selection items are available:

:guilabel:`StepsX`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - 1 thru 6
     - Gradually increases the blur fineness

:guilabel:`Planes`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - Alpha
     - Alpha channel
   * - Y
     - Luminance
   * - U
     - Chroma (U plane)
   * - YU
     - Both Y and U planes
   * - V
     - Chroma (V plane)
   * - YV
     - Both Y and V planes
   * - UV
     - Both U and V planes
   * - YUV
     - All planes will be affected by the blur effect (default)
   * - None
     - No effect application
