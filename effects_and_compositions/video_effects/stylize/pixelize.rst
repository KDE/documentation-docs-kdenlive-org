.. meta::

   :description: Kdenlive Video Effects - Pixelize
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, pixelize

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Pixelize
========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-pixelize.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-pixelize

.. sidebar:: |kdenlive-show-video| Pixelize

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

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter pixelizes the input image. It works similar to the :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/obscure` effect but allows you to control the block size individually and independently from the image size, but by contrast applies it to the entire frame. In order to apply the **Pixelize** effect only to a certain region use it in combination with the :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/alpha_shapes_mask` effect.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Block Size X
     - Integer
     - Horizontal size of one "pixel"
   * - Block Size Y
     - Integer
     - Vertical size of one "pixel"


.. note::
    The :guilabel:`Block Size` takes the aspect ratio into account. That means that in a 16:9 project, the ratio of the two values has to be 16:9 in order to produce square pixels. Otherwise, identical values will produce rectangles.
