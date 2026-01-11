.. meta::

   :description: Kdenlive Video Effects - Interlace Field Order
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, image adjustment, interlace field order

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Interlace Field Order
=====================

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-interlace_field_order.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Interlace Field Order

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      fieldorder
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter transforms the :term:`field order` of the (interlaced) input video.

The transformation is done by shifting the picture content up or down by one line, and filling the remaining line with appropriate picture content. This method is consistent with most broadcast field order converters.

If the input video is not flagged as being :term:`interlaced`, or it is already flagged as being of the required output field order, then this filter does not alter the incoming video.

It is very useful when converting to or from PAL DV material, which is bottom field first.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Field priority
     - Selection
     - Specifies the output field order

The following selection items are available:

:guilabel:`Field priority`

.. list-table::
   :width: 100%
   :widths: 22 78
   :class: table-simple

   * - Top field first
     - Default
   * - Bottom field first
     - 
