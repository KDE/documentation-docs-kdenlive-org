.. meta::
   :description: Kdenlive Documentation - Compositing: Composite Transitions
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, compositing, transition, transitions

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0



Composite Transitions
=====================

This method was the standard mode of transitioning between clips before :doc:`mixes </compositing/transitions/mixes>` (same-track transitions) were introduced. It requires two clips on two tracks overlapping for however long you want the transition to last. Normally this is about one second but you can make them as long or short as you need. Simply adjust the duration of the overlap.

There are three options to add a transition to overlapping clips like in the example below:

:Method 1:
   Click on the purple circle in the lower left or right hand corner of the clip you want to transition from. The default transition **Wipe** with :guilabel:`None (Dissolve)` with a duration of exactly the number of frames the two clips overlap is added.
   
   .. figure:: /images/effects_and_compositions/transition-composition_add_1.gif
      :width: 400px
  
   Using the left-hand purple circle creates a transition going from the lower track to the upper track; using the right-hand purple circle creates a transition going from the upper track to lower track. 

:Method 2:
   Right-click the clip you want to transition from, select :guilabel:`Insert a composition`, and select :guilabel:`Wipe`.

   .. figure:: /images/effects_and_compositions/transition-composition_add_2.gif
      :width: 400px

   You can add transitions to your favorites by right-clicking on the transition composition in the Compositions widget and selecting :guilabel:`Add to favorites`. Your favorite transitions show up as options when using this method.

:Method 3:
   Drag a transition composition from the Compositions widget and drop it on the clip you want to transition from. Adjust the start and end points by dragging the left and/or right edge of the composition bar in the timeline.

   .. figure:: /images/effects_and_compositions/transition-composition_add_3.gif
      :width: 400px

Once you added the transition, select it to change any of the parameter.

.. container:: clear-both

  .. figure:: /images/effects_and_compositions/transition-composition.webp
    :figwidth: 600px
    :align: left

    A transition Composition in the timeline. The transition properties are on the right.

    
.. rst-class:: clear-both

:1: :guilabel:`Composition Type`. Select a different one from the drop-down list if needed. See this list of :doc:`available transitions </compositing/transitions/transitions_list>`.
:2: :guilabel:`Composition Track`. Default is **Automatic** (the track immediately below), but you can select other tracks if needed.
:3: :guilabel:`Wipe Method`. Default is **None (Dissolve)**. Select a built-in method from the drop-down list, or select **Custom** to use a greyscale image (:file:`.pgm` format) from your local file system. See this list of :ref:`available wipe methods <transitions-wipe_methods>`.
:3a: :doc:`Adding transitions <add_transitions>` by downloading and installing additional wipes from the KDE Store\ [1]_.
:4: Adjust the :abbr:`feathering (Smoothing or blurring the edges of a feature)` of the transition. Setting :guilabel:`Softness` to 0 creates a hard edge between the two clips.
:5: Additional settings to control the transition.


----

.. |kde_store| raw:: html

   <a href="https://store.kde.org/browse?cat=333&ord=latest" target="_blank">KDE Store</a>

.. [1] Kdenlive has a direct link to the |kde_store| from where you can download and install new transitions in form of luma files (greyscale images of type :file:`.pgm`). Click on the |edit-download| :guilabel:`Download` icon. If you have an active Internet connection, Kdenlive queries the KDE Store for all of the luma files available and opens a dialog window.