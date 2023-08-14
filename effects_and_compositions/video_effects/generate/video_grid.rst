.. meta::

   :description: Do your first steps with Kdenlive video editor, using videogrid effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, generate, videogrid, video, grid

   :authors: - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-video_grid:

Video Grid
==========

This effect creates a grid of copies of the video footage.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-video_grid.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-video_grid

   Video Grid effect

* **Rows** - Number of rows in the image grid. Input range 0 - 1 is interpreted as range 1 - 20.

* **Columns** - Number of columns in the image grid. Input range 0 - 1 is interpreted as range 1 - 20.

.. rst-class:: clear-both


You adjust the number of rows and columns in the image with the :guilabel:`Rows` and :guilabel:`Columns` parameters. These take decimal fractions from zero to 1. The maximum value of 1 means 20 rows or columns.

``Number of rows/columns = (p X 19) + 1``    [where p = the value of the row or column parameter]

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-video_grid_3x6.webp
   :width: 800px
   :figwidth: 800px
   :align: left
   :alt: kdenlive2304_effects-video_grid_3x6

   Video Grid effect with 3 rows and 6 columns

..

.. rst-class:: clear-both

In this example:

rows = 0.105 ⇒  means (0.1 X 19) + 1 =  3 rows

columns = 0.263 ⇒ means (0.263 X 19) + 1 = 6  columns

In order to calculate the fractional value for :guilabel:`Rows` and :guilabel:`Columns` for a specific number of rows and/or columns use this formula:

``Rows/Columns = (#_of_rows/columns - 1) * 0.05263``

In this example:

#_of_rows = 3 ⇒ means (3 - 1) * 0.05263 = 0.105

#_of_columns = 6 ⇒ means (6 -1) * 0.05263 = 0.263
