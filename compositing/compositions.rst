.. meta::
   :description: Kdenlive Documentation - Compositing: Compositions
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, compositing, composition, compositions

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)
             - Eugen Mohr

   :license: Creative Commons License SA 4.0


.. _compositing_and_transitions:

############
Compositions
############

Compositions, outside of the use for :doc:`transitioning <transitions>` from one clip to another, are mostly used for aesthetic or artistic purposes, or to combine images and/or videos to create the illusion that all the elements are parts of the same scene.


.. _compositions-effects_tab:

Compositions Tab
================

.. .. versionchanged:: 24.12

Make the Compositions widget visible in :menuselection:`Menu --> View --> Compositions`.

The Compositions widget has six control icons that show or hide the different effect categories:

.. figure:: /images/effects_and_compositions/kdenlive2412_compositions_tab.webp
   :align: left
   :width: 350px
   :figwidth: 350px
   :alt: kdenlive_compositions_tab

   Kdenlive Compositions widget as a tab in the Project Bin area

|show-all-effects|\ :guilabel:`Main effects` shows all compositions (default view)

|transform-move-horizontal|\ :guilabel:`Show transitions only` shows the transitions only

|favorite|\ :guilabel:`Show all favorite items` shows all compositions and transitions that were flagged as a favorite. This is the same list that appears when selecting :guilabel:`Insert a composition` from the right-click menu of a clip in the Timeline.

|edit-download|\ :guilabel:`Download New Effects` opens a dialog window where compositions templates are listed from the KDE Store

|view-filter|\ :guilabel:`Only show reviewed assets` toggles between the compositions which are reviewed and tested by the Kdenlive team and not tested compositions (still in test phase)
:guilabel:`Show 10 bit compatible only` it hides assets not compatible with a 10-bit pipeline. Use the :guilabel:`10 Bit` category or the :guilabel:`NVENC H265 ABR 10 bit` codec for :ref:`rendering <rendering_preset_categories>`.

|help-about|\ :guilabel:`Show/hide description of effects` toggles the information display below the compositions list where a short description of what the composition does is displayed when on. Clicking on the link opens the online documentation to this effect.


.. _compositing-how:

.. rubric:: How to Composite Two Clips

.. note:: Alpha channels are taken into account automatically so that clips with alpha can be stacked on top of each other without the need of compositions. You can create alpha channels in clips using effects from the :doc:`/effects_and_filters/video_effects/alpha_mask_keying` category.

:Method 1:
   Click on the grey dot in the lower left or right hand corner of the clip you want to composite with the one below. The default composition **Wipe** is added (which is more a :doc:`transition <transitions>`, so you need to :ref:`change the composition type <compositing-composition_type>` to something like **Cairo Blend**).
   
   .. image:: /images/effects_and_compositions/composition_add-method_1.gif
      :width: 400px
  
   Using the left-hand grey dot creates a Wipe composition going from the lower track to the upper track; using the right-hand grey dot creates a Wipe composition going from the upper track to lower track. 

:Method 2:
   Right-click the clip you want to composite with the one below, select :guilabel:`Insert Composition`, and select :guilabel:`Composite and Transform` or :guilabel:`Wipe`.

   .. image:: /images/effects_and_compositions/composition_add-method_2.gif
      :width: 400px

   You can add compositions to your favorites by right-clicking on the composition in the Compositions widget and selecting :guilabel:`Add to favorites`. Your favorite compositions show up as options when using this method.

:Method 3:
   Drag a composition from the Compositions widget and drop it on the clip you want to composite with the one below. Adjust the start and end points by dragging the left and/or right edge of the composition bar in the timeline.

   .. image:: /images/effects_and_compositions/composition_add-method_3.gif
      :width: 400px


.. _compositing-composition_track:

Composition Track
=================

By default, Kdenlive uses the clip in the track immediately below for the compositing. In most cases, this is what you want. But you can instruct Kdenlive to use the clip in another track by changing the :guilabel:`Composition track`. Kdenlive lists all possible tracks for the composition, and they are all below the one in which the clip with the composition is. It is not possible to composite upwards.


.. _compositing-composition_type:

Composition Type
================

With method #1 and #2, Kdenlive by default creates a composition with a composition type **Wipe**, **Composite and Transform**, or whatever composition you may have added as a favorite. A **Wipe** is really more of a :doc:`transition <transitions>`, and **Composite and Transform** may not be needed all the time due to its wealth of additional parameters.

You can change the composition type in the Effect/Composition Stack widget. Kdenlive uses the same space in the UI to display effects or compositions. See the section about :doc:`/user_interface`.

.. container:: clear-both

   .. figure:: /images/effects_and_compositions/composition_type.gif
     :width: 300px
     :figwidth: 300px
     :align: left

     Composition type drop-down

   In the top left corner of the :guilabel:`Composition Stack` is the drop-down list for the composition type. It lists both compositions, :doc:`blend modes </compositing/compositions/blend_modes>` and transitions, as well as :doc:`alpha channel operations </compositing/compositions/alpha_operations>`. Depending on the selected composition type, additional fields (or parameters) are displayed.

.. rst-class:: clear-both

.. toctree:: 
   :maxdepth: 1

   compositions/composite_and_transform
   compositions/blend_modes
   compositions/alpha_operations