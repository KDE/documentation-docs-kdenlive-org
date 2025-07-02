.. meta::

   :description: Kdenlive Video Effects - Histogram 
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, utility, histogram

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Histogram
=========

.. figure:: /images/effects_and_compositions/effects-histogram-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-histogram-2504.webp

.. sidebar:: |kdenlive-show-video| Histogram

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      histogram
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      Yes
   :**Color depth**:
      10bit |color-management|
   :**Tutorial**:
      :ref:`Yes <tutorials-histogram>` |view-presentation|

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter computes and draws a color distribution histogram for the input video as an overlay to the clip. Below each graph a color component scale meter is shown.

.. seealso:: :ref:`view-histogram` widget in the :ref:`view_menu` and :doc:`/tips_and_tricks/scopes/histogram_working`


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 10 65
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Level Height
     - Integer
     - Set height of level. Allowed range is from 50 to 2048, default value is 200.
   * - Scale Height
     - Integer
     - Set height of color scale. Allowed range is from 0 to 40, default value is 12
   * - Display
     - Selection
     - Set display mode
   * - Mode
     - Selection
     - Set mode
   * - Components to Display
     - Selection
     - Set what color components to display
   * - Foreground Opacity
     - Float
     - Set foreground opacity\ [1]_. Default is 0.7.
   * - Background Opacity
     - Float
     - Set background opacity\ [1]_. Default is 0.5
   * - Colors Mode
     - Selection
     - Set how the scope is using various color combinations for displaying the results

The following selection items are available:

:guilabel:`Display`

.. list-table::
   :width: 100%
   :widths: 25 75
   :class: table-simple

   * - Overlay
     - 
   * - Stack
     - default
   * - Parade
     - 

:guilabel:`Mode`

.. list-table::
   :width: 100%
   :widths: 25 75
   :class: table-simple

   * - Linear
     - default
   * - Logarithmic
     - 

:guilabel:`Components to Display`

.. list-table::
   :width: 100%
   :widths: 25 75
   :class: table-simple

   * - None
     - 
   * - Y (Luminance)
     - 
   * - U (Chroma red-diff)
     - 
   * - YU
     - 
   * - V (Chroma blue-diff)
     - 
   * - YV
     - 
   * - UV
     - 
   * - All
     - 
   * - Alpha
     - 

:guilabel:`Colors Mode`

.. list-table::
   :width: 100%
   :widths: 25 75
   :class: table-simple

   * - White on Black
     - 
   * - Black on White
     - 
   * - White on Gray
     - 
   * - Black on Gray
     - 
   * - Color on Black
     - 
   * - Color on White
     - 
   * - Color on Gray
     - 
   * - Black on Color
     - 
   * - White on Color
     - 
   * - Gray on Color
     - 


----

.. [1] Doesn't seem to work
