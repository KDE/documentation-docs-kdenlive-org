.. meta::

   :description: Kdenlive Video Effects - Photosensitivity
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, photosensitivity

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Photosensitivity
================

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-photosensitivity.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-photosensitivity

.. sidebar:: |kdenlive-show-video| Photosensitivity

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      avfilter
   :**Source filter**:
      photosensitivity
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter filters out flashes in the source video that may induce photosensitivity epilepsy (PSE)\ [1]_ seizures.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Bypass
     - Switch
     - Leave frames unchanged. Default is **off**.
   * - Frames to use
     - Integer
     - Set how many frames to use when filtering. Default is 30
   * - Threshold
     - Float
     - Set detection threshold factor. Default is 1. Lower is stricter.
   * - Skip
     - Integer
     - Set how many pixels to skip when sampling frames. Default is 1. Allowed range is from 1 to 1024.


----

.. |pse| raw:: html

   <a href="https://en.wikipedia.org/wiki/Photosensitive_epilepsy" target="_blank">PSE</a>

.. [1] For more details about Photosensitive Epilepsy refer to the |pse| article in Wikipedia
