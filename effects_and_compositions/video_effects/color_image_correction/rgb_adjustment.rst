.. meta::

   :description: Do your first steps with Kdenlive video editor, using rgb adjustment effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, color and image correction, rgb adjustment

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Marko (https://userbase.kde.org/User:Marko)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-rgb_adjustment:

RGB Adjustment
==============

This filter is for simple manual color adjustment by RGB channel, either through adding constants, or changing the channel :term:`gammas<gamma>` or gains.

The effect has keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-rgb_adjustment.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-rgb_adjustment

   RGB Adjustment effect

* **Action:** - Set the action to be performed [1]_
  - *Add constant* adds a fixed value between -150 and +150 (this is sometimes called "black level" or "setup").
  - *Change gamma* changes channel gamma between 0.3333 and 3.0.
  - *Multiply* multiplies channel with a value between 0.3333 and 3.0 (sometimes called "gain" or "contrast").

* **Keep luma** - Set to keep the luma value and the R/G/B sliders only affect the respective color channel

* **Alpha controlled** - Check this if only areas with non-zero alpha are to be affected

* **Luma formula** - Set the color space to operate in. Options are **Rec. 709** (default) and **Rec. 601**.

* **R / G / B** - Determines the change in each of the three color channels

.. rst-class:: clear-both


**Add constant** simply shifts the RGB "cube" colorspace. This means, that on one end we are left with empty space, which is filled with zeros, and on the other end, values can "fall outside", and in this case they will be truncated to max (255).

**Change gain** changes the size of the cube, keeping the "black" corner fixed, affecting predominately highlights, but the other end can still "fall out" and get 255 truncated.

**Change gamma** keeps the whole cube in the same place, just stretches and squeezes its interior, so no zero filling or truncation is necessary.

.. hint:: To visualize this effect's actions, apply it to a gray gradient and watch the result with :ref:`view-histogram`.


**Notes**

.. [1] To apply more than one action, use stacked instances of the effect. Note that Kdenlive executes the stack from top down so sequence is important.
