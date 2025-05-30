.. meta::

   :description: Kdenlive Video Effects - Backgroundkey
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, alpha mask and keying, alpha, mask, keying, backgroundkey

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Backgroundkey
=============

.. figure:: /images/effects_and_compositions/effects-backgroundkey-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-backgroundkey-2504.webp

.. sidebar:: |kdenlive-show-video| Backgroundkey

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
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


.. note::
   This effect/filter works best if the background is somewhat uniform in color. In that regard it works similar to :doc:`Chroma Key</effects_and_filters/video_effects/alpha_mask_keying/chroma_key>` and :doc:`Chroma Key (Advanced)</effects_and_filters/video_effects/alpha_mask_keying/chroma_key_advanced>`, but it is able to work with changing backgrounds.

   The :doc:`Object Mask</effects_and_filters/video_effects/alpha_mask_keying/object_mask>` feature is working much better and allows for more flexibility in mask creation thanks to its use of :abbr:`AI(Artifical Intelligence)` and :abbr:`LLM(Large Language Model)`\ s.