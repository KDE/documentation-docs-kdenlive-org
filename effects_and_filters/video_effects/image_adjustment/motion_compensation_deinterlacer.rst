.. meta::

   :description: Kdenlive Video Effects - Motion Compensation Deinterlacer
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, image adjustment, motion compensation deinterlacer

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Motion Compensation Deinterlacer
================================

.. figure:: /images/effects_and_compositions/effects-motion_compensation_deinterlacer-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-motion_compensation_deinterlacer-2504.webp

.. sidebar:: |kdenlive-show-video| Motion Compensation Deinterlacer

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      mcdeint
   :**Available**:
      |linux| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter applies motion-compensation deinterlacing.

It needs one field per frame as input and must thus be used together with ``yadif=1/3`` or equivalent.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 23 10 67
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Mode
     - Selection
     - Sets the deinterlacing mode
   * - Picture field parity
     - Selection
     - Sets the picture field parity assumed for the input video
   * - QP
     - Switch
     - Sets the per-block quantizing parameter (QP) used by the internal encoder. Higher values should result in a smoother motion vector field but less optimal individual vectors. Default value is 1.

The following selection items are available:

:guilabel:`Mode`

.. list-table::
   :width: 100%
   :widths: 23 77
   :class: table-wrap

   * - Fast
     - Iterative motion estimation
   * - Medium
     - Iterative motion estimation (default)
   * - Slow
     - Iterative motion estimation
   * - Extra slow
     - Iterative motion estimation using multiple reference frames

:guilabel:`Picture field parity`

.. list-table::
   :width: 100%
   :widths: 23 77
   :class: table-wrap

   * - Top field first
     - 
   * - Bottom field first
     - default


.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Icons used here (remove comment indent to enable them for this document)
   
   .. |linux| image:: /images/icons/linux.png
   :width: 14px
   :alt: Linux
   :class: no-scaled-link

   .. |appimage| image:: /images/icons/kdenlive-appimage_3.svg
   :width: 14px
   :alt: appimage
   :class: no-scaled-link

   .. |windows| image:: /images/icons/windows.png
   :width: 14px
   :alt: Windows
   :class: no-scaled-link

   .. |apple| image:: /images/icons/apple.png
   :width: 14px
   :alt: MacOS
   :class: no-scaled-link
