.. meta::

   :description: Kdenlive Video Effects - Binarize 
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, binarize

.. metadata-placeholder

   :authors: - Roger (https://userbase.kde.org/User:Roger)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Binarize
========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-binarize.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-binarize

.. sidebar:: |kdenlive-show-video| Binarize\ [1]_

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      threshold
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter creates a monochrome (black & white) image based on the threshold value.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Use transparency
     - 
     - If selected, compares the midpoint (set by :guilabel:`Threshold value`) with the alpha channel instead of :term:`luma`
   * - Threshold value
     - 
     - Set the threshold (midpoint)

----

.. |threshold| raw:: html

   <a href="https://ffmpeg.org/ffmpeg-filters.html#threshold" target="_blank">ffmpeg.threshold</a>

.. [1] This is the |threshold| filter that used to be called *Threshold*
