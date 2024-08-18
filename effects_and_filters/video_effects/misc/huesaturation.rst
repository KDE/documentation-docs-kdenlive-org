.. meta::

   :description: Kdenlive Video Effects - Huesaturation
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, misc, miscellaneous, huesaturation

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Huesaturation
=============

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-huesaturation.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-huesaturation

.. sidebar:: |kdenlive-show-video| Huesaturation

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      huesaturation
   :**Available**:
      |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      See footnote\ [1]_

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter applies hue-saturation-intensity adjustments to the input video stream.

This filter operates in :abbr:`RGB (Red, Green, Blue)` :term:`color space`.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - av.hue
     - Float
     - Set the :term:`hue` shift in degrees to apply. Allowed range is from -180.000 to 180.000. Default is 0.000.
   * - av.saturation
     - Float
     - Set the :term:`saturation` shift. Allowed range is from -1.000 to 1.000. Default is 0.000.
   * - av.intensity
     - Float
     - Set the intensity shift. Allowed range is from -1.000 to 1.000. Default is 0.000.
   * - av.strength
     - Float
     - Set the strength of filter. Allowed range is from 0.000 to 100.000. Default is 1.000.
   * - av.rw / av.gw / av.bw
     - Float
     - Set weight for each RGB component. Allowed range is from 0.000 to 1.000. By default is set to 0.333, 0.334, 0.333. Those options are used in saturation and lightness\ [1]_ processing.


----

.. [1] Lightness processing not yet implemented
