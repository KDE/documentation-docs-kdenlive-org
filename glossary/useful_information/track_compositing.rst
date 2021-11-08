.. metadata-placeholder

   :authors: - TheDiveO
             - Eugen Mohr
             
   :license: Creative Commons License SA 4.0

.. moved from https://kdenlive.org/en/project/configuring-the-default-transition-duration/   

.. _track_compositing:

Track Compositing
=================



.. image:: /images/toolbar-timeline-compositing.png
   :align: left
   :alt: toolbar-timeline-compositing
   

The track compositing applies uniformly to all tracks in your timeline.

So what do these settings mean?

* **None:** this is basically kind of an expert mode when you need full control over any compositing in your timeline. Under certain compositing conditions, if you see the outcome of a transition not to be what you would expect, try to switch track compositing off for a quick check. If the oddity is gone, then this is an interference between the automatic timeline track compositing and your user transitions.

.. deprecated:: 21.12

   *  **Preview:** trade in some timeline preview quality for preview speed, accepting, for instance, some luma bleat. Internally, Kdenlive then uses the Composite transition for achieving track transparency.

.. note::

    Final rendering always uses either **High Quality** or **None**. So Preview quality is, well, for preview only.
