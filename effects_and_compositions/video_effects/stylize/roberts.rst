.. meta::

   :description: Do your first steps with Kdenlive video editor, using roberts effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, roberts

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |roberts| raw:: html

   <a href="https://en.wikipedia.org/wiki/Roberts_cross" target="_blank">Roberts Cross</a>


.. _effects-roberts:

Roberts
=======

This effect/filter applies the Roberts cross operator\ [1]_ to the input video stream. It detects edges (differential operator) and, in the default settings, colors them white and grainy. Compare :ref:`effects-kirsch`, :ref:`effects-prewitt` and :ref:`effects-sobel` effects.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-roberts.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-roberts

   Roberts effect

* **Planes** - Set which :term:`planes<plane>` will be processed, unprocessed planes will be copied. Default is **YUV**.

* **Scale** - Set value which will be multiplied with filtered result

* **Delta** - Set value which will be added to filtered result

.. rst-class:: clear-both


**Notes**

.. [1] For more details refer to the |roberts| article in Wikipedia
