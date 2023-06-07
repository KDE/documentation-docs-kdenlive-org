.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - TheMickyRosen-Left (https://userbase.kde.org/User:TheMickyRosen-Left)
             - Bernd Jordan

   :license: Creative Commons License SA 4.0


.. |lesson_18| raw:: html

   <a href="https://youtu.be/bMwbffYIS40" target="_blank">Lesson 18 'Chroma Key and Green Screen'</a>

.. _effects-chroma_key_basic:

Chroma Key: Basic
=================

This effect allows you to do Chroma Keying (also known as Green Screen or Blue Screen). Chroma keying is a visual-effects and post-production compositing technique where you remove backgrounds of a similar color.

As it name suggest this effect is very basic. It only allows to select a color and specify the variance. While this may suffice for some use cases or scenarios the :ref:`Chroma Key (Advanced) <effects-chroma_key_advanced>` offers more parameters for more control over the keying process (background removal).

For black backgrounds it is more efficient to use a :guilabel:`Screen` Composition. More details are available in the :ref:`Compositions <effects-compositions>` section of the documentation.


Basic Chroma Keying Steps
-------------------------

1. Select the clip you want to chroma key in the Timeline

2. Search for *Chroma Key* in the Effects Tab, and drag it onto the clip's effect stack (properties tab).

3. Press on the button that looks like pipette, and then click on the background of the video. This will chroma key out the background.

4. Use the :guilabel:`Variance` slider to control the amount of background chroma keyed out. This will require adjustment if your chroma key didn't immediately turn out perfect.


Video Tutorial
--------------

* Kdenlive |lesson_18| (by TJ Free)


**Notes**

See also the :ref:`Rotoscoping <effects-rotoscoping>` effect. Rotoscoping is where you manually draw a region and everything outside/inside that region will disappear. This is useful for backgrounds with multiple different colours.

See also the :ref:`Key Spill Mop Up <effects-key_spill_mop_up>` effect. The Key Spill Mop Up effect can be used to improve the edges of the Chroma Key effect when edge problems occur that are caused by "key spill". Key spill is when the color of the screen used for color keying spills onto the subject due to light reflection.

For more complicated scenery use the :ref:`Chroma Key (Advanced) <effects-chroma_key_advanced>` effect which also does color based alpha selection but in a much more detailed fashion. Use it for less contrasting or more complex backgrounds.

