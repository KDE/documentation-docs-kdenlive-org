.. meta::

   :description: Do your first steps with Kdenlive video editor, using the color channel mixer effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, color channel mixer

   :authors: - Bernd Jordan

   :license: Creative Commons License SA 4.0

.. _effects-color_channel_mixer:

Color Channel Mixer
===================

This effect/filter modifies a color channel by adding the values associated to the other channels of the same pixels. For example, if the value to modify is *red*, the output value will be:

.. code::

   red = red*red-red + blue*red-blue + green*red-green

This effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-color_channel_mixer.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-color_channel_mixer

   Color Channel Mixer effect

* **Red-Red / Red-Green / Red-Blue** - Adjust contribution of input red, green and blue for output red channel. Default is 1 for Red-Red, and 0 for Red-Green and Red-Blue.

* **Green-Red / Green-Green / Green-Blue** - Adjust contribution of input red, green and blue for output green channel. Default is 1 for Green-Green, and 0 for Green-Red and Green-Blue.

* **Blue-Red / Blue-Green / Blue-Blue** - Adjust contribution of input red, green and blue for output blue channel. Default is 1 for Blue-Blue, and 0 for Blue-Green and Blue-Red.
