.. meta::
   :description: Set markers in Kdenlive video editor
   :keywords: KDE, Kdenlive, set guides, DVD, youtube, editing, timeline, documentation, user manual, video editor, open source, free, learn, easy


.. metadata-placeholder

   :authors: - Eugen Mohr

   :license: Creative Commons License SA 4.0



.. _markers:

Markers
=======

.. contents::
 

Markers in the picture below are the green flags inside the clip. Not to be confused with :ref:`guides` (purple flags in the picture below). Markers are inside the clips and move with the clips.


.. image:: /images/Kdenlive_Markers_and_guides_crop.png
   :align: left
   :alt: Kdenlive_Markers_and_guides_crop


Markers can be used for certain points in a clip that are important.


Markers are clip related and "fix" to this clip. When you put the same clip again in the timeline and you change a marker, this marker is changed on both clips simultaneously. 


.. _add_markers:

2 ways to add markers
---------------------

Add markers to your clips via the :ref:`clip_monitor_overview`. That allows you to preview the clip at the location where you adding a marker.

Following procedures add a marker at the playhead position (clip monitor, timeline):


* **Menu**

  * Clip monitor: From the main menu choose :menuselection:`Clip --> Marker --> Add Marker`, :ref:`menu_markers`
  * Timeline: Click on the clip. From the main menu choose :menuselection:`Clip --> Marker --> Add Marker`, :ref:`menu_markers`
  * Clip monitor: Right click on the clip monitor and choose :menuselection:`Marker --> Add Marker`
  * Timeline: Right click the clip in the timeline and choose :menuselection:`Marker --> Add Marker`. The marker is added at the play-head position.

* **Keyboard**

  * Clip monitor: numeric keypad :kbd:`*` adds a marker
  * Timeline: Move the playhead on the desired position on the clip. Click on the clip. Numeric keypad :kbd:`*` adds a marker

* **Mouse**

  * not possible



.. _managing_markers:

Managing categories and markers
-------------------------------

.. versionadded:: 22.12

Categories
~~~~~~~~~~

Markers using the same categories as :ref:`guides`. More details about :ref:`categories`.

Markers in the clip monitor
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once markers are put in your clip, you can access them in the :ref:`clip monitor <monitors>` by right-clicking and selecting :menuselection:`Go To Marker` or by the hamburger menu :menuselection:`Go To Marker` (see picture).  Also note how the markers appear as vertical lines according the category color you have chosen (see yellow highlighted regions in the picture). You can turn on the display of the marker comments in the timeline too (see :ref:`editing`).

.. image:: /images/Markers_in_clip_monitor_22-12.png
   :alt: Markers_in_clip_monitor



.. _markers_view:

Markers View
~~~~~~~~~~~~

Markers using the same window as :ref:`guides <guide_view>`. Yellow marking show the differences compare to the guide view. 


.. image:: /images/Kdenlive_guides_view_markers.png
   :alt: Kdenlive guides view

:menuselection:`View --> Guides` opens the guides window were you can managing your markers.

To show clip markers in this view you have to:

Project bin: click on the desired clip and the markers of the clip show up in the window. 

On the timeline: right click on the desired clip and choose :menuselection:`Clip in Project Bin` and the markers of this clip show up in the window.

The complete description of the view see :ref:`guide_view`.


You can put a comment in the marker and make the comment display by choosing :ref:`editing` in the :menuselection:`Timeline` menu or by clicking on the :ref:`editing` button.


.. _export_markers:

Export markers as chapters description
--------------------------------------

.. versionadded:: 22.12

You can export markers of a single clip as chapters like guides. You have to select a clip before you export.

More details see :ref:`export_guides`



.. _move_edit_marker:

Move and edit markers
---------------------

.. image:: /images/Kdenlive_edit_marker.png
   :alt: Kdenlive edit guide


Double-click on a marker text in the timeline opens the edit window (beside the possibility in :ref:`guides/markers view <guide_view>`)

Markers can only be moved by changing the :guilabel:`Position` in the edit window.


:guilabel:`Comment` text and :guilabel:`Category` can be changed in the edit window.

  


