.. meta::

   :description: Do your first steps with Kdenlive video editor, using transform effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, transform

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Roger (https://userbase.kde.org/User:Roger)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. |rotate| replace:: on the **rotate** icon

.. _effects-transform:

Transform
=========

This effect/filter allows transformation and compositing of the clip at the same time.

The effect has keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-transform.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-transform

   Transform effect

* **Compositing** - Defines which composition operation will be performed. See below for available options.

* **Distort** - If checked, allows the non-uniform stretching of the clip

* **Rotate from center** - If checked, process the rotation from center, otherwise from top left corner

* **X / Y / W / H / Size** - This is where the action is for the transformation

* **Rotation** - Angle for rotation. Clicking |rotate| increments the value by 90 degrees. After reaching 360 it wraps to -360 and continues counting up with each click.

.. rst-class:: clear-both


.. rubric:: Compositing options

.. hlist::
   :columns: 3

   * **Alpha Blend**
   * **Xor**
   * **Plus**
   * **Multiply**
   * **Screen**
   * **Overlay**
   * **Darken**
   * **Lighten**
   * **Color dodge**
   * **Color burn**
   * **Hard light**
   * **Soft light**
   * **Difference**
   * **Exclusion**
   * **Bitwise or**
   * **Bitwise and**
   * **Bitwise xor**
   * **Bitwise nor**
   * **Bitwise nand**
   * **Bitwise not xor**
   * **Destination in**
   * **Destination out**

\* (default)

.. **Examples of compositing options:**

   .. image:: /images/effects_and_compositions/kdenlive2304_effects-transform_compositions_1.webp
   :align: left
   :alt: kdenlive2304_effects-transform_compositions_1

   .. image:: /images/effects_and_compositions/kdenlive2304_effects-transform_compositions_2.webp
   :align: left
   :alt: kdenlive2304_effects-transform_compositions_2
