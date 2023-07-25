.. meta::

   :description: Do your first steps with Kdenlive video editor, using photosensitivity effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, photosensitivity

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |pse| raw:: html

   <a href="https://en.wikipedia.org/wiki/Photosensitive_epilepsy" target="_blank">PSE</a>


.. _effects-photosensitivity:

Photosensitivity
================

This effect/filter filters out flashes in the source video that may induce photosensitivity epilepsy (PSE)\ [1]_ seizures.

The effect has keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-photosensitivity.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-photosensitivity

   Photosensitivity effect

* **Bypass** - Leave frames unchanged. Default is **off**.

* **Frames to use** - Set how many frames to use when filtering. Default is 30

* **Threshold** - Set detection threshold factor. Default is 1. Lower is stricter.

* **Skip** - Set how many pixels to skip when sampling frames. Default is 1. Allowed range is from 1 to 1024.

.. rst-class:: clear-both


**Notes**

.. [1] For more details about Photosensitive Epilepsy refer to the |pse| article in Wikipedia
