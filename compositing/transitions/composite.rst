.. meta::
   :description: Kdenlive Documentation - Composition Type "Composite" (Transition)
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, compositing, composition type, transition, composite

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0



Composite
=========

The composition type **Composite** is a transition and combines composition methods with the :doc:`Transform </effects_and_filters/video_effects/transform_distort_perspective/transform>` effect. It is not animated by default but has keyframes which gives you fine control over what is happening when. The :guilabel:`Opacity` parameter controls the level of compositing with the selected :guilabel:`Compositing` method.

The **Composite** transition by default assigns a simple dissolve. You can select a different :guilabel:`Composite Method`, download from KDE Store, or use a file from your local file system.

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/composition_type-composite_setup.webp
     :width: 360px
     :figwidth: 360px
     :align: left

     Settings for the Composite transition

   Only the parameters below the keyframe ruler can be animated via keyframes. By default, this composition just applies the selected :guilabel:`Composite Method`. You can use the keyframes to move and scale the clip. Use :guilabel:`Opacity` to control the amount of compositing. :guilabel:`Softness` controls the amount of feathering (0 creates a sharp edge between the clips).


.. rst-class:: clear-both


This list shows the standard available composite methods:

.. list-table:: 
   :header-rows: 1
   :widths: 20 30 50
   :class: table-wrap

   * - Composite Method
     - Example
     - Notes
   * - None (Dissolve)
     - .. image:: /images/effects_and_compositions/composition-wipe_method-none_dissolve.gif
     - This is a simple dissolve transition between the two tracks. The :guilabel:`Softness` slider has no effect.
   * - Bar Horizontal
     - .. image:: /images/effects_and_compositions/composition-wipe_method-bar_horizontal.gif
     - 
   * - Bar Vertical
     - .. image:: /images/effects_and_compositions/composition-wipe_method-bar_vertical.gif
     - 
   * - Barn Door Diagonal NW-SE
     - .. image:: /images/effects_and_compositions/composition-wipe_method-barn_nwse.gif
     - 
   * - Barn Door Diagonal SW-NE
     - .. image:: /images/effects_and_compositions/composition-wipe_method-barn_swne.gif
     - 
   * - Barn Door Horizontal
     - .. image:: /images/effects_and_compositions/composition-wipe_method-barn_horizontal.gif
     - 
   * - Barn Door Vertical
     - .. image:: /images/effects_and_compositions/composition-wipe_method-barn_vertical.gif
     - 
   * - Barn V Up
     - .. image:: /images/effects_and_compositions/composition-wipe_method-barn_v_up.gif
     - 
   * - Bi-Linear X
     - .. image:: /images/effects_and_compositions/composition-wipe_method-bilinear_x.gif
     - 
   * - Bi-Linear Y
     - .. image:: /images/effects_and_compositions/composition-wipe_method-bilinear_y.gif
     - 
   * - Box Bottom Left
     - .. image:: /images/effects_and_compositions/composition-wipe_method-box_bottom_left.gif
     - 
   * - Box Bottom Right
     - .. image:: /images/effects_and_compositions/composition-wipe_method-box_bottom_right.gif
     - 
   * - Box Right Center
     - .. image:: /images/effects_and_compositions/composition-wipe_method-box_right_center.gif
     - 
   * - Burst
     - .. image:: /images/effects_and_compositions/composition-wipe_method-burst.gif
     - 
   * - Checkerboard Small
     - .. image:: /images/effects_and_compositions/composition-wipe_method-checkerboard_small.gif
     - 
   * - Clock
     - .. image:: /images/effects_and_compositions/composition-wipe_method-clock.gif
     - 
   * - Clock Top
     - .. image:: /images/effects_and_compositions/composition-wipe_method-clock_top.gif
     - 
   * - Cloud
     - .. image:: /images/effects_and_compositions/composition-wipe_method-cloud.gif
     - 
   * - Curtain
     - .. image:: /images/effects_and_compositions/composition-wipe_method-curtain.gif
     - 
   * - Diagonal Top Left
     - .. image:: /images/effects_and_compositions/composition-wipe_method-diagonal_tl.gif
     - 
   * - Diagonal Top Right
     - .. image:: /images/effects_and_compositions/composition-wipe_method-diagonal_tr.gif
     - 
   * - Double Iris
     - .. image:: /images/effects_and_compositions/composition-wipe_method-double_iris.gif
     - 
   * - Horizontal Blinds
     - .. image:: /images/effects_and_compositions/composition-wipe_method-horizontal_blinds.gif
     - 
   * - Iris Box
     - .. image:: /images/effects_and_compositions/composition-wipe_method-iris_box.gif
     - 
   * - Iris Circle
     - .. image:: /images/effects_and_compositions/composition-wipe_method-iris_circle.gif
     - 
   * - Linear X
     - .. image:: /images/effects_and_compositions/composition-wipe_method-linear_x.gif
     - 
   * - Linear Y
     - .. image:: /images/effects_and_compositions/composition-wipe_method-linear_y.gif
     - 
   * - Matrix Snake Horizontal
     - .. image:: /images/effects_and_compositions/composition-wipe_method-matrix_snake_hor.gif
     - 
   * - Matrix Snake Parallel Horizontal
     - .. image:: /images/effects_and_compositions/composition-wipe_method-matrix_snake_prl_hor.gif
     - 
   * - Matrix Snake Parallel Vertical
     - .. image:: /images/effects_and_compositions/composition-wipe_method-matrix_snake_prl_ver.gif
     - 
   * - Matrix Snake Vertical
     - .. image:: /images/effects_and_compositions/composition-wipe_method-matrix_snake_ver.gif
     - 
   * - Matrix Waterfall Horizontal
     - .. image:: /images/effects_and_compositions/composition-wipe_method-matrix_wfall_hor.gif
     - 
   * - Matrix Waterfall Vertical
     - .. image:: /images/effects_and_compositions/composition-wipe_method-matrix_wfall_ver.gif
     - 
   * - Radial
     - .. image:: /images/effects_and_compositions/composition-wipe_method-radial.gif
     - 
   * - Radial Bars
     - .. image:: /images/effects_and_compositions/composition-wipe_method-radial_bars.gif
     - 
   * - Spiral
     - .. image:: /images/effects_and_compositions/composition-wipe_method-spiral.gif
     - 
   * - Spiral 2
     - .. image:: /images/effects_and_compositions/composition-wipe_method-spiral_2.gif
     - 
   * - Square
     - .. image:: /images/effects_and_compositions/composition-wipe_method-square.gif
     - 
   * - Square 2
     - .. image:: /images/effects_and_compositions/composition-wipe_method-square_2.gif
     - 
   * - Square 2 Bars
     - .. image:: /images/effects_and_compositions/composition-wipe_method-square_2_bars.gif
     - 
   * - Symmetric Clock
     - .. image:: /images/effects_and_compositions/composition-wipe_method-symmetric_clock.gif
     - :guilabel:`Revert` is checked by default, flipping the direction of the transition (goes from the upper track to the lower track)

