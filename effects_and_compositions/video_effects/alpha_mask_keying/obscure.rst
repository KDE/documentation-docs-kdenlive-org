.. meta::

   :description: Kdenlive Video Effects - Obscure
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, alpha, mask, keying, obscure

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


Obscure
-------

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-obscure.webp
   :width: 365px
   :figwidth: 365px
   :align: left
   :alt: kdenlive2304_effects-obscure

.. sidebar:: |kdenlive-show-video| Obscure

   :**Status**:
      Maintained
   :**Keyframes**:
      No
   :**Source library**:
      MLT
   :**Source filter**:
      obscure
   :**Available**:
      |linux| |appimage| |windows| |apple|
   :**On Master only**:
      No
   :**Known bugs**:
      No

.. rst-class:: clear-both


.. rubric:: Description

Hide a region of the clip by pixelizing it (obscure). The effect's pixelization cannot be adjusted and may therefore not work satisfactorily with all source material. Compare the :doc:`/effects_and_compositions/video_effects/stylize/pixelize` effect.


.. rubric:: Parameters

.. list-table::
   :header-rows: 1
   :width: 100%
   :widths: 20 10 70
   :class: table-wrap

   * - Parameter
     - Value
     - Description
   * - Size
     - Percentage
     - Determines the size of the area. Can also be changed via the rectangle's coordinates and dimensions.


.. rubric:: Notes

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-obscure_1.webp
   :align:  left
   :width: 400px
   :figwidth: 400px
   :alt: kdenlive2304_effects-obscure

   Obscure effect panel and results (default settings)

Use the handles on the red rectangle\ [1]_ in the Project Monitor to change the size: use the center handle to move the rectangle around.

.. rst-class:: clear-both


----

.. [1] If you do not see a red rectangle in the Project Monitor, enable Edit Mode by clicking on the |edit-mode| icon in the Project Monitor toolbar
