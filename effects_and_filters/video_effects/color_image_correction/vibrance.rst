.. meta::

   :description: Kdenlive Video Effects - Vibrance
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, vibrance

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |vib_sat| raw:: html

   <a href="https://www.wix.com/blog/photography/vibrance-vs-saturation" target="_blank">Vibrance vs. Saturation</a>


Vibrance
========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-vibrance.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-vibrance

.. sidebar:: |kdenlive-show-video| Vibrance

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      vibrance
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter boosts or alters :term:`saturation`. The results from using the vibrance effect are different compared to the :doc:`/effects_and_filters/video_effects/color_image_correction/saturation` effect\ [1]_.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Intensity
     - Float
     - Set the strength of the boost with positive values, strength of :guilabel:`Alternate` with negative values. Allowed range is from -2.0 to 2.0, default is 0.
   * - Red /Green / Blue balance
     - Float
     - Set the red, green and blue balance. Allowed range is from -10.0 to 10.0, default is 1.0
   * - Red / Green / Blue luma
     - Float
     - Set the red, green and blue :term:`luma` coefficient.
   * - Alternate
     - Switch
     - If :guilabel:`Intensity` is negative and this is checked, colors will change, otherwise colors will be less saturated more towards grey.

.. rst-class:: clear-both


----

.. [1] For more details about vibrance and saturation see the article about |vib_sat|.
