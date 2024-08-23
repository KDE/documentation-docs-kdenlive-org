.. meta::

   :description: Kdenlive Video Effects - Chroma Key Basic
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, alpha, chroma key, greenscreen, bluescreen, keying

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - TheMickyRosen-Left (https://userbase.kde.org/User:TheMickyRosen-Left)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |lesson_18| raw:: html

   <a href="https://youtu.be/bMwbffYIS40" target="_blank">Lesson 18 'Chroma Key and Green Screen'</a>


Chroma Key: Basic
=================

.. figure:: /images/effects_and_compositions/kdenlive2308_effects-chroma_key.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: Color_selection_effect

.. sidebar:: |kdenlive-show-video| Chroma Key Basic

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      
   :**Source filter**:
      chroma
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect allows you to do Chroma Keying (also known as Green Screen or Blue Screen). Chroma keying is a visual-effects and post-production compositing technique where you remove backgrounds of a similar color.

As it name suggest this effect is very basic. It only allows to select a color and specify the variance. While this may suffice for some use cases or scenarios the :doc:`Chroma Key (Advanced) </effects_and_filters/video_effects/alpha_mask_keying/chroma_key_advanced>` offers more parameters for more control over the keying process (background removal).

For black backgrounds it is more efficient to use a :guilabel:`Screen` Composition. More details are available in the :doc:`Compositions </compositing/compositions>` section of the documentation.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Variance
     - Integer
     - The difference between the Color Key and the pixel. The smaller the value, the closer the pixel color must be to the Color Key to be made transparent.
   * - Color Key
     - Picker
     - The color to select. This is the color that will be transparent.


.. rubric:: Basic Chroma Keying Steps

1. Select the clip you want to chroma key in the Timeline

2. Search for *Chroma Key* in the Effects Tab, and drag it onto the clip's effect stack (properties tab).

3. Press on the button that looks like pipette, and then click on the background of the video. This will chroma key out the background.

4. Use the :guilabel:`Variance` slider to control the amount of background chroma keyed out. This will require adjustment if your chroma key didn't immediately turn out perfect.


.. rubric:: Video Tutorial

Kdenlive |lesson_18| (by TJ Free)


.. rubric:: Notes

For more complicated scenery use the :doc:`/effects_and_filters/video_effects/alpha_mask_keying/chroma_key_advanced` effect which also does color based alpha selection but in a much more detailed fashion. Use it for less contrasting or more complex backgrounds.

.. seealso:: :doc:`/effects_and_filters/video_effects/alpha_mask_keying/rotoscoping` effect. Rotoscoping is where you manually draw a region and everything outside/inside that region will disappear. This is useful for backgrounds with multiple different colors.

.. seealso:: :doc:`/effects_and_filters/video_effects/alpha_mask_keying/key_spill_mop_up` effect. It can be used to improve the edges of the Chroma Key effect when edge problems occur that are caused by "key spill". Key spill is when the color of the screen used for color keying spills onto the subject due to light reflection.
