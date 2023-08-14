.. meta::

   :description: Do your first steps with Kdenlive video editor, using curves effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, curves

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-curves:

Curves
======

This effect/filter adjusts shadows, midtones and highlights of an image using curves. It is similar to the :ref:`effects-color_levels` or :ref:`effects-levels` effects but with the option to create additional points along the curve allowing for pinpoint accuracy when adjusting brightness values.

This filter does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-curves.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-curves

   Curves effect

* **Channel** - Set the channel to which the curve applies. Options are **RGB** (default), **Red**, **Green**, **Blue**, **Alpha**, **Luma** and **Saturation**.

* **Luma formula** - Set the color space in which the application takes place. Options are **Rec. 709** (default) and **Rec. 601**.

* **In** - Set the Input value

* **Out** - Set the Output value

* **Show graph in picture** - Check this box to overlay the graph onto the image in the Project Monitor. Note that this influences the :ref:`view-rgb_parade` and :ref:`view-histogram` :term:`widgets<widget>`.

* **Graph position** - Select the position for the graph. Options are **Top left**, **Top right**, **Bottom left** and **Bottom right** (default).

.. rst-class:: clear-both

.. hint:: It is recommended to use this effect while in Color layout as this comes with :ref:`RGB Parade <view-rgb_parade>` and :ref:`view-histogram` already switched on. If you want to use the effect while in Editing or Effects layout turn on the Histogram :term:`widget` with :menuselection:`Menu --> View --> Histogram`.
