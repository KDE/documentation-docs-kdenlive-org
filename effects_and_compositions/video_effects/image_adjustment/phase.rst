.. meta::

   :description: Do your first steps with Kdenlive video editor, using phase effect
   :keywords: KDE, Kdenlive, video editor, help, learn, easy, effects, filter, video effects, image adjustment, phase

.. metadata-placeholder

   :authors: - Bernd Jordan (https://discuss.kde.org/u/berndmj)

   :license: Creative Commons License SA 4.0


.. _effects-phase:

Phase
=====

This effect/filter delays interlaced video by one field time so that the field order changes.

The intended use is to fix PAL movies that have been captured with the opposite field order to the film-to-video transfer.

The effect does not have keyframes.

.. figure:: /images/effects_and_compositions/kdenlive2304_effects-phase.webp
   :width: 400px
   :figwidth: 400px
   :align: left
   :alt: kdenlive2304_effects-phase

   Phase effect

* **Mode** - Set the phase mode

.. rst-class:: clear-both

The following options for :guilabel:`Mode` are available:

* **Delay the top field** - Capture field order bottom-first, transfer top-first. Filter will delay the top field.

* **Delay the bottom field** - Capture field order top-first, transfer bottom-first. Filter will delay the bottom field. This is the default mode.

* **Keep the field order** - Capture and transfer with the same field order. This mode only exists for the documentation of the other options to refer to, but if you actually select it, the filter will faithfully do nothing.

* **Capture field order automatically and transfer opposite** - Filter selects among :guilabel:`Delay Top` and :guilabel:`Delay bottom` modes on a frame by frame basis using field flags. If no field information is available, then this works just like :guilabel:`Capture Unknown`.

* **Capture unknown or varying and transfer opposite** - Filter selects among :guilabel:`Delay Top` and :guilabel:`Delay bottom` on a frame by frame basis by analyzing the images and selecting the alternative that produces best match between the fields.

* **Capture top-first and transfer unknown or varying** - Filter selects among :guilabel:`Delay bottom` and :guilabel:`Keep order` using image analysis.

* **Capture bottom-first and transfer unknown or varying** - Filter selects among :guilabel:`Delay Top` and :guilabel:`Keep order` using image analysis.

* **Capture determined by field flags and transfer unknown or varying** - Filter selects among :guilabel:`Delay bottom`, :guilabel:`Delay Top` and :guilabel:`Keep order` using field flags and image analysis. If no field information is available, then this works just like :guilabel:`Both capture`.

* **Both capture and transfer unknown or varying** - Filter selects among :guilabel:`Delay bottom`, :guilabel:`Delay Top` and :guilabel:`Keep order` using image analysis only.
