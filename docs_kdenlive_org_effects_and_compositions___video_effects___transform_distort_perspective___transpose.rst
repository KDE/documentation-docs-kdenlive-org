.. meta::

   :description: Do your first steps with Kdenlive video editor, using transpose effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, transform, distort, perspective, transpose

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-transpose:

Transpose
=========

This effect/filter transposes rows with columns in the clip and optionally flips it. This is useful if a video recorded with a smartphone is imported as a landscape clip.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-transpose.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-transpose

   Transpose effect

* **Direction** - Set the direction of the transposition. Options are **Clock** (default), **Clock flip**, **Counter clock**, and **Counter clock flip**.

* **Override if** - Override the transposition if clip is identified as **Portrait** or **Landscape**. Select **None** if you want to transpose regardless.

.. rst-class:: clear-both


.. note:: Many smartphones and digital cameras nowadays set an ``autorotate`` flag in the recorded video. Kdenlive can read the flag and transposes videos automatically when importing. Check the clip's properties (:ref:`clip_properties`) if you want Kdenlive to handle that differently and set the :guilabel:`Disable autorotate` to any other value than 0 (default) or switch it to **On**.
