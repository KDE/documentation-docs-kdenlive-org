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
   


Kdenlive 16.08 now uses a **track compositing** chooser instead of the previous per-track opacity/transparency controls. This track compositing control can be found in the timeline toolbar, that has been newly introduced with Kdenlive 16.08.

Existing projects are automatically upgraded as necessary when loading them into Kdenlive 16.08. The track compositing applies uniformly to all tracks in your timeline. In contrast, the previous per-track transparency were difficult to use, as you could easily end up with unexpected results when you did not switch on or off all tracks uniformly. The new single control now ensures this, helping especially newcomers to Kdenlive.

So what do these settings mean?

* **High Quality:** uses the new Composite and Transform transition (internally known as qtblend). As its name suggests, it is giving the best compositing quality, at a slight cost of performance. On a fast machine you might be well able to composite several layers of images (with transparency) onto a video clip.

* **None:** this is basically kind of an expert mode when you need full control over any compositing in your timeline. Under certain compositing conditions, if you see the outcome of a transition not to be what you would expect, try to switch track compositing off for a quick check. If the oddity is gone, then this is an interference between the automatic timeline track compositing and your user transitions.

.. deprecated:: 21.12

   *  **Preview:** trade in some timeline preview quality for preview speed, accepting, for instance, some luma bleat. Internally, Kdenlive then uses the Composite transition for achieving track transparency.
 

**Please note** that final rendering always uses either **High Quality** or **None**. So Preview quality is, well, for preview only.


.. rst-class:: clear-both

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   :glob:

   glossary/*