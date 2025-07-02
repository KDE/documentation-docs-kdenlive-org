.. meta::

   :description: Kdenlive Video Effects - Pixelize (basic)
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, pixeliz0r

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Pixelize (basic)
================

.. figure:: /images/effects_and_compositions/effects-pixeliz0r-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-pixeliz0r-2504.webp

.. sidebar:: |kdenlive-show-video| Pixelize (basic)

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      pixeliz0r
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No
   :**Color depth**:
      8bit
   :**Tutorial**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter pixelizes the input image. It works similar to the :doc:`/effects_and_filters/video_effects/alpha_mask_keying/obscure` effect but allows you to control the block size individually and independently from the image size, but by contrast applies it to the entire frame. In order to apply the effect only to a certain region use it in combination with the :doc:`/effects_and_filters/video_effects/alpha_mask_keying/alpha_shapes_mask` effect.

See also :doc:`/effects_and_filters/video_effects/stylize/pixelize`.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Block Width
     - Integer
     - Horizontal size of one "pixel"
   * - Block Height
     - Integer
     - Vertical size of one "pixel"

.. note:: 
   You can set the block size independently from each other generating elongated pixels. In order to produce square pixels you need to take the aspect ratio of your project into account. The default values are already with the correct aspect ratio.