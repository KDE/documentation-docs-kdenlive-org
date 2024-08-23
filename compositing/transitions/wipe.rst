.. meta::
   :description: Kdenlive Documentation - Composition Type "Wipe" (Transition)
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, compositing, composition type, wipe, transition

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0



====
Wipe
====

The composition type **Wipe** is a transition. For the duration of the composition in the timeline the clips are transitioned according to the selected wipe method. It works similar to the Luma composition type / transition.

.. note:: **Luma** and **Dissolve** transitions direct here because they are essentially doing the same thing: use a greyscale image to transition from one clip to the other. They have two additional parameters: :guilabel:`Use transparency` and :guilabel:`Make padding transparent`.

The **Wipe** transition by default performs a simple dissolve. You can select a different Wipe Method, download from KDE Store, or use a file from your local file system.

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/composition_type-wipe.webp
     :width: 300px
     :figwidth: 300px
     :align: left

     Settings for the Wipe transition

   :1: Select the composition type
   :2: Select the composition track. **Automatic** uses the track immediately below. Only tracks with lower numbers can be selected.
   :3: Select the Wipe Method
   :4: :doc:`Download and install </compositing/transitions/add_transitions>` new Wipe Methods from the KDE Store
   :5: Set the softness (:abbr:`feathering (Smoothing or blurring the edges of a feature)`) of the wipe method. Setting :guilabel:`Softness` to zero creates a sharp edge between the two clips.
   :6: Check to invert the direction of the wipe method
   :7: Check to reverse the direction of the wipe method (flips the clips)

.. rst-class:: clear-both


.. _transitions-wipe_methods:

This list shows the standard available wipe methods:

.. list-table:: 
   :header-rows: 1
   :widths: 20 30 50
   :class: table-wrap

   * - Wipe Method
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

