.. meta::
   :description: Set markers in Kdenlive video editor
   :keywords: KDE, Kdenlive, set guides, DVD, youtube, editing, timeline, documentation, user manual, video editor, open source, free, learn, easy


.. metadata-placeholder

   :authors: - Eugen Mohr

   :license: Creative Commons License SA 4.0

.. .. versionchanged:: 25.12 Reorder menu structure to make it clearer, extend marker system with range/duration support


.. _markers:

Markers
=======


Markers in the picture below are the yellow flags inside the clip. Not to be confused with :ref:`timeline markers <guides>` (red flags in the picture below). Markers are inside the clips and move with the clips.

.. figure:: /images/cutting_and_assembling/cutting_and_assembling-markers-2512.webp

Markers can be used for certain points (Marker2) or ranges (Marker1) in a clip that are important.

Markers are clip related and "fix" to this clip. When you put the same clip again in the timeline and you change a marker, this marker is changed on both clips simultaneously. 


.. _add_markers:

2 ways to add markers
---------------------

Add markers to your clips via the :ref:`ui-monitors_clip_monitor`. That allows you to preview the clip at the location where you are adding a marker.

Following procedures add a marker at the playhead position (clip monitor, timeline):


* **Menu**

  * Clip monitor: From the main menu choose :menuselection:`Markers --> Add Marker`, :ref:`add_marker`
  * Timeline: Click on the clip. From the main menu choose :menuselection:`Markers --> Add Marker`, :ref:`add_marker`
  * Clip monitor: Right click on the clip monitor and choose :menuselection:`Markers --> Add Marker`
  * Timeline: Right click the clip in the timeline and choose :menuselection:`Markers --> Add Marker`. The marker is added at the play-head position.

.. .. versionadded:: 24.08 Insert guides in 10 different categories using NumPad 

* **Keyboard**

  * Clip monitor: numeric keypad :kbd:`*` adds a marker
  * Timeline: Move the playhead on the desired position on the clip. Click on the clip. Numeric keypad :kbd:`*` adds a marker
  * :kbd:`1` - :kbd:`0` (number 1 to 0 on the NumPad)

* **Mouse**

  * not possible


.. .. versionchanged:: 25.12 Extend Marker System with Range/Duration Support

.. _markers_with_range:

Markers With Range
------------------

The following two procedures generate markers with a range:

.. figure:: /images/cutting_and_assembling/cutting_and_assembling-markers_with_range-2512.webp
   :align: left
   :scale: 77%

In the Edit Marker window you can enable :guilabel:`Range Marker` which allows you to determine a :guilabel:`Duration` of the marker. Default :guilabel:`Duration` is 1 second.

.. rst-class:: clear-both

You can create a marker with range from a clip zone. 

.. figure:: /images/cutting_and_assembling/cutting_and_assembling-markers_from_zone-2512.webp
   :align: left
   :scale: 77%

.. attention::

   Make sure you select the desired clip in the project bin.

.. rst-class:: clear-both

Define a zone in the clip monitor with :kbd:`I` and :kbd:`O`. Then you can:

* Right click on the zone and choose :guilabel:`Create Maker from Zone`. This opens a window (see above) and you can adjust all settings. 

* Right click on the zone and choose :guilabel:`Create Marker from Zone Quickly`. This creates a marker with the text :guilabel:`Zone Marker` in the currently active category.

Now the advantage is, that you can select this zone marker in the markers windows and drag it to the timeline. In this way you can mark interesting parts of a clip with zone marker instead of :ref:`Insert Zone in Project Bin <insert_zone_in_project_bin>` and creating sub clips. 

.. _managing_markers:

Managing categories and markers
-------------------------------

.. .. versionadded:: 22.12

Categories
~~~~~~~~~~

Markers using the same categories as :ref:`guides`. More details about :ref:`categories`.

Markers in the clip monitor
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once markers are put in your clip, you can access them in the :ref:`ui-monitors_clip_monitor` by right-clicking and selecting :menuselection:`Go To Marker` or by the hamburger menu :menuselection:`Go To Marker` (see picture).  Also note how the markers appear as vertical lines according the category color you have chosen (see yellow highlighted regions in the picture). You can turn on the display of the marker comments in the timeline too (see :ref:`editing`).

.. figure:: /images/Markers_in_clip_monitor_22-12.png
  
   
.. _markers_view:

Markers View
~~~~~~~~~~~~

Markers are using the same window as :ref:`timeline marker <guide_view>`. Yellow markings show the differences compared to the guide view. 


.. figure:: /images/Kdenlive_guides_view_markers.png
 
:menuselection:`View --> Markers` opens the markers window were you can manage your markers.

To show clip markers in this view you have to:

Project bin: click on the desired clip and the markers of the clip show up in the window. 

On the timeline: right click on the desired clip and choose :menuselection:`Clip in Project Bin` and the markers of this clip show up in the window.

The complete description of the view see :ref:`guide_view`.


You can put a comment in the marker and make the comment display by choosing :ref:`editing` in the :menuselection:`Timeline` menu or by clicking on the :ref:`editing` button.


.. _export_markers:

Export markers as chapters description
--------------------------------------

.. .. versionadded:: 22.12

You can export markers of a single clip as chapters like guides. You have to select a clip before you export.

More details see :ref:`export_guides`



.. _move_edit_marker:

Move and Edit Markers
---------------------

.. figure:: /images/cutting_and_assembling/cutting_and_assembling-markers_with_range-2512.webp
   :align: left
   :scale: 77%

A double-click on a marker **text** in the timeline opens the edit window (besides the possibility in :ref:`markers view <guide_view>`)

.. rst-class:: clear-both

Markers can only be moved by changing the :guilabel:`Position` in the edit window.

:guilabel:`Comment` text and :guilabel:`Category` can be changed in the edit window.

