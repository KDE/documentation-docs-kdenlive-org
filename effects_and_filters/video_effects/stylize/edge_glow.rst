.. meta::

   :description: Kdenlive Video Effects - Edge Glow
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, edge glow

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Edge Glow
=========

.. figure:: /images/effects_and_compositions/effects-edge_glow-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-edge_glow-2504.webp

.. sidebar:: |kdenlive-show-video| Edge Glow

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      edgeglow
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No
   :**Color depth**:
      8bit
   :**Tutorial**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter creates an edge glow.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 30 10 60
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Edge lightening threshold
     - Integer
     - Defines the threshold for edge detection. If set to 0 (default), all edges will be detected.
   * - Edge brightness upscaling multiplier
     - Integer
     - Defines the level of brightness in which edges are drawn
   * - Non-edge brightness downscaling multiplier
     - Integer
     - Defines the darkening of areas between edges


For sources with large contiguous areas like a sky or a wall the :guilabel:`Edge lightening threshold` can be used to ignore the small and subtle changes in color or luminance that would otherwise be detected as edges.


.. https://youtu.be/d0MvA_7VuJk

   https://youtu.be/Cl0Z8FXULbQ


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
