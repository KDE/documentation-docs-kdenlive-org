.. meta::

   :description: Do your first steps with Kdenlive video editor, using histogram effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, utility, histogram

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |link| raw:: html

   <a href="link_URI" target="_blank">link_text</a>


.. _effects-histogram:

Histogram
=========

This effect/filter computes and draws a color distribution histogram for the input video as an overlay to the clip. Below each graph a color component scale meter is shown.

See also the :ref:`view-histogram` widget in the :ref:`view_menu`.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-histogram.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-histogram

   Histogram effect

* **Level height** - Set height of level. Allowed range is from 50 to 2048, default value is 200.

* **Scale height** - Set height of color scale. Allowed range is from 0 to 40, default value is 12

* **Display** - Set display mode. Options are **Overlay**, **Stack** (default) or **Parade**.

* **Mode** - Set mode. Options are **Linear** (default) or **Logarithmic**.

* **Components to display** - Set what color components to display. Default is Y (:term:`luma` or luminance).

* **Foreground Opacity** - Set foreground opacity [1]_. Default is 0.7.

* **Background Opacity** - Set background opacity [1]_. Default is 0.5

.. rst-class:: clear-both


**Notes**

.. [1] Doesn't seem to work
