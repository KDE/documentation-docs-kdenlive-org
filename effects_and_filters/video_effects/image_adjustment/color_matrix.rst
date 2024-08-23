.. meta::

   :description: Kdenlive Video Effects - Color Matrix
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, image adjustment, color matrix

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |color_space_descriptions| raw:: html

   <a href="https://www.kernel.org/doc/html/v4.9/media/uapi/v4l/pixfmt-007.html" target="_blank">color space descriptions</a>


Color Matrix
============

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-color_matrix.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-color_matrix

.. sidebar:: |kdenlive-show-video| Color Matrix

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      svfilter
   :**Source filter**:
      colormatrix
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter converts the :term:`color matrix`.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Source color Matrix
     - Selection
     - 
   * - Destination color Matrix
     - Selection
     - 

The following selection items are available:

:guilabel:`Source color Matrix` :guilabel:`Destination color Matrix`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - bt709
     - 
   * - fcc
     - 
   * - bt601
     - 
   * - bt470
     - 
   * - bt470bg
     - 
   * - smpte170m
     - 
   * - smpte240m
     - 
   * - bt2020
     - 

For the technical inclined there is a list of detailed |color_space_descriptions| available in the Linux Kernel documentation.
