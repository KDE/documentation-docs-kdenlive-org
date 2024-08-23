.. meta::

   :description: Kdenlive Video Effects - Video Noise Generator
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, grain and noise, video noise generator

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Video Noise Generator
=====================

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-video_noise_generator.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-video_noise_generator

.. sidebar:: |kdenlive-show-video| Video Noise Generator

   :**Status**:
      Maintained
   :**Keyframes**:
      None
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
   * - All component strength
     - Integer
     - Set noise strength for all pixel components
   * - Component #0 / #1 / #2 / #3 noise seed
     - Integer
     - Set noise strength for specific pixel component
   * - Flag all
     - Selection
     - Set pixel component flag for all components
   * - Flag component 0 / 1 / 2 / 3
     - Selection
     - Set pixel component flags

The following selection items are available:

:guilabel:`Flag`

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
