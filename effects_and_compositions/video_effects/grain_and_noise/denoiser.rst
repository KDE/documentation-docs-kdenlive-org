.. meta::

   :description: Do your first steps with Kdenlive video editor, using denoiser effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, grain and noise, denoiser

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-denoiser:

Denoiser
========

This effect/filter is a high precision/quality 3d de-noise filter. It aims to reduce image noise, producing smooth images and making still images really still. It should enhance compressibility.

The effect has keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-denoiser.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-denoiser

   Denoiser effect

* **Spatial** - Amount of spatial strength to be applied to :term:`luma` and :term:`chroma`

* **Temporal** - Amount of temporal strength to be applied to :term:`luma` and :term:`chroma`

.. rst-class:: clear-both


**Example**

.. |example| raw:: html

   <a href="https://youtu.be/l43Hz7YEcYU" target="_blank">https://youtu.be/l43Hz7YEcYU</a>

Shows usage of Denoiser as well as the following effects: :ref:`effects-chroma_key_basic`, :ref:`effects-alpha_operations` with Shrink Hard, and :ref:`effects-key_spill_mop_up`.

.. note:: **This video is somewhat outdated.** In newer versions of Kdenlive the Key Spill Mop Up effect is installed by default, and it is no longer required to use a composite transition. Nevertheless, the basic steps of chroma keying and key spill mop up are explained and are still valid.

|example|
