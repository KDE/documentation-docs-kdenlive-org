.. meta::

   :description: Kdenlive Video Effects - Denoiser
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, grain and noise, denoiser

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Denoiser
========

.. figure:: /images/effects_and_compositions/effects-denoiser-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-denoiser-2504.webp

.. sidebar:: |kdenlive-show-video| Denoiser

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      hqdn3d
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter is a high precision/quality 3d de-noise filter. It aims to reduce image noise, producing smooth images and making still images really still. It should enhance compressibility.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Spatial
     - Integer
     - Amount of spatial strength to be applied to :term:`luma` and :term:`chroma`
   * - Temporal
     - Integer
     - Amount of temporal strength to be applied to :term:`luma` and :term:`chroma`

.. rst-class:: clear-both


.. rubric:: Example

.. |example_video| raw:: html

   <a href="https://youtu.be/l43Hz7YEcYU" target="_blank">example video</a>

This |example_video| shows usage of Denoiser as well as the following effects: :doc:`/effects_and_filters/video_effects/alpha_mask_keying/chroma_key`, :doc:`/effects_and_filters/video_effects/alpha_mask_keying/alpha_operations` with Shrink Hard, and :doc:`/effects_and_filters/video_effects/alpha_mask_keying/key_spill_mop_up`.

.. note::
   **The video is somewhat outdated.** In newer versions of Kdenlive the Key Spill Mop Up effect is installed by default, and it is no longer required to use a composite transition. Nevertheless, the basic steps of chroma keying and key spill mop up are explained and are still valid.
