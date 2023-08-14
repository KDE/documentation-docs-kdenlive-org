.. meta::

   :description: Do your first steps with Kdenlive video editor, using freeze effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, motion, freeze

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Jack (https://userbase.kde.org/User:Jack)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-freeze:

Freeze
======

This effect causes the video to freeze.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-freeze.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-freeze

   Freeze effect

* **Freeze at** - Set the position via the slider or the time code (using the format hh:mm:ss:ff)

* **Freeze Before** - If checked, freezes the video from the start of the clip to the set :guilabel:`Freeze at` position. Default is **off**

* **Freeze After** - If checked, freezes the video from set :guilabel:`Freeze at` position to the end of the clip. Default is **off**

.. rst-class:: clear_both


By default, the clip will be frozen for its entire length when the effect is added to the clip. To change this, check either the :guilabel:`Freeze Before` or :guilabel:`Freeze After` option and move the :guilabel:`Freeze at` slider to the time where you want the freeze to start or end. The audio in the video plays for the entire length, i.e. the **Freeze** effect does not affect the audio.
