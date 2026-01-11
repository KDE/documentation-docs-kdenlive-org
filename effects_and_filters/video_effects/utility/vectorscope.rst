.. meta::

   :description: Kdenlive Video Effects - Vectorscope 
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, utility, vectorscope

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Vectorscope
===========

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-vectorscope.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   
.. sidebar:: |kdenlive-show-video| Vectorscope

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      frei0r
   :**Source filter**:
      vectorscope
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No
   :**Color depth**:
      10bit |color-management|
   :**Tutorial**:
      :ref:`Yes <tutorials-vectorscope>` |view-presentation|

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter draws and overlays a vectorscope of the video data.

This is different from the :ref:`view-vectorscope` from the :ref:`view_menu` because the Effect version writes the vectorscope into the output video, whereas the View Menu version displays the vectorscope in a separate widget while you still can preview your project.

The effect works like a switch and does not have any parameters nor keyframes. Compare with the :doc:`/effects_and_filters/video_effects/utility/vectorscope_advanced` effect.

.. seealso:: :doc:`/tips_and_tricks/scopes/vectorscope_working` and :doc:`/tips_and_tricks/scopes/vectorscope_i_and_q_lines`
