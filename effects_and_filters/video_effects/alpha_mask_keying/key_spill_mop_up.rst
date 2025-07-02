.. meta::

   :description: Kdenlive Video Effects - Key Spill Mop-up
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, alpha, mask, keying, chroma key, greenscreen, bluescreen, key spill mop-up

.. metadata-placeholder

   :authors: - TheMickyRosen-Left (https://userbase.kde.org/User:TheMickyRosen-Left)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Key Spill Mop Up
================

.. figure:: /images/effects_and_compositions/effects-key_spill_mop_up-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-key_spill_mop_up-2504.webp

.. sidebar:: |kdenlive-show-video| Key Spill Mop-up

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      keyspillm0pup
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No
   :**Color depth**:
      8bit
   :**Tutorial**:
      :ref:`Yes <tutorials-key_spill_mop_up>` |view-presentation|

.. rst-class:: clear-both


.. rubric:: Description

This effect is used in combination with chroma keying (otherwise known as Greenscreen or Bluescreen). Its purpose is to compensate for the fact that sometimes the color from the green or blue screen reflects onto the subject and will make them a shade of blue or green especially around the edges. This is known as "key spill". This effect can attempt to compensate for this issue.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 10 65
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Mask type
     - Selection
     - Selects the type of mask that will determine where the color altering operations will occur
   * - Operation 1
     - Selection
     - Selects which of the four possible operations will be done on the mask-selected pixels. Apart from no operation, there are four possibilities: De-key, Target, De-saturate and Luma adjust.
   * - Operation 2
     - Selection
     - Enable a second operation to be performed with the same mask
   * - Show mask
     - Switch
     - This will show the selected mask as a greyscale image, to help with fine tuning of the masks. Should be OFF for the final render.
   * - Mask to Alpha
     - Switch
     - Copies the active mask to the alpha channel. For all normal spill cleaning operations, this should be OFF. By setting it ON, the Key Spill Mop Up itself can be used as a keyer, or to generate some special effects.
   * - Key color
     - Picker
     - This should be the same or similar to the key color used for the preceding keying operation. Use the color bar or pipette to select the color.
   * - Target color
     - Picker
     - This is only used when "Target" is selected for operation 1 or 2 and used with one of the masks. The colors in the affected areas will be moved towards this color, according to the "Amount 1" and "Amount 2" parameter, respectively.
   * - Tolerance
     - Integer
     - For the color difference mask, the range of colors around the key, that will be 100% affected. For the transparency mask, the "amplification". For the edge mask, the width of the affected area.
   * - Slope
     - Integer
     - For the color difference mask, the range of colors outside of "Tolerance", that will be gradually less affected. No function for the transparency and edge masks.
   * - Hue gate
     - Integer
     - Reduces the mask according to difference from key hue, to prevent change to pixels that are within the mask, but not polluted by key.
   * - Saturation threshold
     - Integer
     - Reduces the mask according to color saturation, to avoid affecting the neutral areas.
   * - Amount 1
     - Integer
     - The amount of the selected operation 1, how much the colors will change.
   * - Amount 2
     - Integer
     - The amount of the selected operation 2, how much the colors will change.

The following selection items are available:

:guilabel:`Mask type`

.. list-table::
   :width: 100%
   :widths: 25 75
   :class: table-simple

   * - Color distance
     - 
   * - Transparency
     - 
   * - Edge inwards
     - 
   * - Edge outwards
     - 

Color difference masks are based on the color of the image, and do not depend on the alpha from the preceding keying, except for ignoring the 100% transparent areas, to increase speed.

Transparency and Edge masks are based on the alpha channel from the preceding chroma keying operation. Transparency masks will affect only the parts that are neither 100% opaque nor 100% transparent, based on the alpha values from the preceding keying operation. The effect will be proportional to the transparency.

.. note:: If a "hard key" was used in the preceding chroma keying effect, there will be no areas that :guilabel:`Transparency` operations could affect. Edge masks will affect only pixels close to the edge, with the effect diminishing away from the edge. The outer edge is the edge of the fully opaque part, where the alpha from the preceding keying is 1.0 (255).

.. note:: The edge masking algorithm is not yet what the author of the filter would like it to be. They will have to look some more into this, and improve it, so consider it a "temporary solution" that will change in the future.

All masks can be further pruned with two parameters: a :guilabel:`Hue gate`, which will limit the mask to hues close to the key hue, and a :guilabel:`Saturation threshold`, which will limit the mask to areas with color saturation above a threshold.


:guilabel:`Operation 1/2`

.. list-table::
   :width: 100%
   :widths: 25 75
   :class: table-simple

   * - None
     - Default for :guilabel:`Operation 2`
   * - De-Key
     - Default for :guilabel:`Operation 1`
   * - Target
     - 
   * - Desaturate
     - 
   * - Luma adjust
     - 


.. rubric:: Notes

This effect can be cascaded, but it is not possible to get the same color based mask in the second instance, because the colors will be changed by the first instance. To enable two operations with the same mask, each effect instance can do two operations. With transparency and edge masks, cascading is a bit easier. If the hue gate and saturation threshold are not used, transparency and edge masks can be exactly the same in cascaded effects.


**Tutorial**

.. |tutorial_1| raw:: html

   <a href="https://youtu.be/l43Hz7YEcYU" target="_blank">tutorial</a>

This |tutorial_1| shows usage of the following effects: :doc:`Key Spill Mop Up </effects_and_filters/video_effects/alpha_mask_keying/key_spill_mop_up>`, blue screen (now called :doc:`Chroma Key: Basic </effects_and_filters/video_effects/alpha_mask_keying/chroma_key>`), :doc:`Alpha Operations </effects_and_filters/video_effects/alpha_mask_keying/alpha_operations>` using Shrink Hard and :doc:`/effects_and_filters/video_effects/grain_and_noise/denoise_hqdn3d`.

.. note:: **This video is somewhat outdated.** In newer versions of Kdenlive the Key Spill Mop Up effect is installed by default, and it is no longer required to use a composite transition. Nevertheless, the basic steps of chroma keying and keyspill mop up are explained and are still valid.
