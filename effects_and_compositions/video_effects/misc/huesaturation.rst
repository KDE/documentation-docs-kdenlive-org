.. meta::

   :description: Do your first steps with Kdenlive video editor, using huesaturation effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, misc, miscellaneous, huesaturation

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-huesaturation:

Huesaturation
=============

This effect/filter applies hue-saturation-intensity adjustments to the input video stream.

This filter operates in RGB colorspace.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-huesaturation.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-huesaturation

   Huesaturation effect

* **av.hue** - Set the :term:`hue` shift in degrees to apply. Allowed range is from -180.000 to 180.000. Default is 0.000.

* **av.saturation** - Set the :term:`saturation` shift. Allowed range is from -1.000 to 1.000. Default is 0.000.

* **av.intensity** - Set the intensity shift. Allowed range is from -1.000 to 1.000. Default is 0.000.

* **av.strength** - Set the strength of filter. Allowed range is from 0.000 to 100.000. Default is 1.000.

* **av.rw / av.gw / av.bw** - Set weight for each RGB component. Allowed range is from 0.000 to 1.000. By default is set to 0.333, 0.334, 0.333. Those options are used in saturation and lightness\ [1]_ processing.

.. rst-class:: clear-both


**Notes**

.. [1] Lightness processing not yet implemented
