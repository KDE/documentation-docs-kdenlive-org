.. meta::

   :description: Do your first steps with Kdenlive video editor, using color matrix effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, image adjustment, color matrix

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |color_space_descriptions| raw:: html

   <a href="https://www.kernel.org/doc/html/v4.9/media/uapi/v4l/pixfmt-007.html" target="_blank">Color Space Descriptions</a>


.. _effects-color_matrix:

Color Matrix
============

This effect/filter converts the :term:`color matrix`.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-color_matrix.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-color_matrix

   Color Matrix effect

* **Source color Matrix**

* **Destination color Matrix**

.. rst-class:: clear-both

The :guilabel:`Matrix` parameters have the following options:

* bt709
* fcc
* bt601
* bt470
* bt470bg
* smpte170m
* smpte240m
* bt2020

For the technical inclined there is a list of detailed |color_space_descriptions| available in the Linux Kernel documentation.
