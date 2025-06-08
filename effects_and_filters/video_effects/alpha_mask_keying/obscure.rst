.. meta::

   :description: Kdenlive Video Effects - Obscure
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, alpha, mask, keying, obscure

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Obscure
-------

.. figure:: /images/effects_and_compositions/effects-obscure-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-obscure-2504.webp

.. sidebar:: |kdenlive-show-video| Obscure

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      MLT
   :**Source filter**:
      obscure
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

Hide a region of the clip by pixelizing it (obscure). The effect's pixelization cannot be adjusted and may therefore not work satisfactorily with all source material. Compare the :doc:`/effects_and_filters/video_effects/stylize/pixelize` effect.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Position X / Y
     - Integer
     - X and Y coordinates of the area (in pixels) to be obscured (pixelated)
   * - Size W / H
     - Integer
     - Width and Height of the area (in pixels) to be obscured (pixelated)
   * - Scale
     - Percentage
     - Determines the size of the area. Can also be changed via the rectangle's coordinates and dimensions.


.. rubric:: Notes

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-obscure_1.webp
   :align:  left
   :width: 400px
   :figwidth: 400px
   :alt: kdenlive2304_effects-obscure

   Obscure effect panel and results (default settings)

Use the handles on the red rectangle\ [1]_ in the Project Monitor to change the size: use the center handle to move the rectangle around.

The `Align` buttons can be used to align the red rectangle with the left, vertical center, right, top, horizontal center, bottom edge of the clip, respectively. You can also adjust to original size, adjust to and center in frame, fit width, and fit height.

.. rst-class:: clear-both


----

.. [1] If you do not see a red rectangle in the Project Monitor, enable Edit Mode by clicking on the |edit-mode| icon in the Project Monitor toolbar


.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Icons used here (remove comment indent to enable them for this document)
   
   .. |edit-mode| image:: /images/icons/kdenlive-edit-mode.svg
   :width: 22px
   :class: no-scaled-link

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
