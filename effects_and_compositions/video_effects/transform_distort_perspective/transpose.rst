.. meta::

   :description: Kdenlive Video Effects - Transpose 
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, transpose

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Transpose
=========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-transpose.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-transpose

.. sidebar:: |kdenlive-show-video| Transpose

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      transpose
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter transposes rows with columns in the clip and optionally flips it. This is useful if a video recorded with a smartphone is imported as a landscape clip.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Direction
     - Selection
     - Set the direction of the transposition
   * - Override if
     - Selection
     - Override the transposition if clip is identified as **Portrait** or **Landscape**. Select **None** if you want to transpose regardless.

The following selection items are available:

:guilabel:`Direction`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - Clock
     - default
   * - Clock flip
     - 
   * - Counter clock
     - 
   * - Counter clock flip
     - 

:guilabel:`Override if`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - None
     - default
   * - Portrait
     - 
   * - Landscape
     - 


.. note:: 
   Many smartphones and digital cameras nowadays set an ``autorotate`` flag in the recorded video. Kdenlive can read the flag, and transposes videos automatically when importing. Check the clip's properties (:ref:`clip_properties`) if you want Kdenlive to handle that differently and set the :guilabel:`Disable autorotate` to any other value than 0 (default) or switch it to **On**.


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