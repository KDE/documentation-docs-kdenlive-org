.. meta::

   :description: Kdenlive Video Effects - Normaliz0r
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, normaliz0r

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |wikipedia_normalization| raw:: html

   <a href="https://en.wikipedia.org/wiki/Normalization_(image_processing)" target="_blank">normalization</a>


Normaliz0r
==========

.. figure:: /images/effects_and_compositions/effects-normaliz0r-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-normaliz0r-2504.webp

.. sidebar:: |kdenlive-show-video| Normaliz0r

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      normaliz0r
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter normalizes RGB video (aka histogram stretching, contrast stretching).


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - BlackPt / WhitePt
     - Picker
     - Colors which define the output range. The minimum input value is mapped to the *blackpt*. The maximum input value is mapped to the *whitept*. The defaults are black and white respectively. Specifying white for *blackpt* and black for *whitept* will give color-inverted, normalized video. Shades of grey can be used to reduce the dynamic range (contrast). Specifying saturated colors here can create some interesting effects. Use the |color-picker| color picker or the color button to select the color.
   * - Smoothing
     - Float
     - The number of previous frames to use for temporal smoothing. The input range of each channel is smoothed using a rolling average over the current frame and the smoothing previous frames. The default is 0 (no temporal smoothing).
   * - Independence
     - Float
     - Controls the ratio of independent (color shifting) channel normalization to linked (color preserving) normalization. 0.0 is fully linked, 1.0 is fully independent. Defaults to 1.0 (fully independent).
   * - Strength
     - Float
     - Overall strength of the filter. 1.0 is full strength. 0.0 is a rather expensive no-op. Defaults to 1.0 (full strength).

.. rst-class:: clear-both

.. note::
   The Normaliz0r and :doc:`/effects_and_filters/video_effects/color_image_correction/normalize_rgb_video` effects essentially do the same but produce slightly different results.


.. rubric:: Notes

For more information refer to the Wikipedia article about |wikipedia_normalization|.


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
