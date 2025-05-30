.. meta::

   :description: Kdenlive Video Effects - Vignette
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, generate, vignette

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Vignette
========

.. figure:: /images/effects_and_compositions/effects-vignette-2504.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: effects-vignette-2504.webp

.. sidebar:: |kdenlive-show-video| Vignette

   :**Status**:
      Maintained
   :**Keyframes**:
      Yes
   :**Source library**:
      frei0r
   :**Source filter**:
      vignette
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

This effect/filter creates a natural lens vignetting effect. It is similar to the :doc:`/effects_and_filters/video_effects/generate/vignette_effect` effect but lacks the built-in ability to move the center around.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Aspect ratio
     - Integer
     - Select the aspect ratio of the vignette to make it more circular or more elliptical. Default is 500 (circular). Values below 500 "squash" the vignette vertically making it look elongated horizontally; values above 500 "squash" the vignette horizontally making it look elongated vertically.
   * - Clear center size
     - Integer
     - Set the size of the unaffected center
   * - Softness
     - Integer
     - Set the softness of the vignette


.. note::
   Even with :kbd:`Softness` at 0, there will always be some softness (or feathering) in the vignette.