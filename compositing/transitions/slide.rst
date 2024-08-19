.. meta::
   :description: Kdenlive Documentation - Composition Type "Slide" (Transition)
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, compositing, composition type, slide, transition

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _transitions-slide:

Slide
=====

The composition type **Slide** is a transition. For the duration of the composition in the timeline the clips are transitioned like slides in an old-fashioned slideshow.

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/composition_type-slide.webp
     :width: 300px
     :figwidth: 300px
     :align: left

     Settings for the Slide transition

   :1: Select the composition type
   :2: Select the composition track. **Automatic** uses the track immediately below. Only tracks with lower numbers can be selected.
   :3: Start position of the slide (click to select)
   :4: End position of the slide (click to select)
   :5: Transparency (opacity) sliders. Can be used to add a fade in or out.

.. rst-class:: clear-both

The default settings are start position :guilabel:`S1` and end position :guilabel:`E5`. This slides the clip in from left offscreen covering the other clip in the process.

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/transitions-slide_timeline.webp
     :width: 300px
     :figwidth: 300px
     :align: left

     Settings for the Slide transition

   Note the **Slide** being set up as a :doc:`Mix </compositing/transitions/mixes>` to work properly sliding the second slip over the first one. If set up as a :doc:`Composite Transition </compositing/transitions/composite_transitions>`, the second clip overlapping the first in the track below is slid over the first, tripping the whole transition. 

.. rst-class:: clear-both


This list shows the reasonable combinations of start and end position:

.. list-table:: 
   :header-rows: 1
   :widths: 20 30 50
   :class: table-wrap

   * - Start-End
     - Example
     - Notes
   * - S1-E5
     - .. image:: /images/effects_and_compositions/composition_type-slide_s1e5.gif
     - Slides from left offscreen to center. Default setting.
   * - S1-E3
     - .. image:: /images/effects_and_compositions/composition_type-slide_s1e3.gif
     - Slides from left offscreen to right offscreen. S3-E1 is the reverse.
   * - S1-E2
     - .. image:: /images/effects_and_compositions/composition_type-slide_s1e2.gif
     - Slides from left offscreen diagonally up offscreen. S2-E1 is the reverse.
   * - S1-E4
     - .. image:: /images/effects_and_compositions/composition_type-slide_s1e4.gif
     - Slides from left offscreen diagonally down offscreen. S4-E1 is the reverse.
   * - S5-E3
     - .. image:: /images/effects_and_compositions/composition_type-slide_s5e3.gif
     - Same as S1-E5 but flips the clips 
   * - S2-E5
     - .. image:: /images/effects_and_compositions/composition_type-slide_s2e5.gif
     - Slides from top offscreen down to center. S5-E2 is the reverse.
   * - S2-E4
     - .. image:: /images/effects_and_compositions/composition_type-slide_s2e4.gif
     - Slides from top offscreen down to bottom offscreen. S4-E2 is the reverse.
