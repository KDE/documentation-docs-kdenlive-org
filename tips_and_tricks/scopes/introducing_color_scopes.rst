.. meta::
   :description: Kdenlive Tips & Tricks - Introducing Scopes
   :keywords: KDE, Kdenlive, tips, tricks, tips & tricks, scopes, editing, timeline, documentation, user manual, video editor, open source, free, learn, easy

.. metadata-placeholder

   :authors: - Simon "Granjow" Eugster <simon.eu@gmail.com>
             - Eugen Mohr
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |minority_report| raw:: html

   <a href="https://en.wikipedia.org/wiki/File:Minority_Report_bleached.jpg" target="_blank">Minority Report</a>

.. |the_departed| raw:: html

   <a href="https://www.acmi.net.au/stories-and-ideas/art-making-b-movie-the-departed/" target="_blank">The Departed</a>


.. _scopes-introducing_color_scopes:

Introducing Color Scopes
========================

This section contains a brief overviews over scopes in general and explains the most basic scope, the histogram, in detail.

Color correction is a really important topic in video editing. It starts with simple stretching of the tonal range if the brightness is not ideal, goes on with white balance to ensure that white remains white and not blue, and finally ends with creating looks which make your video look unique. Remember the blue-ish |minority_report|\ ? The contrasty |the_departed|\ ?

For color correction you basically need two things: Effects or filters for changing the colors and scopes for monitoring the changes. The first scope to look at is the histogram.

.. figure:: /images/tips_and_tricks/kdenlive2308_scopes_histogram.webp

   Kdenlive Histogram :term:`widget`

.. rubric:: Basic Scope Options

Let's first take a look at the basic options available in all scopes. :kbd:`RMB` while overing over the scope :term:`widget<widget>` opens the scope context menu.

.. figure:: /images/tips_and_tricks/kdenlive2308_scopes_histogram_rmb.webp
   :align: left

- :guilabel:`Auto Refresh` automatically refreshes the scope if the project/clip monitor changes. During the process of color correction you'll want to keep this option enabled. When not color correcting, it should be disabled as it usually heavily impacts the performance of playback. (There is a lot of calculations going on in the scopes.)
- :guilabel:`Realtime` tries to maintain a certain frame rate in the scopes by dropping part of the color information received (e.g. taking a look at every 8th pixel only instead of every single pixel).
- :guilabel:`Unscaled` fixes the width of the horizontal axis irrespective of the Histogram :term:`widget`'s size. If unchecked, the horizontal axis contracts and expands with the width of widget.
- :guilabel:`Rec 601` selects the Rec 601 :term:`color space`
- :guilabel:`Rec 709` selects the Rec 709 :term:`color space` (high definition content and digital video uses this one)

Note that you can always update a scope by clicking on it.


.. rubric:: Notes

.. |web_archive| raw:: html

   <a href="https://web.archive.org/web/20160319081747/https://kdenlive.org/users/granjow/introducing-color-scopes-histogram" target="_blank">web.archive.org</a>

**Sources**
  The original text was submitted by *Simon A. Eugster (Granjow)* on Mon, 8/30/2010 - 23:10 to the now defunct kdenlive.org blog. For this documentation it has been lifted from |web_archive|, updated and adapted to match the overall style.