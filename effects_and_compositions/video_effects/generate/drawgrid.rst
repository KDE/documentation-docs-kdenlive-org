.. meta::

   :description: Do your first steps with Kdenlive video editor, using draw grid effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, generate, draw grid

.. metadata-placeholders

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-draw_grid:

Draw Grid
=========

This effect/filter draws a colored grid on the input video.

The effect has keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-draw_grid.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-draw_grid

   Draw Grid effect

* **X / Y Offset** - Defines the starting point of the grid in pixels from the top left-hand corner of the monitor (coordinates are based on the project dimension settings)

* **Width** - Defines the distance between vertical grid lines in pixels

* **Height** - Defines the distance between horizontal grid lines in pixels

* **Thickness** - Defines the thickness of the lines in pixels

* **Color** - Defines the color for the grid

.. rst-class:: clear-both


.. note:: As of this writing and in version 23.04.2 the color parameter is being ignored and black is used.

.. hint:: This effect can be used in combination with the :ref:`effects-chroma_key_basic` or :ref:`effects-chroma_key_advanced` effects to create interesting transitions by animating the number of grid lines and their thickness.
