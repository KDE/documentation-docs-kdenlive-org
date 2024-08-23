.. meta::

   :description: Kdenlive Video Effects - Set Range
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, image adjustment, set range

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Set Range
=========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-set_range.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-set_range

.. sidebar:: |kdenlive-show-video| Set Range

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      setrange
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter forces color range for the output video frame.

The filter marks the color range property for the output frames. It does not change the input frame, but only sets the corresponding property, which affects how the frame is treated by following filters.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 15 65
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Set range
     - Selection
     - Define the property for the output frame


The following selection items are available:

:guilabel:`Set range`

.. list-table::
   :width: 100%
   :widths: 35 65
   :class: table-simple

   * - auto
     - Keep the same color range property (default)
   * - unspecified / unknown
     - Set the color range as unspecified
   * - limited / tv / mpeg
     - Set the color range as limited
   * - full / pc / jpeg
     - Set the color range as full
