.. metadata-placeholder

   :authors: - TheMickyRosen-Left (https://userbase.kde.org/User:TheMickyRosen-Left)
             - Bernd Jordan

   :license: Creative Commons License SA 4.0

.. _effects-key_spill_mop_up:

Key Spill Mop Up
================

This effect is used in combination with chroma keying (otherwise known as Greenscreen or Bluescreen). Its purpose is to compensate for the fact that sometimes the color from the green or blue screen reflects onto the subject and will make them a shade of blue or green especially around the edges. This is known as "key spill". This effect can attempt to compensate for this issue.


**Parameters**

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-key_spill_mop_up.webp
   :width: 80%
   :alt: kdenlive2304_effects-key_spill_mop_up

   Key Spill Mop Up effects panel

:guilabel:`Mask type`: Selects the type of mask that will determine where the color altering operations will occur.

:guilabel:`Operation 1`: Selects which of the four possible operations will be done on the mask-selected pixels. Apart from no operation, there are four possibilities: De-key, Target, De-saturate and Luma adjust.

:guilabel:`Operation 2`: Enable a second operation to be performed with the same mask.

:guilabel:`Show mask`: This will show the selected mask as a greyscale image, to help with fine tuning of the masks. Should be OFF for the final render.

:guilabel:`Mask to Alpha`: Copies the active mask to the alpha channel. For all normal spill cleaning operations, this should be OFF. By setting it ON, the Key Spill Mop Up itself can be used as a keyer, or to generate some special effects.

:guilabel:`Key color`: This should be the same or similar to the key color used for the preceding keying operation. Use the color bar or pipette to select the color.

:guilabel:`Target color`: This is only used when "Target" is selected for operation 1 or 2 and used with one of the masks. The colors in the affected areas will be moved towards this color, according to the "Amount 1" and "Amount 2" parameter, respectively.

:guilabel:`Tolerance`: For the color difference mask, the range of colors around the key, that will be 100% affected. For the transparency mask, the "amplification". For the edge mask, the width of the affected area.

:guilabel:`Slope`: For the color difference mask, the range of colors outside of "Tolerance", that will be gradually less affected. No function for the transparency and edge masks.

:guilabel:`Hue gate`: Reduces the mask according to difference from key hue, to prevent change to pixels that are within the mask, but not polluted by key.

:guilabel:`Saturation threshold`: Reduces the mask according to color saturation, to avoid affecting the neutral areas.

:guilabel:`Amount 1`: The amount of the selected operation 1, how much the colors will change.

:guilabel:`Amount 2`: The amount of the selected operation 2, how much the colors will change.


**Masks**

Color difference masks are based on the color of the image, and do not depend on the alpha from the preceding keying, except for ignoring the 100% transparent areas, to increase speed.

Transparency and Edge masks are based on the alpha channel from the preceding chroma keying operation. Transparency masks will affect only the parts that are neither 100% opaque nor 100% transparent, based on the alpha values from the preceding keying operation. The effect will be proportional to the transparency.

.. note:: If a "hard key" was used in the preceding chroma keying effect, there will be no areas that T operations could affect. Edge masks will affect only pixels close to the edge, with the effect diminishing away from the edge. The outer edge is the edge of the fully opaque part, where the alpha from the preceding keying is 1.0 (255).

.. note:: The edge masking algorithm is not yet what the author of the filter would like it to be. They will have to look some more into this, and improve it, so consider it a "temporary solution" that will change in the future.

All masks can be further pruned with two parameters: an "hue gate", which will limit the mask to hues close to the key hue, and an "saturation threshold", which will limit the mask to areas with color saturation above a threshold.

**Cascading**

This effect can be cascaded, but it is not possible to get the same color based mask in the second instance, because the colors will be changed by the first instance. To enable two operations with the same mask, each plugin instance can do two operations. With transparency and edge masks, cascading is a bit easier. If the hue gate and saturation threshold are not used, transparency and edge masks can be exactly the same in cascaded effects.


**Tutorial**

.. |tutorial_1| raw:: html

   <a href="https://youtu.be/l43Hz7YEcYU" target="_blank">https://youtu.be/l43Hz7YEcYU</a>

This tutorial shows usage of the following effects: :ref:`Key Spill Mop Up <effects-key_spill_mop_up>`, blue screen (now called :ref:`Chroma Key: Basic <effects-chroma_key_basic>`), :ref:`Alpha Operations <effects-alpha_operations>` using Shrink Hard and :ref:`denoiser`.

.. note:: **This video is somewhat outdated.** In newer versions of Kdenlive the Key Spill Mop Up effect is installed by default, and it is no longer required to use a composite transition. Nevertheless, the basic steps of chroma keying and keyspill mop up are explained and are still valid.

|tutorial_1|
