.. meta::

   :description: Do your first steps with Kdenlive video editor, using video values effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, utility, video values

.. metadata-placeholder

   :authors: - Roger (https://userbase.kde.org/User:Roger)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-video_values:

Video Values
============

This effect/filter draws and overlays a window in the clip that shows a zoomed version of the area covered by a small crosshair, and specific values of the covered area of the video stream.

The effect has keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-video_values.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-video_values

   Video Values effect

* **Measurement** - Select what will be measured. Options are **RGB** (default), **Y'PbPr - rec.601** and **Y'PbPr - rec.709**

* **256 scale** - Use the scale 0..256 instead of 0.0..1.0 (default)

* **Show alpha** - Show the Alpha channel

* **Big window** - show a bigger version of the video values window

* **X / Y / X size / Y size** - Set the position (X / Y) and the size (X size / Y size) of the crosshair (determines the area covered and analyzed)
