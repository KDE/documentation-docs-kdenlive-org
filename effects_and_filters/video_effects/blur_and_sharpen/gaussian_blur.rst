.. meta::

   :description: Kdenlive Video Effects - Gaussian Blur (gblur)
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, blur and sharpen, gaussian blur, gblur

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0



Gaussian Blur
=============

.. .. versionadded:: 24.02 keyframeable

.. figure:: /images/effects_and_compositions/effects-gaussian_blur-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-gaussian_blur-2504.webp

.. sidebar:: |kdenlive-show-video| Gaussian Blur

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
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
   * - Steps 
     - Selection
     - Set number of steps for Gaussian approximation
   * - Planes
     - Selection
     - Set which planes to filter. By default all planes are filtered (YUV).
   * - Sigma
     - Integer
     - Set horizontal sigma, standard deviation of Gaussian blur. Determines the strength of the horizontal blur. Default is 10.
   * - Vertical Sigma
     - Integer
     - Set vertical sigma. Determines the strength of the vertical blur. Default is 10.

The following selection items are available:

:guilabel:`Steps`

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
