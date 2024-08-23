.. meta::

   :description: Kdenlive Video Effects - Videogrid
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, generate, videogrid, video, grid

   :authors: - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Video Grid
==========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-video_grid.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-video_grid

.. sidebar:: |kdenlive-show-video| Video Grid

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      cairoimagegrid
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect creates a grid of copies of the video footage. You adjust the number of rows and columns in the image with the :guilabel:`Rows` and :guilabel:`Columns` parameters. These take decimal fractions from zero to 1. The maximum value of 1 means 20 rows or columns.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Rows
     - Float
     - Number of rows in the image grid. Input range 0 - 1 is interpreted as range 1 - 20.
   * - Columns
     - Float
     - Number of columns in the image grid. Input range 0 - 1 is interpreted as range 1 - 20.

:Formula:
 ``Number of rows/columns = (p X 19) + 1``    [where p = the value of the row or column parameter]


.. rubric:: Examples
   
.. figure:: /images/effects_and_compositions/kdenlive2304_effects-video_grid_3x6.webp
   :width: 650px
   :figwidth: 650px
   :align: left
   :alt: kdenlive2304_effects-video_grid_3x6

   Video Grid effect with 3 rows and 6 columns

.. rst-class:: clear-both

:In this example:
 rows = 0.105 ⇒  means (0.1 X 19) + 1 =  3 rows

 columns = 0.263 ⇒ means (0.263 X 19) + 1 = 6  columns

In order to calculate the fractional value for :guilabel:`Rows` and :guilabel:`Columns` for a specific number of rows and/or columns use this formula:

``Rows/Columns = (#_of_rows/columns - 1) * 0.05263``

:In this example:
 #_of_rows = 3 ⇒ means (3 - 1) * 0.05263 = 0.105
 
 #_of_columns = 6 ⇒ means (6 -1) * 0.05263 = 0.263
