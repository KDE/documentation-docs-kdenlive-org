.. meta::

   :description: Kdenlive Video Effects - Chroma Hold
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, chroma hold

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |chromahold| raw:: html

   <a href="https://ffmpeg.org/ffmpeg-filters.html#chromahold" target="_blank">chromahold</a>


.. https://youtu.be/dXnFsOjS734


Chroma Hold
===========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-chroma_hold.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-chroma_hold

.. sidebar:: |kdenlive-show-video| Chroma Hold

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      avfilter
   :**Source filter**:
      |chromahold|
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect removes all color information for all colors except the selected one.


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
     - Similarity percentage with the selected color. 0.01 matches only the exact key color, 1.0 matches everything.
   * - Blend
     - Float
     - Blend percentage. 0.0 makes pixels either fully grey, or not grey at all. Higher values result in more preserved color
   * - For YUV color
     - Switch
     - Select this if the clip has YUV data instead of RGB
   * - Color key
     - Picker
     - Select the color to be preserved (held) using the |color-picker| color picker or by clicking the color bar

.. rst-class:: clear-both


.. note:: 
   This effect is not as effective and easy to apply as the :doc:`/effects_and_compositions/video_effects/color_image_correction/chroma_keep` effect.


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
