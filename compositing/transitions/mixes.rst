.. meta::
   :description: Kdenlive Documentation - Mixes / Same-track Transition
   :keywords: KDE, Kdenlive, documentation, user manual, video editor, open source, free, learn, easy, compositing, transition, transitions, mix, mixes, same track

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0



.. _same_track_transition:

Mixes / Same-track Transitions
==============================

.. .. versionadded:: 20.12

A **Mix** is a transition between two adjacent clips in the same track, hence the term **same-track transition**.

.. note:: For a **Mix** to work you need at least 1/2 second worth of frames on either side of the two clips. Trim video clips accordingly, otherwise an error message will be displayed and the **Mix** is not applied.

You can add a **Mix** either by double-clicking the line between the two clips, or by selecting one of the clips and pressing :kbd:`U`, or clicking the |composite-track-preview| icon in the timeline toolbar.

.. note:: When using :kbd:`U`, Kdenlive tries to place the transition at the most logical spot. First, if there is a clip after the selected one, the transition is put between the selected and the one right after it; if there is no clip after the selected one but one before, the transition is put between the clip before and the selected one.

.. figure:: /images/effects_and_compositions/transition-mix.webp
  :align: left

  A **Mix** transition in the timeline. Note the toolbar button (top left) and the transition properties on the right.

By default, Kdenlive creates a transition for one second based on the **Luma** composition. The transition properties change depending on the selected transition.

:1: :guilabel:`Composition Type`. Select a different one from the drop-down list if needed. See this list of :doc:`available transitions </compositing/transitions/transitions_list>`.
:2: :guilabel:`Wipe Method`. Select a built-in method from the drop-down list, or select **Custom** to use a greyscale image (:file:`.pgm` format) from your local file system. See this list of :ref:`available wipe methods <transitions-wipe_methods>`.
:2a: :doc:`Adding transitions <add_transitions>` by downloading and installing additional wipes from the KDE Store\ [1]_.
:3: Adjust the :abbr:`feathering (Smoothing or blurring the edges of a feature)` of the transition. Setting :guilabel:`Softness` to 0 creates a hard edge between the two clips.
:4: Additional settings to control the transition.
:5: Change the duration of the transition
:6: Change the alignment of the transition 


----

.. |kde_store| raw:: html

   <a href="https://store.kde.org/browse?cat=333&amp;ord=latest" target="_blank">KDE Store</a>

.. [1] Kdenlive has a direct link to the |kde_store| from where you can download and install new transitions in form of luma files (greyscale images of type :file:`.pgm`). Click on the |edit-download| :guilabel:`Download` icon. If you have an active Internet connection, Kdenlive queries the KDE Store for all of the luma files available and opens a dialog window.