.. meta::

   :description: Kdenlive Video Effects - Color Hold
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, color hold

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. .. versionchanged:: 25.04
   no keyframes

   
Color Hold
==========

.. figure:: /images/effects_and_compositions/effects-color_hold-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-color_hold-2504.webp

.. sidebar:: |kdenlive-show-video| Color Hold

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      colorhold
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter removes all color information for all RGB colors except for the selected one.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Similarity
     - Float
     - Similarity percentage with the above color. 0.01 matches only the exact key color, while 1.0 matches everything.
   * - Blend
     - Float
     - Blend percentage. 0.0 makes pixels fully gray. Higher values result in more preserved color.
   * - Color key
     - Picker
     - The color which will not be replaced with neutral gray. Use the |color-picker| color picker or the color button to select the color to hold.


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

   .. |color-picker| image:: /images/icons/color-picker.svg
   :width: 22px
   :class: no-scaled-link
