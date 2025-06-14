.. meta::

   :description: Kdenlive Video Effects - 3-Point Balance
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, 3-point balance, three point balance

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Mmaguire (https://userbase.kde.org/User:Mmaguire)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


3-Point Balance
===============

.. figure:: /images/effects_and_compositions/effects-3_point_balance-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-3_point_balance-2504.webp

.. sidebar:: |kdenlive-show-video| 3-Point Balance

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      three_point_balance
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect is a simple implementation of the Bezier Curves effect. With the simplified interface you select the shades of grey using the |color-picker| color picker for Black Level, Grey Level and White Level, or use the color selection buttons.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Black color
     - Picker
     - Represents the black levels (dark tones) for the clip
   * - Gray color
     - Picker
     - Represents the grey levels (mid tones) for the clip
   * - White color
     - Picker
     - Represents the white levels (highlights) for the clip


.. .. versionchanged:: 25.04
   removed
   * - Split screen preview
     - Switch
     - Select this to have a split screen in the Project Monitor where you can compare the results of the effect/filter with the original clip.
   * - Source image on left side
     - Switch
     - If :guilabel:`Split screen preview` is enabled, the original clip is on the left side of the split screen. Uncheck this to have the original on the right-hand side of the split screen.


.. rubric:: Notes

.. seealso::  
   :doc:`/effects_and_filters/video_effects/color_image_correction/bezier_curves` effect


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
