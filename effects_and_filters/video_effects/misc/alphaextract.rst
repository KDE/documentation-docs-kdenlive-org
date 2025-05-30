.. meta::

   :description: Kdenlive Video Effects - Alphaextract
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, misc, miscellaneous, alphaextract

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Alphaextract
============

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-alphaextract.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-alphaextract

.. sidebar:: |kdenlive-show-video| Alphaextract

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      alphaextract
   :**Available**:
      |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter extracts the alpha component from the input as a grayscale video. This is especially useful with the :doc:`/effects_and_filters/video_effects/misc/alphamerge` effect/filter.

.. rst-class:: clear-both

If the source does not have an alpha channel, the following error message comes up:

.. figure:: /images/effects_and_compositions/effects-alphaextract_error-2504.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: effects-alphaextract_error-2504.webp

   Alphaextract effect error message
