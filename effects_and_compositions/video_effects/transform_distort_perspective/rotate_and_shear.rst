.. meta::

   :description: Do your first steps with Kdenlive video editor, using rotate and shear effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, rotate and shear

.. metadata-placeholder

   :authors: - Claus Christensen
             - Yuri Chornoivan
             - Ttguy (https://userbase.kde.org/User:Ttguy)
             - Bushuev (https://userbase.kde.org/User:Bushuev)
             - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0

.. _effects-rotate_and_shear:

Rotate and Shear
================

This effect/filter allows to rotate the clip in any three directions.

The effect has keyframes but not for the rotation and the shear degrees. This is controlled by the :guilabel:`Animate` parameters.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-rotate_and_shear.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-rotate_and_shear

   Rotate and Shear effect

* **Rotate X / Y / Z** - Set the amount of rotation in ``degrees * 10``. For example: 900 = 90 degrees rotation.

* **Animate Rotate X / Y / Z** - Same as :guilabel:`Rotate`. The clip is rotated by that amount every frame.

* **Shear X / Y** - Set the amount of shear in ``degrees * 10``. For example: 450 = 45 degrees shear (diagonal).

* **Animate Shear X / Y** - Same as :guilabel:`Shear`. The clip is sheared by that amount every frame.

* **X / Y / W / H / Size** - Allows to move (X, Y) and zoom (Size) the clip at the same time

* **Background Color** - Define the background color to be used when rotating or shearing reveals the background. Default is Alpha.

.. rst-class:: clear-both


.. attention:: The axes for rotation and shear are different than for moving a clip. The latter uses the monitor plane: X = width or horizontal axis, Y = height or vertical axis. For rotation and shear the plane is tilted by 90 degrees "into the monitor" and rotated 90 degrees clockwise around the vertical axis. This results in the X axis coming out of/going into the monitor, the Y axis being along the width of the monitor and the Z axis being along the height of the monitor. See image below.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-rotate_and_shear_axes.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-rotate_and_shear_axes

   Rotate and Shear effect axis visualization

..



.. .. image:: /images/Kdenlive_Rotate_and_shear.png
   :align: left
   :alt: Kdenlive_Rotate_and_shear

   https://youtu.be/WadSGu05HAw

