.. meta::

   :description: Kdenlive Video Effects - Histogram 
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, utility, histogram

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Histogram
=========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-histogram.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-histogram

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

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter computes and draws a color distribution histogram for the input video as an overlay to the clip. Below each graph a color component scale meter is shown.

See also the :ref:`view-histogram` widget in the :ref:`view_menu`.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Level height
     - Integer
     - Set height of level. Allowed range is from 50 to 2048, default value is 200.
   * - Scale height
     - Integer
     - Set height of color scale. Allowed range is from 0 to 40, default value is 12
   * - Display
     - Selection
     - Set display mode
   * - Mode
     - Selection
     - Set mode
   * - Components to display
     - Selection
     - Set what color components to display
   * - Foreground Opacity
     - Float
     - Set foreground opacity [1]_. Default is 0.7.
   * - Background Opacity
     - Float
     - Set background opacity [1]_. Default is 0.5

The following selection items are available:

:guilabel:`Display`

.. list-table::
   :width: 100%
   :widths: 20 80
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
   :widths: 20 80
   :class: table-simple

   * - Linear
     - default
   * - Logarithmic
     - 

:guilabel:`Components to display`

.. list-table::
   :width: 100%
   :widths: 20 80
   :class: table-simple

   * - All
     - 
   * - Y
     - default (:term:`luma`)
   * - U
     - 
   * - YU
     - 
   * - V
     - 
   * - YV
     - 
   * - UV
     - 
   * - All
     - (sic)
   * - Alpha
     - 


----

.. [1] Doesn't seem to work
