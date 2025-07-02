.. meta::

   :description: Kdenlive Video Effects - Chroma Key Advanced
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, alpha, chroma key, greenscreen, bluescreen, keying, advanced

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Marko (https://userbase.kde.org/User:Marko)
             - TheMickyRosen-Left (https://userbase.kde.org/User:TheMickyRosen-Left)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Chroma Key: Advanced
====================

.. figure:: /images/effects_and_compositions/effects-chroma_key_advanced-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: Color_selection_effect

.. sidebar:: |kdenlive-show-video| Chroma Key Advanced

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      select0r
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No
   :**Color depth**:
      8bit
   :**Tutorial**:
      :ref:`Yes <tutorials-chroma_key_advanced>` |view-presentation|

.. rst-class:: clear-both


.. rubric:: Description

This effect is a more advanced version of the :doc:`Chroma Key: Basic </effects_and_filters/video_effects/alpha_mask_keying/chroma_key>` effect. It allows for some basic feathering (by changing the :guilabel:`Edge Mode`) and much more fine-grained control over how much and in which way you remove the background.

This is better for backgrounds that have less contrast with the foreground or for more complex backgrounds. For simple (uniform) backgrounds (such as green, blue, red or possibly black), use the :doc:`Chroma Key: Basic </effects_and_filters/video_effects/alpha_mask_keying/chroma_key>` effect.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 10 65
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Invert selection
     - Switch
     - When ON (default), the selected color will be transparent. When OFF the selected color will be opaque. Keeping the selected color opaque may be more effective if the foreground is simple and the background is complicated.
   * - Color Model\ [1]_
     - Selection
     - These different options yield different results. While RGB should yield the sharpest and best results, sometimes the other options HCI and ABI can yield much better results than RGB. So if RGB is not producing good results, try one of the other options.
   * - Shape
     - Selection
     - Determines the shape for subspace selection
   * - Edge Mode
     - Selection
     - Determines the amount of feathering
   * - Operation
     - Selection
     - Determines how the alpha channel is processed
   * - Color to select
     - Picker
     - The color to select. This is the color that will be transparent or the only color that is opaque depending on the setting for :guilabel:`Invert selection`.
   * - | Red/Hue Delta
       | Green/Chroma Delta
       | Blue/Intensity Delta
     - Integer
     - These three parameters determine the tolerance of the chroma keying. The higher the value, the more of the background is removed; the lower the value, less is removed. A bit of experimenting is required to find the correct values for each clip.
   * - Soften
     - Integer
     - This slider determines the smoothness of the edges. The higher the value, the smoother the edges of your color selection will be. Only works if :guilabel:`Edge mode` is set to **Slope**.


The following selection items are available:

:guilabel:`Color Model`\ [1]_

.. list-table::
   :width: 100%
   :widths: 25 75
   :class: table-wrap

   * - RGB
     - Red Green Blue
   * - ABI
     - Advanced Baseline Imager
   * - HCI
     - Hue Chromacity Intensity

.. tip:: These different options yield different results. While **RGB** should yield the sharpest and best results, sometimes the other options **HCI** and **ABI** can yield much better results than **RGB**. So if **RGB** is not producing good results, try one of the other options.

.. note:: Previews of video clips that were chroma keyed using **HCI** will be slow since values for every single pixel have to be calculated. Either lower the Project Monitor playback resolution or use the Preview Render function.

:guilabel:`Shape`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - Box
     - Uses a box to select the pixels leaving no space between them
   * - Ellipsoid
     - Uses an ellipsoid to select pixels leaving some space between them
   * - Diamond
     - Uses a  diamond shape to select pixels leaving space between them

**Box** is the most thorough selection method, and **Diamond** the one with the largest gaps.

:guilabel:`Edge Mode`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - Hard
     - No feathering (edges are not smooth at all). Any part of the image/video is either fully opaque and fully transparent. This means there will be none of the selected color between the removed parts and the remaining parts whatsoever. This option is useful if your chroma key turned out to be perfect.
   * - Fat
     - 
   * - Normal
     - 
   * - Skinny
     - 
   * - Slope
     - Allows to use the :guilabel:`Soften` slider

The options **Fat**, **Normal** and **Skinny** create a gradual transition between transparent and opaque. The fatter the choice, the more the selected areas are filled towards the rim (more feathering for fatter choices). This is useful if your color selection did not turn out that well.

:guilabel:`Operation`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-wrap

   * - Write on clear
     - 
   * - Max
     - 
   * - Min
     - 
   * - Add
     - 
   * - Subtract
     - 


.. rubric:: Basic Technique

Find a clip with a background (preferably multiple, or slightly complex, because the :doc:`/effects_and_filters/video_effects/alpha_mask_keying/chroma_key` effect can do easy backgrounds such as green or blue). Add the *Chroma Key: Advanced* effect to the clip.

Now either choose the color using the color palette by clicking on the colored bar. Or use the little pipette button and then click in the Project Monitor on the background part of the clip you want to remove. Adjust the :guilabel:`Delta` sliders until the background is removed correctly. This might need some experimenting. If you find it is not removing the background well try changing the :guilabel:`Color Model` and experiment again. If you experimented and cycled through all the :guilabel:`Color Models`, and the background is still not removed properly then it is probably too complicated for Kdenlive to remove. At this point, you will most likely need to use :doc:`/effects_and_filters/video_effects/alpha_mask_keying/rotoscoping`.

If the effect took lots of time to experiment, and you want to use this effect again, then click on the |document-save|:guilabel:`Save effect` icon. Give the effect a name and a comment and click on :guilabel:`Ok`. Your custom *Chroma Key: Advanced* effect will be saved in the *Custom* effect category from where you can use it just like any other effect.


.. rubric:: Notes

.. seealso:: :doc:`Chroma Key: Basic </effects_and_filters/video_effects/alpha_mask_keying/chroma_key>` which also does color-based alpha selection, but is a bit simpler.


----

.. |page| raw:: html

   <a href="https://sites.harding.edu/gclayton/Color/Topics/001_HueValueChroma.html" target="_blank">page</a>


.. [1] This |page| covers some color theory to help understand hue, chroma, luminance, etc.


.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Icons used here (remove comment indent to enable them for this document)
   
   .. |document-save| image:: /images/icons/document-save.svg
   :width: 22px
   :class: no-scaled-link
