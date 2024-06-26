.. meta::

   :description: Kdenlive Video Effects - Ciescope 
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, utility, ciescope

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


CIE Scope
=========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-ciescope.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-ciescope

.. sidebar:: |kdenlive-show-video| CIE Scope

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      ciescope
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter displays a CIE color diagram with overlaid input pixels.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - av.size / av.s
     - Integer
     - Set CIE Scope size, by default set to 512. [1]_
   * - av.intensity / av.i
     - Float
     - Set intensity used to map input pixel values to CIE diagram [2]_
   * - av.contrast
     - Float
     - Set contrast used to draw tongue colors that are out of active color system gamut
   * - av.gamma
     - Float
     - Correct gamma displayed on scope, by default enabled [3]_


----

.. [1] Only **av.s** is taken into account

.. [2] Only **av.i** is taken into account

.. [3] At the moment this parameter has no effect


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