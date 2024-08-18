.. meta::

   :description: Kdenlive Video Effects - Chroma Keep
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, chroma keep

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. .. |color-picker| image:: /images/icons/color-picker.svg
   :width: 22px
   :class: no-scaled-link


.. https://youtu.be/dXnFsOjS734


Chroma Keep
===========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-chroma_keep.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-chroma_keep

.. sidebar:: |kdenlive-show-video| Chroma Keep

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      chroma_hold
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect turns the clip into grey scale except for the selected color.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Variance
     - Percent
     - Percentage of deviation from the selected color value. Lower values keep the colors closer to the selected one; higher values include more colors.
   * - Color key
     - Picker
     - Set the color to be preserved (kept)

.. rst-class:: clear-both


.. hint:: 
   This effect is much more effective and easier to apply than the :doc:`/effects_and_filters/video_effects/color_image_correction/chroma_hold` effect.
