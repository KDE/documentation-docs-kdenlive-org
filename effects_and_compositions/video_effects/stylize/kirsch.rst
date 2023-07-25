.. meta::

   :description: Do your first steps with Kdenlive video editor, using kirsch effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, kirsch

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |kirsch| raw:: html

   <a href="https://en.wikipedia.org/wiki/Kirsch_operator" target="_blank">Kirsch operator</a>


.. _effects-kirsch:

Kirsch
======

This effect/filter applies the Kirsch\ [1]_ operator to the input video stream. It detects edges (non-linear edge detector) and, in the default settings, colors them in yellowish green, and colors are somewhat posterized. Compare :ref:`effects-prewitt`, :ref:`effects-roberts` and :ref:`effects-sobel` effects.

The effect has keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-kirsch.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-kirsch

   Kirsch effect

* **Planes** - Set which :term:`planes<plane>` will be processed, unprocessed planes will be copied. Default is **Y**.

* **Scale** - Set value which will be multiplied with filtered result

* **Delta** - Set value which will be added to filtered result

.. rst-class:: clear-both


**Notes**

.. [1] For more (mathematical) details about this refer to the |kirsch| article in Wikipedia.
