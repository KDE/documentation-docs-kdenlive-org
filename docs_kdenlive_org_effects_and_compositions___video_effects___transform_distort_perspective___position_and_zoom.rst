.. meta::

   :description: Do your first steps with Kdenlive video editor, using position and zoom effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, position and zoom, pan and zoom

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jack (https://userbase.kde.org/User:Jack)
             - Roger (https://userbase.kde.org/User:Roger)
             - Smolyaninov (https://userbase.kde.org/User:Smolyaninov)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-position_and_zoom:

Position and Zoom
=================

This effect/filter allows to adjust size and position of the clip using smooth affine transformations. Formerly known as *Pan and Zoom*.

The effect has keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-position_and_zoom.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-position_and_zoom

   Position and Zoom effect

* **Distort** - Determines whether the image aspect ratio will be distorted while scaling to completely fill the rectangle

* **Normalise** - Use the video resolution instead of the project resolution

* **X / Y / W / H / Size** - This is where the action is for *Position* (X, Y) and *Zoom* (Size)

* **Background Color** - Define the background color to be used when zooming out reveals the background. Default is Alpha.

.. rst-class:: clear_both


.. warning:: As of this writing and in version 23.04 there are many confirmed reports that the compositing of clips using the **Position and Zoom** effect does not work properly and leaves artifacts. A bug report has been created, and until it is fixed use the :ref:`effects-transform` effect instead.


.. In this example we have two keyframes in the pan and zoom, one at the beginning and one at the end. Size is 25% at the start keyframe and 100% at the end. The images are centered on the screen at both keyframes.

   https://youtu.be/0aSe1y6e4RE

   See also this :ref:`effects-chroma_key_basic` that describes how to use:

   * Alpha Manipulation -> :ref:`effects-chroma_key_basic`
   * :ref:`effects-rotoscoping`
   * :ref:`composite`
   * Crop and Transform -> Pan and Zoom effect
   * Enhancement -> :ref:`sharpen`
   * Alpha Manipulation -> :ref:`effects-alpha_operations`

   `Tutorial: How to do pan and zoom with Kdenlive video editor - Peter Thomson(YouTube) <https://youtu.be/B8ZPoWaxQrA>`_
