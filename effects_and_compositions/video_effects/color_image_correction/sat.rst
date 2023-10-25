.. meta::

   :description: Do your first steps with Kdenlive video editor, using sop/sat effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, sop/sat, slope offset power saturation

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Mmaguire (https://userbase.kde.org/User:Mmaguire)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |cdl_explained| raw:: html

   <a href="https://lowepost.com/courses/blog/color-decision-list-explained-r30/" target="_blank">Color Decision List Explained</a>

.. .. |infty| image:: /icons/infinity.webp


.. _effects-sop_sat:

SOP/Sat Effect
==============

This effect/filter changes Slope, Offset, and Power of the color components, and the overall Saturation, according to the ASC CDL (Color Decision List)\ [1]_

The effect has keyframes.

Changing the slope means multiplying the pixel value with a constant value. Black pixels will remain black, while brighter ones will be changed. All effects can be observed well when applied on a greyscale gradient and looking at the :ref:`view-rgb_parade`.

You can use this effect to achieve proper white balance.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-sop_sat.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-sop_sat

   SAP/Sat effect

* **Slope R / G / B / @** - Slope is the multiplier to the incoming data in the respective color channels. Allowed values are from 0 to 1000, default is 50.

* **Offset R / G / B / @** - Offset is a summation to the incoming data in the respective color channels. Allowed values are from 0 to 2048, default is 1024.

* **Power R / G / B / @** - Power is a power function (i.e. 2\ :sup:`2`) to the incoming data in the respective color channels. Allowed values are from 0 to 1000, default is 50.

* **Overall Saturation** - Changes the overall :term:`saturation`. Allowed values are from 0 to 1000, default is 100.

.. rst-class:: clear-both


This filter implements a standard way of color correction proposed by the American Society of Cinematographers: The Color Decision List, also known as the ASC :abbr:`CDL (Color Decision List)`\ [1]_ with the goal to exchange rudimentary color correction information between post-production tools.

The ASC CDL is a standard format for basic primary color correction (primary meaning affecting the whole image and not only selected parts).

Basically there are two stages in the correction:

1. SOP correction for each channel separately
2. Overall saturation correction

All corrections work on [0,1], so the RGB(A) values need to be transposed from [0,...,255] to [0,1].

1. SOP correction

   * Slope:   ``out = in * slope;   0 <= slope < ∞``
   * Offset:  ``out = in + offset;  -∞ < offset < ∞``
   * Power:   ``out = in^power;     0 < power < ∞``

2. Saturation

   * Luma:    ``Y = 0.2126 R + 0.7152 G + 0.0722 B`` (according to Rec. 709)
   * For all channels: ``out = luma + sat * (in-luma)``

As the values may exceed 1 (or 0), they need to be clipped where necessary.


**Notes**

.. [1] More details can be found in this article: |cdl_explained|.

See the Tips & Tricks chapter :ref:`scopes-waveform_and_rgb_parade` where this effect is used to adjust the white balance of a clip.