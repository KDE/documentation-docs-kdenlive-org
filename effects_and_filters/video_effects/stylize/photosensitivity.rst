.. meta::

   :description: Kdenlive Video Effects - Photosensitivity Filter
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, photosensitivity filter, 10bit

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Photosensitivity Filter
=======================

.. figure:: /images/effects_and_compositions/effects-photosensitivity-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Photosensitivity Filter

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
   :**Color depth**:
      10bit |color-management|
   :**Tutorial**:
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
