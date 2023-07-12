.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Smolyaninov (https://userbase.kde.org/User:Smolyaninov)
             - Bernd Jordan

   :license: Creative Commons License SA 4.0

.. _effects-alpha_operations:

Alpha Operations
================

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-alpha_operations.webp
   :align: left
   :width: 430px
   :figwidth: 430px
   :alt: kdenlive2304_effects-alpha_operations

   Alpha Operations effect panel

This effect can shrink, grow, threshold and invert the alpha channel. It is mainly intended to improve keying edges. It can also display the alpha channel in various ways to enable quick assessment of the effect. It is cascadable and thus allows a soft shrink first followed by threshold which gives a slightly different result than a hard shrink.  (frei0r.alpha0ps) [1]_

.. rst-class:: clear-both


Parameters
----------

Display
~~~~~~~

What to display. There are seven options:

* Image (default)
* Alpha as gray
* Gray + red
* Selection on black
* Selection on gray
* Selection on white
* Selection on checkers

This is intended for monitoring during adjustment mostly. After adjusting the parameters, it should be left on :guilabel:`Image`, which lets the unchanged input image through - this effect is intended to change only the alpha channel.

Display input alpha
~~~~~~~~~~~~~~~~~~~

Use input alpha for the display function above (check what alpha we are getting on the input).

Operation
~~~~~~~~~~

Select the operation to be done on the alpha channel. Currently there are eight choices:

* NO OP
* Shave
* Shrink hard
* Shrink soft
* Grow hard
* Grow soft
* Threshold
* Blur

:guilabel:`Shave` tries to remove the "hairy" stuff, and also shrinks the selection a bit.

The *hard* operations introduce no new values to the alpha channel, so if you have a "hard" key (only 0 and 255) it will stay that way.

The *soft* operations will introduce interpolated values, making the edge softer.

.. note:: The shave, shrink and grow operations are quite slow, because they do many conditional operations on each pixel.


Threshold
~~~~~~~~~~

This is only used for the Threshold operation.


Shrink/Grow/Blur amount
~~~~~~~~~~~~~~~~~~~~~~~

How far the shrinking/growing will extend, or the amount of blur.

Invert
~~~~~~

Inverts the input alpha channel, transparent will become opaque and vice versa.


.. link to the Tutorial section is better

Tutorial 1
----------

.. |tutorial_1| raw:: html

   <a href="https://youtu.be/l43Hz7YEcYU" target="_blank">https://youtu.be/l43Hz7YEcYU</a>

Shows usage of Alpha Operations with Shrink Hard as well as the following effects: :ref:`effects-chroma_key_basic`, :ref:`effects-denoiser`, and :ref:`effects-key_spill_mop_up`.

.. note:: **This video is somewhat outdated.** In newer versions of Kdenlive the Key Spill Mop Up effect is installed by default, and it is no longer required to use a composite transition. Nevertheless, the basic steps of chroma keying and key spill mop up are explained and are still valid.

|tutorial_1|

**Notes**

.. |alphaops| raw:: html

   <a href="https://github.com/dyne/frei0r/blob/master/src/filter/alpha0ps/readme" target="_blank">frei0r alpha0ps plugins</a>

.. [1] The description of this effect has been taken in parts from the readme file for the |alphaops|. You find much more detailed information there.
