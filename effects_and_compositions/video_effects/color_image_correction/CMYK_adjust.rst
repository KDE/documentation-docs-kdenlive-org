.. meta::

   :description: Do your first steps with Kdenlive video editor, using the CMYK Adjust effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, CMYK adjust

   :authors: - Bernd Jordan

   :license: Creative Commons License SA 4.0

.. _effect-cmyk_adjust:

CMYK Adjust
===========

This effect applies CMYK [1]_ adjustments to specific color ranges [2]_. The adjustment range is defined by the "purity" of the color (i.e. how saturated it already is).

This effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-cmyk_adjust.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-cmyk_adjust

   CMYK Adjust effect

* **Correction Method** - Select the color correction method: *Absolute* (specified adjustments are applied "as-is"), *relative* (specified adjustments are relative to the original component value). Default is *absolute*.

* **Reds** - Adjustments for red pixels (pixels where the red component is the maximum)

* **Yellows** - Adjustments for yellow pixels (pixels where the blue component is the minimum)

* **Greens** - Adjustments for green pixels (pixels where the green component is the maximum)

* **Cyans** - Adjustments for cyan pixels (pixels where the red component is the minimum)

* **Blues** - Adjustments for blue pixels (pixels where the blue component is the maximum)

* **Magentas** - Adjustments for magenta pixels (pixels where the green component is the minimum)

* **Whites** - Adjustments for white pixels (pixels where all component are greater then 128)

* **Neutrals** - Adjustments for all pixels except pure black and pure white

* **Blacks** - Adjustments for black pixels (pixels where all component are less then 128)

.. rst-class:: clear-both


**Notes**

.. [1] CMYK stands for Cyan, Magenta, Yellow, Black

.. [2] Color ranges are "reds", "yellows", "greens", etc.
