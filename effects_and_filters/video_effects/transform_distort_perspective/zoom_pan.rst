.. meta::

   :description: Kdenlive Video Effects - Zoom Pan
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, zoom pan, 10bit

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |ken_burns| raw:: html

   <a href="https://en.wikipedia.org/wiki/Ken_Burns_effect" target="_blank">Ken Burns Effect</a>


Zoom Pan
========

.. figure:: /images/effects_and_compositions/effects-zoom_pan-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Zoom Pan

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      avfilter
   :**Source filter**:
      zoompan
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No
   :**Color depth**:
      10bit |color-management|
   :**Tutorial**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter applies a zoom and pan effect (similar to the Ken Burns effect\ [1]_).


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Zoom
     - Integer
     - Set the zoom factor. The clip is zoomed with the top left corner as the origin.
   * - X / Y
     - Integer
     - Move the clip along the X / Y axis


.. attention:: 
   As of this writing and with version 23.04 the effect seems to be missing several parameters in order to make it useful as a zoom and pan effect, like the |ken_burns|. A bug report has been created. Until this is fixed use the :doc:`/effects_and_filters/video_effects/transform_distort_perspective/transform` effect.


----

.. [1] For more details refer to the |ken_burns| article in Wikipedia
