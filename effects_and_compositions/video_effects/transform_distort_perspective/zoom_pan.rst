.. meta::

   :description: Do your first steps with Kdenlive video editor, using zoom pan effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, zoom pan

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |ken_burns| raw:: html

   <a href="https://en.wikipedia.org/wiki/Ken_Burns_effect" target="_blank">Ken Burns Effect</a>


.. _effects-zoom_pan:

Zoom Pan
========

This effect/filter applies a zoom and pan effect (similar to the Ken Burns effect\ [1]_).

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-zoom_pan.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-zoom_pan

   Zoom Pan effect

* **Zoom** - Set the zoom factor. The clip is zoomed with the top left corner as the origin.

* **X / Y** - Move the clip along the X / Y axis

.. rst-class:: clear-both


.. attention:: As of this writing and with version 23.04 the effect seems to be missing several parameters in order to make it useful (a zoom and pan effect, like Ken Burns effect). A bug report has been created. Until this is fixed use the :ref:`effects-transform` effect.


**Notes**

.. [1] For more details refer to the |ken_burns| article in Wikipedia
