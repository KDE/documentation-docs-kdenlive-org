.. meta::

   :description: Do your first steps with Kdenlive video editor, using edge detection effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, stylize, edge detection

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |canny_edge_detector| raw:: html

   <a href="https://en.wikipedia.org/wiki/Canny_edge_detector" target="_blank">Canny edge detector</a>


.. _effects-edge_detection:

Edge Detection
==============

This effect/filter detects and draws edges using the Canny edge detection algorithm\ [1]_.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-edge_detection.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-edge_detection

   Edge Detection effect

* **Low / High threshold** - Set low and high threshold values used by the algorithm. The :guilabel:`High threshold` selects the "strong" edge pixels, which are then connected through 8-connectivity with the "weak" edge pixels selected by the :guilabel:`Low threshold`. Range is from 0.000 to 1.000 with :guilabel:`Low threshold` being lower or equal to :guilabel:`High threshold`.

* **Modes** - Define the drawing mode: Options are **Wires** (default; draw white/gray wires on black background), **Colormix** (mix the colors to create a paint/cartoon effect), and **Canny** (applies Canny edge detector on all selected :term:`planes<plane>`).

* **Planes** - Select the :term:`planes<plane>` for filtering. Options are **None**, **Y/U/V** and combinations (default is **YUV**), and **Alpha**

.. rst-class:: clear-both


**Notes**

.. [1] For more details refer to the |canny_edge_detector| article in Wikipedia.
