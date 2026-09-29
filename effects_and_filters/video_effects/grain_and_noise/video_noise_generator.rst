.. meta::

   :description: Kdenlive Video Effects - Video Noise Generator
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, grain and noise, video noise generator

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Video Noise Generator
=====================

.. figure:: /images/effects_and_compositions/effects-video_noise_generator-2608.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Video Noise Generator

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      noise
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter adds noise to the video input frame.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 40 10 50
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - All components noise seed
     - Integer
     - Set noise seed for all pixel components
   * - Component #0 / #1 / #2 / #3 noise seed
     - Integer
     - Set noise seed for specific pixel component
   * - All components strength
     - Integer
     - Set noise strength for all pixel components
   * - Component #0 / #1 / #2 / #3 strength
     - Integer
     - Set noise strength for specific pixel component
   * - All components type
     - Selection
     - Set noise type for all components
   * - Component #0 / #1 / #2 / #3 type
     - Selection
     - Set pixel component noise type

The following selection items are available:

:guilabel:`Type`

.. list-table::
   :width: 100%
   :widths: 40 60
   :class: table-simple

   * - Average temporal noise
     - Averaged temporal noise (smoother). Default setting.
   * - Mixed random noise
     - Mix random noise with a (semi-)regular pattern
   * - Temporal noise
     - Temporal noise (noise pattern changes between frames)
   * - Uniform noise
     - Uniform noise (Gaussian otherwise)
