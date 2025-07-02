.. meta::

   :description: Kdenlive Video Effects - Alpha Operations
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, alpha operations

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Smolyaninov (https://userbase.kde.org/User:Smolyaninov)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |alphaops| raw:: html

   <a href="https://github.com/dyne/frei0r/blob/master/src/filter/alpha0ps/readme" target="_blank">alpha0ps_alpha0ps</a>


Alpha Operations
================

.. figure:: /images/effects_and_compositions/effects-alpha_operations-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-show-video| Alpha Operations

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      |alphaops|
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect can shrink, grow, threshold and invert the alpha channel. It is mainly intended to improve keying edges. It can also display the alpha channel in various ways to enable quick assessment of the effect. It is cascadable and thus allows a soft shrink first followed by threshold which gives a slightly different result than a hard shrink\ [1]_\ .


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Display
     - Selection
     - What to display (see below)
   * - Display input alpha
     - Switch
     - Use input alpha for the display function above (check what alpha we are getting on the input)
   * - Operation
     - Selection
     - Select the operation to be done on the alpha channel (see below)
   * - Invert
     - Switch
     - Inverts the input alpha channel, transparent will become opaque and vice versa.
   * - Threshold
     - Integer
     - This is only used for the Threshold operation
   * - Shrink/Grow/Blur
     - Integer
     - Depending on the chosen operation: How far the shrinking/growing will extend, or the amount of blur

The following selection items are available:

:guilabel:`Display`

This is intended for monitoring during adjustment mostly. After adjusting the parameters, it should be left on **Image**, which lets the unchanged input image through - this effect is intended to change only the alpha channel.

.. list-table::
   :width: 100%
   :widths: 30 70
   :class: table-wrap

   * - Image
     - Image after the operation  (default)
   * - Alpha as gray
     - Displays the alpha channel as gray
   * - Gray + red
     - Displays the alpha channel as gray, everything else as red
   * - Selection on black
     - Displays the non-alpha channels on a black background
   * - Selection on gray
     - Displays the non-alpha channels on a gray background
   * - Selection on white
     - Displays the non-alpha channels on a white background
   * - Selection on checkers
     - Displays the non-alpha channels on a checkered background


:guilabel:`Operation`

.. list-table::
   :width: 100%
   :class: table-wrap

   * - NO OP
     - No operation is performed
   * - Shave
     - Tries to remove the "hairy" stuff, and also shrinks the selection a bit
   * - Shrink hard
     - Shrinks the area of the alpha channel
   * - Shrink soft
     - Shrinks the area of the alpha channel
   * - Grow hard
     - Grows the area of the alpha channel
   * - Grow soft
     - Grows the area of the alpha channel
   * - Threshold
     - Increases or decreases the area of the alpha channel by the threshold
   * - Blur
     - Blurs the area between the alpha and the other channels

The **... hard** operations introduce no new values to the alpha channel, so if you have a **hard** key (only 0 and 255) it will stay that way.

The **... soft** operations will introduce interpolated values, making the edge softer.

.. note:: The shave, shrink and grow operations are quite slow, because they do many conditional operations on each pixel.


.. link to the Tutorial section is better

.. rubric:: Notes

.. |tutorial_1| raw:: html

   <a href="https://youtu.be/l43Hz7YEcYU" target="_blank">tutorial</a>

This |tutorial_1| shows usage of Alpha Operations with Shrink Hard as well as the following effects: :doc:`/effects_and_filters/video_effects/alpha_mask_keying/chroma_key`, :doc:`/effects_and_filters/video_effects/grain_and_noise/denoise_hqdn3d`, and :doc:`/effects_and_filters/video_effects/alpha_mask_keying/key_spill_mop_up`.

.. note:: **This video is somewhat outdated.** In newer versions of Kdenlive the :doc:`/effects_and_filters/video_effects/alpha_mask_keying/key_spill_mop_up` effect is installed by default, and it is no longer required to use a composite transition. Nevertheless, the basic steps of chroma keying and key spill mop up are explained and are still valid.


----

.. [1] The description of this effect has been taken in parts from the readme file for the frei0r |alphaops| plugin. You find much more detailed information there.
