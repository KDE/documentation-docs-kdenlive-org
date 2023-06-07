.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Marko (https://userbase.kde.org/User:Marko)
             - TheMickyRosen-Left (https://userbase.kde.org/User:TheMickyRosen-Left)
             - Bernd Jordan

   :license: Creative Commons License SA 4.0

.. _effects-chroma_key_advanced:

Chroma Key: Advanced
====================

This effect is a more advanced version of the :ref:`Chroma Key: Basic <effects-chroma_key_basic>` effect. *Chroma Key: Advanced* [1]_ allows for some basic feathering (by changing the :guilabel:`Edge Mode`) and much more fine-grained control over how much and in which way you remove the background.

This is better for backgrounds that have less contrast with the foreground or for more complex backgrounds. For simple (uniform) backgrounds (such as green, blue, red or possibly black), use the :ref:`Chroma Key: Basic <effects-chroma_key_basic>` effect.


Basic Technique
---------------

Find a clip with a background (preferably multiple, or slightly complex, because the :ref:`Chroma Key: Basic <effects-chroma_key_basic>` effect can do easy backgrounds such as green or blue). Add the *Chroma Key: Advanced* effect to the clip.

Now either choose the color using the color palette by clicking on the colored bar. Or use the little pipette button and then click in the Project Monitor on the background part of the clip you want to remove. Adjust the :guilabel:`Delta` sliders until the background is removed correctly. This might need some experimenting. If you find it is not removing the background well try changing the :guilabel:`Color Model` and experiment again. If you experimented and cycled through all the :guilabel:`Color Models`, and the background is still not removed properly then it is probably too complicated for **Kdenlive** to remove. At this point, you will most likely need to use :ref:`Rotoscoping <effects-rotoscoping>`.

If the effect took lots of time to experiment, and you want to use this effect again, then click on the |document-save|:guilabel:`Save effect` icon. Give the effect a name and a comment and click on :guilabel:`Ok`. Your custom *Chroma Key: Advanced* effect will be saved in the *Custom* effect category from where you can use it just like any other effect.


All Options
-----------

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-chroma_key_advanced.webp
   :width: 90%
   :alt: Color_selection_effect

   Chroma Key: Advanced effect panel

:guilabel:`Invert selection`
   When ON (default), the selected color will be transparent. When OFF the selected color will be opaque. Keeping the selected color opaque may be more effective if the foreground is simple and the background is complicated.

:guilabel:`Color Model` [2]_
   The options are: :guilabel:`RGB` (Red Green Blue), :guilabel:`ABI` and :guilabel:`HCI` (Hue Chromacity Intensity).
   These different options yield different results. While RGB should yield the sharpest and best results, sometimes the other options HCI and ABI can yield much better results than RGB. So if RGB isnt producing good results then try one of the other options.

.. note:: Previews of video clips that were chroma keyed using HCI will be **slow** since values for every single pixel have to be calculated. Either lower the Project Monitor playback resolution or use the Preview Render function.

:guilabel:`Edge Mode`
   Options are: Hard, Fat, Normal, Skinny, Slope

   If the Edge Mode is set to Slope, you can use the :guilabel:`Soften` slider.

   "Hard" means there is no feathering (edges are not smooth at all). Any part of the image/video is either fully opaque and fully transparent. This means there will be none of the selected color between the removed parts and the remaining parts whatsoever. This option is useful if your chroma key turned out to be perfect.

   The remaining options ("Fat", "Normal" and "Skinny") create a gradual transition between transparent and opaque. The fatter the choice, the more the selected areas are filled towards the rim (more feathering for fatter choices). This is useful if your color selection did not turn out that well.

:guilabel:`Color to select`
   The color to select. This is the color that will be transparent or the only color that is opaque depending on the setting for :guilabel:`Invert selection`.

:guilabel:`Delta`
   These three parameters determine the tolerance of the chroma keying. The higher the value, the more of the background is removed; the lower the value, less is removed. A bit of experimenting is required to find the correct values for each clip.

:guilabel:`Soften`
   This slider determines the smoothness of the edges. The higher the value, the smoother the edges of your color selection will be. Only works if :guilabel:`Edge mode` is set to Slope.


**Notes**

.. |page| raw:: html

   <a href="https://sites.harding.edu/gclayton/Color/Topics/001_HueValueChroma.html" target="_blank">page</a>


See :ref:`Chroma Key: Basic <effects-chroma_key_basic>` which also does color-based alpha selection but is a bit simpler.

.. [1] This effect used to be called *Color Selection*

.. [2] This |page| covers some color theory to help understand hue, chroma, luminance, etc.

