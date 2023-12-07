.. meta::

   :description: Kdenlive Video Effects - Position and Zoom
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, position and zoom, pan and zoom

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jack (https://userbase.kde.org/User:Jack)
             - Roger (https://userbase.kde.org/User:Roger)
             - Smolyaninov (https://userbase.kde.org/User:Smolyaninov)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Position and Zoom
=================

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-position_and_zoom.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-position_and_zoom

.. sidebar:: |kdenlive-show-video| EFFECT_NAME

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      MLT
   :**Source filter**:
      affine
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      Yes (see warning)

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter allows to adjust size and position of the clip using smooth affine transformations. Formerly known as *Pan and Zoom*.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Distort
     - Switch
     - Determines whether the image aspect ratio will be distorted while scaling to completely fill the rectangle
   * - Normalise
     - Switch
     - Use the video resolution instead of the project resolution
   * - X / Y / W / H / Size
     - Various
     - This is where the action is for *Position* (X, Y) and *Zoom* (Size)
   * - Background Color
     - Picker
     - Define the background color to be used when zooming out reveals the background. Default is Alpha.


.. warning:: 
   As of this writing and in version 23.04 there are many confirmed reports that the compositing of clips using the **Position and Zoom** effect does not work properly and leaves artifacts. A bug report has been created, and until it is fixed use the :doc:`/effects_and_compositions/video_effects/transform_distort_perspective/transform` effect instead.


.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. The following section needs a decision whether to keep it here, move it to the Tips&Tricks section, or delete it

   In this example we have two keyframes in the pan and zoom, one at the beginning and one at the end. Size is 25% at the start keyframe and 100% at the end. The images are centered on the screen at both keyframes.

   https://youtu.be/0aSe1y6e4RE

   See also this :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/chroma_key` that describes how to use:

   * Alpha Manipulation -> :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/chroma_key`
   * :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/rotoscoping`
   * :ref:`composite`
   * Crop and Transform -> Pan and Zoom effect
   * Enhancement -> :doc:`/effects_and_compositions/video_effects/blur_and_sharpen`
   * Alpha Manipulation -> :doc:`/effects_and_compositions/video_effects/alpha_mask_keying/alpha_operations`

   `Tutorial: How to do pan and zoom with Kdenlive video editor - Peter Thomson(YouTube) <https://youtu.be/B8ZPoWaxQrA>`_
