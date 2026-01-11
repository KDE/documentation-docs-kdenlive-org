.. meta::

   :description: Kdenlive Video Effects - Interleave - Deinterleave
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, image adjustment, interleave - deinterleave

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Interleave - Deinterleave
=========================

.. figure:: /images/effects_and_compositions/effects-interleave-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Interleave - Deinterleave

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      il
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter interleaves or de-interleaves fields. It allows one to process interlaced image fields without deinterlacing them. De-interleaving splits the input frame into 2 fields (so-called half pictures). Odd lines are moved to the top half of the output image, even lines to the bottom half. You can process (filter) them independently and then re-interleave them.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Luma / Chroma / Alpha Mode
     - Selection
     - Set the action for the various channels. Default is **none**
   * - Swap Luma / Chroma / Alpha fields
     - Switch
     - Swap :term:`luma`, :term:`chroma` or alpha fields, Exchanges even and odd lines. Default is **off**.

The following selection items are available:

:guilabel:`Luma / Chroma / Alpha Mode`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - None
     - do nothing
   * - Deinterleave
     - Deinterleave fields, placing one above the other
   * - Interleave
     - Interleave fields; reverse the effect of deinterleaving
