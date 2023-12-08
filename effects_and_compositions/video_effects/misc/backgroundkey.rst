.. meta::

   :description: Kdenlive Video Effects - Backgroundkey
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, misc, miscellaneous, backgroundkey

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Backgroundkey
=============

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-backgroundkey.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-backgroundkey

.. sidebar:: |kdenlive-show-video| Backgroundkey

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      backgroundkey
   :**Available**:
      |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter turns a static background into transparency.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - av.threshold
     - Float
     - Threshold for scene change detection
   * - av.similarity
     - Float
     - Similarity percentage with the background
   * - av.blend
     - Float
     - Sets the blend amount for pixels that are not similar
