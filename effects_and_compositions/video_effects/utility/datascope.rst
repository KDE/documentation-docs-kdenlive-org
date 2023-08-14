.. meta::

   :description: Do your first steps with Kdenlive video editor, using datascope effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, utility, datascope

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-datascope:

DataScope
=========

This effect/filter analyses the video data and shows hexadecimal pixel values of parts of the video.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-datascope.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-datascope

   DataScope effect

* **Size** - Set output video size. Options are **128p**, **360p**, **PAL SD**, **NTSC SD**, **480p**, **720HD** (default), **1080FullHD**, **2K**, **4K**.

* **X / Y Offset** - Set the x / y offset from where to pick the pixels

* **Mode** - Set scope mode [1]_. Options are **mono** (default; draw hexadecimal pixel values with white color on black background), **color** (draw hexadecimal pixel values with input video pixel color on black background), and **color2** (draw hexadecimal pixel values on color background picked from input video, the text color is picked in such way so its always visible).

* **Show Axis** - If set to **On**, draws rows and columns numbers on left and top of video. Default is **Off**.

* **Opacity** - Set background opacity [1]_

* **Format** - Set display number format [1]_. Can be **Hex** (default) or **Dec**.

.. rst-class:: clear-both


**Notes**

.. [1] Doesn't seem to work
