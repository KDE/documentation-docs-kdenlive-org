.. meta::

   :description: Do your first steps with Kdenlive video editor, using prewitt effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, prewitt

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |prewitt| raw:: html

   <a href="https://en.wikipedia.org/wiki/Prewitt_operator" target="_blank">Prewitt Operator</a>


.. _effects-prewitt:

Prewitt
=======

This effect/filter applies the Prewitt\ [1]_ operator to the input video stream. It detects edges (discrete differentiation operator) and, in the default settings, colors them white and pinkish. Compare :ref:`effects-kirsch`, :ref:`effects-roberts` and :ref:`effects-sobel` effects.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-prewitt.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-prewitt

   Prewitt effect

* **Planes** - Set which :term:`planes<plane>` will be processed, unprocessed planes will be copied. Default is **YUV**.

* **Scale** - Set value which will be multiplied with filtered result

* **Delta** - Set value which will be added to filtered result

.. rst-class:: clear-both


**Notes**

.. [1] For more details refer to the |prewitt| article in Wikipedia
