.. meta::

   :description: Kdenlive Video Effects - Pixelize (advanced)
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, pixelize, advanced, 10bit

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Pixelize (advanced)
===================

.. figure:: /images/effects_and_compositions/effects-pixelize-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Pixelize (basic)

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      avfilter
   :**Source filter**:
      pixelize
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No
   :**Color depth**:
      10bit |color-management|
   :**Tutorial**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter pixelizes the input image. It works similar to the :doc:`/effects_and_filters/video_effects/alpha_mask_keying/obscure` effect but allows you to control the block size individually and independently from the image size, but by contrast applies it to the entire frame. In order to apply the effect only to a certain region use it in combination with the :doc:`/effects_and_filters/video_effects/alpha_mask_keying/alpha_shapes_mask` effect.

The result is the same as using the :doc:`/effects_and_filters/video_effects/stylize/pixeliz0r` effect, but **Pixelize (advanced)** allows to choose the pixelization mode and which color channel to apply the pixelization to.

.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Pixelize Mode
     - Selection
     - Defines the mode of pixelization used. Default is **Average**
   * - Planes
     - Selection
     - Defines what planes to filter. Default is **All**
   * - Block Width
     - Integer
     - Horizontal size of one "pixel"
   * - Block Height
     - Integer
     - Vertical size of one "pixel"
