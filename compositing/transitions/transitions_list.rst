.. meta::
   :description: Kdenlive Documentation - List of Available Transitions
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, compositing, transition, transitions, list

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _compositing-all_transitions:

Available Transitions
=====================

The following composition types are used for transitioning between two clips because the change over time is built in (Wipe, Dissolve), or they have keyframes with which the transition can be fine-tuned for your use case.

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 25 30 45
   :class: table-wrap

   * - Composition Type
     - Example
     - Details (filter name)
   * - :doc:`Wipe </compositing/transitions/wipe>`
     - .. image:: /images/effects_and_compositions/transition-dissolve.gif
     - Refer to the :doc:`details page </compositing/transitions/wipe>` for this transition. You can select from a variety of different wipes, download additional ones from KDE Store, or select a local file.
   * - .. _circle-wipe:
   
       Circle Wipe
     - .. image:: /images/effects_and_compositions/transition-circle_wipe.gif
     - Wipe from center to edge in a circle (|frei0r.sleid0r_wipe-circle|)
   * - :doc:`Dissolve </compositing/transitions/wipe>`
     - .. image:: /images/effects_and_compositions/transition-dissolve.gif
     - This example uses the default :guilabel:`Luma Map` **None (Dissolve)**. **Dissolve** works exactly like :doc:`/compositing/transitions/wipe` but has additional parameters.
   * - .. _horizontal-barn-door-wipe:
   
       Horizontal Barn Door Wipe
     - .. image:: /images/effects_and_compositions/transition-horizontal_barn_door_wipe.gif
     - Horizontal barn door wipe (|frei0r.sleid0r_wipe-barn-door-h|)
   * - :doc:`Luma </compositing/transitions/wipe>`
     - .. image:: /images/effects_and_compositions/transition-luma_burst.gif
     - This example uses the :guilabel:`Wipe Method` **Burst**. **Luma** works exactly like :doc:`/compositing/transitions/wipe` but has additional parameters.
   * - .. _push-down-up:
   
       Push Down / Up
     - .. image:: /images/effects_and_compositions/transition-push_down.gif
     - Push from top to bottom, or from bottom to top (|frei0r.sleid0r_push-down|, |frei0r.sleid0r_push-up|)
   * - .. _push-left-right:
   
       Push Left / Right
     - .. image:: /images/effects_and_compositions/transition-push_left.gif
     - Push from left to right, or from right to left (|frei0r.sleid0r_push-right|, |frei0r.sleid0r_push-left|)
   * - .. _rectangular-wipe:
   
       Rectangular Wipe
     - .. image:: /images/effects_and_compositions/transition-rectangular_wipe.gif
     - Wipe from center to edge in a rectangle (|frei0r.sleid0r_wipe-rect|)
   * - :doc:`Slide </compositing/transitions/slide>`
     - .. image:: /images/effects_and_compositions/transition-slide.gif
     - Refer to the :doc:`details page </compositing/transitions/slide>` for this transition
   * - .. _slide-down-up:
   
       Slide Down / Up
     - .. image:: /images/effects_and_compositions/transition-slide_down.gif
     - Slide from top to bottom, or bottom to top. Note the black bar between the two clips which is not there with **Slide**. (|frei0r.sleid0r_slide-down|, |frei0r.sleid0r_slide-up|)
   * - .. _slide-left-right:
   
       Slide Left / Right
     - .. image:: /images/effects_and_compositions/transition-slide_left.gif
     - Slide from left to right, or right to left. Note the black bar between the two clips which is not there with **Slide**. (|frei0r.sleid0r_slide-left|, |frei0r.sleid0r_slide-right|)
   * - .. _vertical-barn-door-wipe:
   
       Vertical Barn Door Wipe
     - .. image:: /images/effects_and_compositions/transition-vertical_barn_door_wipe.gif
     - Vertical barn door wipe (|frei0r.sleid0r_wipe-barn-door-v|)
   * - .._wipe-down-up:
   
       Wipe Down / Up
     - .. image:: /images/effects_and_compositions/transition-wipe_down.gif
     - Wipe from top to bottom, or bottom to top (|frei0r.sleid0r_wipe-down|, |frei0r.sleid0r_wipe-down|)
   * - .. _wipe-left-right:
   
       Wipe Left / Right
     - .. image:: /images/effects_and_compositions/transition-wipe_left.gif
     - Wipe from left to right, or right to left (|frei0r.sleid0r_wipe-left|, |frei0r.sleid0r_wipe-right|)

More transitions are available through the composition type :doc:`/compositing/transitions/wipe`.

----

.. ===========================================================================
   Link list

.. +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Compositions
   +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. |frei0r.sleid0r_wipe-circle| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_wipe-circle/" target="_blank">frei0r.sleid0r_wipe-circle</a>

.. |composite| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionComposite/" target="_blank">composite</a>

.. |qtblend| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionQtblend/" target="_blank">qtblend</a>

.. |luma| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionLuma/" target="_blank">luma</a>

.. |frei0r.sleid0r_wipe-barn-door-h| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_wipe-barn-door-h/" target="_blank">frei0r.sleid0r_wipe-barn-door-h</a>

.. |matte| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionMatte/" target="_blank">matte</a>

.. |frei0r.sleid0r_push-down| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_push-down/" target="_blank">frei0r.sleid0r_push-down</a>

.. |frei0r.sleid0r_push-left| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_push-left/" target="_blank">frei0r.sleid0r_push-left</a>

.. |frei0r.sleid0r_push-right| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_push-right/" target="_blank">frei0r.sleid0r_push-right</a>

.. |frei0r.sleid0r_push-up| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_push-up/" target="_blank">frei0r.sleid0r_push-up</a>

.. |frei0r.sleid0r_wipe-rect| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_wipe-rect/" target="_blank">frei0r.sleid0r_wipe-rect</a>

.. |frei0r.sleid0r_slide-down| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_slide-down/" target="_blank">frei0r.sleid0r_slide-down</a>

.. |frei0r.sleid0r_slide-left| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_slide-left/" target="_blank">frei0r.sleid0r_slide-left</a>

.. |frei0r.sleid0r_slide-right| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_slide-right/" target="_blank">frei0r.sleid0r_slide-right</a>

.. |frei0r.sleid0r_slide-up| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_slide-up/" target="_blank">frei0r.sleid0r_slide-up</a>

.. |frei0r.sleid0r_wipe-barn-door-v| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_wipe-barn-door-v/" target="_blank">frei0r.sleid0r_wipe-barn-door-v</a>

.. |frei0r.sleid0r_wipe-down| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_wipe-down/" target="_blank">frei0r.sleid0r_wipe-down</a>

.. |frei0r.sleid0r_wipe-left| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_wipe-left/" target="_blank">frei0r.sleid0r_wipe-left</a>

.. |frei0r.sleid0r_wipe-right| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_wipe-right/" target="_blank">frei0r.sleid0r_wipe-right</a>

.. |frei0r.sleid0r_wipe-up| raw:: html

   <a href="https://www.mltframework.org/plugins/TransitionFrei0r-sleid0r_wipe-up/" target="_blank">frei0r.sleid0r_wipe-up</a>
