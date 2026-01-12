.. meta::

   :description: Kdenlive Video Effects - Color Channel Mixer
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, color channel mixer

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Color Channel Mixer
===================

.. figure:: /images/effects_and_compositions/effects-color_channel_mixer-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left

.. sidebar:: |kdenlive-show-video| Color Channel Mixer

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      colorchannelmixer
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter modifies a color channel by adding the values associated to the other channels of the same pixels. For example, if the value to modify is *red*, the output value will be:

.. code::

   red = red * red-red + blue * red-blue + green * red-green


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - | Red-Red
       | Red-Green
       | Red-Blue
     - Float
     - Adjust contribution of input red, green and blue for output red channel. Default is 1 for Red-Red, and 0 for Red-Green and Red-Blue.
   * - | Green-Red
       | Green-Green
       | Green-Blue
     - Float
     - Adjust contribution of input red, green and blue for output green channel. Default is 1 for Green-Green, and 0 for Green-Red and Green-Blue.
   * - | Blue-Red
       | Blue-Green
       | Blue-Blue
     - Float
     - Adjust contribution of input red, green and blue for output blue channel. Default is 1 for Blue-Blue, and 0 for Blue-Green and Blue-Red.
