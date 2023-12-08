.. meta::

   :description: Kdenlive Video Effects - Phase
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, image adjustment, phase

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Phase
=====

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-phase.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-phase

.. sidebar:: |kdenlive-show-video| Phase

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      avfilter
   :**Source filter**:
      phase
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter delays interlaced video by one field time so that the field order changes.

The intended use is to fix PAL movies that have been captured with the opposite field order to the film-to-video transfer.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 15 65
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Mode
     - Selection
     - Set the phase mode

The following selection items are available:

:guilabel:`Mode`

.. list-table::
   :width: 100%
   :widths: 35 65
   :class: table-simple

   * - Delay the top field
     - Capture field order bottom-first, transfer top-first. Filter will delay the top field.
   * - Delay the bottom field
     - Capture field order top-first, transfer bottom-first. Filter will delay the bottom field. This is the default mode.
   * - Keep the field order
     - Capture and transfer with the same field order. This mode only exists for the documentation of the other options to refer to, but if you actually select it, the filter will faithfully do nothing.
   * - Capture field order automatically and transfer opposite
     - Filter selects among **Delay Top** and **Delay bottom** modes on a frame by frame basis using field flags. If no field information is available, then this works just like **Capture Unknown**.
   * - Capture unknown or varying and transfer opposite
     - Filter selects among **Delay Top** and **Delay bottom** on a frame by frame basis by analyzing the images and selecting the alternative that produces best match between the fields.
   * - Capture top-first and transfer unknown or varying
     - Filter selects among **Delay bottom** and **Keep order** using image analysis.
   * - Capture bottom-first and transfer unknown or varying
     - Filter selects among **Delay Top** and **Keep order** using image analysis.
   * - Capture determined by field flags and transfer unknown or varying
     - Filter selects among **Delay bottom**, **Delay Top** and **Keep order** using field flags and image analysis. If no field information is available, then this works just like **Both capture**.
   * - Both capture and transfer unknown or varying
     - Filter selects among **Delay bottom**, **Delay Top** and **Keep order** using image analysis only.
